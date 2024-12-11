from utils.base import Day


class Day4(Day):
    def __init__(self, args):
        self.word_db = []
        for row in args[0]:
            self.word_db.append(list(row.strip()))

    def part1(self):
        total = 0
        matrix = Matrix(self.word_db)
        for x in range(len(matrix.data)):
            for y in range(len(matrix.data[x])):
                if matrix.data[x][y] == 'X':
                    if matrix.look_up(x, y, 4) == 'XMAS':
                        total += 1

                    if matrix.look_up_right(x, y, 4) == 'XMAS':
                        total += 1

                    if matrix.look_right(x, y, 4) == 'XMAS':
                        total += 1

                    if matrix.look_down_right(x, y, 4) == 'XMAS':
                        total += 1

                    if matrix.look_down(x, y, 4) == 'XMAS':
                        total += 1

                    if matrix.look_down_left(x, y, 4) == 'XMAS':
                        total += 1

                    if matrix.look_left(x, y, 4) == 'XMAS':
                        total += 1

                    if matrix.look_up_left(x, y, 4) == 'XMAS':
                        total += 1

        return total

    def part2(self):
        total = 0
        matrix = Matrix(self.word_db)
        for x in range(len(matrix.data)):
            for y in range(len(matrix.data[x])):
                if matrix.data[x][y] == 'A':
                    if (((matrix.look_up_left(x, y, 2) == 'AM' and matrix.look_up_right(x, y, 2) == 'AS') and
                        (matrix.look_down_left(x, y, 2) == 'AM' and matrix.look_down_right(x, y, 2) == 'AS')) or

                            ((matrix.look_up_left(x, y, 2) == 'AS' and matrix.look_up_right(x, y, 2) == 'AM') and
                         (matrix.look_down_left(x, y, 2) == 'AS' and matrix.look_down_right(x, y, 2) == 'AM')) or

                            ((matrix.look_up_left(x, y, 2) == 'AM' and matrix.look_down_left(x, y, 2) == 'AS') and
                         (matrix.look_up_right(x, y, 2) == 'AM' and matrix.look_down_right(x, y, 2) == 'AS')) or

                            ((matrix.look_up_left(x, y, 2) == 'AS' and matrix.look_down_left(x, y, 2) == 'AM') and
                         (matrix.look_up_right(x, y, 2) == 'AS' and matrix.look_down_right(x, y, 2) == 'AM'))):
                        total += 1
        return total

class Matrix:
    def __init__(self, data):
        self.data = data
        self.n_rows = len(data)
        self.n_columns = len(data[0])

    def look_up(self, x, y, positions):
        if x - (positions-1) < 0:
            return ''

        result = []
        for i in range(positions):
            value = self.data[x - i][y]
            result.append(value)

        return ''.join(result)

    def look_up_right(self, x, y, positions):
        if x - (positions-1) < 0 or y + positions > self.n_columns:
            return ''

        result = []
        for i in range(positions):
            value = self.data[x - i][y + i]
            result.append(value)

        return ''.join(result)

    def look_right(self, x, y, positions):
        if y + positions > self.n_columns:
            return ''

        result = []
        for i in range(positions):
            value = self.data[x][y + i]
            result.append(value)

        return ''.join(result)

    def look_down_right(self, x, y, positions):
        if x + positions > self.n_rows or y + positions > self.n_columns:
            return ''

        result = []
        for i in range(positions):
            value = self.data[x + i][y + i]
            result.append(value)

        return ''.join(result)

    def look_down(self, x, y, positions):
        if x + positions > self.n_rows:
            return ''

        result = []
        for i in range(positions):
            value = self.data[x + i][y]
            result.append(value)

        return ''.join(result)

    def look_down_left(self, x, y, positions):
        if x + positions > self.n_rows or y - (positions-1) < 0:
            return ''

        result = []
        for i in range(positions):
            value = self.data[x + i][y - i]
            result.append(value)

        return ''.join(result)

    def look_left(self, x, y, positions):
        if y - (positions-1) < 0:
            return ''

        result = []
        for i in range(positions):
            value = self.data[x][y - i]
            result.append(value)

        return ''.join(result)

    def look_up_left(self, x, y, positions):
        if x - (positions-1) < 0 or y - (positions-1) < 0:
            return ''

        result = []
        for i in range(positions):
            value = self.data[x - i][y - i]
            result.append(value)

        return ''.join(result)
