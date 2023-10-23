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
    # Define la consulta para buscar el juego
    body = f'''
    fields name, summary, involved_companies.company.name, platforms.name, cover.url, rating;
    where name ~ "{game_name}";'''
    
    # Realiza la solicitud a la API
    response = requests.post(url, headers=headers, data=body)
    
    # Devuelve los datos del juego
    return response.json()

# Si se introduce un nombre de juego, busca la información del juego
if game_name:
    game_info = get_game_info(game_name)
    
    # Verifica si game_info contiene algún elemento
    if game_info:
        # Muestra la información del juego en Streamlit
        st.write(f"**Nombre:** {game_info[0]['name']}" if 'name' in game_info[0] else "Nombre no disponible")
        st.write(f"**Sinopsis:** {game_info[0]['summary']}" if 'summary' in game_info[0] else "Sinopsis no disponible")
        st.write(f"**Desarrollador:** {game_info[0]['involved_companies'][0]['company']['name']}" if 'involved_companies' in game_info[0] and game_info[0]['involved_companies'] else "Desarrollador no disponible")
        st.write(f"**Plataformas:** {', '.join([platform['name'] for platform in game_info[0]['platforms']])}" if 'platforms' in game_info[0] and game_info[0]['platforms'] else "Plataformas no disponibles")
        
        # Muestra la portada del juego
        if 'cover' in game_info[0] and 'url' in game_info[0]['cover']:
            image_url = 'https://images.igdb.com/igdb/image/upload/t_cover_big/' + game_info[0]['cover']['url'].split('/')[-1]
            col1.image(image_url, use_column_width=True)
        
        # Muestra la calificación del juego
        if 'rating' in game_info[0]:
            st.write(f"**Calificación:** {game_info[0]['rating']}")
    else:
        st.write("Lo siento, no pude encontrar ningún juego con ese nombre.")

