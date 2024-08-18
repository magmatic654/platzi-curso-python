class vehicle:
    def __init__(self, name, company, year, price):
        self.name = name
        self.company = company
        self.year = year
        self.price = price
        self.aviable = True

    def add_vehicle(self):
        if self.aviable == True:
            self.aviable = False
            print(f" El vehiculo: {vehicle.name} año: {vehicle.year} ha sido añadido")
        else:
            print(f"El vehiculo: {vehicle.name} año: {vehicle.year} no está disponible")

    def return_vehicle(self):
        if self.aviable == False:
            self.aviable = True
            print(f"Vehiculo {self.name, self.year} ha sido devuelto")

class client:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.vehicles_own = []

    def buy_vehicle(self, vehicle):
        if vehicle in dealerShip.vehicles:
            self.vehicles_own.append(vehicle)
            dealerShip.vehicles.remove(vehicle)
            print(f"!Felicidades {self.name}, has comprado {vehicle.name} año: {vehicle.year}!")
        else:
            print(f"El vehiculo: {vehicle.name} año: {vehicle.year} no está dispoible para su compra")

    def sell_vehicle(self, vehicle):
        if len(self.vehicles_own) == 0:
            print("El cliente no cuenta con algún vehiculo registrado")
        elif vehicle in self.vehicles_own:
            print(f"!Enhorabuena {self.name}, has vendido tu vehiculo: {vehicle.name} año: {vehicle.year}!")
            self.vehicles_own.remove(vehicle)
        else:
            print("El cliente no cuenta con el vehiculo para su venta")
            
class dealerShip:
    def __init__(self):
        self.clients = []
        self.vehicles = []

    def register_client(self, client):
        self.clients.append(client)
        print(f"Cliente: {client.name} con id: {client.user_id} registrado correctamente")
    
    def add_vehicle(self, vehicle):
        if vehicle.aviable == True:
            self.vehicles.append(vehicle)
            print(f"Vehiculo: {vehicle.name} año: {vehicle.year} añadido correctamente al consesionario")
        else:
            print(f"No está disponible el vehiculo: {vehicle.name} año: {vehicle.year}")
    
    def show_aviable_vehicles(self):
        if len(self.vehicles) == 0:
            print("No hay vehiculos en el inventario")
        else:
            print("Vehiculos disponibles:")
            for vehicle in self.vehicles:
                print(f"{vehicle.company}, {vehicle.name}, {vehicle.year}, {vehicle.price}")

#Crear vehiculo
vehicle1 = vehicle("Aveo","Chevrolet","2008", 180000)
vehicle2 = vehicle("Murcielago","Lamborghini","2012", 8480000)
vehicle3 = vehicle("Aveo","Chevrolet","2008", 180000)

#Crear cliente
client1 = client("Harold", "001")

#Registrar cliente
dealerShip = dealerShip()
dealerShip.register_client(client1)
dealerShip.add_vehicle(vehicle1)
dealerShip.add_vehicle(vehicle2)


#Muestra vehiculos disponibles
dealerShip.show_aviable_vehicles()

#Comprar vehiculo
client1.buy_vehicle(vehicle1)
client1.buy_vehicle(vehicle2)
client1.buy_vehicle(vehicle1)

#Venta vehiculo
client1.sell_vehicle(vehicle1)
client1.sell_vehicle(vehicle1)
