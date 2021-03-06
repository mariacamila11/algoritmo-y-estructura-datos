import serial
import matplotlib as plt

Fs = 1000   #Frecuencia de muestreo en Hz
t = 5       #segundos de lectura

serial_com = '/dev/cu.usbmodem14101'  # seleccionar el COM adecuado
ser = serial.Serial(serial_com, baudrate = 115200, timeout=10)

for x in range(Fs*t):
        try:
            dat = int(ser.readline())
        except:
            dat = 0
        print(dat)

ser.close()
from matplotlib import pyplot as plt
import serial
import numpy as np

Fs = 1000   #Frecuencia de muestreo en Hz
t = 5       #segundos de lectura
signal = np.ones((Fs*t,1))

serial_com = '/dev/cu.usbmodem14101'  # seleccionar el COM adecuado
ser = serial.Serial(serial_com, baudrate = 115200, timeout=10)

for x in range(Fs*t):
        try:
            dat = int(ser.readline())
        except:
            dat = 0
        signal[x] = dat
        print(dat)

# Plot
plt.figure()
plt.plot(signal)
plt.show()
ser.close()