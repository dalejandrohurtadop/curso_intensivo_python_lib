import time


inicio = time.perf_counter()

print('Bienvenido al cine')

while True:
    edad = 4 #int(input('Ingrese su edad para informale el valor de la boleta: '))

    if edad < 0 or edad > 150:
        print('Valor incorrecto\n')
    elif edad < 3 and edad > 0:
        precio = 0
        break
    elif edad < 12:
        precio =8
        break
    else:
        precio = 12
        break

print(f'El precio de la entrada es ${precio}')

fin = time.perf_counter()

print(f'El programa 1 se ejecutó en {fin - inicio:0.6f} segundos')



#------------------------------

inicio2 = time.perf_counter()

print('Bienvenido al cine')
bandera =True
while bandera:

    edad = 4 #int(input('Ingrese su edad para informale el valor de la boleta: '))

    if edad < 0 or edad > 150:
        print('Valor incorrecto\n')
    elif edad < 3 and edad > 0:
        precio = 0
        bandera = False
    elif edad > 3 and edad <12:
        precio = 8
        bandera = False
    elif edad >= 12:
        precio =12
        bandera = False


print(f'El precio de la entrada es ${precio}')

fin2 = time.perf_counter()

print(f'El programa 2 se ejecutó en {fin2 - inicio2:0.6f} segundos')