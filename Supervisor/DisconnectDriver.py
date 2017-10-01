# Based on code from https://pypi.python.org/pypi/paho-mqtt/1.1#installation

import paho.mqtt.client as mqtt
import time
from SmartHome.Common.DisconnectEvent import DisconnectEvent

# Constants
server = "iot.eclipse.org"  # URL for broker
qos = 2  # Quality of Service level


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected to broker!")


client = mqtt.Client()
client.on_connect = on_connect

client.connect("iot.eclipse.org", 1883, 60)
time.sleep(5)  # Block to allow some time to connect to server

#disconnect = DisconnectEvent("iot.eclipse.org")
disconnect = DisconnectEvent("broker.hivemq.com")
client.publish("disconnect/ABCDEF12345", str(disconnect.to_json()), 2)

print("Sent disconnect event!")

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
