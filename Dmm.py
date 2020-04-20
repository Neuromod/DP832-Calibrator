import visa


class Dmm:
    def __init__(self, resource, timeout = 10_000):
        self._dmm = visa.ResourceManager().open_resource(resource)
        self._dmm.timeout = timeout
        self._dmm.clear()


    def reset(self):
        self._dmm.write('reset()')


    def setVoltage(self, nplc = 1, count = 25):
        self._dmm.write('dmm.measure.func = dmm.FUNC_DC_VOLTAGE')
        self._dmm.write('dmm.measure.autozero.enable = dmm.ON')
        self._dmm.write('dmm.measure.autodelay = dmm.DELAY_ON')
        self._dmm.write('dmm.measure.nplc = {:f}'.format(nplc))
        self._dmm.write('dmm.measure.filter.enable = dmm.ON')
        self._dmm.write('dmm.measure.filter.type = dmm.FILTER_REPEAT_AVG')
        self._dmm.write('dmm.measure.filter.count = {:d}'.format(count))


    def setCurrent(self, nplc = 1, count = 25):
        self._dmm.write('dmm.measure.func = dmm.FUNC_DC_CURRENT')
        self._dmm.write('dmm.measure.autozero.enable = dmm.ON')
        self._dmm.write('dmm.measure.autodelay = dmm.DELAY_ON')
        self._dmm.write('dmm.measure.range = 10')
        self._dmm.write('dmm.measure.nplc = {:f}'.format(nplc))
        self._dmm.write('dmm.measure.filter.enable = dmm.ON')
        self._dmm.write('dmm.measure.filter.type = dmm.FILTER_REPEAT_AVG')
        self._dmm.write('dmm.measure.filter.count = {:d}'.format(count))


    def measure(self):
        return float(self._dmm.query('print(dmm.measure.read())'))
