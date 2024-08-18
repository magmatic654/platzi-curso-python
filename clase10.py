numbers = {1: "uno", 2: "dos", 3: "tres"}
print(numbers)
print(numbers[2])
print(type(numbers))

information = {"nombre": "Harold",
               "Apellido": "Navarro",
               "Altura": 1.88,
               "Edad": 29}

print(information)
del information["Edad"]
print(information)

claves = information.keys()
print(claves)
print(type(claves))

values = information.values()
print(values)

pairs = information.items()
print(pairs)

contacts = {"Harold":{
                "Apellido": "Navarro",
                "Altura": 1.88,
                "Edad": 25},
            "Ximena":{
                "Apellido": "Castillo",
                "Altura": 1.62,
                "Edad": 22}}

print(contacts)
print(contacts["Harold"])
print(contacts["Ximena"])