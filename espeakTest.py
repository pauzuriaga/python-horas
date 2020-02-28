import os, time
def tiempos(t1,t2):
    os.system('espeak -ves+f3 -s 165 -a 100 -k 30 --stdout " Vehículo 8 6 8, tu espacio de tiempo hacia adelante es de' + t1 + ' minutos, y hacia atrás es de '+ t2 +' minutos" | aplay')
def broadcast(texto):
	os.system('espeak -ves+f3 -s 165 -a 100 -k 30 --stdout " '+ texto +'" | aplay')
def mensaje(msj):
	os.system('espeak -ves+f3 -s 165 -a 100 -k 30 --stdout " Vehículo 8 6 8, '+ msj+'" | aplay')
mensaje("esto es una prueba")
#broadcast("hola mundo esto es una prueba")
