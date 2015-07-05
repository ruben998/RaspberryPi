#!/usr/bin/env python
 
#importamos el modulo socket
import socket

def adelante():
    GPIO.output(11, True)
    GPIO.output(13, True)
    time.sleep(0.2)
    GPIO.output(11, False)
    GPIO.output(13, False)

def atras():
    GPIO.output(15, True)
    GPIO.output(7, True)
    time.sleep(0.2) 
    GPIO.output(15, False)
    GPIO.output(7, False)

def derecha():
    GPIO.output(7, True)
    GPIO.output(13, True)
    time.sleep(0.2) 
    GPIO.output(7, False)
    GPIO.output(13, False)

def izquierda():
    GPIO.output(11, True)
    GPIO.output(15, True)
    time.sleep(0.2)     
    GPIO.output(11, False)
    GPIO.output(15, False)

def stop():
    GPIO.output(7, False)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, False)

def menu(opcio):
    if opcio == 'w':
        adelante()
        return 0
    elif opcio == 's':
        atras()
        return 0
    elif opcio == 'a':
        izquierda()
        return 0
    elif opcio == 'd':
        derecha()
        return 0
    elif opcio == 'close':
        stop()
        return -1
    else:
        stop()
        return 0

def main(): 
    #instanciamos un objeto para trabajar con el socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     
    #Con el metodo bind le indicamos que puerto debe escuchar y de que servidor esperar conexiones
    #Es mejor dejarlo en blanco para recibir conexiones externas si es nuestro caso
    s.bind(("", 9999))
     
    #Aceptamos conexiones entrantes con el metodo listen, y ademas aplicamos como parametro
    #El numero de conexiones entrantes que vamos a aceptar
    s.listen(1)
     
    #Instanciamos un objeto sc (socket cliente) para recibir datos, al recibir datos este 
    #devolvera tambien un objeto que representa una tupla con los datos de conexion: IP y puerto
    sc, addr = s.accept()
     
     
    while True:
     
        #Recibimos el mensaje, con el metodo recv recibimos datos y como parametro 
        #la cantidad de bytes para recibir
        recibido = sc.recv(1024)
     
        if menu(recibido) == -1:
            break
        #Si el mensaje recibido es la palabra close se cierra la aplicacion
        #if recibido == "close":
        #   break
     
        #Si se reciben datos nos muestra la IP y el mensaje recibido
        print str(addr[0]) + " dice: ", recibido
     
        #Devolvemos el mensaje al cliente
        sc.send(recibido)
    print "Adios."
     
    #Cerramos la instancia del socket cliente y servidor
    sc.close()
    s.close()

main()