from SmartHome.Common.Event import Event
from SmartHome.HomeMonitor.MqttPublisher import MqttPublisher
import time

publisher = MqttPublisher("ABCDEF12345")

# Publish event
e = Event("Event1", "Non-Critical", "Some Description", "12:00", "HM1", "SENS-1")
publisher.publish_event(e)
time.sleep(300)