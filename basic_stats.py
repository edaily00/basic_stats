import statistics
class Student:
    # initializing student class
    def __init__(self, name, grade):
        self._name = name
        self._grade = grade
    # creating method to get grade
    def get_grade(self):
        return self._grade

    # function to gather grades and return mean, median, mode
def basic_stats(student):
    # created a list to hold all grades
    all_grades = []
    # looping through the student to add grades
    for grade in student:
        all_grades.append(grade.get_grade())
    # doing calculations and creating tuple
    mean = statistics.mean(all_grades)
    median = statistics.median(all_grades)
    mode = statistics.mode(all_grades)
    tuple_stats = (mean, median, mode)

    return tuple_stats





