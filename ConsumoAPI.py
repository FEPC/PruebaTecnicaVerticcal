#Librerias
import requests

#Nombre del pokemon que se va a buscar"
nombre = "mewtwo"
#Url desde que se obtendra la información
url = f"https://pokeapi.co/api/v2/pokemon/{nombre}/"

try:
    #Pedido de la información al API
    respuesta = requests.get(url)
    #Verificación de la respuesta
    respuesta.raise_for_status()
    info = respuesta.json()
    #Filtra la información mas relevante del pokemon
    infoF = {
        "nombre": info.get("name"),
        "altura": info.get("height"),
        "peso": info.get("weight"),
        "tipo(s)": info.get("types")
    }
    print(infoF)
#Excepción en caso de que se presente un error de cliente o servidor
except requests.exceptions.HTTPError as err:
    print(f"Error HTTP: {err}")
#Excepción por falta de conexión
except requests.exceptions.ConnectionError:
    print("Error de conexión")
#Excepción por tiempo
except requests.exceptions.Timeout:
    print("La solicitud ha tomado demaciado tiempo")
#Otras excepciones
except requests.exceptions.RequestException as err:
    print(f"Error: {err}")
