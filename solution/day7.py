import re

from utils.base import Day


class Day7(Day):
    def __init__(self, args):
        regex = r'(\d+):(( \d+)+)'
        self.calibration_equations = dict()
        for row in args[0]:
            group = re.fullmatch(regex, row.strip()).groups()
            self.calibration_equations[int(group[0])] = list(map(lambda x: int(x), group[1].strip().split(' ')))

    def part1(self):
        total = 0
        for result, calibration_equation in self.calibration_equations.items():
            root = Node(calibration_equation[0])
            if self.start(result, calibration_equation[1:], root) is True:
                total += result

        return total

    def part2(self):
        total = 0
        for result, calibration_equation in self.calibration_equations.items():
            root = Node(calibration_equation[0])
            if self.start_with_concat(result, calibration_equation[1:], root) is True:
                total += result

        return total

    def start(self, result, calibration_equation, node):
        if result == node.value and len(calibration_equation) == 0:
            return True
        if len(calibration_equation) == 0:
            return False

        node.insert_left(node.value + calibration_equation[0])
        node.insert_right(node.value * calibration_equation[0])
        return (self.start(result, calibration_equation[1:], node.left) or
                self.start(result, calibration_equation[1:], node.right))

    def start_with_concat(self, result, calibration_equation, node):
        if result == node.value and len(calibration_equation) == 0:
            return True
        if len(calibration_equation) == 0:
            return False

        node.insert_left(node.value + calibration_equation[0])
        node.insert_right(node.value * calibration_equation[0])
        node.insert_concat(int(str(node.value) + str(calibration_equation[0])))
        return (self.start_with_concat(result, calibration_equation[1:], node.left) or
                self.start_with_concat(result, calibration_equation[1:], node.right) or
                self.start_with_concat(result, calibration_equation[2:], node.concat))


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.concat = None

    def insert_left(self, value):
        self.left = Node(value)

    def insert_right(self, value):
        self.right = Node(value)

    def insert_concat(self, value):
        self.concat = Node(value)

    def __str__(self):
        left_value = self.left.value if self.left is not None else None
        right_value = self.right.value if self.right is not None else None
        concat_value = self.concat.value if self.right is not None else None

        return f'value={self.value}, left={left_value}, right={right_value}, concat={concat_value}'