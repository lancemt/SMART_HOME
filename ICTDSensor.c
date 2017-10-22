/*
 * rht03.c:
 *	Driver for the MaxDetect series sensors
 *
 * Copyright (c) 2012-2013 Gordon Henderson. <projects@drogon.net>
 ***********************************************************************
 * This file is part of wiringPi:
 *	https://projects.drogon.net/raspberry-pi/wiringpi/
 *
 *    wiringPi is free software: you can redistribute it and/or modify
 *    it under the terms of the GNU Lesser General Public License as published by
 *    the Free Software Foundation, either version 3 of the License, or
 *    (at your option) any later version.
 *
 *    wiringPi is distributed in the hope that it will be useful,
 *    but WITHOUT ANY WARRANTY; without even the implied warranty of
 *    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *    GNU Lesser General Public License for more details.
 *
 *    You should have received a copy of the GNU Lesser General Public License
 *    along with wiringPi.  If not, see <http://www.gnu.org/licenses/>.
 ***********************************************************************
 */

#include <stdio.h>
#include <time.h>
#include <wiringPi.h>
#include <maxdetect.h>

#define RHT03_PIN   7

static const int SENSOR_MIN_TEMP = -400;
static const int SENSOR_MAX_TEMP = 800;
static const int SENSOR_CODE_DIVISOR = 10;

/*
 ***********************************************************************
 * The main program
 ***********************************************************************
 */

int main (void)
{
    int result, temp, rh, sensorID = 1;
    int minT, maxT;

    wiringPiSetup();
    piHiPri       (55);
    FILE *filePointer;
  
    for (;;)
    {
        filePointer = fopen("/var/www/html/SensorData.csv", "a");
    
        delay (1000);
    
        char timeStamp[20];
        time_t now = time(NULL);
    
        strftime(timeStamp, 20, "%Y-%m-%dT%H:%M:%S", localtime(&now));

        // Sensor can only be read every 2000ms, returns last known good result if sample interval too low
        result = readRHT03 (RHT03_PIN, &temp, &rh);
    
        if (!result)
        {
            // Sensor read error, print to stdout and continue
            printf (".");
            fflush (stdout);
            continue;
        }

        // Cap sensor reading to sane values
        if (temp < SENSOR_MIN_TEMP)
            temp = SENSOR_MIN_TEMP;
        if (temp > SENSOR_MAX_TEMP)
            temp = SENSOR_MAX_TEMP;

        fprintf(filePointer, "%f,%d,%s", temp / SENSOR_CODE_DIVISOR, sensorID, timeStamp);
        fclose(filePointer);
    }

    return 0;
}
