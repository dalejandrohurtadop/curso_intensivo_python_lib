edad = int(input('Ingrese la edad de la persona: '))

if edad < 2:
    print('La persona es un bebé.')
elif edad >= 2 and edad < 4:
    print('La persona es un niño pequeño.')
elif edad >= 4 and edad < 13:
    print('La persona es un niño.')
elif edad >= 13 and edad < 20:
    print('La persona es un adolecente.')
elif edad >= 20 and edad < 65:
    print('La persona es un adulto.')
else:
    print('La tiene 65 años o más')

