import numpy

from Psu import *


# Settings

resource = 'TCPIP0::192.168.0.35::inst0::INSTR'


# Code

psu = Psu(resource)
print('Connected to PSU at \'{:s}\''.format(resource))
print('')

psu.reset()

for channel in numpy.arange(1, 4):
    psu.calibrationClear(channel, 'ALL')

print("Calibration cleared!")

