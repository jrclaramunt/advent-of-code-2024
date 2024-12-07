import re
from collections import defaultdict

from utils.base import Day


class Day5(Day):
    def __init__(self, args):
        self.rules = defaultdict(list)
        self.updates = []

        split_index = args[0].index('\n')
        rules = args[0][0:split_index]
        updates = args[0][split_index+ 1 :]

        for rule in rules:
            pages = rule.strip().split('|')
            self.rules[pages[0]].append(pages[1])

        for update in updates:
            self.updates.append(update.strip().split(','))


    def part1(self):
        return self.valid_updates_calculation(self.updates)

    def part2(self):
        wrong_updates = []

        for update in self.updates:
            add = False
            for i in range(len(update) - 1):
                if update[i + 1] not in self.rules[update[i]]:
                    add = True
                    break
            if add:
                wrong_updates.append(update)

        pass

    def valid_updates_calculation(self, updates):
        total = 0

        for update in updates:
            add = True
            for i in range(len(update) - 1):
                if update[i + 1] not in self.rules[update[i]]:
                    add = False
                    break
            if add:
                total += int(update[int(len(update) / 2)])

        return total # 69148 too high