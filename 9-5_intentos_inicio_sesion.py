class Usuario:
    def __init__(self, nombre, apellido, edad, alias, departamento, intentos_inicio = 0):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.alias = alias
        self.departamento = departamento
        self.intentos_inicio = intentos_inicio
    
    def describir_usuario(self):
        mensaje = f'Nombre: {self.nombre.title()}'
        mensaje += f'\nApellido: {self.apellido.title()}'
        mensaje += f'\nEdad: {self.edad}'
        mensaje += f'\nDepartamento: {self.departamento.title()}'
        mensaje += f'\nAlias: {self.alias}'

        print(mensaje)

    def saludar_usuario(self):
        print(f'Hola {self.nombre.title()} {self.apellido.title()}. !Bienvenido¡')
    
    def incrementar_intentos_inicio(self):
        self.intentos_inicio += 1

    def restablecer_intentos(self):
        self.intentos_inicio = 0

mi_usuario = Usuario('david', 'hurtado', 34, 'dalejandrohurtadop', 'infraestructura')

mi_usuario.describir_usuario()
mi_usuario.saludar_usuario()

for i in range(10):
    mi_usuario.incrementar_intentos_inicio()
    print(f'Número de intentos: {mi_usuario.intentos_inicio}')

mi_usuario.restablecer_intentos()


print(mi_usuario.intentos_inicio)
