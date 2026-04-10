#nombre  ='admin'

usuarios = []

if usuarios:
    for usuario in usuarios:
        if usuario == 'admin':
            print('Hola admin, le presente el informe a continuación')
        else:
            print(f'Hola, {usuario.title()}, gracias por volver a entrar')
else:
    print(f'¡Necesitamos encontrar algún usuario!')
