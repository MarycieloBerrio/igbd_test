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

    # Inicializa la fila HTML
    row_html = "<table><tr>"

    # Muestra los juegos en Streamlit
    for game in games:
        if 'cover' in game and count < 50:
            image_url = game['cover']['url'].replace('t_thumb', 't_cover_big')
            image_url = 'https:' + image_url
                
            # Incrementa el contador
            count += 1

            # Añade el juego a la fila HTML
            row_html += f"<td style='border: none; width: 100px; text-align: center;'><img src='{image_url}' style='width: 100px; object-fit: contain;'/><br/><div style='width: 100px; word-wrap: break-word;'>{game['name']}</div></td>"

            # Si se han añadido tres juegos a la fila, muestra la fila y comienza una nueva
            if count % 3 == 0:
                row_html += "</tr></table>"
                st.write(row_html, unsafe_allow_html=True)
                row_html = "<table><tr>"

    # Si quedan juegos en la última fila, muestra la fila
    if count % 3 != 0:
        row_html += "</tr></table>"
        st.write(row_html, unsafe_allow_html=True)
