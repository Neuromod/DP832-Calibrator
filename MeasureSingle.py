import time
import numpy
import matplotlib.pyplot as pyplot

from Psu import *
from Dmm import *
from Measure import *


# Settings

psuResource = 'TCPIP0::192.168.0.35::inst0::INSTR'
dmmResource = 'TCPIP0::192.168.0.30::inst0::INSTR'

file = 'Single.npy'

channel = 2
mode    = 'V'

delay = 1.

dV = .1
dI = .01


# Code

psu = Psu(psuResource)
print('Connected to PSU at \'{:s}\''.format(psuResource))

dmm = Dmm(dmmResource)
print('Connected to DMM at \'{:s}\''.format(dmmResource))

psu.reset()

table = measure(psu, dmm, channel, mode, dV, dI, delay)

numpy.save(file, table)

if mode == 'V':
    limit = table[:, 2] * 0.0005 + 0.01
else:
    limit = table[:, 2] * 0.0015 + 0.005

pyplot.plot(table[:, 2], (table[:, 2] - table[:, 0]) * 1000.)
pyplot.plot(table[:, 2], (table[:, 2] - table[:, 1]) * 1000.)
pyplot.plot(table[:, 2],  limit * 1000., 'k')
pyplot.plot(table[:, 2], -limit * 1000., 'k')

if mode == 'V':
    pyplot.ylim([-30, 30])
    pyplot.xlabel('Output voltage (V)')
    pyplot.ylabel('Accuracy (mV)')
else:
    pyplot.ylim([-12, 12])
    pyplot.xlabel('Output current (A)')
    pyplot.ylabel('Accuracy (mA)')

pyplot.legend(['{:s}-DAC'.format(mode), '{:s}-ADC'.format(mode), 'DAC Spec'], frameon = False, loc = 2)
pyplot.show()

