# Based on code from https://pypi.python.org/pypi/paho-mqtt/1.1#installation

import paho.mqtt.client as mqtt
from SmartHome.Common.Event import Event

# Constants
server = "iot.eclipse.org"  # URL for broker
qos = 2  # Quality of Service level


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected to broker!")

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("events", qos)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    if msg.topic == "events":
        print("Received packet with payload: " + str(msg.payload))
        event = Event.from_json(str(msg.payload.decode("utf-8")))
        process_event(event)


def process_event(event):
    # Stub for testing
    print("Received event with ID: " + event.event_id)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
