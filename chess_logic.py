from motor_control import MotorController

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
            self.move_to(to_rank, to_file, True)
            self.cnc.kill_piece()

        x, y = get_xy_for(to_rank, to_file, True)

        self.cnc.move_to(x, y, )


        self.cnc.move_to(startX, startY, FAST_FEED_RATE)
        self.cnc.engage_magnet(True)
        if startX == endX or startY == endY or abs(startY - endY) == abs(startX - endX):
            # if moving horizontally, vertically, or diagonally
            self.cnc.move_to(endX, endY, SLOW_FEED_RATE)
        elif abs(startX - endX) == 1 and abs(startY - endY) == 2:
            self.cnc.move_to(0.5 * (startX + endX), startY, SLOW_FEED_RATE)
            self.cnc.move_to(0.5 * (startX + endX), endY, SLOW_FEED_RATE)
            self.cnc.move_to(endX, endY, SLOW_FEED_RATE)
        elif abs(startX - endX) == 1 and abs(startY - endY) == 2:
            self.cnc.move_to(startX, (startY + endY) * 0.5, SLOW_FEED_RATE)
            self.cnc.move_to(endX, (startY + endY) * 0.5, SLOW_FEED_RATE)
            self.cnc.move_to(endX, endY, SLOW_FEED_RATE)
        else:
            self.cnc.engage_magnet(False)
            return False
        self.cnc.engage_magnet(False)

        self.grid[endX][endY] = self.grid[startX][startY]
        self.grid[startX][startY] = None

        return True

    def is_move_legal(startX, startY, endX, endY):
        # TODO make work properly
        if startX == endX or startY == endY or abs(startY - endY) == abs(startX - endX):
            return True
        elif abs(startX - endX) == 1 and abs(startY - endY) == 2:
            return True
        elif abs(startX - endX) == 1 and abs(startY - endY) == 2:
            return True
        else:
            return False

    # def findcoordinates(self, command):
    #     coordinates = []
    #     for coord in command:
    #         coordinates.append(self.length/2 + (int(coord)-1)*self.length)
    #     return coordinates
