from DesiredPerformance import DesiredPerformance
from RealPerformance import RealPerformance
from SaveJSON import SaveJSON
from Student import Student
from StudentData import StudentData


student = Student("Koval Olexandr Serhiiovych", "PDM-51", "01-06-2004", "Ivankiv")

# Реальна успішність
subjects = ["Game Development", "Physics", "Theory of Gravity"]
grades = [70, 70, 95]
real_perf = RealPerformance(subjects, grades)

# Бажана успішність
desired_perf = DesiredPerformance(subjects, [100, 100, 100], 100)

# Дані студента
data = StudentData(student, real_perf, desired_perf).to_dict()

# Ім'я файлу
base_filename = f"{student.get_pib().replace(' ', '_')}_{student.get_group()}_SR2"

# Збереження файлу
SaveJSON().save(data, f"{base_filename}.json")

print("Файли збережено успішно!")