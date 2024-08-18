# # sep="" agrega separaciones de con cualquier caracter que desees
# print("Hola","Mundo","agua", "con pollo", sep=" + ")

# #end="" hace que todo el texto aparezca en una linea
# print("Nunca", end=" ")
# print("Pares de aprender")

#Variables
frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase:", frase, "Autor:", author)

#f-strings (Utilizar expresiones dentro de cadenas de texto)
print(f"Frase: {frase}, Autor: {author}")

#format
print("Frase: {}, Autor: {}".format(frase,author))

#formato especifico
valor = 3.14159
print("Valor: {:.2f}".format(valor))

#salto especial
print("Hola\nMundo")

print("Hola \"mundo\"")

print("\\\\\\\\\\\\\\\\\\\\")