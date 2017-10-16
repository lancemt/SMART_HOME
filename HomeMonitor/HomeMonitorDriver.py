import uuid
import time
from SmartHome.Common.Event import Event
from SmartHome.HomeMonitor.MqttPublisher import MqttPublisher
#from SmartHome.HomeMonitor.Configurator import Configurator

publisher = MqttPublisher("ABCDEF12345")

# /Users/UTS/Desktop/ICT-D/SensorData.csv --> should be changed to csv file location

while(1):
    r = Configurator("http://192.168.43.64/SensorData.csv")

    Sensorvalue = r.Mean_Sensor_Value()
    TimeStamp = r.Time_Stamp()
    SensorID = r.SensorID()
    eventStatus = r.Rule_Engine(r)

    if (eventStatus == "None"):
        e = Event(str(uuid.uuid4()), "dfdf", "Some Description", "12:00", "HM1", "fdfds")
        publisher.publish_event(e)

    # Give time for the event to be published, leave MQTT publisher open for disconnect events etc.
    # Real HM code will loop infinitely
    time.sleep(10)

