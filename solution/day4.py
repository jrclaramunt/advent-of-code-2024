from utils.base import Day
from utils.utils import Matrix


class Day4(Day):
    def __init__(self, args):
        self.matrix = Matrix(args[0])

    def part1(self):
        total = 0
        for x in range(len(self.matrix.data)):
            for y in range(len(self.matrix.data[x])):
                if self.matrix.data[x][y] == 'X':
                    if ''.join(self.matrix.look_up(x, y, 4)) == 'XMAS':
                        total += 1

                    if ''.join(self.matrix.look_up_right(x, y, 4)) == 'XMAS':
                        total += 1

                    if ''.join(self.matrix.look_right(x, y, 4)) == 'XMAS':
                        total += 1

                    if ''.join(self.matrix.look_down_right(x, y, 4)) == 'XMAS':
                        total += 1

                    if ''.join(self.matrix.look_down(x, y, 4)) == 'XMAS':
                        total += 1

                    if ''.join(self.matrix.look_down_left(x, y, 4)) == 'XMAS':
                        total += 1

                    if ''.join(self.matrix.look_left(x, y, 4)) == 'XMAS':
                        total += 1

                    if ''.join(self.matrix.look_up_left(x, y, 4)) == 'XMAS':
                        total += 1

        return total

    def part2(self):
        total = 0

        for x in range(len(self.matrix.data)):
            for y in range(len(self.matrix.data[x])):
                if self.matrix.data[x][y] == 'A':
                    if (((''.join(self.matrix.look_up_left(x, y, 2)) == 'AM' and ''.join(self.matrix.look_up_right(x, y, 2)) == 'AS') and
                        (''.join(self.matrix.look_down_left(x, y, 2)) == 'AM' and ''.join(self.matrix.look_down_right(x, y, 2)) == 'AS')) or

                            ((''.join(self.matrix.look_up_left(x, y, 2)) == 'AS' and ''.join(self.matrix.look_up_right(x, y, 2)) == 'AM') and
                         (''.join(self.matrix.look_down_left(x, y, 2)) == 'AS' and ''.join(self.matrix.look_down_right(x, y, 2)) == 'AM')) or

                            ((''.join(self.matrix.look_up_left(x, y, 2)) == 'AM' and ''.join(self.matrix.look_down_left(x, y, 2)) == 'AS') and
                         (''.join(self.matrix.look_up_right(x, y, 2)) == 'AM' and ''.join(self.matrix.look_down_right(x, y, 2)) == 'AS')) or

                            ((''.join(self.matrix.look_up_left(x, y, 2)) == 'AS' and ''.join(self.matrix.look_down_left(x, y, 2)) == 'AM') and
                         (''.join(self.matrix.look_up_right(x, y, 2)) == 'AS' and ''.join(self.matrix.look_down_right(x, y, 2)) == 'AM'))):
                        total += 1
        return total
