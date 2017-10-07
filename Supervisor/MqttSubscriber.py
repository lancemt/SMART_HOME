# Based on code from https://pypi.python.org/pypi/paho-mqtt/1.1#installation

from pymongo import MongoClient
import paho.mqtt.client as mqtt
from SmartHome.Common.Event import Event
from SmartHome.Common.Alarm import Alarm

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


# Converting received event into an alarm
def process_event(event):
    a = Alarm("Alarm1", event.event_id, event.home_monitor_id, event.sensor_id,
              event.time_of_event, event.description, event.state)
    print("Alarm Created!")
    store_in_database(a)


# Converting received event into an alarm
def store_in_database(alarm):
    client = MongoClient()
    db = client.SUPERVISOR_DB
    event = db.event
    new_events = [{"eventID": "1001",
                   "eventTimeStamp": "10/07/17 11:05:02",
                   "sensorID": "AGJJ74",
                   "sensorType": "temperature"}]
    result = event.insert_many(new_events)
    result.inserted_ids


# Create client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to broker
client.connect("iot.eclipse.org", 1883, 60)

# Block and process network activity
client.loop_forever()
