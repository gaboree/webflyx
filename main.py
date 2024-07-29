class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        is_x = False
        is_y = False
        if x_1 <= self.pos_x <= x_2:
            is_x = True
        if y_1 <= self.pos_y <= y_2:
            is_y = True
        return is_x and is_y

class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        #define AoE of dragon breath
        d_x1 = x - self.__fire_range
        d_y1 = y - self.__fire_range
        d_x2 = x + self.__fire_range
        d_y2 = y + self.__fire_range
        # Check if any unit is in within that AoE
        damaged_units = []       
        for unit in units:
            if (d_x1 <= unit.pos_x <= d_x2) and (d_y1 <= unit.pos_y <= d_y2):
                damaged_units.append(unit)
        return damaged_units

