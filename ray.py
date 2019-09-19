from point import Point
from line import Line


class Ray(object):

    def __init__(self):
        self.P1 = Point(0, 0)
        self.P2 = Point(0, 0)

    def define(self, p1_in, unit_vector_in):
        self.P1 = p1_in
        self.P2 = Point(0, 0)
        self.P2.x = self.P1.x + unit_vector_in.x
        self.P2.y = self.P1.y + unit_vector_in.y

    def find_intersection(self, line_in):
        x1 = line_in.P1.x
        y1 = line_in.P1.y
        x2 = line_in.P2.x
        y2 = line_in.P2.y
        x3 = self.P1.x
        y3 = self.P1.y
        x4 = self.P2.x
        y4 = self.P2.y

        denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

        if denominator == 0:
            return False

        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denominator
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denominator

        if 0 < t < 1 and u > 0:
            value = Point(0, 0)
            value.x = x1 + t * (x2 - x1)
            value.y = y1 + t * (y2 - y1)
            return value
        else:
            return False
