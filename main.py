import socket
import os
import sys
from time import sleep
from connexionManager import *
from tempProc import *
from soundProc import *
from accProc import *
from globals import *
import mraa
import pyupm_mic as upmMicrophone
import pyupm_mma7660 as upmMMA7660

# Init accelerometer
initAcc()
# Init messages list
message = []

while (1):
    global message
    global buffer
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexionInit(s)
    s.send("login:\n")
    initTemp()
    initSound()
    initAcc()
    print("test")

    i = 0

    while (1):
        buffer = ""
        alert = alertTemp(message) + alertSound(message) + alertProc(message)
        buffer += "\n"



        s.send(buffer)
        s.send( )
        sleep(i)
    s.close()
