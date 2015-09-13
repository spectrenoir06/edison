import socket
import os
import sys
from time import sleep
import mraa
from globals import *
import pyupm_mma7660 as upmMMA7660

ACTIVITY_TRES = 50

myDigitalAccelerometer, x, y, z


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


def accProc(message):
    global buffer
    global Alert
    myDigitalAccelerometer.getRawValues(x, y, z)
    buffer += "x=" + str(upmMMA7660.intp_value(x)) + ", y=" + str(upmMMA7660.intp_value(y)) + ", z=" + \
              str(upmMMA7660.intp_value(z))
    if (x*x + y*y + z*z) < ACTIVITY_TRES:
        return False
    else:
        message.append(Alert.ACTIVE)
        return True

