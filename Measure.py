import time
import numpy

from Psu import *
from Dmm import *


# Settings

nplc  = 1.
count = 20


# Code

def measure(psu, dmm, channel, mode, dV, dI, delay, coolingTime = 0.):
    start = time.time()
    
    print('\a')
    print('Connect Ch{:d} to {:s} input!'.format(channel, mode))
    input('press Enter to begin the measurements...')
    print('')
    print('Measuring Ch{:d} {:s}'.format(channel, mode))

    if mode == 'V':
        dmm.setVoltage(nplc, count)
    else:
        dmm.setCurrent(nplc, count)

    if mode == 'V':
        if channel != 3:
            sweep = numpy.arange(0., 32. + dV / 2., dV)
        else:
            sweep = numpy.arange(0, 5.3 + dV / 2., dV)
    else:
        sweep = numpy.arange(0, 3.2 + dI / 2., dI)

    table = []

    if mode == 'I':
        wait = max(coolingTime - (time.time() - start), 0)

        if wait > 0:
            print('Waiting {:.0f} s for the PSU to cool down...'.format(wait))

        time.sleep(wait)

    psu.channelState(channel, True)

    for i in range(sweep.size):
        dac = sweep[i]

        if mode == 'V':
            psu.channelSetting(channel, dac, 3.2)
        else:
            if channel != 3:
                psu.channelSetting(channel, 32., dac)
            else:
                psu.channelSetting(channel, 5.3, dac)
            
        time.sleep(delay)

        value = dmm.measure()

        adc = psu.measure(channel)[mode == 'I']
            
        table.append([dac, adc, value])

        print('{:s}-DAC: {:.3f}, {:s}-ADC: {:.4f}, {:s}-DMM: {:.5f}'.format(mode, dac, mode, adc, mode, value))

    psu.reset()

    return numpy.array(table)

