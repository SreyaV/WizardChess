from chess_logic import Game
import parse_speech
import time
import sys

def main():
    game = Game()
    while True:
        command = parse_speech.get_command()
        if command is not None:
            try:
                game.move_piece(command)
            except: 
                print(sys.exc_info())

def main_text():
    game = Game()
    while True:
        command = input("Enter move:")
        try:
            game.move_piece(command)
        except: 
            print(sys.exc_info())
if __name__ == '__main__':
    main()
    # main_text()