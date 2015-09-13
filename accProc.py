import socket
import os
import sys
from time import sleep
import mraa
from globals import *
import pyupm_mma7660 as upmMMA7660

ACTIVITY_TRES = 50

myDigitalAccelerometer, x, y, z = None, None, None, None


def initAcc():
    global myDigitalAccelerometer, x, y, z
    # Init Accelerometer connexion
    myDigitalAccelerometer = upmMMA7660.MMA7660(upmMMA7660.MMA7660_I2C_BUS, upmMMA7660.MMA7660_DEFAULT_I2C_ADDR)
    myDigitalAccelerometer.setModeStandby()
    myDigitalAccelerometer.setSampleRate(upmMMA7660.MMA7660.AUTOSLEEP_64)
    myDigitalAccelerometer.setModeActive()
    x = upmMMA7660.new_intp()
    y = upmMMA7660.new_intp()
    z = upmMMA7660.new_intp()
    print("Acc init")


def alertAcc(message, buffer):
    global Alert
    myDigitalAccelerometer.getRawValues(x, y, z)
    valx = upmMMA7660.intp_value(x)
    valy = upmMMA7660.intp_value(y)
    valz = upmMMA7660.intp_value(z)
    buffer.append(str(valx) + ", " + str(valy) + ", " + str(valz))
    if (valx*valx + valy*valy + valz*valz) < ACTIVITY_TRES:
        return False
    else:
        message.append(Alert.ACTIVE)
        return True

