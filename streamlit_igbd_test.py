import streamlit as st
import requests
import json

# Título de la página
st.title("50 videojuegos que deberías probar")

# URL de la API de IGDB
url = "https://api.igdb.com/v4/games"

# Tus credenciales para la API de IGDB
headers = {
    'Client-ID': 'ju1vfy05jqstzoclqv1cs2hsomw1au',
    'Authorization': 'Bearer 8h1ymcezojqdpcvmz5fvwxal2myoxp',
}

# Parámetros de la consulta a la API de IGDB
body = 'fields name,cover.url; limit 50;'

response = requests.post(url, headers=headers, data=body)

# Comprueba si la solicitud fue exitosa
if response.status_code == 200:
    # Convierte la respuesta en JSON
    games = json.loads(response.text)

    # Muestra los juegos en Streamlit
    for game in games:
        st.header(game['name'])
        if 'cover' in game:
            # La API de IGDB devuelve las URLs de las imágenes en un formato especial
            # Necesitamos convertirlo a una URL completa
            image_url = game['cover']['url'].replace('t_thumb', 't_cover_big')
            image_url = 'https:' + image_url
            st.image(image_url)
        else:
            st.write("Hubo un error al obtener los datos de la API de IGDB.")
