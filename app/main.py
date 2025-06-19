from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.recomender import recomendar as recomendar_peliculas

app = FastAPI(title="Recomendador de Películas por IA")

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
