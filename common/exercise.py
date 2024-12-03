from abc import ABC
from typing import Any


class Exercise(ABC):
    PREFIX = 'twenty_four/inputs/'

    sample_file: str
    exercise_file: str

    def parse(self, file: str) -> Any:
        return {}

    def solve_first(self, **kwargs) -> None:
        ...

    def solve_second(self, **kwargs) -> None:
        ...

    def solve(self) -> None:
        kwargs = self.parse(self.sample_file)
        self.solve_first(**kwargs)

        kwargs = self.parse(self.exercise_file)
        self.solve_first(**kwargs)
        self.solve_second(**kwargs)
