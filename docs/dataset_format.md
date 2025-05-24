# Formato del Dataset TMDB

Este directorio contiene los datos en crudo descargados desde la [API de TMDB](https://developer.themoviedb.org/), mediante un script personalizado en Python (tmdb_download.py). Para cada año consultado se obtuvieron las películas más populares (sort_by=popularity.desc) y se enriquecieron con metadatos adicionales.

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
- `release_date`: Fecha de estreno (YYY-MM-DD)
- `original_language`: Idioma original
- `genres`: Lista de géneros (es español)
- `vote_average`: Puntuación media
- `director`: Nombre del director principal

## Notas

- Solo se incluyen películas populares (`sort_by=popularity.desc`)
- Se han descargado hasta 10 páginas por año (máx 200 películas por archivo)
- El idioma de los datos está fijado en `es-Es`


