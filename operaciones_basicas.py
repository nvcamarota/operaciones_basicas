""" 
OPERACIONES BÁSICAS
1) Crear un programa que solicite dos números enteros.
2) Realizar las siguientes operaciones: suma, resta, multiplicación y módulo.
3) Mostrar el resultado de cada operación en un formato claro y amigable. Incluir un mensaje personalizado que explique cada resultado obtenido.
"""

numero1 = int(input("Ingrese su primer número: "))
numero2 = int(input("Ingrese su segundo número: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
modulo = numero1 % numero2

print(f"La suma del número {numero1} y el número {numero2} da, como resultado, {suma}")
print(f"La resta del número {numero1} y el número {numero2} da, como resultado, {resta}")
print(f"La multiplicación del número {numero1} y el número {numero2} da, como resultado, {multiplicacion}")
print(f"El módulo del número {numero1} y el número {numero2} da, como resultado, {modulo}")
