class Restaurante:
    def __init__(self, nombre_restaurate, tipo_cocina, numero_servicio):
        self.nombre_restaurate = nombre_restaurate
        self.tipo_cocina = tipo_cocina
        self.numero_servicio = numero_servicio

    def describir_restaurante(self):
        describ_resta = f'El {self.nombre_restaurate.title()} es un restaurante de tipo {self.tipo_cocina.title()}'
        return describ_resta

    def abrir_restaurante(self):
        mensaje = f'Buen dìa, el restaurante {self.nombre_restaurate.title()} le da la bienvenida'
        return mensaje

    def establecer_numero_servicio(self, num_servicio_inicial):
        self.numero_servicio = num_servicio_inicial

    def incrementar_numero_servicio(self, num_cliente):
        self.numero_servicio += num_cliente

restaurante = Restaurante('el fogón', 'Comida danesa', 0)

print(restaurante.describir_restaurante())

print(f'Número de clientes: {restaurante.numero_servicio}')

print(restaurante.abrir_restaurante())

restaurante.establecer_numero_servicio(10)

print(f'Número de clientes: {restaurante.numero_servicio}')

restaurante.incrementar_numero_servicio(5)


print(f'Número de clientes: {restaurante.numero_servicio}')
