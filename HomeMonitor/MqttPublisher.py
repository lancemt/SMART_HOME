import paho.mqtt.client as mqtt
from SmartHome.Common.Event import Event
from SmartHome.Common.DisconnectEvent import DisconnectEvent
import time

# Constants
server = "iot.eclipse.org"  # URL for broker
qos = 2  # Quality of Service level


class MqttPublisher:
    def __init__(self, home_monitor_id):
        self.home_monitor_id = home_monitor_id

        # Create MQTT Client and hook on events
        self.client = mqtt.Client(home_monitor_id)
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message

        # Connect to port 1883 with keep alive time of 60
        self.client.connect(server, 1883, 60)

        # Create a background thread to handle network loop
        self.client.loop_start()

        time.sleep(1) # Block to allow some time to connect to server

        print("Started MQTT Client for Home Monitor: " + home_monitor_id)

    def publish_event(self, event):
        # Publish event
        event_json = str(event.to_json())
        self.client.publish("events", event_json, qos)
        print("Published event! Data: " + event_json)

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, rc):
        print("Connected to Supervisor System!")

        # Subscribe to disconnect topic for this home monitor
        client.subscribe("disconnect/" + str(self.home_monitor_id), qos)

    def on_disconnect(self, client, userdata, rc):
        print("Disconnected from supervisor system!")

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        if msg.topic == "disconnect/" + str(self.home_monitor_id):
            disconnect_event = DisconnectEvent.from_json(str(msg.payload.decode("utf-8")))

            print("Received disconnect event! Disconnecting from Broker...")
            client.disconnect()

            reconnect_server = disconnect_event.reconnect_ip_address
            if not reconnect_server  == "":
                print("Reconnecting to another broker: " + reconnect_server)
                client.connect(reconnect_server, 1883, 60)

