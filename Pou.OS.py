"\n"
from os import system
from time import sleep


def menu_principal():
        print("\n""         Pou.OS\n")
a = input("Intordueix nom d'usuari: ")
b = "Dequa20."
b = input("\nConstrasenya: ")
system('clear')
if b == "Dequa20.":  
    print("\n""    Executant Pou.OS\n\n")
    sleep(1)
    system('clear')
elif b >= "":
    print("\n""Contrasenya Incorrecta""\n")
    c = "Dequa20."
    c = input(" Intenta-ho de nou:")
    if c == "Dequa20.":
        print("\n""   Exexutant Pou.OS")
        sleep(2)
        print("\n""          Hola " + a)
        system('clear')
    elif c >= "":
            print("\n""  Usuari Bloquetjat")
            print("\n""   Reincia l'equip")

menu=1
while (menu!=0):
        menu= menu_principal
        sleep(0.5)
        print("\n""Usuari: " + a)
        sleep(0.8)
        print("\n""Menú""\n")
        sleep(0.2)
        print("1.Calculadora""\n")
        sleep(0.2)
        print("2.Document Text""\n")
        sleep(0.2)
        d = input("Executar: ")
        if d == "1":

                reinici=1
                while(reinici!=0):
                        system('clear')
                        sleep(0.1)
                        print("\n""Carregant")
                        sleep(0.4)
                        system('clear')
                        print("\n""Carregant.") 
                        sleep(0.2)
                        system('clear')
                        print("\n""Carregant..")
                        sleep(0.2)
                        system('clear')
                        print("\n""Carregant...")
                        sleep(0.2)
                        system('clear')
                        print("\n""Calculadora Aritmètica""\n\n")
                        n1 = input("Insereix una xifra: ")
                        system('clear')
                        sleep(0.2)
                        print("\n""   Càlculs Disponibles""\n")
                        print("(+).Sumar""\n")
                        print("(-).Restar""\n")
                        print("(*).Multiplicar""\n")
                        print("(/).Dividir""\n")
                        print("(**),Potènciar""\n")
                        n2 = input("Selecciona el operant: ")
                        system('clear')
                        sleep(0.5)
                        n3 = input("\n""Insereix un altre xifra: ")
                        system('clear')
                        if n2 == "+":
                                n4 = int(n1)+int(n3) 
                                system('clear')
                                print("\n",n1,"",n2,"",n3,"=",n4,"")
                        if n2 == "-":
                                n4 = int(n1)-int(n3)
                                print("\n",n1,"",n2,"",n3,"=",n4,"")
                        if n2 == "*":
                                n4 = int(n1)*int(n3)
                                print("\n",n1,"",n2,"",n3,"=",n4,"")
                        if n2 == "/":
                                n4 = int(n1)/int(n3)
                                print("\n",n1,"",n2,"",n3,"=",n4,"")
                        if n2 == "**":
                                n4 = int(n1)**int(n3)
                                print("\n",n1,"",n2,"",n3,"=",n4,"")
                                sleep('1.8')
                
                f = input("\n Fer un altre càlcul (S/N): ")
                if f == "S":
                        system('clear')
                        sleep(0.7)
                        print("reinici")
                if f == "s":
                        print("reinici")
                        system('clear')
                        sleep(0.7)             
                if f == "n":
                        system('clear')
                        sleep(0.7)
                        p
    

    if d == "2":
        system('clear')
        sleep(2)
        e = input("\n""Descarregar Paquet Ofimàtic (S/N): ")
        if  e == "N":
            system('clear')
            print("Instalació Cancelada""\n")
            f = input("Tornar al menú (S/N): ")
            if f == "S":
                "return" == d 
        elif e == "n":
            system('clear')
            print("Instalació Cancelada""\n")
        elif e == "S":
            print("\n""Instalant Paquet Ofimàtic")
            sleep(0.4)
            system('clear')
            print("|")
            sleep(0.2)
            system('clear')
            print("/")
            sleep(0.2)
            system('clear')
            print("|")
            sleep(0.1)
            system('clear')
            print("/")
            sleep(0.2)
            system('clear')
            print("|")
            sleep(0.1)
            system('clear')
            print("/")
            sleep(0.2)
            system('clear')
            print("|")
            sleep(0.1)
            system('clear')
            print("/")
            sleep(0.1)
            system('clear')
            print("|")
            sleep(0.1)
            system('clear')
            print("/")
            sleep(0.1)
            system('clear')
            print("|")
            sleep(0.1)
            system('clear')
            print("/")
            sleep(0.1)
            system('clear')
            print("|")
            sleep(0.1)
            system('clear')
            print("/")
            sleep(0.1)
            system('clear')
            print("|")
            sleep(0.1)
            system('clear')
            sleep(0.2)
            print("\n""  Instalació Completada")
            sleep(1.7)
            system('clear')
            t1 = input("\n""    Títol del Document: ")
            system('clear')
            sleep(0.7)
            print("\n"  "   "                                                         ,     t1,"")
            b1 = input("\n""Insereix text: ")
            system('clear')
            print("\n""                                                              ",t1,"")
            print("\n""",b1,"")
            b2 = input(" ")
            system('clear')
            print("\n"  "   "                                                         ,     t1,"")
            print("\n\n""",b1,"")
            print("",b2,"")



