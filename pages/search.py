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
