# 🤖🎙️ [SpotifAI](https://alejandrorod-tajamar-spotifai-new-app-kfzcq4.streamlit.app/)

SpotifAI es una aplicación desarrollada en Streamlit que utiliza Azure Language Studio y la API de Spotify para ofrecer recomendaciones de canciones, artistas, álbumes y listas de reproducción, así como información relevante y enlaces directos a Spotify, todo esto mediante el uso de CLU (COnversational Language Understanding).

## Funcionalidades

Recomendaciones personalizadas de canciones, artistas y playlists.
Consulta de información sobre canciones, artistas y álbumes.
Integración con Azure Language Studio para el análisis de consultas.
Uso de la API de Spotify para acceder a datos musicales en tiempo real.

## Uso de la aplicación

- Acceder al enlace: [https://alejandrorod-tajamar-spotifai-new-app-kfzcq4.streamlit.app/](https://alejandrorod-tajamar-spotifai-new-app-kfzcq4.streamlit.app/)
- Utilizar las [preguntas de ejemplo](/example_inputs.md) como guía para probar el chatbot.
- Escribir mensajes propios en el chat que sean similares a los de ejemplo para comprobar cuáles funcionan mejor.
- Para ver la intención y las entidades detectadas en cada mensaje mandado, expandir el desplegable de la parte superior del chat.
- Para ver más detalles sobre el CLU, revisar el archivo [modeldata_exported.json](/modeldata_exported.json).

## [OPCIONAL] Integración

Para implementar un proyecto similar a este, basarse en la guía del siguiente enlace y fijarse en el código de la versión de la app sin Streamlit:

- [Create a language understanding model with the Language service](https://microsoftlearning.github.io/mslearn-ai-language/Instructions/Exercises/03-language-understanding.html)
- [app.py](/app.py)

## [OPCIONAL] Instalación en local

Clona este proyecto:

```bash
git clone https://github.com/alejandrorod-tajamar/SpotifAI.git
```

Navega hasta la carpeta del proyecto:

```cmd
cd SpotifAI
```

Crea un entorno virtual:

```cmd
py -m venv .venv
```

Activa el entorno virtual:

```cmd
.venv\Scripts\activate
```

Instala las dependencias del proyecto:

```cmd
pip install -r requirements.txt
```

Configura tus credenciales de Azure y Spotify:

- Para Azure, crea un recurso de Language Services y sigue el tutorial mencionado anteriormente ([Create a language understanding model with the Language service](https://microsoftlearning.github.io/mslearn-ai-language/Instructions/Exercises/03-language-understanding.html)). Después, ve a la sección _Keys and Endpoint_ de tu recurso de Language Services en Azure.
- Para Spotify, crea una aplicación en [Spotify for Developers](https://developer.spotify.com/) y consigue tu Client ID y Client Secret.

Crea un archivo `.env`, con la siguiente estructura:

```init
SPOTIPY_CLIENT_ID="tu_client_id"
SPOTIPY_CLIENT_SECRET="tu_client_secret"
SPOTIPY_REDIRECT_URI="puerto_donde_se_lanza_la_app"
CLU_ENDPOINT=tu_endpoint_azure
CLU_API_KEY=tu_key_azure
CLU_PROJECT_NAME=tu_nombre_proyecto
CLU_DEPLOYMENT_NAME=tu_nombre_despliegue
```

Por último, utiliza la última sección de código en [app.py](/app.py) para hacer pruebas y editar el input que le quieras mandar a tu app. Para ejecutarla, utiliza:

```cmd
py app.py
```
