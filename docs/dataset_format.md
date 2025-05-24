# Formato y estructura del Dataset TMDB

Este documento describe el formato y origen de los datasets utilizados para entrenar el recomendador de películas.

## Origen de los datos

Los datos fueron descargados usando la [API de TMDB](https://developer.themoviedb.org/), mediante un script personalizado en Python (tmdb_download.py). Para cada año consultado se obtuvieron las películas más populares (sort_by=popularity.desc) y se enriquecieron con metadatos adicionales.

## Archivos disponibles

- `movies_1950.json`
- `movies_1970.json`
- `movies_1990.json`
- `movies_2005.json`
- `movies_2024.json`

## Estructura de cada entrada

Cada objeto de película incluye los siguientes campos:

- `ìd`: ID numérico único en TMDB
- `tittle`: Título en español
- `original_title`: Título original
- `overview`: Descripción corta de la película
- `tagline`: Frase promocional si está disponible
- `release_date`: Fecha de estreno (YYY-MM-DD)
- `original_language`: Idioma original
- `genres`: Lista de géneros (es español)
- `production_countries`: Lista de países de producción
- `runtime`: Duración en minutos
- `budget`: Presupuesto estumado (en USD)
- `revenue`: Recaudación estimada (en USD)
- `vote_average`: Puntuación media
- `director`: Nombre del director principal
- `cast`: Lista de actores principales
- `keywords`: Lista de palabras clave asociadas

## Estructura de archivos

Los archivos se almacenan en `data/raw/` con el nombre `movies_XXXX.json`, donde XXXX representa el año:

<pre>
data/raw/
├── movies_1950.json
├── movies_1970.json
├── movies_1990.json
├── movies_2005.json
├── movies_2024.json
└── tmdb_download.py
</pre>

Cada archivo contiene aproximadamente 200 entradas por año.

## Notas

- Se utilizó paginación de hasta 10 páginas por año (`pages=10`), con una pausa de 0.25 segundos entre llamadas a la API para respetar el límite de peticiones.
- El script se puede editar fácilmente para descargar otros años modificando el valor del año y el nombre del archivo de salida.
- Solo se incluyen películas populares (`sort_by=popularity.desc`).
- El idioma de los datos está fijado en `es-Es`.
- El campo `cast`incluye solo los primeros actores listados por TMDB.


