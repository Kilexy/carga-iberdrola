
import requests
import json

# URL de la solicitud POST
url = "https://www.iberdrola.es/o/webclipb/Iberdrola/puntosrecargacontroller/gerDatosPuntoRecarga"

# Datos de la solicitud POST (reemplaza con tus propios datos)
datos = {
    # Añade aquí los datos necesarios para la solicitud POST
    # Por ejemplo:
    "idPuntoRecarga": "12345",
    "otroDato": "valor"
}

# Realizar la solicitud POST
response = requests.post(url, json=datos)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Obtener el estado del cargador
    estado = response.json()["statusCode"]
    
    # Verificar si el cargador está libre o ocupado
    if estado == "AVAILABLE":
        print("El cargador está libre")
    elif estado == "OCCUPIED":
        print("El cargador está ocupado")
    else:
        print("Estado desconocido")
else:
    print("Error al realizar la solicitud")
