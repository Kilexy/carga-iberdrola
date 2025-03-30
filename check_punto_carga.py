import requests
import time
import telegram_send

# URL de la API de Iberdrola (REEMPLAZA con la URL que copiaste)
URL_API = "https://www.iberdrola.es/o/webclipb/iberdrola/puntosrecargacontroller/getDatosPuntoRecarga"

# ID del punto de carga que quieres monitorear
PUNTO_CARGA_ID = "132898"

def check_availability():
    try:
        # Realiza la petición a la API
        response = requests.get(URL_API)
        data = response.json()  # Convierte la respuesta en JSON
        
        # Busca el punto de carga por su ID
        for punto in data["puntos"]:
            if str(punto["id"]) == PUNTO_CARGA_ID:
                disponible = punto["disponibles"]  # Número de cargadores libres
                
                if disponible > 0:
                    telegram_send.send(messages=[f"⚡ ¡Punto de carga disponible! ({disponible} libres)"])
                else:
                    print("⛔ No hay puntos libres.")

    except Exception as e:
        print(f"Error al obtener datos: {e}")

# Ejecutar la función cada 30 segundos
while True:
    check_availability()
    time.sleep(30)
