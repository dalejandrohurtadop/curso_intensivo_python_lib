class Car:
    """Un intento de representar un coche
    """
    def __init__(self, make, model, year):
        """Incicializa atributos para describir coche
        Args:
            make (str): Marca del coche
            model (str): Modelo del coche
            year (int): Año de fabricación
        """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reding = 0

    def get_descriptive_name(self):
        """Devuelve el nombre descriptivo del coche
        """
        long_name = f'{self.make} {self.model} {self.year}'
        return long_name.title()
    
    def read_odometer(self):
        """Imprime una declaraciòn mostrando el kilometraje del vehiculo
        """
        print(f'This car has {self.odometer_reding} miles on it')

    def update_odometer(self, mileage):
        """Configura la lectura del cuentakilometros para el valor dado.
        """
        if mileage >= self.odometer_reding:
            self.odometer_reding = mileage
        else:
            print("You can't roll back an odometer!")
        
    def increment_odometer(self, miles):
        """Incrementa el cuenta kilometros un valor dado

        Args:
            miles (int): Numero de millas a incrementar en el odometro
        """
        self.odometer_reding += miles

class Battery:
    """Un intento de modelar una bateria de un coche eléctrico
    """
    def __init__(self, batery_size=40):
        """Inicializando atributos de la bateria

        Args:
            batery_size (int, optional): Tamaño de la mbateria. Defaults to 45.
        """
        self.batery_size = batery_size

    def describe_battery(self):
        """Imprime una declaración que describe el tamaño de la batería
        """
        print(f'This car has a {self.batery_size}-kWh battery.')

    def get_range(self):
        """Imprime una frase sobre la autonomia que ofrece la batería
        """
        if self.batery_size == 40:
            range =150
        elif self.batery_size == 65:
            range = 225
        
        print(f'This car can go about {range} milles on a full charge')

    def upgrade_battery(self):
        """Actualiza la capacidad de la bateria a 65 kWh
        """
        if self.batery_size < 65:
            self.batery_size = 65


class ElectricCar(Car):
    """Representa aspectos de un coche electrico

    Args:
        Car (class): clase heredada
    """

    def __init__(self, make, model, year):
        """Inicializa los atributos de la clase base

        Args:
            make (str): Marca del coche
            model (str): Modelo del coche
            year (int): Año de fabricación
        """
        super().__init__(make, model, year)
        self.battery = Battery()


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()