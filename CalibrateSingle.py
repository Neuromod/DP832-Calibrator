import time
import numpy
from Psu import *
from Dmm import *
from Calibrate import *


# Settings

psuResource = 'TCPIP0::192.168.0.35::inst0::INSTR'
dmmResource = 'TCPIP0::192.168.0.30::inst0::INSTR'

channel = 2
mode    = 'V'


# Code

psu = Psu(psuResource)
print('Connected to PSU at \'{:s}\''.format(psuResource))

dmm = Dmm(dmmResource)
print('Connected to DMM at \'{:s}\''.format(dmmResource))

psu.reset()

calibrate(psu, dmm, channel, mode)
