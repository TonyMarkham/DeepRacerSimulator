import math
from line import Line
from point import Point


class Track(object):

    def __init__(self):
        self.center_points = []
        self.center_lines = []
        self.outside_points = []
        self.outside_lines = []
        self.inside_points = []
        self.inside_lines = []
        self.minimum_x = math.inf *  1
        self.maximum_x = math.inf * -1
        self.minimum_y = math.inf *  1
        self.maximum_y = math.inf * -1
        self.width = math.inf
        self.height = math.inf

    def setup(self, track_width):
        self.offset(track_width)
        self.set_limits()
        self.setup_center_lines()
        self.setup_inside_lines()
        self.setup_outside_lines()

    def set_limits(self):
        self.minimum_x = math.inf * 1
        self.maximum_x = math.inf * -1
        self.minimum_y = math.inf * 1
        self.maximum_y = math.inf * -1
        self.width = math.inf
        self.height = math.inf
        for point in self.outside_points:
            self.set_minimum_x(point.x)
            self.set_maximum_x(point.x)
            self.set_minimum_y(point.y)
            self.set_maximum_y(point.y)
        for point in self.inside_points:
            self.set_minimum_x(point.x)
            self.set_maximum_x(point.x)
            self.set_minimum_y(point.y)
            self.set_maximum_y(point.y)

        self.width = self.maximum_x - self.minimum_x
        self.height = self.maximum_y - self.minimum_y

    def set_minimum_x(self, x_in):
        if x_in < self.minimum_x:
            self.minimum_x = x_in

    def set_maximum_x(self, x_in):
        if x_in > self.maximum_x:
            self.maximum_x = x_in

    def set_minimum_y(self, y_in):
        if y_in < self.minimum_y:
            self.minimum_y = y_in

    def set_maximum_y(self, y_in):
        if y_in > self.maximum_y:
            self.maximum_y = y_in

    def setup_center_lines(self):
        previous_point = Point(0, 0)
        for i, point in enumerate(self.center_points):
            if i > 0:
                p1 = previous_point
                p2 = point
                line = Line(p1, p2)
                self.center_lines.append(line)
            previous_point = point

    def setup_inside_lines(self):
        previous_point = Point(0, 0)
        for i, point in enumerate(self.inside_points):
            if i > 0:
                p1 = previous_point
                p2 = point
                line = Line(p1, p2)
                self.inside_lines.append(line)
            previous_point = point

    def setup_outside_lines(self):
        previous_point = Point(0, 0)
        for i, point in enumerate(self.outside_points):
            if i > 0:
                p1 = previous_point
                p2 = point
                line = Line(p1, p2)
                self.outside_lines.append(line)
            previous_point = point

    def offset(self, track_width):
        self.inside_lines = []
        self.outside_lines = []

        before_zero = len(self.center_points) - 1

        if self.center_points[before_zero] == self.center_points[0]:
            before_zero -= 1

        for i, pt in enumerate(self.center_points):
            if i == 0:
                p1 = self.center_points[before_zero]
                p2 = self.center_points[i + 1]
            elif i == len(self.center_points) - 1:
                p1 = self.center_points[i - 1]
                p2 = self.center_points[1]
            else:
                p1 = self.center_points[i - 1]
                p2 = self.center_points[i + 1]
            offset_line = Line(p1, p2)
            inside_x = pt.x + offset_line.PerpendicularUnitVector.x * track_width * -0.5
            inside_y = pt.y + offset_line.PerpendicularUnitVector.y * track_width * -0.5
            inside_point = Point(inside_x, inside_y)
            self.inside_points.append(inside_point)
            outside_x = pt.x + offset_line.PerpendicularUnitVector.x * track_width * 0.5
            outside_y = pt.y + offset_line.PerpendicularUnitVector.y * track_width * 0.5
            outside_point = Point(outside_x, outside_y)
            self.outside_points.append(outside_point)
