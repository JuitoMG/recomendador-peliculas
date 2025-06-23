from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from app.recomender import recomendar as recomendar_peliculas
import requests
import os
from dotenv import load_dotenv

# Carga del entorno
load_dotenv()
TMDB_BEARER = os.getenv("TMDB_BEARER_TOKEN")

app = FastAPI(title="Recomendador de Películas por IA")

# Archivos estáticos y templates
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def formulario(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/recomendar", response_class=HTMLResponse)
def recomendar(request: Request, titulo: str = Form(...), top_n: int = Form(...)):
    recomendaciones, titulo_original = recomendar_peliculas(titulo, top_n)
    return templates.TemplateResponse("resultados.html", {
        "request": request,
        "titulo": titulo_original,
        "recomendaciones": recomendaciones
    })

@app.get("/buscar_pelicula", response_class=JSONResponse)
def buscar_pelicula(titulo: str):
    url = f"https://api.themoviedb.org/3/search/movie"
    headers = {
        "Authorization": f"Bearer {TMDB_BEARER}",
        "Accept": "application/json"
    }
    params = {
        "query": titulo,
        "language": "es-ES"
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"❌ Error al buscar película: {e}")
        return JSONResponse(status_code=500, content={"error": "Error al buscar en TMDB"})

    resultados = response.json().get("results", [])
    peliculas = []
    for r in resultados[:5]:  # Puedes ajustar la cantidad
        peliculas.append({
            "id": r["id"],
            "titulo": r["title"],
            "anio": r.get("release_date", "")[:4],
            "poster": f"https://image.tmdb.org/t/p/w200{r['poster_path']}" if r.get("poster_path") else None
        })

    return {"peliculas": peliculas}
