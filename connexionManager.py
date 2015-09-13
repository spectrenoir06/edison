import socket
import os
import sys
from globals import *
from time import sleep
import mraa

TCP_IP = '192.168.100.62'
TCP_PORT = 1234

def connexionInit( s):
    while (1):
        try:
            s.connect((TCP_IP, TCP_PORT))
            break
        except:
            print("erreur fdp")
            sleep(1)

    s.send("login:\n")


