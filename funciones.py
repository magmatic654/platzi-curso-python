def greet(name, last_name="No tiene apellido"):
    print(f"Hola {name} {last_name}")

greet("Harold","Navarro")
greet("Diego")
greet(last_name="Navarro", name="Harold")