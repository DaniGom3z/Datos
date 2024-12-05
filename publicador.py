import paho.mqtt.client as mqtt
import json
import random
import time

# Configuración del broker
BROKER = "localhost"
PUERTO = 1883
TOPICO = "avitech/sensores"

# Configura el cliente MQTT
cliente = mqtt.Client("Simulador-Publicador", protocol=mqtt.MQTTv311)
cliente.connect(BROKER, PUERTO, 60)

def generar_datos():
    return {
        "dht11": {
            "temperatura": round(random.uniform(15, 35), 2),
            "humedad": round(random.uniform(20, 80), 2),
        },
        "ultrasonico": {
            "agua": round(random.uniform(0, 50), 2),
            "comida": round(random.uniform(0, 30), 2),
        },
    }

# Publicar datos cada 5 segundos
while True:
    datos = generar_datos()
    cliente.publish(TOPICO, json.dumps(datos))
    print(f"Publicado: {datos}")
    time.sleep(5)
