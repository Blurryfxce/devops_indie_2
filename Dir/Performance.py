from abc import ABC, abstractmethod


class Performance(ABC):
    def __init__(self, subjects: list[str], grades: list[float]):
        self._subjects = subjects
        self._grades = grades

    @abstractmethod
    def average_grade(self):
        pass
