from chess_logic import Board
import parse_speech
import time

board = Board()

#board.cnc.move_to(-100,100
try:
    while True:
        command = parse_speech.get_command()
        if command:
            board.move_piece(command[0], command[1], command[2], command[3])
            time.sleep(10)
except:
    board.cnc.move_to(0,0)
