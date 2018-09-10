from minesweeper import GameBoard


user = input("name? ")
board_len = int(input("height? "))
board_wid = int(input("width? "))
mines = int(input("mines? "))

board = GameBoard(board_len, board_wid, mines)

print("Please input your clicks, " + user + ".")

 
# main game loop
alive = True
while alive:
    x = int(input("x coordinate? "))
    y = int(input("y coordinate? "))
    alive = board.unmask(x-1, y-1)
    print(board.mask_to_string())
