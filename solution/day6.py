from enum import IntEnum

from utils.base import Day
from utils.utils import Coordinate


class Direction(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Day6(Day):
    def __init__(self, args):
        self.map = []
        for row in args[0]:
            self.map.append(list(row.strip()))

    def part1(self):
        initial_position = self.get_initial_position()
        direction = Direction.UP
        current_position = initial_position
        self.positions_visited = set()

        while True:
            if direction == Direction.UP:
                new_position = self.move_up(current_position)

            if direction == Direction.RIGHT:
                new_position = self.move_right(current_position)

            if direction == Direction.DOWN:
                new_position = self.move_down(current_position)

            if direction == Direction.LEFT:
                new_position = self.move_left(current_position)

            direction = (direction + 1)%4

            if new_position is None:
                break
            else:
                current_position = new_position

        return len(self.positions_visited) + 1

    def part2(self):
        pass

    def get_initial_position(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == '^':
                    return Coordinate(i, j)

    def move_up(self, position):
        for i in range(position.x, 0, -1):
            self.positions_visited.add(Coordinate(i, position.y))
            if self.map[i - 1][position.y] == '#':
                return Coordinate(i, position.y)

    def move_right(self, position):
        for i in range(position.y, len(self.map) - 1, 1):
            self.positions_visited.add(Coordinate(position.x, i))
            if self.map[position.x][i + 1] == '#':
                return Coordinate(position.x, i)

    def move_down(self, position):
        for i in range(position.x, len(self.map) - 1, 1):
            self.positions_visited.add(Coordinate(i, position.y))
            if self.map[i + 1][position.y] == '#':
                return Coordinate(i, position.y)

    def move_left(self, position):
        for i in range(position.y, 0, -1):
            self.positions_visited.add(Coordinate(position.x, i))
            if self.map[position.x][i - 1] == '#':
                return Coordinate(position.x, i)