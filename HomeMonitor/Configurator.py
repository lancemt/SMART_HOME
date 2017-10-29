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


class Configurator:

    def __init__(self, filepath):
        self.path = filepath

        # Load the .csv file to count the columns.
        self.csvdataframe = pd.read_csv ( filepath )

        # Count the columns.
        #calculate size
        self.size = (self.csvdataframe).shape[0]

        #self.row_count = sum(1 for row in self.csvdataframe)
        self.colnames = ['SensorValue', 'SensorID', 'TIMESTAMP']

        # Re-load the .csv file, manually setting the column names
        self.csvdataframefinal = pd.read_csv ( filepath, names=self.colnames, skiprows = (self.size - 10), header=None )


    def csvdataframe(self):
        df1 = self.csvdataframefinal
        return df1

    def Mean_Sensor_Value(self):
        MeanSensorValue = self.csvdataframefinal.loc[self.csvdataframefinal['SensorID'] == 1, 'SensorValue'].mean()
        return MeanSensorValue

    def Time_Stamp(self):
        TimeStamp = self.csvdataframefinal.iloc[0]['TIMESTAMP']
        return TimeStamp

    # capture sensorID
    def SensorID(self):
        SensorID = self.csvdataframefinal.iloc[0]['SensorID']
        return SensorID

    # simple rules engine
    def Rule_Engine(self,r):
        if r.Mean_Sensor_Value() > 22.5 and  r.Mean_Sensor_Value() <= 23.5:
            return "Non Critical"
        elif r.Mean_Sensor_Value()> 23.5 and r.Mean_Sensor_Value() <= 24.5:
            return "Urgent"
        elif r.Mean_Sensor_Value () > 24.5:
            return "Critical"
        else:
            return "None"
