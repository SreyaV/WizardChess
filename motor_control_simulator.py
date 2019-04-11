import serial
import time
import math


class MotorController:
    def __init__(self):
        print("__init__")

    def move_to(self, x, y, fast):
        print("move_to: ", x, ", ", y, ", ", fast)

    def __del__(self):
        print("__del__")

    
    def engage_magnet(self, engaged):
        print("engage_magnet: ", engaged)

    def kill_piece(self):
        print("kill_piece")
