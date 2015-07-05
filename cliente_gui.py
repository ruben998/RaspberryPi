#!/usr/bin/env python
 
import socket
import Tkinter

class Client():
	def init(self):
		s = socket.socket()
		s.connect(('192.168.0.98', 9999))
 		root = Tkinter.Tk()
		boton1 = Tkinter.Button(root, text = "Adelante", command = s.send('w'))
		boton2 = Tkinter.Button(root, text = "Atras", command = s.send('s'))
		boton3 = Tkinter.Button(root, text = "Izquierda", command = s.send('a'))
		boton4 = Tkinter.Button(root, text = "Derecha", command = s.send('d'))
		boton5 = Tkinter.Button(root, text = "Salir", command = s.send('close'))

		boton1.pack()
		boton2.pack()
		boton3.pack()
		boton4.pack()
		root.mainloop()

 		while True:
 			mensaje = raw_input('Introduce mensaje')
 			s.send(mensaje)
	
	def close(self):
		print "Adios."
		s.close()

	def message(self, message):
		s.send(message)

cliente = Client()
cliente.init()
