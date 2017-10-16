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

class Configurator:

    def __init__(self, filepath):
        self.path = filepath

        # Load the .csv file to count the columns.
        self.csvdataframe = pd.read_csv ( filepath )
        # Count the columns.
        self.numcolumns = len ( self.csvdataframe.columns )
        #calculate size
        #self.size = sum ( 1 for l in open ( filepath) )
        self.size = sum (1 for l in self.csvdataframe)
        self.colnames = ['SensorValue', 'SensorID', 'TIMESTAMP']

        # Re-load the .csv file, manually setting the column names
        self.csvdataframe = pd.read_csv ( filepath, names=self.colnames, skiprows=range ( 1, self.size - 10 ), header=None )

    def csvdataframe(self):
        df1 = self.csvdataframe

        return df1

    def Mean_Sensor_Value(self):
        MeanSensorValue = self.csvdataframe.loc[self.csvdataframe['SensorID'] == 1, 'SensorValue'].mean()
        return MeanSensorValue

    def Time_Stamp(self):
        TimeStamp = self.csvdataframe.iloc[0]['TIMESTAMP']
        return TimeStamp

    # capture sensorID
    def SensorID(self):
        SensorID = self.csvdataframe.iloc[0]['SensorID']
        return SensorID

    # simple rules engine
    def Rule_Engine(self,r):

        if 20 < r.Mean_Sensor_Value() <= 25:
            return "Urgent"
        if 10 < r.Mean_Sensor_Value() < 20:
            return "Critical"
        else:
            return "Non Critical"


#testing-----------------------

r = Configurator("http://192.168.43.64/SensorData.csv")


print(r.Mean_Sensor_Value(),r.Time_Stamp(),r.SensorID(), r.Rule_Engine(r))
print(r.csvdataframe)
