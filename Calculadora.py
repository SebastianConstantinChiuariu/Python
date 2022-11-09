#Definició de funcions auxiliar
#Funció del menú  principal
def menu_principal():
        print("\n Calculadora")
        print("Menú:")
        print("""
        1. Números Enters 
        2. Numeros reals
        3. Canvis de base 
        0. Sortir
        """)
        opcio = input ("Selecciona la primera opció que vulguis: ")
        return opcio

# Funció Menú nombres Enters
def menu_enters():
    print("""
        Calculadora de nombres enters
        1.Sumar
        2.Restar
        3.Dividir
        4.Multiplicar
        5.Potència
        6.Mòdul
        0. Sortir""")
    opcio= input("Selecciona l'opció que vulguis: ")
    return opcio

# Funció Menú nombres Reals
def menu_reals():
    print("""
        Calculadora de nombres enters
        1.Sumar
        2.Restar
        3.Dividir
        4.Multiplicar
        0. Sortir""")
    opcio= input("Selecciona l'opció que vulguis: ")
    return opcio

#Funció Canvis de Base

def menu_canvis_de_base():
    print("""
        Calculadora de nombres enters
        1.Sumar
        2.Restar
        3.Dividir
        4.Multiplicar
        0. Sortir""")
    opcio= input("Selecciona l'opció que vulguis: ")
    return opcio

#Programa principal de la Calculadora
opcio=1
while(opcio!=0):
    opcio=menu_principal()
    match opcio:
        case "1":
            opcio2=menu_enters()
            a = int(input("Indiqui el primer operand: "))
            b = int(input("Insereix un segon opreand"))

