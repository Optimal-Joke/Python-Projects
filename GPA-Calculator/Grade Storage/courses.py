import pandas as pd

COURSE_DATA = "/Users/hunterholland/Documents/Projects/Grade Storage/coursedata.csv"


class DataBase():
    """
    """

    def __init__(self):
        self.data_file = pd.read_csv(COURSE_DATA)

    def add_course(self, sem_number, course_name, course_number, professor_name, grade, credits=3):
        pass

    def calculate_gpa(self, sem_number=None):
        pass


class Course(DataBase):
    """
    """

    def __init__(self):
        pass

    def update_grade(self, newgrade):
        self.data_file.at[]

    def update_course_number(self, newcoursenumber):
        pass


test = DataBase()
