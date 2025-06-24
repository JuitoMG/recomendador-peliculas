import requests
import json
import os
from time import sleep
from dotenv import load_dotenv
from tqdm import tqdm

#Cargar la clave de la API
load_dotenv()
API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "http://api.themoviedb.org/3"
LANG = "es-ES"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json;charset=utf-8"
}

def get_movies_by_year(year, pages=5):
    all_movies = []
    print(f"Descargando películas del año {year} ({pages} páginas)...")
    for page in tqdm(range(1, pages+1), desc="Paginas TMDB"):
        url = f"{BASE_URL}/discover/movie?language={LANG}&sort_by=popularity.desc&primary_release_year={year}&page={page}"
        resp = requests.get(url, headers= HEADERS)
        if resp.status_code == 200:
            data = resp.json()
            all_movies.extend(data['results'])
        else:
            print(f"Error en la página {page}: {resp.status_code}")
        sleep(0.25)
    return all_movies

def get_movie_details(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}?language={LANG}"
    resp = requests.get(url,headers=HEADERS)
    return resp.json() if resp.status_code == 200 else None

def get_director(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}/credits"
    resp = requests.get(url, headers=HEADERS)
    if resp.status_code == 200:
        credits = resp.json()
        for person in credits['crew']:
            if person['job'] == 'Director':
                return person['name']
    return None

def get_keywords(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}/keywords"
    resp = requests.get(url, headers=HEADERS)
    if resp.status_code == 200:
        data = resp.json()
        return [kw['name'] for kw in data.get('keywords', [])]
    return []

def get_main_cast(movie_id, max_actors=3):
    url = f"{BASE_URL}/movie/{movie_id}/credits"
    resp = requests.get(url, headers=HEADERS)
    if resp.status_code == 200:
        credits = resp.json()
        cast = [actor['name'] for actor in credits['cast'][:max_actors]]
        return cast
    return []

def save_to_json (data, filename):
    os.makedirs("data/raw", exist_ok=True)
    with open(f"data/raw/{filename}", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    year = 1980
    pages = 15
    movies = get_movies_by_year(year, pages=pages)
    enriched = []

    print(f"Detalles para {len(movies)} películas...")
    for m in tqdm(movies, desc="Películas procesadas"):
        details = get_movie_details(m['id'])
        director = get_director(m['id'])
        if details:
            enriched.append({
                "id": m['id'],
                "title": m['title'],
                "original_title": m['original_title'],
                "production_countries": [c['name'] for c in details.get('production_countries', [])],
                "overview": m['overview'],
                "tagline": details.get("tagline"),
                "release_date": m['release_date'],
                "original_language": m['original_language'],
                "genres": [g['name'] for g in details.get('genres', [])],
                "runtime": details.get("runtime"),
                "budget": details.get("budget"),
                "revenue": details.get("revenue"),
                "cast": get_main_cast(m['id']),
                "vote_average": details.get("vote_average"),
                "director": director,
                "keywords": get_keywords(m['id'])

            })
        sleep(0.25) 
    save_to_json(enriched, f"movies_{year}.json")
    print("Descarga completada.") 

if __name__ == "__main__":
    main()                  



