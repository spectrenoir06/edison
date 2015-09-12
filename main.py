import socket
import os
import sys
from time import sleep
import mraa
import pyupm_mic as upmMicrophone 
import pyupm_mma7660 as upmMMA7660

myDigitalAccelerometer = upmMMA7660.MMA7660(upmMMA7660.MMA7660_I2C_BUS, upmMMA7660.MMA7660_DEFAULT_I2C_ADDR)

myDigitalAccelerometer.setModeStandby()
myDigitalAccelerometer.setSampleRate(upmMMA7660.MMA7660.AUTOSLEEP_64)
myDigitalAccelerometer.setModeActive()

TCP_IP = '192.168.100.62'
TCP_PORT = 1234
BUFFER_SIZE = 1024

while (1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while (1):
        try:
            s.connect((TCP_IP, TCP_PORT))
            break
        except:
            print("erreur fdp")
            sleep(1)


    s.send("login:\n")
    
    temperature = mraa.Aio(0)
    myMic = upmMicrophone.Microphone(1)
    
    threshContext = upmMicrophone.thresholdContext()
    threshContext.averageReading = 0
    threshContext.runningAverage = 0
    threshContext.averagedOver = 2
	

    print("test")   
 
    x = upmMMA7660.new_intp()
    y = upmMMA7660.new_intp()
    z = upmMMA7660.new_intp()

    i = 0;
    while (1):
       buffer = upmMicrophone.uint16Array(32)
       len = myMic.getSampledWindow(2, 32, buffer)        
       if len:
          thresh = myMic.findThreshold(threshContext, 30, buffer, len)

        
       myDigitalAccelerometer.getRawValues(x, y, z)
       
       s.send(str(temperature.read()) + ";" + str(thresh) + ", x=" + str(upmMMA7660.intp_value(x)) + ", y=" + str(upmMMA7660.intp_value(y)) + ", z=" + str(upmMMA7660.intp_value(z)) + "\n")
       i = i + 1 
       sleep(i)
    s.close()
