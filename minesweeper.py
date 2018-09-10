# minesweeper.py
# Learning AI Compatible minesweeper program
# Copyright Alex Weavers
# Free to use, copy, distribute
from random import randint

def user_input():
    return (1,1)


# Game board class. For easy resets, starting values are saved in a class.
class GameBoard:
    def __init__(self, length, width, mines):
        self.length, self.width, self.mines = length, width, mines
        self.create_matrix()

    # Make the initial mine matrix
    def create_matrix(self):
        self.list_of_mines = []
        self.matrix = []
        self.mask = []  # true if a square is revealed, false if not revealed

        # generate board...
        # TODO: Not use lists
        for l in range(0, self.length):
            self.matrix.append([])
            self.mask.append([])

            for w in range(0, self.width):
                self.matrix[l].append(0)
                self.mask[l].append(False)
        # lay mines
        for mine in range(1, self.mines):
            a, b = randint(0, self.length - 1), randint(0,self.width - 1)
            self.list_of_mines.append((a, b))
            self.matrix[a][b] = 9  # we'll use 9 for a mine. No square can be a 9

        self.matrix = self.evaluate_squares(self.matrix)


    # Scan local squares in a matrix and return the number to display
    def evaluate_square(self, l, w, matrix):
        delta = [(-1, -1), (0, -1), (1, -1), (-1, 0),
                 (1, 0), (-1, 1), (0, 1), (1, 1)]
        result = 0

        for d in delta:
            a = l + d[0]
            b = w + d[1]

            if not (a < 0 or b < 0):
                # TODO: Fix lazy try/catch.
                try:
                    if matrix[a][b] == 9:
                        result += 1
                except IndexError:
                    # List index out of range is fine.
                    pass

        return result

    def evaluate_squares(self, matrix):
        for l in range(0, self.length):
            for w in range(0, self.width):
                if matrix[l][w] != 9:  # if not mine
                    matrix[l][w] = self.evaluate_square(l, w, matrix)

        return matrix

    def get_square(self, a, b):
        return self.matrix[a][b]

    # prints the entire matrix
    def map_to_string(self):
        result = ""
        for l in self.matrix:
            for w in l:
                result = result + str(w)
            result = result + "\n"

        return result
 
    def mask_to_string(self):
        result = ""
        for a in range(0, self.length):
            for b in range(0, self.width):
                if self.mask[a][b]:
                    result = result + str(self.matrix[a][b])
                else:
                    result = result + "#"
            result = result + "\n"

        return result


    # reveals a square on the map and continues revealing if square is 0
    # returns False if it's a bomb
    def unmask(self, a, b):
        # return if out of range
        print(a,b)
        if a >= self.length or b >= self.width:
            return True

        if a < 0 or b < 0:
            return True

        # do nothing if location already unmasked_list
        if self.mask[a][b] == True:
            return True

        self.mask[a][b] = True  # unmask this square first

        delta = [(-1, -1), (0, -1), (1, -1), (-1, 0),
                (1, 0), (-1, 1), (0, 1), (1, 1)]

        if self.matrix[a][b] == 9:
            return False # player dies

        if self.matrix[a][b] == 0:
            for d in delta:
                self.unmask(a + d[0], b + d[1])

        return True


    def __repr__(self):
        return "Minefield object. To show grid use the map_to_string method."

if __name__ == '__main__':
    field = GameBoard(randint(3,15),randint(3,15), randint(0,9))
    print(field.map_to_string())
