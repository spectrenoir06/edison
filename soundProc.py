import socket
import os
import sys
from time import *
import mraa
from globals import *
import pyupm_mic as upmMicrophone
mymic, threshContext = None, None
VOLUME_THRES = 10
reset = True
t


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
    global t
    global reset
    buf = upmMicrophone.uint16Array(32)
    len = mymic.getSampledWindow(2, 32, buf)
    if len:
        thresh = mymic.findThreshold(threshContext, 30, buf, len)
    buffer.append(str(thresh) + ",")
    if thresh > VOLUME_THRES:
        if reset:
            t = time.time()
            reset = False
        else:
            dt = time.time() - t
            if( dt > 10 ) :
                message.append(Alert.BARKING)
                reset = True
        return True
    else:
        return False

