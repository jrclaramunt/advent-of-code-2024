import re
from functools import total_ordering

from utils.base import Day


class Day4(Day):
    def __init__(self, args):
        self.word_db = []
        for row in args[0]:
            self.word_db.append(list(row.strip()))

    def part1(self):
        total = 0

        for row in self.word_db:
            word_row = ''.join(row)
            total += len(re.findall(r'XMAS', word_row))
            total += len(re.findall(r'SAMX', word_row))

        for i in range(len(self.word_db)):
            a = []
            for j in range(len(self.word_db[i])):
                a.append(self.word_db[j][i])
            word_row = ''.join(a)
            total += len(re.findall(r'XMAS', word_row))
            total += len(re.findall(r'SAMX', word_row))

        for i in range(0, len(self.word_db)):
            self.gen(i)

        return total
        # for i in range(0, 5):
        #     self.gen(i)

    def part2(self):
        pass

    def gen(self, n):
        total = 0
        a = []
        for i in range(n + 1):
            for j in range(i):
                a.append(self.word_db[j][i])
                a.append(self.word_db[i][j])
        # if n%2 != 0 and n != 0:
        #     a.append(self.word_db[n - 1][n - 1])
        word_row = ''.join(a)
        total += len(re.findall(r'XMAS', word_row))
        total += len(re.findall(r'SAMX', word_row))
        return total

