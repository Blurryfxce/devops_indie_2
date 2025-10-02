from DesiredPerformance import DesiredPerformance
from RealPerformance import RealPerformance
from Student import Student


class StudentData:
    def __init__(self, student: Student, real_perf: RealPerformance, desired_perf: DesiredPerformance):
        self.student = student
        self.real_perf = real_perf
        self.desired_perf = desired_perf

    def to_dict(self):
        return {
            "student": {
                "pib": self.student.get_pib(),
                "group": self.student.get_group(),
                "dob": self.student.get_dob(),
                "address": self.student.get_address(),
            },
            "real_performance": {
                "subjects": self.real_perf._subjects,
                "grades": self.real_perf._grades,
                "average": self.real_perf.average_grade()
            },
            "desired_performance": {
                "subjects": self.desired_perf._subjects,
                "grades": self.desired_perf._grades,
                "desired_average": self.desired_perf.average_grade()
            }
        }