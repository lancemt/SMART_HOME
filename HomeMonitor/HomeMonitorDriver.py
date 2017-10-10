import time
from SmartHome.Common.Event import Event
from SmartHome.HomeMonitor.MqttPublisher import MqttPublisher
from HomeMonitor.Configurator import Configurator

publisher = MqttPublisher("ABCDEF12345")

r = Configurator("/Users/UTS/Desktop/ICT-D/SensorData.csv")
Sensorvalue = r.Mean_Sensor_Value()
TimeStamp = r.Time_Stamp()
SensorID = r.SensorID()
eventStatus = r.Rule_Engine(r)


e = (r.Mean_Sensor_Value(),r.Time_Stamp(),r.SensorID(), r.Rule_Engine())


e = Event("Event1", "Non-Critical", "Some Description", "12:00", "HM1", "SENS-1")
publisher.publish_event(e)

# Give time for the event to be published, leave MQTT publisher open for disconnect events etc.
# Real HM code will loop infinitely
time.sleep(300)
