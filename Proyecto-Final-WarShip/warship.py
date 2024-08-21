import os
class Board:
    def __init__(self, row=10, col=10):
        self.row = row
        self.col = col
        self.water = '.'
        self.board = []

    def createBoard(self):
        for row in range(self.row):
            self.board.append([self.water for i in range(self.col)])

    def printBoard(self):
        for y in self.board:
            counter = 1
            for x in y:
                if counter == self.col:
                    print(x, " ")
                else:
                    print(x," ", end="")
                counter += 1
    
    def modifyBoard(self, col, row, element):
        self.board[col-1][row-1] = element

class Ship:
    def __init__(self, player):
        self.player = player
        self.cells = []
        self.name = ""
        self.coordinates_xy = []
        self.ship = {
            "name": self.name,
            "coordinates_xy": self.coordinates_xy,
        }
    def create_ship(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
    
    def set_ship_in_board(self, board, start_col, start_row, position):
        if position == "H":
            row = board.board[start_row - 1]
            for i in range(len(self.cells)):
                row[start_col - 1 + i] = self.cells[i]
                self.coordinates_xy.append([start_row, i+1])
        elif position == "V":
            for i in range(len(self.cells)):
                board.board[start_row - 1 + i][start_col - 1] = self.cells[i]
                self.coordinates_xy.append([i+1, start_col])
        else:
            raise ValueError("No se ha seleccionado una posicion H o V")
        
        
        self.player.ships.append(self.ship)

        # print(self.player.ships[0]["coordinates_xy"])
    
class AircraftCarrier(Ship):
    def create_ship(self):
        self.name = "AircraftCarrier"
        self.cells = ["A"] *5
        self.ship = {
            "name": self.name,
            "coordinates_xy": self.coordinates_xy,

        }
class Battleship(Ship):
    def create_ship(self):
        self.name = "Battleship"
        self.cells = ["B"] * 4
        self.ship = {
            "name": self.name,
            "coordinates_xy": self.coordinates_xy
        }
        
class Cruiser(Ship):
    def create_ship(self):
        self.name = "Cruiser"
        self.cells = ["C"] * 3
        self.ship = {
            "name": self.name,
            "coordinates_xy": self.coordinates_xy
        }
class Submarine (Ship):
    def create_ship(self):
        self.name = "Submarine"
        self.cells = ["S"] * 3
        self.ship = {
            "name": self.name,
            "coordinates_xy": self.coordinates_xy
        }
class Destroyer (Ship):
    def create_ship(self):
        self.name = "Destroyer"
        self.cells = ["D"] * 2
        self.ship = {
            "name": self.name,
            "coordinates_xy": self.coordinates_xy
        }

class Player:
    def __init__(self, name):
        self.name = name
        self.ships = []

    def atack(self, board, row, col):
        # Identificar si la coordenada atacada tiene un barco
        coordinate_atack = (board.board[row - 1][col - 1])
        
        if coordinate_atack != board.water:
            board.modifyBoard(row, col, "*")
            print("¡Has dado en un blanco!")
            
            for ship in self.ships:
                coordenates = ship['coordinates_xy']
                
                # Convertir la coordenada del ataque en una lista para comparación
                ataque = [row, col]
                
                if ataque in coordenates:
                    # Eliminar la coordenada atacada
                    coordenates.remove(ataque)
                    
                    # Verificar si el barco ha sido destruido
                    if not coordenates:
                        print(f"¡{ship['name']} ha sido destruido!")
                        self.ships.remove(ship)  # Eliminar el barco destruido
                    break
        else:
            board.modifyBoard(row, col, "a")
            print("¡Agua!")
    
    def printShips(self):
        print(self.ships)

class Game():
    def __init__(self):
        self.players = []

    def inicialize_game(self):
        print("Bienvenidos a warShip")
        jugador_1_name = input("Jugador 1, escribe tu nombre: ")
        jugador_2_name = input("Jugador 2, escribe tu nombre: ")
        player_1 = Player(jugador_1_name)
        player_2 = Player(jugador_2_name)
        self.add_player(player_1)
        self.add_player(player_2)
        board_1 = Board() 
        board_2 = Board()
        board_1.createBoard()
        board_2.createBoard()
        
        os.system('cls')
        self.template_ships(player_1, board_1)
        os.system('cls')
        self.template_ships(player_2, board_2)
        os.system('cls')
        self.turn([player_1, player_2], [board_1, board_2])
        
    def set_ships(self, player, board, barcos):
        print(f"{player.name}, Elige las posiciones de tus barcos en el tablero")
        board.printBoard()
        try:
            for barco in barcos:
                x = int(input(f"{player.name}. Elige las coordenadas X para: {barco.name}.\n"))
                y = int(input(f"{player.name}. Elige las coordenadas Y para: {barco.name}.\n"))
                position = input(f"{player.name}. Elige la orientación del barco para: {barco.name}. \"H\": Horizontal / \"V\": Vertical. \n").upper()
                barco.set_ship_in_board(board, x, y, position)
                board.printBoard()
        except:
               print("Intenta nuevamente")
               player.ships = []
               return self.set_ships(player, board, barcos) 
                
    
    def template_ships(self, player, board):
        aircraftCarrier =AircraftCarrier(player)
        battleship = Battleship(player)
        cruiser = Cruiser(player)
        submarine = Submarine(player)
        destroyer = Destroyer(player)

        aircraftCarrier.create_ship()
        battleship.create_ship()
        cruiser.create_ship()
        submarine.create_ship()
        destroyer.create_ship()

        self.set_ships(player, board, [aircraftCarrier, battleship, cruiser, submarine, destroyer])
        

    def add_player(self, player):
        self.players.append({"name":player.name, "ships":player.ships, "player_obj": player})
    
    def print_players(self):
        print(self.players)
                
    def win_condition(self):
        for i in self.players:
            if len(i["ships"]) == 0:
                return True
            
    def turn(self, players, boards):
        turn_player = 1
        while turn_player:
            player_name = players[turn_player-1].name
            player_obj = players[turn_player-1]

            if turn_player == 1:
                print(f"{player_name}, es hora de atacar")
                row = int(input("Elige la fila de ataque, coordenada X "))
                col = int(input("Elige la columna de ataque, coordenada Y "))
                player_obj.atack(boards[1], row, col)
                boards[0].printBoard()
                turn_player = 2
            else:
                row = int(input("Elige la fila de ataque, coordenada X "))
                col = int(input("Elige la columna de ataque, coordenada Y "))
                player_obj.atack(boards[0], row, col)
                input(f"{player_name}, es hora de atacar")
                boards[1].printBoard()
                turn_player = 1
            
                
            if self.win_condition():
                return print(f"{player_name} ha ganado")

        
        
game1 = Game()
game1.inicialize_game()
