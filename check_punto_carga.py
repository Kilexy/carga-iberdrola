import requests
from bs4 import BeautifulSoup
import time
import telegram_send

# Url del punto de carga ajusta con la USL real.

URL = ""

def check_availability():
  response = requests.get(URL)
  soup = BeautifulSoup(response.text,"html.parser")

#Ajusta "Disponible" segun el texto que muestra la web
  if "Disponible 0/2" in soup.text:
    telegram_send.send(messages=["Punto de Carga Disponible"])
while True:
    check_availability()
    time.sleep(5) #Esperar 5 segundos
