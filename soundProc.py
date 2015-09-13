import socket
import os
import sys
from time import sleep
import mraa
from globals import *
import pyupm_mic as upmMicrophone
mymic, threshContext
VOLUME_THRES = 10


def initSound():
    global mymic
    global threshContext
    mymic = upmMicrophone.Microphone(1)
    threshcontext = upmMicrophone.thresholdContext()
    threshcontext.averageReading = 0
    threshcontext.runningAverage = 0
    threshcontext.averagedOver = 2


def soundProc(message):
    global buffer
    global Alert
    buf = upmMicrophone.uint16Array(32)
    len = mymic.getSampledWindow(2, 32, buf)
    if len:
        thresh = mymic.findThreshold(threshContext, 30, buf, len)
    buffer += str(thresh) + ", "
    if thresh > VOLUME_THRES:
        message.append(Alert.BARKING)
        return True
    else:
        return False

