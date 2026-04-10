current_users = ['david', 'alejandro', 'fabian', 'raul', 'juan']
new_users = ['david', 'sebastian', 'miguel', 'juan', 'esteban']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f'El usuario "{new_user.lower()}" ya existe, por favor utilice otro nombre')
    else:
        print(f'El usuario "{new_user.lower()}" esta disponible para ser usado')

