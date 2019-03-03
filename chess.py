from chess_logic import Board
from parse_speech import get_command

board = Board()

while True:
    command = get_command()
    if command:
        coordinates = board.findcoordinates(command)
        board.move_piece(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
