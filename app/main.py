from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.recomender import recomendar_peliculas

app = FastAPI(title="Recomendador de Películas por IA")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def formulario(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/recomendar")
def procesar_recomendacion(data: dict):
    titulo = data.get('titulo')
    top_n = int(data.get('top_n', 5))
    recomendaciones = recomendar_peliculas(titulo, top_n)
    return {"recomendaciones": recomendaciones}
