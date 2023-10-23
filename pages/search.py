import streamlit as st
import pandas as pd
import requests

# Configura el título y el favicon de la página
st.set_page_config(
    page_title="Gamer's Companion 🎮",
    page_icon="🎮",
)

# Forzar el tema oscuro
st.markdown("""
    <style>
        .stApp {
            background: #0e1117;
        }

        div.stTabs button {
            background: #0e1117;
        }

        .stApp header {
            background: #0e1117;
        }
        
    </style>
    """, unsafe_allow_html=True)

# Lee los datos del archivo
df = pd.read_csv('Base_datos/dataset_videojuegos.csv')

# Crea una barra de búsqueda en Streamlit
game_name = st.text_input('Busca un videojuego')

# Si se introduce un nombre de juego, busca la información del juego en el DataFrame
if game_name:
    game_info = df[df['name'] == game_name]
    
    # Muestra la información del juego en Streamlit
    if not game_info.empty:
        st.write(f"**Nombre:** {game_info.iloc[0]['name']}")
        st.write(f"**Sinopsis:** {game_info.iloc[0]['summary']}")
        st.write(f"**Desarrollador:** {game_info.iloc[0]['developer']}")
        st.write(f"**Editor:** {game_info.iloc[0]['publisher']}")
        st.write(f"**Plataformas:** {', '.join(game_info.iloc[0]['platforms'])}")
    else:
        st.write("Lo siento, no pude encontrar ningún juego con ese nombre.")
