#Librerias
import requests
from flask import Flask, jsonify, request

#Inicialización
app = Flask(__name__)

#Ruta para obtener la información
@app.route('/api/nombre/<string:nombre>', methods=['GET'])

#Función para obtener la información de un pokemon
def getPokemon(nombre):
    #Url desde que se obtendra la información
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre}/"
    try:
        #Pedido de la información al API
        respuesta = requests.get(url)
        #Verificación de la respuesta
        respuesta.raise_for_status()
        info = respuesta.json()
        infoF = {
            "nombre": info.get("name"),
            "altura": info.get("height"),
            "peso": info.get("weight"),
            "tipo(s)": info.get("types")
        }
        return jsonify(infoF)
    #Excepción en caso de que se presente un error de cliente o servidor
    except requests.exceptions.HTTPError as err:
        if respuesta.status_code == 404:
            return jsonify({"error": "Pokemon no encontrado"}), 404
        else:
            return jsonify({"error": "Error en la solicitud a la API"}), 500
    #Excepción por falta de conexión
    except requests.exceptions.RequestException:
        return jsonify({"error": "No se pudo conectar con la API"}), 503
    #Otras excepciones
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#Ruta para obtener la información
@app.route('/filtroTipo', methods=['POST'])

#Función que enlista los nombres de diferentes Pokemon y su forma de encontrar basado en el tipo
def filtroTipo():
    #Json con el tipo
    filtro = request.get_json()
    #Lista con la información buscada
    pokemonF = []
    #Url desde que se obtendra la información
    url = f'https://pokeapi.co/api/v2/type/{filtro["type"]}'
    try:
        #Pedido de la información al API
        respuesta = requests.get(url)
        #Verificación de la respuesta
        respuesta.raise_for_status()
        info = respuesta.json()
        #Enlista los pokemon obtenidos previamente
        for pokemon in info['pokemon']:
            #Obtención de la información del pokemon
            respuestaU = requests.get(pokemon['pokemon']['url'])
            infoU = respuestaU.json()
            #Información completa que se enviara a la lista
            infoT = {
                "Nombre": infoU.get("name"),
                "Forma de encontrar": infoU.get("location_area_encounters")
            }
            pokemonF.append(infoT)
        return jsonify({'Pokemon Filtrados': pokemonF}), 200
    #Excepción en caso de que se presente un error de cliente o servidor
    except requests.exceptions.HTTPError as err:
        if respuesta.status_code == 404:
            return jsonify({"error": "Tipo no encontrado"}), 404
        else:
            return jsonify({"error": "Error en la solicitud a la API"}), 500
    #Excepción por falta de conexión
    except requests.exceptions.RequestException:
        return jsonify({"error": "No se pudo conectar con la API"}), 503
    #Otras excepciones
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#Main
if __name__ == '__main__':
    app.run(debug=True)
