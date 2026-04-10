favorite_lenguges ={
        'jen': 'python',
        'sarah': 'c',
        'edward': 'rust',
        'phil': 'python'
        }

encuestados = ['phil', 'david', 'sarah', 'alejandro', 'jen', 'angelica', 'angel', 'edwar']

for k in encuestados:
    if k not in favorite_lenguges.keys():
        print(f'Hola! {k.title()}, Te invitamos a hacer la encuesta para conocer cual es tu lenguaje favorito')
    else:
        print(f'{k.title()}, Gracias por participar en a encuesta')
