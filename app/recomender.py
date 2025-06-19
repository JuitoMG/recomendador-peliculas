import pandas as pd
import joblib
from sklearn.metrics.pairwise import cosine_similarity
import ast

# Cargamos los datos de películas
df = pd.read_csv("data/processed/peliculas_enriquecidas.csv")
df = df.reset_index(drop=True)

#Carga del vectorizador y creación de la matriz
vectorizer = joblib.load('model/modelos_guardados/tfidf_vectorizer.pkl')
df['keywords_text'] = df['keywords_tfidf'].apply(lambda x: ' '.join(ast.literal_eval(x)) if isinstance(x, str) else '')
df['genres_text'] = df['genres'].apply(lambda x: ' '.join(ast.literal_eval(x)) if isinstance(x, str) else '')
df['topic_id_str'] = df['topic_id'].astype(str)
df['main_country'] = df['main_country'].fillna('unknown')
df['title'] = df['title'].fillna('')

df['text_for_vector'] = (
    df['overview_lemmatized'] + ' ' +
    df['keywords_text'] + ' ' +
    df['genres_text'] + ' ' +
    df['director'] + ' ' +
    df['main_country'] + ' ' +
    df['topic_id_str'] + ' ' +
    df['title']
)

# Generar la matriz tf-idf y similitud
tfidf_matrix = vectorizer.transform(df['text_for_vector'])
similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Mapa título -> indice
title_to_index = pd.Series(df.index, index=df['title'].str.strip().str.lower())


def recomendar(titulo: str, top_n: int=5):
    titulo_normalizado = titulo.strip().lower()
    if titulo_normalizado not in title_to_index:
        return None, None
    idx = title_to_index[titulo_normalizado]
    sim_scores = list(enumerate(similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n+1]
    titulo_original = df.iloc[idx]['title']
    recomendaciones = [(df.iloc[i]['title'], df.iloc[i]['id'], round(score, 3)) for i, score in sim_scores]
    return recomendaciones, titulo_original