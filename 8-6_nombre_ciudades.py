def ciudad_pais(ciudad, pais):
    return f'{ciudad}, {pais}'

while True:
    print(f'Ingrese el nombre de un ciudad con su respectivo pais.')
    print(f'En caso de querer salir ingrese "q"')

    ciudad = input("Ingrese el nombre de la ciudad: ")
    pais = input("Ingrese el nombre del pais: ")

    if ciudad.lower() =='q' or pais.lower() == 'q':
        break
    else:
        print(ciudad_pais(ciudad, pais))
        