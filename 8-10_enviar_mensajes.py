messages = [
    "Hola, ¿cómo va todo?",
    "No olvides practicar Python hoy.",
    "¿Viste el nuevo video de programación?",
    "Llego en 5 minutos.",
    "El código finalmente funcionó.",
    "¿Quieres ir por un café?",
    "Recuerda hacer commit de tus cambios.",
    "¡Felicidades por terminar el capítulo!",
    "Mañana hay reunión a las 10.",
    "Python es genial para automatizar tareas."
]

def enviar_mensajes(lista_mensajes:list)->None:
    """
    A partir de una lista de mensajes, la funciòn imprime todos los mensajes
    """
    i = 0
    mensajes_enviados =[]
    
    while lista_mensajes:
        mensaje = lista_mensajes.pop()
        mensajes_enviados.append(mensaje)

        print(f'El mensaje es: {mensaje}\n')
        i+=1
    
    print(lista_mensajes)
    print(mensajes_enviados)


enviar_mensajes(messages)
