class Restaurante:
    def __init__(self, nombre_restaurate, tipo_cocina, numero_servicio):
        self.nombre_restaurate = nombre_restaurate
        self.tipo_cocina = tipo_cocina
        self.numero_servicio = numero_servicio

    def describir_restaurante(self):
        describ_resta = f"El {self.nombre_restaurate.title()} es un restaurante de tipo {self.tipo_cocina.title()}"
        return describ_resta

    def abrir_restaurante(self):
        mensaje = f"Buen dìa, el restaurante {self.nombre_restaurate.title()} le da la bienvenida"
        return mensaje

    def establecer_numero_servicio(self, num_servicio_inicial):
        self.numero_servicio = num_servicio_inicial

    def incrementar_numero_servicio(self, num_cliente):
        self.numero_servicio += num_cliente


class CarritoDeHelados(Restaurante):
    def __init__(self, nombre_restaurate, tipo_cocina, numero_servicio):
        super().__init__(nombre_restaurate, tipo_cocina, numero_servicio)
        self.sabores = ["Arequipe", "Mora", "Vainilla", "Chocolate", "Mandarina"]

    def elegir_sabor(self):
        print("Los sabores de helados disponibles son: ")
        for i, sabor in enumerate(self.sabores):
            print(f"{i + 1}. {sabor}")


mi_carrito_helados = CarritoDeHelados("Mi carrito", "Helados", 0)

mi_carrito_helados.elegir_sabor()
