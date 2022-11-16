#Definició de funcions auxiliar
#Funció del menú  principal
def menu_principal():
        print("\n           Calculadora\n")
        print("               Menú")
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
    Calculadora de nombres enters\n
            1.Sumar
            2.Restar
            3.Dividir
            4.Multiplicar
            5.Potència
            6.Mòdul
            0. Sortir\n""")
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

#Funció Canvis de Base Menú

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

decimal = int(input("Ingresa un número decimal: "))
binario = decimal_a_binario(decimal)
print(f"El número {decimal} es {binario} en binario")


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
        case "1":
            opcio2=menu_enters()
            a = int(input("Indiqui el primer operand: "))
            b = int(input("Insereix un segon opreand"))

