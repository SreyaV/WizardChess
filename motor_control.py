import serial
import time
import math


class MotorController:
    def __init__(self):

        self.feedrate_z = 500
        self.feedrate_xy_fast = 500
        self.feedrate_xy_slow = 200

        self.z_engaged = -1.1
        self.z_disengaged = 1.0
        self.z_launch = 2.2

        # Open grbl serial port
        self.serial_instance = serial.Serial('/dev/tty.usbserial-DN05JLOK', 115200)

        # Wake up grbl
        self.serial_instance.write(("\r\n\r\n").encode())
        time.sleep(2)  # Wait for grbl to initialize
        self.serial_instance.flushInput()  # Flush startup text in serial input

        self.serial_instance.write(("G90" + '\n').encode())  # Send g-code block to grbl
        grbl_out = self.serial_instance.readline()  # Wait for grbl response with carriage return
        print(' : ' + grbl_out.decode().strip())
        
        self.home()

    def home(self):
        command_buffer = "$H"
        print('Sending: ' + command_buffer)
        self.serial_instance.write((command_buffer + '\n').encode())  # Send g-code block to grbl
        grbl_out = self.serial_instance.readline()  # Wait for grbl response with carriage return
        print(' : ' + grbl_out.decode().strip())

        self.lastX = 0
        self.lastY = 0
        self.lastZ = 0

    def move_to(self, x, y, fast):
        """
        Move magnet to x, y location at feedrate
        :param x: loc to move
        :param y: loc to move
        :param feedrate: feedrate of move in mm/min
        :return:
        """

        # Stream g-code to grbl
        feedrate = self.feedrate_xy_fast if fast else self.feedrate_xy_slow
        command_buffer = "G01 X{} Y{} F{}".format(x, y, feedrate)
        print('Sending: ' + command_buffer)
        self.serial_instance.write((command_buffer + '\n').encode())  # Send g-code block to grbl
        grbl_out = self.serial_instance.readline()  # Wait for grbl response with carriage return
        print(' : ' + grbl_out.decode().strip())

        time_to_wait = max(abs(x - self.lastX), abs(y - self.lastY)) / feedrate * 60.0 + 0.25
        time.sleep(time_to_wait)

        self.lastX = x
        self.lastY = y

    def __del__(self):

        # Close file and serial port
        self.set_z(0)
        self.serial_instance.close()

    def set_z(self, z):

        command_buffer = "G01 Z{} F{}".format(z, self.feedrate_z)
        print('Sending: ' + command_buffer)
        self.serial_instance.write((command_buffer + '\n').encode())  # Send g-code block to grbl
        grbl_out = self.serial_instance.readline()  # Wait for grbl response with carriage return
        print(' : ' + grbl_out.decode().strip())

        time_to_wait = abs(z - self.lastZ) / self.feedrate_z * 60.0 + 0.25
        time.sleep(time_to_wait)

        self.lastZ = z

    def set_solenoid(self, retracted):

        command_buffer = "M8" if retracted else "M9"
        print('Sending: ' + command_buffer)
        self.serial_instance.write((command_buffer + '\n').encode())  # Send g-code block to grbl
        grbl_out = self.serial_instance.readline()  # Wait for grbl response with carriage return
        print(' : ' + grbl_out.decode().strip())
        time.sleep(0.25)
        return

    def engage_magnet(self, engaged):
        z = self.z_engaged if engaged else self.z_disengaged
        self.set_z(z)

    def kill_piece(self):
        self.set_z(self.z_disengaged)
        self.set_solenoid(True)
        self.set_z(self.z_launch)
        self.set_solenoid(False)

    def test(self):
        self.move_to(5, 10, True)
        self.engage_magnet(False)
        self.move_to(20, 10, False)
        self.engage_magnet(True)
        time.sleep(1)
        self.kill_piece()

    def dist(self,x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


if __name__ == '__main__':
    mc = MotorController()
    mc.test()
