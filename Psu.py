import csv
import datetime
import visa


class Psu:
    def __init__(self, resource, timeout = 10_000):
        self._psu = visa.ResourceManager().open_resource(resource)
        self._psu.timeout = timeout
        self._psu.clear()


    def reset(self):
        self._psu.write('*RST')


    def channelState(self, channel, state):
        stateString = ['OFF', 'ON'][state]
        self._psu.write(':OUTP CH{:d},{:s}'.format(channel, stateString))


    def channelSetting(self, channel, voltage, current):
        self._psu.write(':APPL CH{:d},{:.3f},{:.3f}'.format(channel, voltage, current))


    def measure(self, channel):
        query = self._psu.query(':MEAS:ALL? CH{:d}'.format(channel))
        voltage, current = list(csv.reader([query], delimiter = ','))[0][0 : 2]

        return float(voltage), float(current)


    def calibrationStart(self, channel):
        self._psu.write(':CAL:START 11111,CH{:d}'.format(channel))


    def calibrationEnd(self, channel):
        self._psu.write(':CAL:END {:s},CH{:d}'.format(datetime.datetime.today().strftime('%Y-%m-%d'), channel))


    # <mode> = 'V', 'I', 'ALL'
    def calibrationClear(self, channel, mode):
        modeValue = {'V': 'V', 'I': 'C', 'ALL': 'ALL'}
        self._psu.write(':CAL:CLEAR CH{:d},{:s}'.format(channel, modeValue[mode]))


    # <mode>   = 'V', 'I'   
    # <device> = 'ADC', 'DAC' 
    def calibrationSet(self, channel, mode, device, step, value):
        modeValue = {'V': 'V', 'I': 'C'}
        deviceValue = {'ADC': 0, 'DAC': 1}
        self._psu.write(':CAL:SET CH{:d},{:s},{:d},{:.3f},{:d}'.format(channel, modeValue[mode], step, value, deviceValue[device]))
        

    # <mode>   = 'V', 'I'   
    # <device> = 'ADC', 'DAC' 
    def calibrationMeasurement(self, channel, mode, device, step, value):
        modeValue = {'V': 'V', 'I': 'C'}
        deviceValue = {'ADC': 0, 'DAC': 1}
        self._psu.write(':CAL:MEAS CH{:d},{:s},{:d},{:.6f},{:d}'.format(channel, modeValue[mode], step, value, deviceValue[device]))
