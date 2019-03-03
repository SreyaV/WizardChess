from chess_logic import Board
import parse_speech
import time

board = Board()

#board.cnc.move_to(-100,100)
try:
    while True:
        command = parse_speech.get_command()
        if command:
            coordinates = board.findcoordinates(command)
            board.cnc.move_to(-1*coordinates[2], coordinates[3])
            time.sleep(5)
except:
    board.cnc.move_to(0,0)
