import requests
import json

def obtener_juegos():
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
        return games
