from os import system
from time import sleep

#Menú 
print("\n            Multiplicador de Caracters")
sleep(1.5)
print("\nInsereix el caracter i el digit per multpilicar-lo")
sleep(3)


def multplicador(x):
    a = list(x)
    b = str(a)
    for i in b :
        resultat = int (i*i)
    return resultat
    
    
x = input("\n\nCaracter: ")
print(multplicador(x))




