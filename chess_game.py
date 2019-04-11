from chess_logic import Board
import parse_speech
import time

board = Board()

#command = parse_speech.get_command()
#board.cnc.move_to(-45, 0)


#board.cnc.move_to(-100,100)
try:
    while True:
        command = parse_speech.get_command()
        # if command:
        #     board.cnc.move_to(-1*command[0], command[1])
        #     time.sleep(5)
        #     board.cnc.move_to(-1*command[2], command[3])
        #     time.sleep(10)

