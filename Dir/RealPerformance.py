import Performance


class RealPerformance(Performance):
    def average_grade(self):
        return sum(self._grades) / len(self._grades) if self._grades else 0
