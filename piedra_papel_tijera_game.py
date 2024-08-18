game = True
while game:
    print("Bienvenido a piedra, papel o tijera")
    jugador1 = input("Jugador 1, elige \"piedra\", \"papel\" o \"tijera\" \n").lower()
    jugador2 = input("Jugador 2, elige \"piedra\", \"papel\" o \"tijera\" \n").lower()

    if jugador1 == jugador2:
        print("Ha habido un empate")
    elif (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "piedra" and jugador2 == "tijera"):
        print("Jugador 1 Gana")
    else:
        print ("Jugador 2 Gana")
    end = input("Deseas terminar el juego? Escribe \"Si\" o \"No\" \n").lower()
    if end == "si":
        game = False