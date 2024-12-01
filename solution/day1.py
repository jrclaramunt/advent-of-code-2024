import re

from utils.base import Day


class Day1(Day):
    def __init__(self, args):
        self.left_list = []
        self.right_list = []
        regex = r'(\d+)   (\d+)'

        for row in args[0]:
            ids = re.match(regex, row.strip()).groups()
            self.left_list.append(int(ids[0]))
            self.right_list.append(int(ids[1]))

    def part1(self):
        self.left_list.sort()
        self.right_list.sort()
        total_distance = 0

        for idx in range(len(self.left_list)):
            total_distance += abs(self.left_list[idx] - self.right_list[idx])

        return total_distance

    def part2(self):
        appearances = {}
        for id in self.left_list:
            appearances[id] = 0

        for id in self.right_list:
            try:
                appearances[id] += 1
            except KeyError:
                pass

        similarity_score = 0
        for key, value in appearances.items():
            similarity_score += key * value

        return similarity_score

