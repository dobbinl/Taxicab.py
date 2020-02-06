class Taxicab:
    """Represents the odometer distance driven by the Taxicab"""
    def __init__(self, x_coord, y_coord, odom):
        """initializes the coordinates and odometer"""

        self.x_coord = x_coord
        self.y_coord = y_coord
        self.odom = odom

    """returns coordinate values"""
    def get_move_x(self):
        return self.x_coord

    def get_move_y(self):
        return self.y_coord

    def get_odometer(self):
        return abs(self.x_coord) + abs(self.y_coord)

    def move_x(self, xmove):
        return self.x_coord + xmove

    def move_y(self,ymove):
        return self.y_coord + ymove

cab = Taxicab(5,-8, 0)
cab.move_x(3)
cab.move_y(-4)
cab.move_x(-1)

#print(cab.get_move_x())
#print(cab.get_move_y())
#print(cab.get_odometer())