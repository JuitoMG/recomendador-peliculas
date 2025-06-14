import pandas as pd

# Cargamos los datos de películas
df = pd.read_csv("data(processed/movies_merged.csv")

def recomendar(pelicula_base, n_resultados=5):
    resultados = df[df['title'].str.contains(pelicula_base, case=False, na=False)]

    if resultados.empty:
        return []
    
    recomendaciones = resultados.head(n_resultados).to_dict(orient="records")
    return recomendaciones