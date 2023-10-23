import streamlit as st

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
