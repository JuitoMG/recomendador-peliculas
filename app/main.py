from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Recomendador de Películas por IA")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/recomendar", response_class=HTMLResponse)
async def recomendar(request: Request, pelicula_base: str = Form(...)):
    return HTMLResponse(f"<h2>Película recibida: {pelicula_base}</h2>")