class Usuario:
    def __init__(self, nombre, apellido, edad, alias, departamento):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.alias = alias
        self.departamento = departamento
    
    def describir_usuario(self):
        mensaje = f'Nombre: {self.nombre.title()}'
        mensaje += f'\nApellido: {self.apellido.title()}'
        mensaje += f'\nEdad: {self.edad}'
        mensaje += f'\nDepartamento: {self.departamento.title()}'
        mensaje += f'\nAlias: {self.alias}'

        print(mensaje)

    def saludar_usuario(self):
        print(f'Hola {self.nombre.title()} {self.apellido.title()}. !Bienvenido¡')
    

mi_usuario = Usuario('david', 'hurtado', 34, 'dalejandrohurtadop', 'infraestructura')

mi_usuario.describir_usuario()
mi_usuario.saludar_usuario()
    
