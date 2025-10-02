import Performance


class DesiredPerformance(Performance):
    def __init__(self, subjects: list[str], grades: list[float], desired_avg: float):
        super().__init__(subjects, grades)
        self.__desired_avg = desired_avg

    def average_grade(self):
        return self.__desired_avg
