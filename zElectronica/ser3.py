import serial

serial_com = '/dev/cu.usbmodem14101'  # seleccionar el COM adecuado
ser = serial.Serial(serial_com, baudrate = 9600, timeout=10)

x1 = input("Seleccione LED (verde o rojo): ")
x2 = input("Seleccione delay (s): ")

print("LED " + x1 + " Delay " + x2 + " (ms)" )

if x1=="rojo":
    mensaje = ("0" + x2).encode()

if x1=="verde":
    mensaje = ("1" + x2).encode()

ser.write(mensaje)
ser.close()