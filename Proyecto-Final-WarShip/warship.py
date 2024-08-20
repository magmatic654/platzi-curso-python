class Board:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.water = '.'
        self.board = []
        self.ships = []

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
    def __init__(self):
        self.cells = []
        self.name = ""
        self.coordinates_x = []
        self.coordinates_y = []
        self.ship = {
            "Name": self.name,
            "Coordinates_x": self.coordinates_x,
            "Coordinates_y": self.coordinates_y,
        }
    def create_ship(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
    
    def set_ship_in_board(self, board, start_row, start_col, position):
        ok = False
        if position == "H":
            row = board.board[start_row - 1]
            for i in range(len(self.cells)):
                if row[start_col - 1 + i] != board.water:
                    return print("Hubo un error")
            for i in range(len(self.cells)):
                row[start_col - 1 + i] = self.cells[i]
                self.coordinates_x.append(i)
                self.coordinates_y.append(start_row)
            print(self.ship)
        elif position == "V":
            for i in range(len(self.cells)):
                if board.board[start_row - 1 + i][start_col - 1] != board.water:
                    return print("Hubo un error")
            for i in range(len(self.cells)):
                board.board[start_row - 1 + i][start_col - 1] = 'B'
        ok = True
        return ok
    
class AircraftCarrier(Ship):
    def create_ship(self):
        self.name = "AircraftCarrier"
        self.cells = ["A"] *5
        self.ship = {
            "Name": self.name,
            "Coordinates_x": self.coordinates_x,
            "Coordinates_y": self.coordinates_y,
        }
class Battleship(Ship):
    def create_ship(self):
        self.name = "Battleship"
        self.cells = ["B"] * 4
        self.ship = {
            "Name": self.name,
            "Coordinates_x": self.coordinates_x,
            "Coordinates_y": self.coordinates_y,
        }
        
class Cruiser(Ship):
    def create_ship(self):
        self.name = "Cruiser"
        self.cells = ["C"] * 3
        self.ship = {
            "Name": self.name,
            "Coordinates_x": self.coordinates_x,
            "Coordinates_y": self.coordinates_y,
        }
class Submarine (Ship):
    def create_ship(self):
        self.name = "Submarine"
        self.cells = ["S"] * 3
        self.ship = {
            "Name": self.name,
            "Coordinates_x": self.coordinates_x,
            "Coordinates_y": self.coordinates_y,
        }
class Destroyer (Ship):
    def create_ship(self):
        self.name = "Destroyer"
        self.cells = ["D"] * 2
        self.ship = {
            "Name": self.name,
            "Coordinates_x": self.coordinates_x,
            "Coordinates_y": self.coordinates_y,
        }

class Player():
    def __init__(self, name):
        self.name = name

    def atack(self, board, row, col):
        coordinate_atack = (board.board[row - 1][col -1])
        if coordinate_atack != board.water:
            board1.modifyBoard(row,col, "*")
            print("¡Has dado en un blanco!")
        else:
            board1.modifyBoard(row,col, "a")
            print("¡Agua!")
        board.printBoard()


board1 = Board(10,10)
board1.createBoard()

aircraftCarrier1 = AircraftCarrier()
battleship1 = Battleship()
cruiser1 = Cruiser()
submarine1 = Submarine()
destroyer1 = Destroyer()

aircraftCarrier1.create_ship()
battleship1.create_ship()
cruiser1.create_ship()
submarine1.create_ship()
destroyer1.create_ship()

aircraftCarrier1.set_ship_in_board(board1,1,1,"H")
battleship1.set_ship_in_board(board1,2,1,"H")
cruiser1.set_ship_in_board(board1,3,1,"H")
submarine1.set_ship_in_board(board1,4,1,"H")
destroyer1.set_ship_in_board(board1,5,1,"H")

player1 = Player("Harold")
player1.atack(board1,2, 2)
