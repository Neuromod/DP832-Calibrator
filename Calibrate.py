import time
import numpy
from Psu import *
from Dmm import *


# Settings

delayV      = 2.
delayI      = 30.
coolingTime = 300.

nplc  = 1.
count = 50

dvDac12 = .5
dvAdc12 = 1.
vDac12 = numpy.concatenate(([.25], numpy.arange(dvDac12, 32. + dvDac12 / 2., dvDac12)))
vAdc12 = numpy.arange(0., 32. + dvAdc12 / 2., dvAdc12)

dvDac3 = .2
dvAdc3 = .4
vDac3 = numpy.concatenate(([.01, .05], numpy.arange(.1, 5.3 + dvDac3 / 2., dvDac3)))
vAdc3 = numpy.arange(0., 5.3 + dvAdc3 / 2., dvAdc3)
vAdc3[-1] = 5.3

diDac = .1
diAdc = .2
iDac = numpy.arange(diDac, 3.2 + diDac / 2., diDac)
iAdc = numpy.arange(0., 3.2 + diAdc / 2., diAdc)


# Code

def calibrate(psu, dmm, channel, mode):
    start = time.time()

    print('\a')
    print('Connect Ch{:d} to {:s} input!'.format(channel, mode))
    input('press Enter to begin calibration...')

    if mode == 'V':
        dmm.setVoltage(nplc, count)
    else:
        dmm.setCurrent(nplc, count)

    psu.calibrationStart(channel)
    psu.calibrationClear(channel, mode)

    for device in ['DAC', 'ADC']:
        print('')
        print('Calibrating Ch{:d} {:s}-{:s}'.format(channel, mode, device))
            
        if mode == 'V':
            if channel != 3:
                if device == 'DAC':
                    sweep = vDac12
                else:
                    sweep = vAdc12
            else:
                if device == 'DAC':
                    sweep = vDac3
                else:
                    sweep = vAdc3
        else:
            if device == 'DAC':
                sweep = iDac
            else:
                sweep = iAdc

        if mode == 'I':
            wait = coolingTime
            
            if device == 'DAC':
                wait = max(wait - (time.time() - start), 0)

            if wait > 0:
                print('Waiting {:.0f} s for the PSU to cool down...'.format(wait))

            time.sleep(wait)

        psu.channelState(channel, True)

        for step in range(len(sweep)):
            psu.calibrationSet(channel, mode, device, step, sweep[step])
   
            if mode == 'V':
                time.sleep(delayV)
            else:
                time.sleep(delayI)

            value = dmm.measure()
            psu.calibrationMeasurement(channel, mode, device, step, dmm.measure())

            print('[{:d}/{:d}] {:s}-DAC: {:.3f}, {:s}-DMM: {:.5f}'.format(step + 1, len(sweep), mode, sweep[step], mode, value))

        psu.reset()

    psu.calibrationEnd(channel)
