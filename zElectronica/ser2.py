import serial

serial_com = '/dev/cu.usbmodem14101'  # seleccionar el COM adecuado
ser = serial.Serial(serial_com, baudrate = 9600, timeout=10)

x1 = input("Seleccione LED (verde o rojo): ")

if x1=="rojo":
    mensaje = "0".encode()

if x1=="verde":
    mensaje = "1".encode()

ser.write(mensaje)
ser.close()