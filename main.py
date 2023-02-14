from joystick import JoystickReader


class Main:
    """ main class that will handle the loop """

    def __init__(self):
        """
        init function
        """
        self._joystick = JoystickReader(vr_x=26, vr_y=27, vr_z=28)

    def run(self) -> None:
        """
        core function to do whatever you want with the Joystick values
        For each iteration the joystick value will be read and display in the terminal
        """
        self._joystick.calibrate()
        while True:
            x, y, z = self._joystick.read()
            print(f"x: {x} -- y: {y} -- z: {z}")


if __name__ == '__main__':
    run = Main()
    run.run()
