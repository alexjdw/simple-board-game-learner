

class GameBoard:

    def __init__(self):
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.turn = "X"

    # x is horizontal, y is vertical
    def add_token(self, token, xcoord, ycoord):
        if self.board[ycoord][xcoord] == '-':
            self.board[ycoord][xcoord] = token
        else:
            raise ValueError("This square is occupied.")

    def print_board(self):
        s = ""
        for row in self.board:
            for i in range(0,3):
                s = s + row[i]
                if i < 2:
                    s = s + "|"
            s = s + '\n'

        print(s)

    def is_full(self):
        for row in self.board:
            for col in row:
                print(col)
                if col == '-':
                    return False

        return True

    def ai_move(self):
        if self.is_full(:
            raise FullBoardError("AI: No legal moves.")
        for x in range(0, 3):
            for y in range(0, 3):
                if self.board[y][x] == '-':
                    self.add_token('O', x, y)
                    return
 
if __name__ == '__main__':
    board = GameBoard()
    board.print_board()

    while True:
        if board.is_full():
            break

        x = int(input('x '))
        y = int(input('y '))
        try:
            board.add_token('X', x-1, y-1)
            board.ai_move()
        except (ValueError, IndexError):
            print("Invalid move.")

        board.print_board()
