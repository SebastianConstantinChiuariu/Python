
from os import system
system('clear')

from time import sleep

#Menú

llista_menu = ["Suma de numeros","Multiplicació de numeros"]
print("\n             Menú")
print("________________________________")
print ("\n           1.Sumar")
print("           2.Restar")
print("________________________________")
opcio = input("\n            Opció: ")


# Funcions

if opcio == "1":
    
    system('clear')
    def sumar_llista():

        numeros = "1,2,3,4,5"
        digits = 0
        
        resultat = int(digits) + int(numeros) 
        print(" la suma total és: ",resultat)

    print("\n",llista_menu[0])
    print(sumar_llista())
    