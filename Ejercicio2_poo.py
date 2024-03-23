"""Ejercicio:
Hacer un programa que pida 3 números y determine cuál es mayor.
"""
num1=int(input("Digite el primer número: "))
num2=int(input("Digite el segundo número: "))
num3=int(input("Digite el tercer número: "))
print()
if num1>=num2 and num1>=num3:
    print(f"El número mayor es {num1}")
elif num2>=num1 and num2>=num3:
    print(f"El número mayor es {num2}")
elif num3>=num1 and num3>=num2:
    print(f"El número mayor es {num3}")
