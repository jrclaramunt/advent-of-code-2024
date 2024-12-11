class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


class Matrix:
    def __init__(self, input_data):
        self.data = []
        for row in input_data:
            self.data.append(list(row.strip()))

        self.n_rows = len(self.data)
        self.n_columns = len(self.data[0])

    def look_up(self, x, y, positions):
        if x - (positions- 1) < 0:
            return []

        result = []
        for i in range(positions):
            value = self.data[x - i][y]
            result.append(value)

        return result

    def look_up_right(self, x, y, positions):
        if x - (positions - 1) < 0 or y + positions > self.n_columns:
            return []

        result = []
        for i in range(positions):
            value = self.data[x - i][y + i]
            result.append(value)

        return result

    def look_right(self, x, y, positions):
        if y + positions > self.n_columns:
            return []

        result = []
        for i in range(positions):
            value = self.data[x][y + i]
            result.append(value)

        return result

    def look_down_right(self, x, y, positions):
        if x + positions > self.n_rows or y + positions > self.n_columns:
            return []

        result = []
        for i in range(positions):
            value = self.data[x + i][y + i]
            result.append(value)

        return result

    def look_down(self, x, y, positions):
        if x + positions > self.n_rows:
            return []

        result = []
        for i in range(positions):
            value = self.data[x + i][y]
            result.append(value)

        return result

    def look_down_left(self, x, y, positions):
        if x + positions > self.n_rows or y - (positions-1) < 0:
            return []

        result = []
        for i in range(positions):
            value = self.data[x + i][y - i]
            result.append(value)

        return result

    def look_left(self, x, y, positions):
        if y - (positions - 1) < 0:
            return []

        result = []
        for i in range(positions):
            value = self.data[x][y - i]
            result.append(value)

        return result

    def look_up_left(self, x, y, positions):
        if x - (positions - 1) < 0 or y - (positions - 1) < 0:
            return []

        result = []
        for i in range(positions):
            value = self.data[x - i][y - i]
            result.append(value)

        return result
