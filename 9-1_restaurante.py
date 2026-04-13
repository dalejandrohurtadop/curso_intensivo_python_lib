class Restaurante:
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina

    def describir_restaurante(self):
        mensaje = f'El restaurante se llama "{self.nombre_restaurante.upper()}" y es tipo {self.tipo_cocina}'
        print(mensaje)

    def abrir_restaurante(self):
        print(f'El restaurante "{self.nombre_restaurante}" ha abierto sus puertas')

mi_restaurante = Restaurante('Comida tìpica DAHP', 'Comida Colombiana')

print(mi_restaurante.nombre_restaurante)
print(mi_restaurante.tipo_cocina)

mi_restaurante.describir_restaurante()
mi_restaurante.abrir_restaurante()