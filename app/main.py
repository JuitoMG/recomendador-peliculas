from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.recomender import recomendar

app = FastAPI(title="Recomendador de Películas por IA")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def formulario(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/recomendar", response_class=HTMLResponse)
async def obtener_recomendacion(request: Request, pelicula_base: str = Form(...)):
    recomendaciones = recomendar(pelicula_base)
    return templates.TemplateResponse("resultados.html", {
        "request": request,
        "pelicula_base": pelicula_base,
        "recomendaciones": recomendaciones
    })    