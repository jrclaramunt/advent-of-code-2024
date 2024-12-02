from utils.base import Day

class Report:
    def __init__(self, levels):
        self.levels = levels
        self.increasing = self.is_increasing()

    def is_increasing(self):
        return self.levels[0] <= self.levels[1]

    def is_difference_allowed(self, a, b):
        if self.increasing:
            return -3 <= (a - b) <= -1
        else:
            return 1 <= (a - b) <= 3

    def is_safe(self):
        for i in range(len(self.levels) - 1):
            if not self.is_difference_allowed(self.levels[i], self.levels[i+1]):
                return False
        return True


class Day2(Day):
    def __init__(self, args):
        self.reports =[]

        for row in args[0]:
            report = map(int, row.split(' '))
            self.reports.append(Report(list(report)))

    def part1(self):
        safe_reports = 0
        for report in self.reports:
            if report.is_safe():
                safe_reports += 1

        return safe_reports

    def part2(self):
        safe_reports = 0
        for report in self.reports:
            if report.is_safe():
                safe_reports += 1
            else:
                if self.is_safe_with_problem_dampener(report):
                    safe_reports += 1

        return safe_reports

    @staticmethod
    def is_safe_with_problem_dampener(report):
        for i in range(len(report.levels)):
            levels = report.levels.copy()
            levels.pop(i)
            mew_report = Report(levels)

            if mew_report.is_safe():
                return True

        return False