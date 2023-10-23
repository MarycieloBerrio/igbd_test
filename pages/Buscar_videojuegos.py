from streamlit_igbd_test import local_css
import streamlit as st
import pandas as pd
import requests

# Configura el título y el favicon de la página
st.set_page_config(
    page_title="Gamer's Companion 🎮",
    page_icon="🎮",
)

local_css("style.css")

# Configura tu clave API de IGDB
api_key = '8h1ymcezojqdpcvmz5fvwxal2myoxp'

def get_game_info(game_name):
    # Define la URL y los encabezados para la solicitud de la API
    url = 'https://api.igdb.com/v4/games'
    headers = {'Client-ID': 'ju1vfy05jqstzoclqv1cs2hsomw1au', 'Authorization': f'Bearer {api_key}'}

    # Define la consulta para buscar el juego
    body = f'''
    fields name, summary, involved_companies.company.name, platforms.name;
    where name ~ "{game_name}";'''
    
    # Realiza la solicitud a la API
    response = requests.post(url, headers=headers, data=body)
    
    # Devuelve los datos del juego
    return response.json()

# Crea una barra de búsqueda en Streamlit
game_name = st.text_input('Busca un videojuego')

# Si se introduce un nombre de juego, busca la información del juego
if game_name:
    game_info = get_game_info(game_name)
    
    # Muestra la información del juego en Streamlit
    if game_info:
        st.write(f"**Nombre:** {game_info[0]['name']}")
        st.write(f"**Sinopsis:** {game_info[0]['summary']}")
        st.write(f"**Desarrollador:** {game_info[0]['involved_companies'][0]['company']['name']}")
        st.write(f"**Plataformas:** {', '.join([platform['name'] for platform in game_info[0]['platforms']])}")

