print('Adivine el color del alien')

print('\nPara verde marque la opción 1')
print('Para amarillo marque la opción 2')
print('Para rojo marque la opción 3')

color_alien = input('\nIngrese el color del alien: ')

if color_alien == '1':
    puntaje = 5
    color = 'verde'
    print(f'\nFelicitaciones, el alien es de color {color} y por eso ha ganado {puntaje} puntos.')
elif color_alien == '2':
    puntaje = 10
    color = 'amarillo'
    print(f'\nFelicitaciones, el alien es de color {color} y por eso ha ganado {puntaje} puntos.')
else:
    puntaje = 15
    color = 'rojo'
    print(f'\nFelicitaciones, el alien es de color {color} y por eso ha ganado {puntaje} puntos.')
