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

while (1):
    global message
    global buffer
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexionInit(s)
    s.send("login:\n")
    initTemp()
    initSound()
    initAcc()
    sleep(1)
    print("all inits done")

    i = 0

    while (1):
        buffer = []
        message = []
        alert = alertTemp(message, buffer) + alertSound(message, buffer) + alertAcc(message, buffer)
        buffer_str = buffer[0] + buffer[1] + buffer[2] + "\n"
        print(buffer_str)
        s.send(buffer_str)
        sleep(i)
    s.close()
