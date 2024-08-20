class Board:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.board = []

    def createBoard(self):
        counter = 1
        for y in range(self.row):
            rows = []
            for x in range(self.col):
                rows.append("a")
                counter += 1
                if x == self.col-1:
                    self.board.append(rows)

    def printBoard(self):
        for y in self.board:
            counter = 1
            for x in y:
                if counter == self.col:
                    print(x, " ")
                else:
                    print(x," ", end="")
                counter += 1

class Ship():
    def __init__(self):
        self.cells = []
    
    def create_ship(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
    
    def set_ship_in_board(self, board, start_row, start_col, position):
        if position == "H":
            row = board.board[start_row - 1]
            for i in range(len(self.cells)):
                if row[start_col - 1 + i] != 'a':
                    return print("Hubo un error")
            for i in range(len(self.cells)):
                row[start_col - 1 + i] = 'B'
        elif position == "V":
            for i in range(len(self.cells)):
                if board.board[start_row - 1 + i][start_col - 1] != 'a':
                    return print("Hubo un error")
            for i in range(len(self.cells)):
                board.board[start_row - 1 + i][start_col - 1] = 'B'

class AircraftCarrier(Ship):
    def create_ship(self):
        self.cells = ["A"] * 5
class Battleship(Ship):
    def create_ship(self):
        self.cells = ["B"] * 4
class Cruiser(Ship):
    def create_ship(self):
        self.cells = ["C"] * 3
class Submarine (Ship):
    def create_ship(self):
        self.cells = ["S"] * 3
class Destroyer (Ship):
    def create_ship(self):
        self.cells = ["D"] * 2



board1 = Board(10,10)
board1.createBoard()

aircraftCarrier1 = AircraftCarrier()
aircraftCarrier2 = Battleship()
aircraftCarrier3 = Cruiser()
aircraftCarrier4 = Submarine()
aircraftCarrier5 = Destroyer()
aircraftCarrier1.create_ship()
aircraftCarrier2.create_ship()
aircraftCarrier3.create_ship()
aircraftCarrier4.create_ship()
aircraftCarrier5.create_ship()

aircraftCarrier1.set_ship_in_board(board1,1,1,"H")
aircraftCarrier2.set_ship_in_board(board1,1,1,"H")
aircraftCarrier3.set_ship_in_board(board1,3,1,"H")
aircraftCarrier4.set_ship_in_board(board1,4,1,"H")
aircraftCarrier5.set_ship_in_board(board1,5,1,"H")

board1.printBoard()