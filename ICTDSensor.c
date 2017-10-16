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

#define	RHT03_PIN	7

/*
 ***********************************************************************
 * The main program
 ***********************************************************************
 */

int main (void)
{
  int result, temp, rh, sensorID = 1;
  int minT, maxT;

  int numGood, numBad ;

  wiringPiSetup () ;
  piHiPri       (55) ;
  FILE *filePointer;
  
  
  /*time_t current_time;
  char* c_time_string;*/

  minT =  1000 ;
  maxT = -1000 ;

  /**minRH =  1000 ;
  maxRH = -1000 ;**/

  numGood = numBad = 0 ;
  
  for (;;)
  {
    filePointer = fopen("/var/www/html/SensorData.csv", "a");
    delay (1000) ;
    /*current_time = time(NULL);
    c_time_string = ctime(&current_time);*/
    char buff[20];
    time_t now = time(NULL);
    strftime(buff, 20, "%Y-%m-%dT%H:%M:%S", localtime(&now));

    result = readRHT03 (RHT03_PIN, &temp, &rh) ;
	
    if (!result)
    {
      printf (".") ;
      fflush (stdout) ;
      ++numBad ;
      continue ;
    }

    ++numGood ;

    if (temp < minT) minT = temp ;
    if (temp > maxT) maxT = temp ;

    fprintf(filePointer, "%f,%d,%s", temp / 10.0, sensorID, buff);
    fclose(filePointer);
  }

  return 0 ;
}
