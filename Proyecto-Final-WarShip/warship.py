class Board:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.board = []

    def createBoard(self):
        for y in range(self.row):
            rows = []
            for x in range(self.col):
                rows.append("A")
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



board1 = Board(10,10)
board1.createBoard()
board1.printBoard()