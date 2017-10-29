import time
import uuid
from SmartHome.Common.Event import Event
from SmartHome.HomeMonitor.MqttPublisher import MqttPublisher
from SmartHome.HomeMonitor.Configurator import Configurator

publisher = MqttPublisher("ABCDEF12345")

eventStatusUnique = "None"
while(1):
    
# /Users/UTS/Desktop/ICT-D/SensorData.csv --> should be changed to csv file locationwhile(1): http://192.168.43.64/SensorData.csv

    r = Configurator("http://192.168.43.64/SensorData.csv")
    eventStatus = r.Rule_Engine(r)
    Sensorvalue = r.Mean_Sensor_Value()
    TimeStamp = r.Time_Stamp()
    SensorID = r.SensorID()
    Description = "Sensor with Sensor ID " + str(SensorID) + " has showed temperature change which triggered an event (" + eventStatus + ") in HM1 at " + str(TimeStamp)
    if (eventStatus == eventStatusUnique) or (eventStatus == "None"):
        continue
    else:
       eventStatusUnique = eventStatus
       e = Event(str(uuid.uuid4()), str(eventStatus), str(Description), str(TimeStamp), "HM1", str(SensorID))
       publisher.publish_event(e)
    # Give time for the event to be published, leave MQTT publisher open for disconnect events etc.
    # Real HM code will loop infinitely
    time.sleep(1)
