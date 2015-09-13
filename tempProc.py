import socket
import os
import sys
from time import sleep
from globals import *
import mraa

#Temperature treshold
LOW_TRES = 25
HIGH_TRES = 35

temperature, degrees = 0, 0

def initTemp():
    global temperature
    temperature = mraa.Aio(0)
    print("Temp Init")


def alertTemp(message, buffer):
    global temperature
    global Alert
    global degrees
    degrees = temperature.read()
    buffer.append(str(degrees)+", ")
    if degrees < LOW_TRES:
        message.append(Alert.TEMP_LOW)
        return True
    elif degrees > HIGH_TRES:
        message.append(Alert.TEMP_HIGH)
        return True
    else:
        return False


def bufferiseTemp():
    global degrees
    return str(degrees) + "; "

