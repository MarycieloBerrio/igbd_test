import streamlit as st
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


# Configura tu clave API de IGDB
api_key = '8h1ymcezojqdpcvmz5fvwxal2myoxp'

# Define la URL y los encabezados para la solicitud de la API
url = 'https://api.igdb.com/v4/games'
headers = {'Client-ID': 'ju1vfy05jqstzoclqv1cs2hsomw1au', 'Authorization': f'Bearer {api_key}'}

# Crea una barra de búsqueda en Streamlit
game_name = st.text_input('Busca un videojuego')

# Si se introduce un nombre de juego, busca la información del juego
if game_name:
    # Define la consulta para buscar el juego
    body = f'''
    fields name, summary, developer, publisher, platforms;
    where name ~ "{game_name}";'''
    
    # Realiza la solicitud a la API
    response = requests.post(url, headers=headers, data=body)
    
    # Devuelve los datos del juego
    game_info = response.json()
    
    # Verifica si game_info contiene algún elemento
    if game_info:
        # Muestra la información del juego en Streamlit
        st.write(f"**Nombre:** {game_info[0]['name']}")
        st.write(f"**Sinopsis:** {game_info[0]['summary']}")
        st.write(f"**Desarrollador:** {game_info[0]['developer']}")
        st.write(f"**Editor:** {game_info[0]['publisher']}")
        st.write(f"**Plataformas:** {', '.join(game_info[0]['platforms'])}")
    else:
        st.write("Lo siento, no pude encontrar ningún juego con ese nombre.")
