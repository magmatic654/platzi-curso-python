class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_avaiable = True
    
    def sell(self):
        if self.is_avaiable:
            self.is_avaiable = False
            print(f"El vehiculo {self.brand} {self.model} {self.price}. Ha sido vendido")
        else:
            print(f"El vehiculo {self.brand} {self.model} {self.price}, No está disponible")

    def check_avaiable(self):
        return self.is_avaiable

    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
    
    def stop_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
    
class Car(Vehicle):
    def start_engine(self):
        if not self.is_avaiable:
            return f"El motor del coche {self.brand} está en marcha"
        else: 
            return f"El coche {self.brand} no está disponible"
        
    def stop_engine(self):
        if self.is_avaiable:
            return f"El motor del coche {self.brand} se ha detenido"
        else:
            return f"El coche {self.brand} no está disponible"
    
class Bike(Vehicle):
    def start_engine(self):
        if not self.is_avaiable:
            return f"La bicicleta {self.brand} está en marcha"
        else: 
            return f"La bicicleta {self.brand} no está disponible"
        
    def stop_engine(self):
        if self.is_avaiable:
            return f"La bicicleta {self.brand} se ha detenido"
        else:
            return f"La bicicleta {self.brand} no está disponible"

class Truck(Vehicle):
    def start_engine(self):
        if not self.is_avaiable:
            return f"El motor del camión {self.brand} está en marcha"
        else: 
            return f"El camión {self.brand} no está disponible"
        
    def stop_engine(self):
        if self.is_avaiable:
            return f"El motor del camión {self.brand} se ha detenido"
        else:
            return f"El camión {self.brand} no está disponible"
        

class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_avaiable():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"Lo siento, {vehicle.brand} no está disponible")

    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_avaiable():
            avaiability = f"Está disponible y cuesta {vehicle.get_price()}"
        else:
            avaiability = "No está disponible"
        print(f"El {vehicle.brand} {avaiability}")

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicles(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"El vehiculo {vehicle.brand} ha sido añadido al inventario")

    def register_customers(self, customer: Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido registrado")

    def show_avaiable_vehicles(self):
        if len(self.inventory) == 0:
            print("No hay vehiculos en el inventario")
        else:
            print("Vehiculos disponibles en la tienda")
            for vehicle in self.inventory:
                if vehicle.check_avaiable():
                    print(f"- {vehicle.brand} {vehicle.model} por ${vehicle.price}")

car1 = Car("Toyota", "Corolla", 20000)
bike1 = Bike("Yamaha", "BMX", 3000)
truck1 = Truck("Honda", "C18", 250000)

customer1 = Customer("Harold")

dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)

#Mostrar vehiculos disponibles
dealership.show_avaiable_vehicles()

#Cliente consulta vehiculo
customer1.inquire_vehicle(car1)

#Cliente compra vehiculo
customer1.buy_vehicle(car1)

# #Mostrar vehiculos disponibles
dealership.show_avaiable_vehicles()