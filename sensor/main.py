
from ruuvitag_sensor.ruuvi import RuuviTagSensor
import paho.mqtt.client as mqtt
import json

def handle_data(found_data):
    merged = {"mac": found_data[0]}
    merged.update(found_data[1])

    client.connect("localhost")
    print(merged)
    msgInfo = client.publish("sensors", json.dumps(merged))
    if False == msgInfo.is_published():
        msgInfo.wait_for_publish()
    client.disconnect()

client = mqtt.Client("1")
RuuviTagSensor.get_datas(handle_data)
