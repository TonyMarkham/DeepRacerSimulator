import math
from point import Point


class Line(object):
    
    def __init__(self, p1_in, p2_in):
        self.P1 = p1_in
        self.P2 = p2_in
        self.Length = 0.0
        self.line_length()
        self.UnitVector = Point(0, 0)
        self.unit_vector()
        self.PerpendicularUnitVector = Point(0, 0)
        self.perpendicular_unit_vector()

    def line_length(self):
        dx = self.P1.x - self.P2.x
        dy = self.P1.y - self.P2.y
        self.Length = math.sqrt(dx * dx + dy * dy)
    
    def unit_vector(self):
        x = (self.P2.x - self.P1.x) / self.Length
        y = (self.P2.y - self.P1.y) / self.Length
        self.UnitVector = Point(x, y)

    def perpendicular_unit_vector(self):
        x = self.UnitVector.x * math.cos(math.pi / 2) - self.UnitVector.y * math.sin(math.pi / 2)
        y = self.UnitVector.x * math.sin(math.pi / 2) + self.UnitVector.y * math.cos(math.pi / 2)
        self.PerpendicularUnitVector = Point(x, y)
