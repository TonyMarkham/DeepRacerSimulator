from point import Point


class Racecar(object):

    def __init__(self):
        self.chassis = [
            Point( 0.040, -0.025),
            Point( 0.040,  0.125),
            Point( 0.025,  0.138),
            Point( 0.025,  0.188),
            Point(-0.025,  0.188),
            Point(-0.025,  0.138),
            Point(-0.040,  0.125),
            Point(-0.040, -0.025),
            Point( 0.040, -0.025)
        ]
        self.right_wheel = [
            Point( 0.000,  0.000),
            Point( 0.000, -0.025),
            Point( 0.025, -0.025),
            Point( 0.025,  0.025),
            Point( 0.000,  0.025),
            Point( 0.000,  0.000)
        ]
        self.left_wheel = [
            Point( 0.000,  0.000),
            Point( 0.000, -0.025),
            Point(-0.025, -0.025),
            Point(-0.025,  0.025),
            Point( 0.000,  0.025),
            Point( 0.000,  0.000)
        ]
        self.right_front_wheel_pivot = Point( 0.025, 0.163)
        self.right_rear_wheel_pivot  = Point( 0.025, 0.000)
        self.left_front_wheel_pivot  = Point(-0.025, 0.163)
        self.left_rear_wheel_pivot   = Point(-0.025, 0.000)
