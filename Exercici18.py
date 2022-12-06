from  os import system
system('clear')
from time import sleep

#Menú Principal
print("\n              Elements comuns")
print(" El programa cercara caracters repetits als textos")
a = input ("\nPrimer text: ")
b = input ("\nSegon text: ")

def superposicio(text):
        x = list (a)
        z = list (b)
        
        
        if x != z:
            print("Si")
        else:
            print("no")

        return
            

        

print(superposicio(a and b))