from os import system
from time import sleep

#Menú
prog = 1
while (prog!=0):
    print("\n                 Dibuix amb Punts")
    print("\n\n      Nombre Introduit = Punts a la pantalla")
    punts = input("\n\nNombre: ")
    def crear_punts(punt):
        x = "."
        a = str(punts)
        b = int(a) + x
        return b

        

    print(crear_punts(punts))


          