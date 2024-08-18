name = 'HAROLD Edward'
last_name = "    Rodriguez Navarro   "
full_name = name +" "+ last_name
print(name)
print(name +" "+ last_name)
print(full_name)

print(len(name))
print(len(last_name))
print(len(full_name))
print(name.lower())
print(name.upper())
print(last_name.strip())

#Capitaliza la primera letra.

texto = "hola mundo"
print(texto.capitalize())  # "Hola mundo"

#title()
#Capitaliza la primera letra de cada palabra.
texto = "hola mundo"
print(texto.title())  # "Hola Mundo"

#strip()
#Elimina los espacios en blanco al inicio y al final.
texto = "  hola  "
print(texto.strip())  # "hola"

#replace(old, new)
#Reemplaza partes de la cadena.
texto = "hola mundo"
print(texto.replace("mundo", "Python"))  # "hola Python"

#split(sep)
#Divide la cadena en una lista según el separador.
texto = "hola,mundo,Python"
print(texto.split(","))  # ['hola', 'mundo', 'Python']

#join(iterable)
#Une elementos de un iterable en una sola cadena.
lista = ["hola", "mundo"]
print(" ".join(lista))  # "hola mundo"

#find(sub)
#Busca una subcadena y devuelve el índice de su primera aparición.
texto = "hola mundo"
print(texto.find("mundo"))  # 5

#startswith(prefix) y endswith(suffix)
#Verifica si la cadena empieza o termina con una subcadena.
texto = "hola mundo"
print(texto.startswith("hola"))  # True
print(texto.endswith("mundo"))  # True

#Ejemplo Completo:
frase = "  Bienvenido a Python!  "
frase = frase.strip().replace("Python", "el mundo de Python").upper()
print(frase)  # "BIENVENIDO A EL MUNDO DE PYTHON!"