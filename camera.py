import cv2
import time
import os

def tomar():
	cam = cv2.VideoCapture(0)
	s, im = cam.read() 
	#cv2.waitKey()
	hora = time.strftime("%H%M%S")
	fecha = time.strftime("%Y%m%d")

	#cv2.imshow(fecha+"_"+hora, im) 
	cv2.imwrite("fotos/"+fecha+"/"+hora+".jpg",im) 

def deteccion():
	fecha = time.strftime("%Y%m%d")
	if not os.path.exists("fotos/"+fecha):
		os.makedirs("fotos/"+fecha)
	for i in range(1,15):
		tomar()
