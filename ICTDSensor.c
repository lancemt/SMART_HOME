 /*
 * ICTDSensor.c
 *
 * Driver to interface the RHT03 (MaxDetect Technology) sensor  on a Raspberry
 * Pi SBC to the Home Monitor
 *
 ******************************************************************************
 * (C) 2017 Team Bronte, UTS 48481 ICTD
 *
 * This file depends on, and is derived from portions of the wiringPi library, 
 * which is licensed under GNU LGPL 3.0.
 *
 * wiringPi is copyright (c) 2012-2013 Gordon Henderson. <projects@drogon.net>
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <wiringPi.h>
#include <maxdetect.h>

#define RHT03_PIN   7

static const int SENSOR_MIN_TEMP = -400;
static const int SENSOR_MAX_TEMP = 800;
static const int SENSOR_CODE_DIVISOR = 10;

void CheckUser(void);

/*
 ***********************************************************************
 * The main program
 ***********************************************************************
 */

int main(void)
{
    int result, temp, rh, sensorID = 1;
    int minT, maxT;
    
    FILE *currentFilePointer;
    FILE *newFilePointer;
    FILE *initFilePointer;

    CheckUser();

    wiringPiSetup();
    piHiPri(55); // Requires root
    
    // Create blank file if one does not already exist, or later code will flip
    // out
    initFilePointer = fopen("/var/www/html/SensorData.csv", "w+");
    fclose(initFilePointer);
  
    for (;;)
    {
        // Slow down sensor read interval
        delay(1000);
    
        char timeStamp[20];
        time_t now = time(NULL);
    
        strftime(timeStamp, 20, "%Y-%m-%dT%H:%M:%S", localtime(&now));

        // Sensor can only be read every 2000ms, returns last known good result
        // if sample interval too low
        result = readRHT03(RHT03_PIN, &temp, &rh);
    
        if (!result)
        {
            // Sensor read error, print to stdout and continue
            printf(".");
            fflush(stdout);
            continue;
        }

        // Cap sensor reading to sane values
        if (temp < SENSOR_MIN_TEMP)
            temp = SENSOR_MIN_TEMP;
        if (temp > SENSOR_MAX_TEMP)
            temp = SENSOR_MAX_TEMP;

        // Copy contents of existing file to a new one
        currentFilePointer = fopen("/var/www/html/SensorData.csv", "r"); // Read only
        newFilePointer = fopen("/var/www/html/SensorData2.csv", "w+"); // Truncate, and write

        while((ch = fgetc(currentFilePointer)) != EOF) // Copy contents until EOF
        {
            fputc(ch, newFilePointer);
        }

        fclose(currentFilePointer);
        fclose(newFilePointer);

        // Yes this is inefficient, but I'm coding blind and am not sure of the
        // fprintf behaviour... feel free to modify once tested.
        newFilePointer = fopen("/var/www/html/SensorData2.csv", "a");
        fprintf(newFilePointer, "%f,%d,%s", temp / SENSOR_CODE_DIVISOR, sensorID, timeStamp);
        fclose (newFilePointer);

        // Atomic on POSIX ONLY, will FAIL on other OSs
        rename("/var/www/html/SensorData2.csv", "/var/www/html/SensorData.csv")
    }

    return 0;
}

/*
 ***********************************************************************
 * Check script is running with root privileges, exit if not
 ***********************************************************************
 */
void CheckUser(void)
{
    if (geteuid() != 0)
    {
        printf("Please re-run with root permissions to set priority to (near) real time")
        exit(1)
    }
}
