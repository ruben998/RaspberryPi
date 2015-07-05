import Tkinter

root = Tkinter.Tk()
boton1 = Tkinter.Button(root, text = "Adelante")
boton2 = Tkinter.Button(root, text = "Atras")
boton3 = Tkinter.Button(root, text = "Izquierda")
boton4 = Tkinter.Button(root, text = "Derecha")
boton5 = Tkinter.Button(root, text = "Salir")

boton1.pack()
boton2.pack()
boton3.pack()
boton4.pack()
root.mainloop()