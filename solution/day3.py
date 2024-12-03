import re

from utils.base import Day


class Day3(Day):
    def __init__(self, args):
        regex = r'(mul\((\d+),(\d+)\)|do\(\)|don\'t\(\))'
        self.operations = []
        for row in args[0]:
            self.operations += re.findall(regex, row)

    def part1(self):
        total = 0
        for operation in self.operations:
            if 'mul' in operation[0]:
                total += int(operation[1]) * int(operation[2])

        return total

    def part2(self):
        total = 0
        enabled = True
        for operation in self.operations:
            if operation[0] == 'do()':
                enabled = True
                continue

            if operation[0] == 'don\'t()':
                enabled = False
                continue

            if 'mul' in operation[0] and enabled:
                total += int(operation[1]) * int(operation[2])
                continue

        return total
