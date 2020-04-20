from Psu import *
from Dmm import *
from Calibrate import *


# Settings

psuResource = 'TCPIP0::192.168.0.35::inst0::INSTR'
dmmResource = 'TCPIP0::192.168.0.30::inst0::INSTR'


# Code

psu = Psu(psuResource)
print('Connected to PSU at \'{:s}\''.format(psuResource))

dmm = Dmm(dmmResource)
print('Connected to DMM at \'{:s}\''.format(dmmResource))

psu.reset()

for mode in ['V', 'I']:
    for channel in numpy.arange(1, 4):
        calibrate(psu, dmm, channel, mode)
