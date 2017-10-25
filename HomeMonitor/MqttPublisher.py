import time
from pymongo import MongoClient
import pprint
import paho.mqtt.client as mqtt
from SmartHome.Common.DisconnectEvent import DisconnectEvent

# Constants
server = "iot.eclipse.org"  # URL for broker
qos = 2  # Quality of Service level


class MqttPublisher:
    def __init__(self, home_monitor_id):
        self.home_monitor_id = home_monitor_id
        self.reconnect_server = ""

        # Create MQTT Client and hook on events
        self.client = mqtt.Client(home_monitor_id)
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message

        # Connect to port 1883 with keep alive time of 60
        self.client.connect(server, 1883, 60)

        # Create a background thread to handle network loop
        self.client.loop_start()
        print("Started MQTT Client for Home Monitor: " + home_monitor_id)

        time.sleep(1)  # Block to allow some time to connect to server


    def publish_event(self, event):
        # Persist raw event in home monitor and publish event
        event_json = str(event.to_json())
        self.store_in_database(event)
        self.client.publish("events", event_json, qos)
        print("\nPublished event! Data: " + event_json)


    def store_in_database(self, event):
        client = MongoClient()
        db = client.HOME_MONITOR_DB

        monitorDB = db.rawEvents
        monitorDB.insert_one(event.__dict__)
    
        print("Raw event was successfully stored in the monitor database!\n")

        #Test line for displaying added records
        pprint.pprint(monitorDB.find_one({"event_id": list(event.__dict__.values())[0]}))


    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, rc):
        print("Connected to Supervisor System!")

        # Subscribe to disconnect topic for this home monitor
        client.subscribe("disconnect/" + str(self.home_monitor_id), qos)

        # Clear state from disconnect event
        if not self.reconnect_server == "":
            self.reconnect_server = ""


    def on_disconnect(self, client, userdata, rc):
        print("Disconnected from supervisor system!")

        if not self.reconnect_server == "":
            print("Reconnecting to another broker: " + self.reconnect_server)
            client.connect(self.reconnect_server, 1883, 60)


    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        if msg.topic == "disconnect/" + str(self.home_monitor_id):
            disconnect_event = DisconnectEvent.from_json(str(msg.payload.decode("utf-8")))

            print("Received disconnect event! Disconnecting from Broker...")
            self.reconnect_server = disconnect_event.reconnect_ip_address
            client.disconnect()

 
