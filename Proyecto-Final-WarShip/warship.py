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
            "Name": self.name,
            "Coordinates_xy": self.coordinates_xy,
        }
    def create_ship(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
    
    def set_ship_in_board(self, board, start_col, start_row, position):
        if position == "H":
            row = board.board[start_row - 1]
            for i in range(len(self.cells)):
                if row[start_col - 1 + i] != board.water:
                    return print("Hubo un error")
            for i in range(len(self.cells)):
                row[start_col - 1 + i] = self.cells[i]
                self.coordinates_xy.append([start_row, i+1])
        elif position == "V":
            for i in range(len(self.cells)):
                if board.board[start_row - 1 + i][start_col - 1] != board.water:
                    return print("Hubo un error")
            for i in range(len(self.cells)):
                board.board[start_row - 1 + i][start_col - 1] = self.cells[i]
                self.coordinates_xy.append([i+1, start_col])
        self.player.ships.append(self.ship)
    
class AircraftCarrier(Ship):
    def create_ship(self):
        self.name = "AircraftCarrier"
        self.cells = ["A"] *5
        self.ship = {
            "Name": self.name,
            "Coordinates_xy": self.coordinates_xy,

        }
class Battleship(Ship):
    def create_ship(self):
        self.name = "Battleship"
        self.cells = ["B"] * 4
        self.ship = {
            "Name": self.name,
            "Coordinates_xy": self.coordinates_xy
        }
        
class Cruiser(Ship):
    def create_ship(self):
        self.name = "Cruiser"
        self.cells = ["C"] * 3
        self.ship = {
            "Name": self.name,
            "Coordinates_xy": self.coordinates_xy
        }
class Submarine (Ship):
    def create_ship(self):
        self.name = "Submarine"
        self.cells = ["S"] * 3
        self.ship = {
            "Name": self.name,
            "Coordinates_xy": self.coordinates_xy
        }
class Destroyer (Ship):
    def create_ship(self):
        self.name = "Destroyer"
        self.cells = ["D"] * 2
        self.ship = {
            "Name": self.name,
            "Coordinates_xy": self.coordinates_xy
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
                coordenates = ship['Coordinates_xy']
                
                # Convertir la coordenada del ataque en una lista para comparación
                ataque = [row, col]
                
                if ataque in coordenates:
                    # Eliminar la coordenada atacada
                    coordenates.remove(ataque)
                    
                    # Verificar si el barco ha sido destruido
                    if not coordenates:
                        print(f"¡{ship['Name']} ha sido destruido!")
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
        
        barco_1 = AircraftCarrier(player_1)
        barco_2 = Battleship(player_1)
        barco_3 = Battleship(player_1)
        barco_4 = Cruiser(player_1)
        barco_5 = Submarine(player_1)

        barco_1.create_ship()
        barco_2.create_ship()
        barco_3.create_ship()
        barco_4.create_ship()
        barco_5.create_ship()
        
        barco_6 = AircraftCarrier(player_1)
        barco_7 = Battleship(player_1)
        barco_8 = Battleship(player_1)
        barco_9 = Cruiser(player_1)
        barco_10 = Submarine(player_1)

        barco_6.create_ship()
        barco_7.create_ship()
        barco_8.create_ship()
        barco_9.create_ship()
        barco_10.create_ship()
        self.colocar_barcos(player_1, board_1, [barco_1, barco_2, barco_3, barco_4, barco_5])
        self.colocar_barcos(player_2, board_2, [barco_6, barco_7, barco_8, barco_9, barco_10])


        
    def colocar_barcos(self, player, board, barcos):
        print(f"{player.name}, Elige las posiciones de tus barcos en el tablero")
        board.printBoard()
        for barco in barcos:
            x = int(input(f"Elige las coordenadas X para: {barco.name}"))
            y = int(input(f"Elige las coordenadas Y para: {barco.name}"))
            position = input(f"Elige la orientación del barco para: {barco.name}. \"H\": Horizontal / \"V\": Vertical \n")
            barco.set_ship_in_board(board, x, y, position)
            board.printBoard()

            # Uso de la función
    def add_player(self, player):
        self.players.append({"name":player.name, "ships":player.ships})
    
    def print_players(self):
        print(self.players)
                
    def win_condition(self):
        for i in self.players:
            if len(i["ships"]) == 0:
                return True
            
    def turn(self):
        turn_player = 1
        while turn_player:
            if turn_player % 2 == 0:
                p = 1
            else:
                p = 2
            print(f"Turno de jugador {p}")
            turn_player += 1
    
    # def positioning_Ships(self, player):
        # Ship.set_ship_in_board(board, start_col, start_row, position)
game1 = Game()
game1.inicialize_game()
