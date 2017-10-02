import time
from SmartHome.Common.Event import Event
from SmartHome.HomeMonitor.MqttPublisher import MqttPublisher

publisher = MqttPublisher("ABCDEF12345")

e = Event("Event1", "Non-Critical", "Some Description", "12:00", "HM1", "SENS-1")
publisher.publish_event(e)

# Give time for the event to be published, leave MQTT publisher open for disconnect events etc.
# Real HM code will loop infinitely
time.sleep(300)
