import streamlit as st
from top_50 import mostrar_pagina as mostrar_pagina_inicio
from info_juegos import mostrar_pagina as mostrar_otra_pagina

# Lista de páginas
paginas = ["Página de inicio", "Otra página"]

# Selectbox en la barra lateral para seleccionar la página
pagina_seleccionada = st.sidebar.selectbox("Elige una página", paginas)

# Mostrar la página seleccionada
if pagina_seleccionada == "Página de inicio":
    mostrar_pagina_inicio()
elif pagina_seleccionada == "Otra página":
    mostrar_otra_pagina()
