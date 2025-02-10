import os
import requests
import json
import streamlit as st
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Cargar variables de entorno
load_dotenv(override=True)

# Datos de CLU en Azure Language Services
CLU_ENDPOINT = os.getenv("CLU_ENDPOINT")
CLU_API_KEY = os.getenv("CLU_API_KEY")
CLU_PROJECT_NAME = os.getenv("CLU_PROJECT_NAME")
CLU_DEPLOYMENT_NAME = os.getenv("CLU_DEPLOYMENT_NAME")

# Datos de Spotify API
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

# Conexión a Spotify
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET))

def consultar_clu(query):
    """Envía una consulta a Conversational Language Understanding (CLU)"""
    url = f"{CLU_ENDPOINT}/language/:analyze-conversations?api-version=2022-10-01-preview"
    
    headers = {
        "Ocp-Apim-Subscription-Key": CLU_API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "analysisInput": {
            "conversationItem": {
                "id": "1",
                "text": query,
                "modality": "text",
                "language": "es",
                "participantId": "user"
            }
        },
        "parameters": {
            "projectName": CLU_PROJECT_NAME,
            "deploymentName": CLU_DEPLOYMENT_NAME,
            "stringIndexType": "TextElement_V8"
        },
        "kind": "Conversation"
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Lanza una excepción si la respuesta es un error HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Error en la conexión con CLU: {str(e)}"}


# FUNCIONES DE CLU Y SPOTIFY

def consultar_clu(query):
    """Envía una consulta a Conversational Language Understanding (CLU)"""
    url = f"{CLU_ENDPOINT}/language/:analyze-conversations?api-version=2022-10-01-preview"
    
    headers = {
        "Ocp-Apim-Subscription-Key": CLU_API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "analysisInput": {
            "conversationItem": {
                "id": "1",
                "text": query,
                "modality": "text",
                "language": "es",
                "participantId": "user"
            }
        },
        "parameters": {
            "projectName": CLU_PROJECT_NAME,
            "deploymentName": CLU_DEPLOYMENT_NAME,
            "stringIndexType": "TextElement_V8"
        },
        "kind": "Conversation"
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Lanza una excepción si la respuesta es un error HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Error en la conexión con CLU: {str(e)}"}


def buscar_info_cancion(cancion):
    """Busca información sobre una canción en Spotify"""
    try:
        results = sp.search(q=f"track:{cancion}", type="track", limit=1)
        if results['tracks']['items']:
            track = results['tracks']['items'][0]
            return {
                "name": track['name'],
                "artist": track['artists'][0]['name'],
                "album": track['album']['name'],
                "release_date": track['album']['release_date'],
                "url": track['external_urls']['spotify']
            }
        return {"error": "Canción no encontrada"}
    except Exception as e:
        return {"error": f"Error en la búsqueda de la canción: {str(e)}"}


def buscar_info_artista(artista):
    """Busca información sobre un artista en Spotify"""
    try:
        results = sp.search(q=f"artist:{artista}", type="artist", limit=1)
        if results['artists']['items']:
            artist = results['artists']['items'][0]
            return {
                "name": artist['name'],
                "genres": artist['genres'],
                "followers": artist['followers']['total'],
                "url": artist['external_urls']['spotify']
            }
        return {"error": "Artista no encontrado"}
    except Exception as e:
        return {"error": f"Error en la búsqueda del artista: {str(e)}"}


def buscar_info_album(album):
    """Busca información sobre un álbum en Spotify"""
    try:
        results = sp.search(q=f"album:{album}", type="album", limit=1)
        if results['albums']['items']:
            album_info = results['albums']['items'][0]
            return {
                "name": album_info['name'],
                "artist": album_info['artists'][0]['name'],
                "release_date": album_info['release_date'],
                "url": album_info['external_urls']['spotify']
            }
        return {"error": "Álbum no encontrado"}
    except Exception as e:
        return {"error": f"Error en la búsqueda del álbum: {str(e)}"}


def buscar_cancion_por_texto(texto):
    """Busca canciones en Spotify basadas en un texto"""
    try:
        results = sp.search(q=texto, type="track", limit=5)
        return [
            {
                "name": track['name'],
                "artist": track['artists'][0]['name'],
                "url": track['external_urls']['spotify']
            }
            for track in results['tracks']['items']
        ]
    except Exception as e:
        return {"error": f"Error en la búsqueda de canciones: {str(e)}"}


def buscar_canciones_por_genero(genero):
    """Busca canciones en Spotify basadas en un género"""
    try:
        results = sp.search(q=f"genre:{genero}", type="track", limit=5)
        return [
            {
                "name": track['name'],
                "artist": track['artists'][0]['name'],
                "url": track['external_urls']['spotify']
            }
            for track in results['tracks']['items']
        ]
    except Exception as e:
        return {"error": f"Error en la búsqueda de canciones por género: {str(e)}"}


def buscar_canciones_por_artista(artista):
    """Busca canciones en Spotify basadas en un artista"""
    try:
        results = sp.search(q=f"artist:{artista}", type="track", limit=5)
        return [
            {
                "name": track['name'],
                "artist": track['artists'][0]['name'],
                "url": track['external_urls']['spotify']
            }
            for track in results['tracks']['items']
        ]
    except Exception as e:
        return {"error": f"Error en la búsqueda de canciones por artista: {str(e)}"}


def buscar_artistas_por_genero(genero):
    """Busca artistas en Spotify basados en un género"""
    try:
        results = sp.search(q=f"genre:{genero}", type="artist", limit=5)
        return [
            {
                "name": artist['name'],
                "url": artist['external_urls']['spotify']
            }
            for artist in results['artists']['items']
        ]
    except Exception as e:
        return {"error": f"Error en la búsqueda de artistas por género: {str(e)}"}


def buscar_artistas_por_cancion(cancion):
    """Busca artistas en Spotify basados en una canción"""
    try:
        results = sp.search(q=f"track:{cancion}", type="track", limit=1)
        if results['tracks']['items']:
            track = results['tracks']['items'][0]
            return [
                {
                    "name": artist['name'],
                    "url": artist['external_urls']['spotify']
                }
                for artist in track['artists']
            ]
        return {"error": "Artistas no encontrados para la canción proporcionada"}
    except Exception as e:
        return {"error": f"Error en la búsqueda de artistas por canción: {str(e)}"}


def recomendar_artistas(artista):
    """Recomienda artistas relacionados en Spotify"""
    # TODO: Revisar la lógica de la función, actualmente no encuentra artistas relacionados
    try:
        results = sp.search(q=f"artist:{artista}", type="artist", limit=1)
        if not results['artists']['items']:
            return {"error": "Artista no encontrado"}
        
        artist_id = results['artists']['items'][0]['id']
        related_artists = sp.artist_related_artists(artist_id)
        return [
            {
                "name": artist['name'],
                "url": artist['external_urls']['spotify']
            }
            for artist in related_artists['artists']
        ]
    except spotipy.exceptions.SpotifyException as e:
        if e.http_status == 404:
            return {"error": "No se encontraron artistas relacionados para el artista proporcionado"}
        return {"error": f"Error en la recomendación de artistas: {str(e)}"}
    except Exception as e:
        return {"error": f"Error en la recomendación de artistas: {str(e)}"}


def buscar_playlist_por_genero(genero):
    """Busca playlists en Spotify basadas en un género"""
    try:
        results = sp.search(q=f"genre:{genero}", type="playlist", limit=5)
        return [
            {
                "name": playlist['name'],
                "url": playlist['external_urls']['spotify']
            }
            for playlist in results['playlists']['items']
        ]
    except Exception as e:
        return {"error": f"Error en la búsqueda de playlists por género: {str(e)}"}


def manejar_recomendacion(intencion, entidades):
    """Maneja la recomendación basada en la intención y las entidades detectadas"""
    # Inicializa las variables para almacenar los valores de las entidades
    entidad_map = {
        'Genre': None,
        'Mood': None,
        'Activity': None,
        'Artist': None,
        'Song': None,
        'Album': None
    }

    # Extrae las entidades de la respuesta
    for entidad in entidades:
        if isinstance(entidad, dict):
            categoria = entidad.get('category', '')
            texto = entidad.get('text', '')
            if categoria in entidad_map:
                entidad_map[categoria] = texto

    genero_detectado = entidad_map['Genre']
    estado_animo_detectado = entidad_map['Mood']
    actividad_detectada = entidad_map['Activity']
    artista_detectado = entidad_map['Artist']
    cancion_detectada = entidad_map['Song']
    album_detectado = entidad_map['Album']

    # Recomendaciones basadas en la intención

    if intencion == "GetSongRecommendation":
        recomendaciones = []
        if estado_animo_detectado:
            recomendaciones.extend(buscar_cancion_por_texto(estado_animo_detectado))
        if actividad_detectada:
            recomendaciones.extend(buscar_cancion_por_texto(actividad_detectada))
        if genero_detectado:
            recomendaciones.extend(buscar_canciones_por_genero(genero_detectado))
        if artista_detectado:
            recomendaciones.extend(buscar_canciones_por_artista(artista_detectado))

        if recomendaciones:
            return f"Recomendaciones de canciones:\n" + "\n".join(
                [f"- {c['name']} de {c['artist']} [Escuchar en Spotify]({c['url']})" for c in recomendaciones])
        else:
            return "No se encontraron canciones para las entidades proporcionadas."

    elif intencion == "GetArtistRecommendation":
        recomendaciones = []
        if genero_detectado:
            recomendaciones.extend(buscar_artistas_por_genero(genero_detectado))
        if cancion_detectada:
            recomendaciones.extend(buscar_artistas_por_cancion(cancion_detectada))
        if artista_detectado:
            artistas_recomendados = recomendar_artistas(artista_detectado)
            if isinstance(artistas_recomendados, list):
                recomendaciones.extend(artistas_recomendados)
            else:
                return artistas_recomendados  # Devuelve un mensaje de error

        if recomendaciones:
            return f"Artistas recomendados:\n" + "\n".join(
                [f"- {a['name']} [Escuchar en Spotify]({a['url']})" for a in recomendaciones])
        else:
            return "No se encontraron artistas para las entidades proporcionadas."

    elif intencion == "GetPlaylistRecommendation":
        if genero_detectado:
            playlists = buscar_playlist_por_genero(genero_detectado)
            if playlists:
                return f"Playlists recomendadas:\n" + "\n".join(
                    [f"- {p['name']} [Escuchar en Spotify]({p['url']})" for p in playlists])
        return "No se encontraron playlists para las entidades proporcionadas."

    # Información detallada basada en la intención

    elif intencion == "GetSongInfo" and cancion_detectada:
        info_cancion = buscar_info_cancion(cancion_detectada)
        if "error" in info_cancion:
            return info_cancion["error"]
        return f"Información de la canción:\n- Nombre: {info_cancion['name']}\n- Artista: {info_cancion['artist']}\n- Álbum: {info_cancion['album']}\n- Fecha de lanzamiento: {info_cancion['release_date']}\n- [Escuchar en Spotify]({info_cancion['url']})"

    elif intencion == "GetArtistInfo" and artista_detectado:
        info_artista = buscar_info_artista(artista_detectado)
        if "error" in info_artista:
            return info_artista["error"]
        return f"Información del artista:\n- Nombre: {info_artista['name']}\n- Géneros: {', '.join(info_artista['genres'])}\n- Seguidores: {info_artista['followers']}\n- [Escuchar en Spotify]({info_artista['url']})"

    elif intencion == "GetAlbumInfo" and album_detectado:
        info_album = buscar_info_album(album_detectado)
        if "error" in info_album:
            return info_album["error"]
        return f"Información del álbum:\n- Nombre: {info_album['name']}\n- Artista: {info_album['artist']}\n- Fecha de lanzamiento: {info_album['release_date']}\n- [Escuchar en Spotify]({info_album['url']})"

    return "Intención no reconocida o falta de datos suficientes para la recomendación."


def app():
    """Función principal de la aplicación de Streamlit"""
    st.set_page_config(page_title="SpotifAI", page_icon="favicon.ico")
    st.title("Spotif:green[AI] Chatbot")

    # Inicializa el historial de chat
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Función para agregar mensajes al historial de chat
    def add_message(sender, message):
        st.session_state.chat_history.append({"sender": sender, "message": message})

    # Ingreso de consulta
    query = st.chat_input("Consulta información o recomendaciones musicales...")

    if query:
        add_message("Usuario", query)
        resultado_clu = consultar_clu(query)

        if "error" in resultado_clu:
            add_message("SpotifAI", resultado_clu["error"])
        else:
            intencion = resultado_clu["result"]["prediction"]["topIntent"]
            entidades = resultado_clu["result"]["prediction"].get("entities", [])

            # Mostrar la intención y las entidades para la depuración en un desplegable
            with st.expander("Detalles de la consulta"):
                st.write(f"**:orange[Intención detectada:]** {intencion}")
                st.write(f"**:orange[Entidades detectadas:]** {entidades}")

            respuesta_recomendacion = manejar_recomendacion(intencion, entidades)
            add_message("SpotifAI", respuesta_recomendacion)

    # Mostrar el historial de chat
    for chat in st.session_state.chat_history:
        if chat["sender"] == "Usuario":
            st.chat_message("Usuario").write(chat["message"])
        else:
            st.chat_message("SpotifAI").write(chat["message"])


# Ejecución de la app de Streamlit
if __name__ == "__main__":
    app()
