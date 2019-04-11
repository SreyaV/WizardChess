# from motor_control import MotorController
from motor_control_simulator import MotorController

# Rank = row = y
# File = column = x
class Game:
    def __init__(self):
        self.board = chess.Board()
        self.cnc = MotorController()

        self.xa = 0
        self.xh = 70
        self.y1 = 0
        self.y8 = 70

        self.dx_kill = 0
        self.dy_kill = 0

    def move_to(rank, file, fast, kill=False):
        x = file / 7.0 * (self.xh - self.xa) + self.xa
        y = rank / 7.0 * (self.y8 - self.y1) + self.y1
        if kill:
            x = x + self.dx_kill
            y = y + self.dy_kill
        self.cnc.move_to(x, y, fast)

    def move_piece(self, uci):

        move = chess.Move.from_uci(uci)

        if move not in self.board.legal_moves:
            print "Move not legal"
            return False
        else if self.board.is_en_passant(move):
            print "En Passant not supported"
            return False
        else if self.board.is_castling(move):
            print "Castling not supported"
            return False

        from_file = square_file(move.from_square)
        from_rank = square_rank(move.from_square)
        to_file = square_file(move.to_square)
        to_rank = square_rank(move.to_square)

        if self.board.is_capture(move):
            self.move_to(to_rank, to_file, True, True)
            self.cnc.kill_piece()

        self.move_to(from_rank, from_file, True)
        self.cnc.engage_magnet(True)

        if from_rank == to_rank or from_file == to_file or abs(to_file - from_file) == abs(to_rank - from_rank):
            # if moving horizontally, vertically, or diagonally, go straight there
            self.move_to(to_rank, to_file, False)
        elif abs(to_rank - from_rank) == 1 and abs(to_file - from_file) == 2:
            #knight move 1 rank 2 files
            self.move_to(0.5 * (from_rank + to_rank), from_file, False)
            self.move_to(0.5 * (from_rank + to_rank), to_file, False)
            self.move_to(to_rank, to_file, False)
        elif abs(to_file - from_file) == 1 and abs(to_rank - from_rank) == 2:
            #knight move 1 file 2 ranks
            self.move_to(from_rank, (from_file + to_file) * 0.5, False)
            self.move_to(to_rank, (from_file + to_file) * 0.5, False)
            self.move_to(to_rank, to_file, False)
        else:
            print "unexpected error, impossible move" 
            raise 
        self.cnc.engage_magnet(False)

        self.board.push(move)

        return True

    def test(self):
        test_moves = ['d2d4', 'c7c6', 'g1f3', 'e7e6', 'c1f4', 'c6c5', 'e2e3', 'd7d5', 'd1d3', 'c5d4', 'e3d4']
        for move in test_moves:
            self.move_piece(move)
            # sleep(2)

if __name__ == '__main__':
    game = Game()
    game.test()

