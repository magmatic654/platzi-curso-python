class car:
    def __init__(self, name, company, year, price):
        self.name = name
        self.company = company
        self.year = year
        self.price = price
        self.aviable = True

    def add_car(self):
        if self.aviable == True:
            self.aviable = False
            print(f" El vehiculo: {car.name} año: {car.year} ha sido añadido")
        else:
            print(f"El vehiculo: {car.name} año: {car.year} no está disponible")

class client:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.cars_own = []

    def buy_car(self, car):
        if car in dealerShip.cars:
            self.cars_own.append(car)
            dealerShip.cars.remove(car)
            print(f"!Felicidades {self.name}, has comprado {car.name} año: {car.year}!")
        else:
            print(f"El vehiculo: {car.name} año: {car.year} no está dispoible para su compra")

    def sell_car(self, car):
        if len(self.cars_own) == 0:
            print("El cliente no cuenta con algún vehiculo registrado")
        elif car in self.cars_own:
            print(f"!Enhorabuena {self.name}, has vendido tu vehiculo: {car.name} año: {car.year}!")
            self.cars_own.remove(car)
            dealerShip.cars.append(car)
        else:
            print("El cliente no cuenta con el vehiculo para su venta")

    def inquire_car(self, car):
        aviability = "está disponible" if car in dealerShip.cars else "No está disponible"
        print(f"El vehiculo {car.company} {car.name} {aviability} ")
            
class dealerShip:
    def __init__(self):
        self.clients = []
        self.cars = []

    def register_client(self, client):
        self.clients.append(client)
        print(f"Cliente: {client.name} con id: {client.user_id} registrado correctamente")
    
    def add_car(self, car):
        if car.aviable == True:
            self.cars.append(car)
            print(f"Vehiculo: {car.name} año: {car.year} añadido correctamente al consesionario")
        else:
            print(f"No está disponible el vehiculo: {car.name} año: {car.year}")
    
    def show_aviable_cars(self):
        if len(self.cars) == 0:
            print("No hay vehiculos en el inventario")
        else:
            print("Vehiculos disponibles:")
            for car in self.cars:
                print(f"{car.company}, {car.name}, {car.year}, {car.price}")

#Crear Carros
car1 = car("Aveo","Chevrolet","2020", 180000)
car2 = car("Murcielago","Lamborghini","2012", 8480000)
car3 = car("i5 sport","BMW","2008", 1250000)

#Crear cliente
client1 = client("Harold", "001")

#Registrar cliente
dealerShip = dealerShip()
dealerShip.register_client(client1)
dealerShip.add_car(car1)
dealerShip.add_car(car2)
dealerShip.add_car(car3)


#Muestra vehiculos disponibles
dealerShip.show_aviable_cars()

#Comprobar disponibilidad de vehiculos
client1.inquire_car(car1)

#Comprar vehiculo
client1.buy_car(car1)
client1.buy_car(car2)

#Venta vehiculo
client1.sell_car(car1)

#Muestra los vehiculos disponibles
dealerShip.show_aviable_cars()