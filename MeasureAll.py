import time
import numpy

from Psu import *
from Dmm import *
from Measure import *


# Settings

file = 'All.npz'

psuResource = 'TCPIP0::192.168.0.35::inst0::INSTR'
dmmResource = 'TCPIP0::192.168.0.30::inst0::INSTR'

delayV       = 1.
delayI       = 2.
delayCooling = 300.

dV = .1
dI = .01


# Code

psu = Psu(psuResource)
print('Connected to PSU at \'{:s}\''.format(psuResource))

dmm = Dmm(dmmResource)
print('Connected to DMM at \'{:s}\''.format(dmmResource))

psu.reset()

ch1v = measure(psu, dmm, 1, 'V', dV, dI, delayV, delayCooling)
ch2v = measure(psu, dmm, 2, 'V', dV, dI, delayV, delayCooling)
ch3v = measure(psu, dmm, 3, 'V', dV, dI, delayV, delayCooling)

ch1i = measure(psu, dmm, 1, 'I', dV, dI, delayI, delayCooling)
ch2i = measure(psu, dmm, 2, 'I', dV, dI, delayI, delayCooling)
ch3i = measure(psu, dmm, 3, 'I', dV, dI, delayI, delayCooling)

numpy.savez(file, ch1v = ch1v, ch2v = ch2v, ch3v = ch3v, ch1i = ch1i, ch2i = ch2i, ch3i = ch3i)
