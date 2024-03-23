'''
 Este código fué hecho para dar respuesta
 al ejercicio propuesto en el vídeo de 
 Programación ATS (https://youtu.be/kAdgwY_mVxM?si=30BcpsM_9tnUXe5_)
 una opción hecha con un bucle está en el siguiente enlace
 https://onlinegdb.com/_UpdKxZNZ
'''

saldo = 1000

print("Menú principal\n1. Ingresar dinero a la cuenta\n2. Retirar dinero de la cuenta\n3. Mostrar dinero de la cuenta")
op = input("Elige una opción: ")
op = int(op)
if op==1:
    saldo_ing = input("Ingresa la cantidad de dinero que quieres agregar a tu cuenta: $")
    saldo_ing = float(saldo_ing)
    if saldo_ing>0:
        saldo+=saldo_ing
        print("El saldo actual de tu cuenta es: ",saldo)
    else:
        print("En ese caso, no vas a ingresar dinero. Tu saldo es: $",saldo)
elif op==2:
    print("Tu saldo actual es: ",saldo)
    if saldo!=0:
        saldo_rt = input("Ingresa la cantidad que quieres retirar: $")
        saldo_rt = float(saldo_rt)
        if saldo_rt<=saldo and saldo_rt>0:
            saldo-=saldo_rt
            print("Perfecto, acabas de retirar $",saldo_rt)
            print("Tu saldo actual es: $",saldo)
        else: print("No se puede hacer esta transacción.")
    
elif op==3:
    print("Tu saldo actual es: ",saldo)
else: print("Opción inválida.")

