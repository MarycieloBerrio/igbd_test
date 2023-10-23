import streamlit as st
from back_top50 import obtener_juegos

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
        
        /* ---------- Main page hacks ---------- */
        
        section[tabindex=0] div.stButton {
            left: -999em;
            position: absolute;
            /* yeah...this is a very hacky way to send buttons probably to mars */
        }
        
        h3 {
            color: #756760;
            margin-bottom: 1rem;
        }
        
    </style>
    """, unsafe_allow_html=True)

# URL de la imagen del encabezado
url_imagen = "https://i.imgur.com/qQH31fg.png?1"

# Añade la imagen como encabezado de la aplicación de Streamlit
st.image(url_imagen)

# Obtiene los juegos desde el back-end
games = obtener_juegos()

# Contador para llevar un registro de cuántos juegos se han mostrado
count = 0

# Inicializa la fila HTML con el estilo de borde
row_html = "<table style='border-color: #fff;'><tr>"

# Muestra los juegos en Streamlit
for game in games:
    if 'cover' in game and count < 50:
        image_url = game['cover']['url'].replace('t_thumb', 't_cover_big')
        image_url = 'https:' + image_url

        # Incrementa el contador
        count += 1

        # Añade el juego a la fila HTML
        row_html += f"<td style='border-top: 1px solid #e7e7e7; border-bottom: 1px solid #e7e7e7; \
                    border-left: 1px solid #0e1117; border-right: 1px solid #0e1117; width: \
                    100px; height: 200px; text-align: center; vertical-align: top;'><img src='\
                    {image_url}'style='width: 100px; object-fit: contain;'/><br/><div style=\
                    'width: 100px; word-wrap: break-word;color: #e7e7e7;'>{game['name']}</div></td>"

        # Si se han añadido tres juegos a la fila, muestra la fila y comienza una nueva
        if count % 5 == 0:
            row_html += "</tr></table>"
            st.write(row_html, unsafe_allow_html=True)
            row_html = "<table><tr>"

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
        <h2 style='margin-bottom: 20px; color: #fff;'>Informacion de contacto</h2>
"""

for dev in developers:
    footer_html += f"<p style='margin-bottom: 10px;'><strong style='color: #fff;'>\
                {dev['name']}</strong>:<a href='mailto:{dev['email']}' style='color:\
                #fff;'>{dev['email']}</a></p>"

footer_html += """
    </div>
</footer>
"""

# Agrega un espacio en blanco al final de la página antes del pie de página
st.write("<br/><br/><br/><br/>", unsafe_allow_html=True)

# Muestra el pie de página en Streamlit
st.markdown(footer_html, unsafe_allow_html=True)
