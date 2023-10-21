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
body = 'fields name,cover.url; limit 100; sort rating desc; where rating > 70; where rating_count > 1000;'

response = requests.post(url, headers=headers, data=body)

# Comprueba si la solicitud fue exitosa
if response.status_code == 200:
    # Convierte la respuesta en JSON
    games = json.loads(response.text)

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
                # Aquí puedes añadir el código para mostrar más detalles sobre el juego
                st.write(f"Mostrando más detalles sobre {game['name']}...")

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
