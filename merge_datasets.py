import os
import json
import pandas as pd

# Rutas

RAW_DIR = "data/raw"
OUTPUT_DIR = "data/processed"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_json_files(folder):
    movies =[]
    for filename in os.listdir(folder):
        if filename.endswith(".json"):
            with open(os.path.join(folder, filename), "r", encoding="utf-8") as f:
                data = json.load(f)
                movies.extend(data)
    return movies

def flattern_movie_data(movies):
    for movie in movies:
        if isinstance(movie.get("genres"), list):
            movie["genres"] = ", ".join(movie["genres"])
    return movies

def main():
    print("Cargando archivos JSON...")
    all_movies = load_json_files(RAW_DIR)
    print(f"{len(all_movies)} peliculas cargadas.")

    print("Procesando campos...")
    flattened = flattern_movie_data(all_movies)

    print("Exportando a CSV...")
    df = pd.DataFrame(flattened)
    output_path = os.path.join(OUTPUT_DIR, "movies_merged.csv")
    df.to_csv(output_path, index=False, encoding="utf-8")
    print(f"Archivo guardado en: {output_path}")

if __name__ == "__main__":
    main()    