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

class Admin(Usuario):
    def __init__(self,nombre, apellido, edad, alias, departamento, intentos_inicio = 0):
        super().__init__(nombre, apellido, edad, alias, departamento, intentos_inicio = 0)
        self.privilegios = ['puede añadir comentario', 'puede borrar comentario', 'puede vetar usuarios']

    def show_privileges(self):
        print('Los prvilegios del administrador son los siguientes: ')

        for i, privilegio in enumerate(self.privilegios):
            print(f'{i+1}. {privilegio}')


mi_usuario = Admin('david', 'hurtado', 34, 'dalejandrohurtadop', 'infraestructura')

mi_usuario.describir_usuario()
mi_usuario.saludar_usuario()

mi_usuario.show_privileges()
