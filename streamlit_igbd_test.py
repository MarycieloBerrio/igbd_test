import streamlit as st
import requests
import json

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
        
        /* Aquí puedes agregar el resto del código CSS que proporcionaste */
    </style>
    """, unsafe_allow_html=True)

# URL de la imagen del encabezado
url_imagen = "https://i.imgur.com/qQH31fg.png?1"

# Añade la imagen como encabezado de la aplicación de Streamlit
st.image(url_imagen)

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
            row_html += f"<td style='border: none; width: 100px; height: 200px;text-align:\
                        center; vertical-align: top;'><img src='{image_url}'style='width: \
                        100px;object-fit: contain;'/><br/><div style='width: 100px; word-wrap:\
                        break-word;\'>{game['name']}</div></td>"

            # Si se han añadido tres juegos a la fila, muestra la fila y comienza una nueva
            if count % 5 == 0:
                row_html += "</tr></table>"
                st.write(row_html, unsafe_allow_html=True)
                row_html = "<table><tr>"

    # Si quedan juegos en la última fila, muestra la fila
    if count % 5 != 0:
        row_html += "</tr></table>"
        st.write(row_html, unsafe_allow_html=True)

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
        <h2 style='margin-bottom: 20px;'style='color: #fff;'>Información de contacto</h2>
"""

for dev in developers:
    footer_html += f"<p style='margin-bottom: 10px;'><strong>{dev['name']}</strong>:\
                    <a href='mailto:{dev['email']}' style='color: #fff;'>{dev['email']}</a></p>"

footer_html += """
    </div>
</footer>
"""

# Agrega un espacio en blanco al final de la página antes del pie de página
st.write("<br/><br/><br/><br/>", unsafe_allow_html=True)

# Muestra el pie de página en Streamlit
st.markdown(footer_html, unsafe_allow_html=True)
