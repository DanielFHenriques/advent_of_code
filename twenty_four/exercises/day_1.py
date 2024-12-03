from typing import Any
from urllib.parse import urljoin

from common.exercise import Exercise


class Day1(Exercise):
    def __init__(self):
        self.sample_file = urljoin(self.PREFIX, '1_sample.txt')
        self.exercise_file = urljoin(self.PREFIX, '1.txt')

    def parse(self, filename: str) -> Any:
        left_list = []
        right_list = []

        with open(filename, 'r') as file:
            for line in file.readlines():
                [left, right] = line.strip().split('  ')

                left_list.append(int(left))
                right_list.append(int(right.strip()))

        return {
            'left_list': left_list,
            'right_list': right_list
        }

    def solve_first(self, **kwargs) -> None:
        left_list = sorted(kwargs['left_list'])
        right_list = sorted(kwargs['right_list'])

        result = 0
        for i in range(len(left_list)):
            result += abs(left_list[i] - right_list[i])

        print(result)

    def solve_second(self, **kwargs) -> None:
        counts = {}

        for right in kwargs['right_list']:
            if right not in counts:
                counts[right] = 0

            counts[right] += 1

        result = 0
        for left in kwargs['left_list']:
            if left in counts:
                result += left * counts[left]

        print(result)
