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

# URL de la API de IGDB
url = "https://api.igdb.com/v4/games"

# Credenciales para la API de IGDB
headers = {
    'Client-ID': 'ju1vfy05jqstzoclqv1cs2hsomw1au',
    'Authorization': 'Bearer 8h1ymcezojqdpcvmz5fvwxal2myoxp',
}

# Parámetros de la consulta a la API de IGDB
body = 'fields name,cover.url; limit 100; sort rating desc;\
        where rating > 70; where rating_count > 1000;'

response = requests.post(url, headers=headers, data=body)

# Comprueba si la solicitud fue exitosa
if response.status_code == 200:
    # Convierte la respuesta en JSON
    games = json.loads(response.text)

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
