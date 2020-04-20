import numpy
import matplotlib.pyplot as pyplot


# Settings

dataFile = 'All.npz'

VDacFile = 'V-Dac.png'
IDacFile = 'I-Dac.png'
VAdcFile = 'V-Adc.png'
IAdcFile = 'I-Adc.png'

dpi = 200
size = (9.6, 5.4)


# Code

data = numpy.load(dataFile)

ch1v = data['ch1v']
ch2v = data['ch2v']
ch3v = data['ch3v']
ch1i = data['ch1i']
ch2i = data['ch2i']
ch3i = data['ch3i']


print('              V-DAC      V-ADC      I-DAC      I-ADC')
print('------------------------------------------------------')

for i in range(3):
    chV = [ch1v, ch2v, ch3v][i]
    chI = [ch1i, ch2i, ch3i][i]

    vDac = numpy.abs((chV[:, 2] - chV[:, 0]) * 1000.).max()
    vAdc = numpy.abs((chV[:, 2] - chV[:, 1]) * 1000.).max()
    iDac = numpy.abs((chI[:, 2] - chI[:, 0]) * 1000.).max()
    iAdc = numpy.abs((chI[:, 2] - chI[:, 1]) * 1000.).max()

    print('Channel {:d}:'.format(i + 1), end = '')
    print('{:>8s} mV'.format('±{:.1f}'.format(vDac)), end = '')
    print('{:>8s} mV'.format('±{:.1f}'.format(vAdc)), end = '')
    print('{:>8s} mA'.format('±{:.1f}'.format(iDac)), end = '')
    print('{:>8s} mA'.format('±{:.1f}'.format(iAdc)))

limit = ch1v[:, 0] * 0.0005 + 0.010

pyplot.plot(ch1v[:, 0], (ch1v[:, 2] - ch1v[:, 0]) * 1000.)
pyplot.plot(ch2v[:, 0], (ch2v[:, 2] - ch2v[:, 0]) * 1000.)
pyplot.plot(ch3v[:, 0], (ch3v[:, 2] - ch3v[:, 0]) * 1000.)

pyplot.plot(ch1v[:, 0],  limit * 1000., 'k')
pyplot.plot(ch1v[:, 0], -limit * 1000., 'k')

pyplot.ylim([-30, 30])

pyplot.xlabel('Programmed voltage (V)')
pyplot.ylabel('Error (mV)')
pyplot.legend(['Channel 1', 'Channel 2', 'Channel 3', 'Annual accuracy'], frameon = False, loc = 2)

pyplot.gcf().set_size_inches(size[0], size[1])
pyplot.savefig(VDacFile, dpi = dpi)
pyplot.clf()


limit = ch1v[:, 1] * 0.0005 + 0.005

pyplot.plot(ch1v[:, 1], (ch1v[:, 2] - ch1v[:, 1]) * 1000.)
pyplot.plot(ch2v[:, 1], (ch2v[:, 2] - ch2v[:, 1]) * 1000.)
pyplot.plot(ch3v[:, 1], (ch3v[:, 2] - ch3v[:, 1]) * 1000.)

pyplot.plot(ch1v[:, 1],  limit * 1000., 'k')
pyplot.plot(ch1v[:, 1], -limit * 1000., 'k')

pyplot.ylim([-30, 30])

pyplot.xlabel('Readback voltage (V)')
pyplot.ylabel('Error (mV)')
pyplot.legend(['Channel 1', 'Channel 2', 'Channel 3', 'Annual accuracy'], frameon = False, loc = 2)

pyplot.gcf().set_size_inches(size[0], size[1])
pyplot.savefig(VAdcFile, dpi = dpi)
pyplot.clf()


limit = ch1i[:, 0] * 0.002 + 0.005

pyplot.plot(ch1i[:, 0], (ch1i[:, 2] - ch1i[:, 0]) * 1000.)
pyplot.plot(ch2i[:, 0], (ch2i[:, 2] - ch2i[:, 0]) * 1000.)
pyplot.plot(ch3i[:, 0], (ch3i[:, 2] - ch3i[:, 0]) * 1000.)

pyplot.plot(ch1i[:, 0],  limit * 1000., 'k')
pyplot.plot(ch1i[:, 0], -limit * 1000., 'k')

pyplot.ylim([-12, 12])

pyplot.xlabel('Programmed current (A)')
pyplot.ylabel('Error (mA)')
pyplot.legend(['Channel 1', 'Channel 2', 'Channel 3', 'Annual accuracy'], frameon = False, loc = 2)

pyplot.gcf().set_size_inches(size[0], size[1])
pyplot.savefig(IDacFile, dpi = dpi)
pyplot.clf()


limit = ch1i[:, 0] * 0.0015 + 0.005

pyplot.plot(ch1i[:, 2], (ch1i[:, 2] - ch1i[:, 1]) * 1000.)
pyplot.plot(ch2i[:, 2], (ch2i[:, 2] - ch2i[:, 1]) * 1000.)
pyplot.plot(ch3i[:, 2], (ch3i[:, 2] - ch3i[:, 1]) * 1000.)

pyplot.plot(ch1i[:, 0],  limit * 1000., 'k')
pyplot.plot(ch1i[:, 0], -limit * 1000., 'k')

pyplot.ylim([-12, 12])

pyplot.xlabel('Readback current (A)')
pyplot.ylabel('Error (mA)')
pyplot.legend(['Channel 1', 'Channel 2', 'Channel 3', 'Annual accuracy'], frameon = False, loc = 2)

pyplot.gcf().set_size_inches(size[0], size[1])
pyplot.savefig(IAdcFile, dpi = dpi)
pyplot.clf()
