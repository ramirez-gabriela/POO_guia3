'''

Comprobar si es una vocal

'''

letra = input("Digite una un caracter: ").lower() # Se utilizo la funcion inpunt para tomar datos de entrada, y se incluye con el método lower para que pase las letras mayusculas a minusculas

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':   # Se utiliza el operador logico or
    print("Es una vocal")    # Aquí se utiliza la funcion print para imprimir en pantalla
else:
    print("No es una vocal")
    
