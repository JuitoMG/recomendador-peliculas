# 🎬 Recomendador de Películas con IA (proyecto en desarrollo)

Este proyecto consiste en un sistema de recomendación de películas con interfáz web, impulsado con modelos de inteligencia artificial entrenados localmente. El objetivo es ofrecer recomendaciones personalizadas a partir de una o varias películas elegidas por el usuario, con opción de filtrar por director, géneros o estilo narrativo.

## 📋 Características principales

- Entrenamiento de un modelo de IA para sugerencias personalizadas.
- Interfaz web intuitiva para seleccionar películas y aplicar filtros.
- Traducción automática de términos mediante un modelo Helsinki-NLP.
- Datos obtenidos desde TMDB (títulos, géneros, directores, carátulas).
- Trabajo en local para garantizar privacidad y autonomía.
- Desarrollo documentado y gestionado con Jira y Github.

---

## 🛠️ Tecnologías utilizadas

- **Python** - Backend y entrenamiento del modelo.
- **Scikit-learn / Pandas / Numpy** - Preprocesamiento y modelos.
- **Helsinki-NLP** - Traducción de temas y géneros.
- **TMDB API** - Fuente de datos de películas y carátulas.
- **HTML + CSSS + FW** - Interfaz del usuario.
- **Google Colab** - Entrenamiento en la nube del modelo.
- **VS Code** - Entorno de desarrollo local.
- **GitHub + Jira** - Gestión de código y planificación del proyecto.

---

## ⏱️ Funcionalidad (Modo de uso)

1. El usuario selecciona una o varias películas.
2. Se muestran datos clave: director, géneros, temas, etc.
3. El usuario puede marcar o desmarcar elementos para refinar la recomendación.
4. El sistema genera sugerencias similares basadas en el estilo deseado.
5. Las carátulas y datos se muestran desde local (Sin conexión a internet).

---

## ✅ Estado actual del proyecto

| Módulo                  | Estado        |
|-------------------------|---------------|
| Diseño inicial          | ✅ Completo   |
| Obtención de datos TMDB | 🔄 En curso   |
| Modelo de traducción    | 🕐 Pendiente  |
| Entrenamiento IA        | 🕐 Pendiente  |
| Interfaz web            | 🕐 Pendiente  |

Proximamente en el tablero de Jira

---

## 📁 Estructura del repositorio prevista

raíz/
├── README.md
├── requirements.txt
├── data/
│ ├── raw/
│ └── processed/
├── models/
├── src/
│ ├── app/
│ └── recommender/
├── static/
│ └── posters/
└── web/
└── templates/

---

## 📜 Licencia

Este proyecto está bajo la licencia [MIT](LICENSE), lo que significa que puedes usarlo, modificarlo y distribuirlo libremente, siempre que mantengas los créditos originales.

---

## 🚀 Cómo contribuir

Este proyecto está pensado como un experimento de aprendizaje individual, pero se aceptan ideas, sugerencias o mejoras. Puedes abrir un *issue* o hacer un *fork* para probar tus propias ideas.

---

## 📌 Notas legales

Este proyecto utiliza datos de [TMDB](https://www.themoviedb.org/). El uso de la API está sujeto a sus términos de uso.

---