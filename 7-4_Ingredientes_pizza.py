print('Bienvenido a la pizzeria de confianza, donde usted arma su propia pizza')

ingredientes = []

while True:
    ingrediente = input('Ingrese el ingredietne de su pizza: ')

    print(f'EL ingrediente {ingrediente} ha sido añadido a su pizza')

    ingredientes.append(ingrediente)

    salir = input('Desea Terminar (S/N): ')

    if salir.upper() == "S":
        break

print(f'\nLos ingredientes de su pizza son: ')

for ingrediente in ingredientes:
    print(f'\t {ingrediente}')



