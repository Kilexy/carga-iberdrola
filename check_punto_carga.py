import time
import sys

def verificar_punto_carga():
    print("🔄 Script iniciado en GitHub Actions...", flush=True)
    start_time = time.time()

    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time > 300:  # 🔹 Detener después de 5 minutos
            print("⏹️ Deteniendo script para evitar bloqueos.", flush=True)
            break

        print("⏳ Revisando disponibilidad de puntos de carga...", flush=True)

        # 🔹 Aquí iría el código que revisa la API o la web de Iberdrola.
        # 🔹 Si hay cargadores libres, enviaría la notificación.

        print("⛔ No hay puntos libres. Reintentando en 30 segundos...", flush=True)
        sys.stdout.flush()  # 🔹 Forzar la salida inmediata en GitHub Actions

        time.sleep(30)  # Espera 30 segundos antes de volver a verificar

# Ejecutar la función
verificar_punto_carga()
