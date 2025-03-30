import requests
from bs4 import BeautifulSoup

URL = "https://www.iberdrola.es/o/webclipb/iberdrola/puntosrecargacontroller/getDatosPuntoRecarga"

def obtener_estado_cargador():
    response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        # 🔹 Aquí debes encontrar el elemento que indica la disponibilidad (esto depende de la estructura de la web).
        estado = soup.find("statusCode")  
        
        if estado and "libre" in estado.text.lower():
            return True  # ✅ Hay un cargador libre
        else:
            return False  # ❌ No hay cargadores libres
    else:
        print("⚠️ Error al acceder a la web de Iberdrola.")
        return False

# Prueba si funciona:
print("🔍 Verificando disponibilidad...")
if obtener_estado_cargador():
    print("✅ Hay un cargador libre")
else:
    print("⛔ No hay cargadores libres")
