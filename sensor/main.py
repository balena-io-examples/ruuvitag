from ruuvitag_sensor.ruuvi import RuuviTagSensor
import paho.mqtt.client as mqtt
import json, os

host = os.environ.get("MQTT_HOST") or "localhost"
topic = os.environ.get("MQTT_TOPIC") or "sensors"

def handle_data(found_data):
    client.connect(host)
    print(found_data[1])
    msgInfo = client.publish(topic, json.dumps(found_data[1]))
    if False == msgInfo.is_published():
        msgInfo.wait_for_publish()
    client.disconnect()

client = mqtt.Client("1")
RuuviTagSensor.get_datas(handle_data)