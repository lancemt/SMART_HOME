# ------------------------------------------------------------
#
# Write simple polling loop to grab CSV file data periodically from hardcoded location,
# pass it to configurator and then transmit the event via MQTT if one is returned.
#
# Reading CSV
# Write simple “configurator” which is just if conditions
# that set priority and return nothing or an event.
# ------------------------------------------------------------

import pandas as pd
import json

 # set coloumn names
colnames = ['SensorValue', 'SensorID', 'TIMESTAMP']

size = sum(1 for l in open("/Users/UTS/Desktop/ICT-D/SensorData.csv"))

# replace with https://192.168.43.64/SensorData.csv but currently linked with my local path
df1 = pd.read_csv("/Users/UTS/Desktop/ICT-D/SensorData.csv", names=colnames, header=None, skiprows=range(1, size - 10))



#print(df1)
#print(df1.columns)

#calculate mean sensor value
def Mean_Sensor_Value(df1):
    MeanSensorValue = df1.loc[df1['SensorID'] == 1, 'SensorValue'].mean()
    return MeanSensorValue
#Take the first timestamp
def Time_Stamp(df1):
    TimeStamp = df1.iloc[0]['TIMESTAMP']
    return TimeStamp
#capture sensorID
def SensorID(df1):
    SensorID = df1.iloc[0]['SensorID']
    return SensorID


#simple rules engine
def Rule_Engine(df1):

   if 20 < Mean_Sensor_Value(df1) <= 25:
       return "Urgent"
   if 10 < Mean_Sensor_Value(df1) < 20:
       return"Critical"
   else:
       return "Non Critical"

#creating an event in form of jason
event = json.dumps(
        dict
        (
            SensorValue=str(Mean_Sensor_Value(df1)),
            TimeStamp=str(Time_Stamp(df1)),
            SensorID=str(SensorID(df1)),
            eventStatus=str(Rule_Engine(df1))
        )
    )

print(event)
