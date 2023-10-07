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
body = 'fields name,cover.url; limit 100;'

response = requests.post(url, headers=headers, data=body)

# Comprueba si la solicitud fue exitosa
if response.status_code == 200:
    # Convierte la respuesta en JSON
    games = json.loads(response.text)

    # Contador para llevar un registro de cuántos juegos se han mostrado
    count = 0

    # Muestra los juegos en Streamlit
    for game in games:
        # Si el juego tiene una imagen de portada y aún no se han mostrado 50 juegos
        if 'cover' in game and count < 50:
            st.header(game['name'])
            image_url = game['cover']['url'].replace('t_thumb', 't_cover_big')
            image_url = 'https:' + image_url
            st.image(image_url)
            
            # Incrementa el contador
            count += 1
