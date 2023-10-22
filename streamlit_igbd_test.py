import streamlit as st
import requests
import json
import streamlit_session_state as SessionState

# Título de la página
st.title("50 videojuegos que deberías probar")

# URL de la API de IGDB
url = "https://api.igdb.com/v4/games"

# Tus credenciales para la API de IGDB
headers = {
    'Client-ID': 'ju1vfy05jqstzoclqv1cs2hsomw1au',
    'Authorization': 'Bearer 8h1ymcezojqdpcvmz5fvwxal2myoxp',
}

@st.cache(allow_output_mutation=True)
def get_games():
    # Parámetros de la consulta a la API de IGDB
    body = 'fields name,cover.url; limit 100; sort rating desc; where rating > 70; where rating_count > 1000;'
    response = requests.post(url, headers=headers, data=body)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return []

games = get_games()

# Inicializa el estado de la sesión
state = SessionState.get(game_id=None)

# Muestra los juegos en Streamlit
for game in games:
    if 'cover' in game:
        image_url = game['cover']['url'].replace('t_thumb', 't_cover_big')
        image_url = 'https:' + image_url

        # Muestra la imagen y el nombre del juego
        st.image(image_url)
        st.write(game['name'])

        # Añade un botón para mostrar más detalles
        if st.button(f"Más detalles sobre {game['name']}"):
            state.game_id = game["id"]

if state.game_id is not None:
    # Realiza una nueva solicitud a la API de IGDB para obtener más detalles sobre el juego
    body = f'fields name,summary,developers.name,publishers.name,platforms.name; where id = {state.game_id};'
    response = requests.post(url, headers=headers, data=body)
    if response.status_code == 200:
        game_details = json.loads(response.text)[0]

        # Muestra los detalles del juego
        st.write(f"Resumen: {game_details['summary']}")
        st.write(f"Desarrollador: {', '.join(dev['name'] for dev in game_details['developers'])}")
        st.write(f"Editor: {', '.join(pub['name'] for pub in game_details['publishers'])}")
        st.write(f"Plataformas: {', '.join(plat['name'] for plat in game_details['platforms'])}")

# Información de los desarrolladores
developers = [
    {"name": "Juan Garbiel Goez Duque", "email": "jgoezd@unal.edu.co"},
    {"name": "Jerónimo Vásquez Gónzales", "email": "jevasquez@unal.edu.co"},
    {"name": "Marycielo Berrio Zapata", "email": "mberrioz@unal.edu.co"},
]

# Crea el HTML para el pie de página
footer_html = """
<footer style='width: 100%; background-color: #333; padding: 20px 0; color: #fff;'>
    <div style='max-width: 600px; margin: auto; text-align: left;'>
        <h2 style='margin-bottom: 20px;'>Información de contacto</h2>
"""

for dev in developers:
    footer_html += f"<p style='margin-bottom: 10px;'><strong>{dev['name']}</strong>: <a href='mailto:{dev['email']}' style='color: #fff;'>{dev['email']}</a></p>"

footer_html += """
    </div>
</footer>
"""

# Agrega un espacio en blanco al final de la página antes del pie de página
st.write("<br/><br/><br/><br/>", unsafe_allow_html=True)

# Muestra el pie de página en Streamlit
st.markdown(footer_html, unsafe_allow_html=True)
