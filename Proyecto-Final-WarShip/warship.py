class Board:
    def __init__(self, row, col):
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

class Ship():
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

class Player():
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
    
    def add_player(self, player):
        self.players.append({player.name: player.ships})
    
    def print_players(self):
        print(self.players)

    def win_condition(self.players):
        return

game1 = Game()

board1 = Board(10,10)
board1.createBoard()

player1 = Player("Harold")

aircraftCarrier1 = AircraftCarrier(player1)
battleship1 = Battleship(player1)
cruiser1 = Cruiser(player1)
submarine1 = Submarine(player1)
destroyer1 = Destroyer(player1)

aircraftCarrier1.create_ship()
battleship1.create_ship()
cruiser1.create_ship()
submarine1.create_ship()
destroyer1.create_ship()


aircraftCarrier1.set_ship_in_board(board1,10,1,"V")
battleship1.set_ship_in_board(board1,1,2,"H")
cruiser1.set_ship_in_board(board1,1,3,"H")
submarine1.set_ship_in_board(board1,1,4,"H")
destroyer1.set_ship_in_board(board1,1,5,"H")

game1.add_player(player1)
player1.printShips()
player1.atack(board1, 1,10)
player1.atack(board1, 2,10)
player1.atack(board1, 3,10)
player1.atack(board1, 4,10)
player1.atack(board1, 5,10)
player1.atack(board1, 2,1)
player1.atack(board1, 2,2)
player1.atack(board1, 2,3)
player1.atack(board1, 2,4)
player1.atack(board1, 3,1)
player1.atack(board1, 3,2)
player1.atack(board1, 3,3)
player1.atack(board1, 4,1)
player1.atack(board1, 4,2)
player1.atack(board1, 4,3)
player1.atack(board1, 5,1)
player1.atack(board1, 5,2)

board1.printBoard()