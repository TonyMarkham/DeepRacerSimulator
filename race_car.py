from point import Point
import math


class Racecar(object):

    def __init__(self):
        self.chassis = []
        self.right_front_wheel = []
        self.left_front_wheel = []
        self.right_rear_wheel = []
        self.left_rear_wheel = []
        self.x_position = 0.0
        self.y_position = 0.0
        self.heading = 0.0
        self.steering_angle = 0.0
        self.base_chassis = [
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
        self.base_right_wheel = [
            Point( 0.000,  0.000),
            Point( 0.000, -0.025),
            Point( 0.025, -0.025),
            Point( 0.025,  0.025),
            Point( 0.000,  0.025),
            Point( 0.000,  0.000)
        ]
        self.base_left_wheel = [
            Point( 0.000,  0.000),
            Point( 0.000, -0.025),
            Point(-0.025, -0.025),
            Point(-0.025,  0.025),
            Point( 0.000,  0.025),
            Point( 0.000,  0.000)
        ]
        self.base_right_front_wheel_pivot = Point( 0.050, 0.163)
        self.base_right_rear_wheel_pivot  = Point( 0.050, 0.000)
        self.base_left_front_wheel_pivot  = Point(-0.050, 0.163)
        self.base_left_rear_wheel_pivot   = Point(-0.050, 0.000)

    def update_car(self, x_in, y_in, heading_in, steering_angle_in):
        self.rotate(heading_in)
        for i, point in enumerate(self.chassis):
            self.chassis[i].x = point.x + x_in
            self.chassis[i].y = point.y + y_in
        for i, point in enumerate(self.right_front_wheel):
            self.right_front_wheel[i].x = point.x + x_in
            self.right_front_wheel[i].y = point.y + y_in
        for i, point in enumerate(self.right_rear_wheel):
            self.right_rear_wheel[i].x = point.x + x_in
            self.right_rear_wheel[i].y = point.y + y_in
        for i, point in enumerate(self.left_front_wheel):
            self.left_front_wheel[i].x = point.x + x_in
            self.left_front_wheel[i].y = point.y + y_in
        for i, point in enumerate(self.left_rear_wheel):
            self.left_rear_wheel[i].x = point.x + x_in
            self.left_rear_wheel[i].y = point.y + y_in
        self.steer(steering_angle_in)

    def rotate(self, heading_in):
        heading_radians = heading_in * math.pi / 180
        self.chassis = []
        for point in self.base_chassis:
            self.chassis.append(
                Point(
                    point.x * math.cos(heading_radians) - point.y * math.sin(heading_radians),
                    point.x * math.sin(heading_radians) + point.y * math.cos(heading_radians)

                )
            )
        self.locate_wheels()
        for i, point in enumerate(self.right_front_wheel):
            x = point.x * math.cos(heading_radians) - point.y * math.sin(heading_radians)
            y = point.x * math.sin(heading_radians) + point.y * math.cos(heading_radians)
            self.right_front_wheel[i].x = x
            self.right_front_wheel[i].y = y
        for i, point in enumerate(self.right_rear_wheel):
            x = point.x * math.cos(heading_radians) - point.y * math.sin(heading_radians)
            y = point.x * math.sin(heading_radians) + point.y * math.cos(heading_radians)
            self.right_rear_wheel[i].x = x
            self.right_rear_wheel[i].y = y
        for i, point in enumerate(self.left_front_wheel):
            x = point.x * math.cos(heading_radians) - point.y * math.sin(heading_radians)
            y = point.x * math.sin(heading_radians) + point.y * math.cos(heading_radians)
            self.left_front_wheel[i].x = x
            self.left_front_wheel[i].y = y
        for i, point in enumerate(self.left_rear_wheel):
            x = point.x * math.cos(heading_radians) - point.y * math.sin(heading_radians)
            y = point.x * math.sin(heading_radians) + point.y * math.cos(heading_radians)
            self.left_rear_wheel[i].x = x
            self.left_rear_wheel[i].y = y

    def locate_wheels(self):
        self.right_front_wheel = []
        self.right_rear_wheel = []
        for point in self.base_right_wheel:
            self.right_front_wheel.append(
                Point(
                    point.x + self.base_right_front_wheel_pivot.x,
                    point.y + self.base_right_front_wheel_pivot.y
                )
            )
            self.right_rear_wheel.append(
                Point(
                    point.x + self.base_right_rear_wheel_pivot.x,
                    point.y + self.base_right_rear_wheel_pivot.y
                )
            )
        self.left_front_wheel = []
        self.left_rear_wheel = []
        for point in self.base_left_wheel:
            self.left_front_wheel.append(
                Point(
                    point.x + self.base_left_front_wheel_pivot.x,
                    point.y + self.base_left_front_wheel_pivot.y
                )
            )
            self.left_rear_wheel.append(
                Point(
                    point.x + self.base_left_rear_wheel_pivot.x,
                    point.y + self.base_left_rear_wheel_pivot.y
                )
            )

    def steer(self, steering_angle_in):
        steering_radians = steering_angle_in * math.pi / 180

        dx = self.right_front_wheel[0].x
        dy = self.right_front_wheel[0].y
        for i, point in enumerate(self.right_rear_wheel):
            x1 = self.right_front_wheel[i].x - dx
            y1 = self.right_front_wheel[i].y - dy
            x2 = x1 * math.cos(steering_radians) - y1 * math.sin(steering_radians)
            y2 = x1 * math.sin(steering_radians) + y1 * math.cos(steering_radians)
            x3 = x2 + dx
            y3 = y2 + dy
            self.right_front_wheel[i].x = x3
            self.right_front_wheel[i].y = y3

        dx = self.left_front_wheel[0].x
        dy = self.left_front_wheel[0].y
        for i, point in enumerate(self.right_rear_wheel):
            x1 = self.left_front_wheel[i].x - dx
            y1 = self.left_front_wheel[i].y - dy
            x2 = x1 * math.cos(steering_radians) - y1 * math.sin(steering_radians)
            y2 = x1 * math.sin(steering_radians) + y1 * math.cos(steering_radians)
            x3 = x2 + dx
            y3 = y2 + dy
            self.left_front_wheel[i].x = x3
            self.left_front_wheel[i].y = y3
