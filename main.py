import serial
import camera
arduino = serial.Serial('COM3', baudrate=9600, timeout=0.2)

hacer = True
i = 0
while(True):
	line = arduino.readline()
	print i,line
	if line == 'Movimiento detectado\r\n' and hacer==True:
		camera.deteccion()         
		hacer = False
	elif line == 'Sin datos\r\n' and hacer == False:
		hacer = True
	i+=1

