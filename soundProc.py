import socket
import os
import sys
from time import sleep
import mraa
from globals import *
import pyupm_mic as upmMicrophone
mymic, threshContext = None, None
VOLUME_THRES = 10


def initSound():
    global mymic
    global threshContext
    mymic = upmMicrophone.Microphone(1)
    threshContext = upmMicrophone.thresholdContext()
    threshContext.averageReading = 0
    threshContext.runningAverage = 0
    threshContext.averagedOver = 2
    print("Sound init")


def alertSound(message, buffer):
    global Alert
    global mymic
    buf = upmMicrophone.uint16Array(32)
    len = mymic.getSampledWindow(2, 32, buf)
    if len:
        thresh = mymic.findThreshold(threshContext, 30, buf, len)
    buffer.append(str(thresh) + ", ")
    if thresh > VOLUME_THRES:
        message.append(Alert.BARKING)
        return True
    else:
        return False

