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

recomendador-peliculas-IA/
│
├── data/                  # Datasets descargados (puedes ignorar en .gitignore si pesan mucho)
│
├── model/                 # Código y modelos entrenados
│   ├── entrenamiento/     # Scripts para entrenar
│   └── modelos_guardados/ # Archivos .pkl o similares
│
├── app/                   # Interfaz web (HTML, CSS, JS o framework como Flask/FastAPI)
│   └── static/            # Archivos estáticos: carátulas, CSS, JS
│
├── translator/            # Scripts relacionados con el modelo de traducción
│
├── docs/                  # Documentación y diseños
│   ├── idea.md
│   ├── arquitectura.drawio
│   ├── interfaz.png
│   ├── flujo_datos.md
│   └── roadmap.md
│
├── tests/                 # Tests automáticos
│
├── .gitignore
├── README.md
├── LICENSE
├── requirements.txt
└── main.py                # Archivo principal que ejecuta la app

---

## 🪾 Estructura de ramas

main                  → Rama principal y estable del proyecto
|
├── dev               → Rama de desarrollo general
|   ├── feature/...   → Nuevas funcionalidades (ej: feature/interfaz-web)
|   ├── bugfix/...    → Correcciones de errores
|   └── experiment/...→ Pruebas y prototipos
|
└── docs              → Documentación y mejoras del README, wiki, etc.

---

## 📈 Diagramas

- Los diagramas de flujo y arquitectura se están desarrollando con [draw.io](http://draw.io).
- Se encuentran en la carpeta `docs/` en formato `.drawio`.

### Diagramas actuales

- `flujo_recomendador.drawio`: Representa el funcionamiento de la app desde la selección de películas hasta la obtención de recomendaciones.

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