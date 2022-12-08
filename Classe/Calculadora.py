from os import system
system('cls')
from time import sleep

#Definició de funcions auxiliar
#Funció del menú  principal
def menu_principal():
        system('cls')
        print("\n           Calculadora_\n")
        print("               Menú")
        print("""
        1. Números Enters 
        2. Numeros reals
        3. Canvis de base 
        0. Aturar Calculadora
        """)
        opcio = input ("  Selecciona l'opció que vulguis: ")
        return opcio

# Funció Menú nombres Enters
def menu_enters():
    system('cls')
    print("""
    Calculadora de nombres enters\n
            1. Sumar
            2. Restar
            3. Dividir
            4. Multiplicar
            5. Potència
            6. Mòdul
            0. Sortir\n""")
    opcio= input("  Selecciona l'opció que vulguis: ")
    return opcio

# Funció Menú nombres Reals
def menu_reals():
    print("""
        Calculadora de nombres reals
        1. Sumar
        2. Restar
        3. Dividir
        4. Multiplicar
        0. Sortir""")
    opcio= input("  Selecciona l'opció que vulguis: ")
    return opcio

#Funció Canvis de Base Menú

def menu_canvis_de_base():

    print("""
        Calculadora de canvis de base
        1. Decimal a Binari
        2. Decimal a Octal
        3. Decimal a Hexadecimal
        0. Sortir""")
    opcio= input("  Selecciona l'opció que vulguis: ")
    return opcio

#Funcions decimal_a_octal
def decimal_a_octal (decimal):
    octal = ""
    while decimal > 0:
        residuo = decimal % 8
        octal = str(residuo) + octal
        decimal = int(decimal / 8)
    return octal

#Funcions decimal_a_binario
def decimal_a_binario(decimal):
    if decimal <= 0:
        return "0"
    binario = ""
    while decimal > 0:
        residuo = int(decimal % 2)
        decimal = int(decimal / 2)
        binario = str(residuo) + binario
    return binario

#Funció decimal_a_hexadecimal
def decimal_a_hexadecimal(decimal):
    hexadecimal = ""
    while decimal > 0:
        residuo = decimal % 16
        verdadero_caracter = obtener_caracter_hexadecimal(residuo)
        hexadecimal = verdadero_caracter + hexadecimal
        decimal = int(decimal / 16)
    return hexadecimal


#Programa principal de la Calculadora
opcio=1
while(opcio!=0):
    opcio=menu_principal()
    match opcio:

        case "":
            print("Opció inexistent")
            sleep(1)

        case "0":
            system('cls')
            sleep(1)
            print("\n     Mode Suspensió")
            sleep(2)
            iniciar=input("\nPitjar ENTER per iniciar: ")
            opcio=1
        case "1":
            opcio2=menu_enters()
            system('cls')
            match opcio2:

                case "other":
                    print("         Opció Inexistent")
                case "1":
                    system('cls')
                    operació=1
                    while(operació!=0):
                        system('cls')
                        print("\n            Sumant")
                        a = int(input("\n  Indiqui el primer operand: "))
                        b = int(input("\n  Insereix un segon opreand: "))
                        c=a+b
                        print("\n       ",a," + ",b," = ",c,"")
                        sleep(2)
                    
                        #Repetir operació?
                        
                        print("\n""          1. Repetir")
                        print("          0. Sortir")
                        repetir = input("\n""Selecciona l'opció que vulguis: ")
                        if repetir == "1":
                            
                            operació=1
                                    
                        if repetir == "0":
                            opcio=1

                case "2":
                    operació=1
                    while(operació!=0):
                        system('cls')
                        print("\n            Restant")
                        a = int(input("\n  Indiqui el primer operand: "))
                        b = int(input("\n  Insereix un segon opreand: "))
                        c=a-b
                        print("\n       ",a," - ",b," = ",c,"")
                        sleep(2)
                    
                        #Repetir operació?
                        
                        print("\n""          1. Repetir")
                        print("          0. Sortir")
                        repetir = input("\n""Selecciona l'opció que vulguis: ")
                        if repetir == "1":
                            operació=1
                                    
                        if repetir == "0":
                            opcio=menu_principal()

                case "3":
                    operació=1
                    while(operació!=0):
                        system('cls')
                        print("\n         Multiplicant")
                        a = int(input("\n  Indiqui el primer operand: "))
                        b = int(input("\n  Insereix un segon opreand: "))
                        c=a*b
                        print("\n       ",a," x ",b," = ",c,"")
                        sleep(2)
                    
                        #Repetir operació?
                        
                        print("\n""          1. Repetir")
                        print("          0. Sortir")
                        repetir = input("\n""Selecciona l'opció que vulguis: ")
                        if repetir == "1":
                            operació=1
                                    
                        if repetir == "0":
                            opcio=menu_principal()

                case "4":
                    operació=1
                    while(operació!=0):
                        system('cls')
                        print("\n           Dividint")
                        a = int(input("\n  Indiqui el primer operand: "))
                        b = int(input("\n  Insereix un segon opreand: "))
                        c=a/b
                        print("\n       ",a," ÷ ",b," = ",c,"")
                        sleep(2)
                    
                        #Repetir operació?
                        
                        print("\n""          1. Repetir")
                        print("          0. Sortir")
                        repetir = input("\n""Selecciona l'opció que vulguis: ")
                        if repetir == "1":
                            operació=1
                                    
                        if repetir == "0":
                            opcio=menu_principal()

                case "5":
                    operació=1
                    while(operació!=0):
                        system('cls')
                        print("\n         Potenciant")
                        a = int(input("\n  Indiqui el primer operand: "))
                        b = int(input("\n  Insereix un segon opreand: "))
                        c=a**b
                        print("\n       ",a," ** ",b," = ",c,"")
                        sleep(2)
                    
                        #Repetir operació?
                        
                        print("\n""         1. Repetir")
                        print("         0. Sortir")
                        repetir = input("\n""Selecciona l'opció que vulguis: ")
                        if repetir == "1":
                            operació=1
                                    
                        if repetir == "0":
                            opcio=menu_principal()

                case "6":
                    operació=1
                    while(operació!=0):
                        system('cls')
                        print("\n           Modul")
                        a = int(input("\n  Indiqui el primer operand: "))
                        b = int(input("\n  Insereix un segon opreand: "))
                        c=a**b
                        print("\n       ",a," ** ",b," = ",c,"")
                        sleep(2)
                    
                        #Repetir operació?
                        
                        print("\n""         1. Repetir")
                        print("         0. Sortir")
                        repetir = input("\n""Selecciona l'opció que vulguis: ")
                        if repetir == "1":
                            operació=1
                                    
                        if repetir == "0":
                            opcio=menu_principal()

                case "0":
                    opcio=1

                
                    
        case "2":
            opcio3=menu_reals()
            match opcio3:
                case "1":
                    operació=1
                    while(operació!=0):
                        system('cls')
                        print("\n            Sumant")
                        a = int(input("\n  Indiqui el primer operand: "))
                        b = int(input("\n  Insereix un segon opreand: "))
                        while(a):
                            c=a+b
                        print("\n       ",a," + ",b," = ",c,"")
                        sleep(2)
                    
                        #Repetir operació?
                        
                        print("\n""          1. Repetir")
                        print("          0. Sortir")
                        repetir = input("\n""Selecciona l'opció que vulguis: ")
                        if repetir == "1":
                            
                            operació=1
                                    
                        if repetir == "0":
                            opcio3=menu_principal()