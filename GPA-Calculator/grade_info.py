import pandas as pd


# MISCELLANEOUS CREDITS
# ap_credits = 16.0

data = pd.read_csv(
    "/Users/hunterholland/Documents/Projects/GPA-Calculator/coursedata.csv")

grades = ["A+", "A", "A-", "B+", "B", "B-",
          "C+", "C", "C-", "D+", "D", "P", "N"]
points = [4.33, 4.00, 3.67, 3.33, 3.00, 2.67,
          2.33, 2.00, 1.67, 1.33, 1.00, 0.00, 0.00]
grades_points = dict(zip(grades, points))


# all_sem_credits = data.groupby("Semester")["Credits"].sum().sum()
all_sem_credits = data[(data["Grade"] != "N") & (
    data["Grade"] != "P")]["Credits"].sum()


def sem_info(sem_number):
    sem_credits = data[(data["Semester"] == sem_number)
                       & (data["Grade"] != "P")]["Credits"].reset_index()
    sem_grades = (data[(data["Semester"] == sem_number)
                       & (data["Grade"] != "P")]["Grade"].reset_index())
    total_credits = data[(data["Semester"] == sem_number)
                         & (data["Grade"] != "P")]["Credits"].sum()
    return sem_credits, sem_grades, total_credits, sem_number


def calculate_semgpa(sem_number):
    sem_points = sem_info(sem_number)[0]["Credits"]
    sem_grades = sem_info(sem_number)[1]["Grade"]
    total_points = sem_info(sem_number)[2]
    class_gpas = []
    for grade in sem_grades:
        class_gpas.append(grades_points[grade])
    gpa_credits = list(zip(class_gpas, sem_points))
    effective_credits = [gpa*credit for (gpa, credit) in gpa_credits]
    sem_gpa = [(sum(effective_credits)/total_points)
               if (total_points != 0.0) else 0.0]
    return sem_gpa[0]


def calculate_cumulgpa():
    partial_gpas = []
    for sem_number in range(1, 9):
        sem_grades = sem_info(sem_number)[1]["Grade"]
        total_points = sem_info(sem_number)[2]
        sem_gpa = calculate_semgpa(sem_number)
        partial_gpa = [((sem_gpa*total_points)/all_sem_credits)
                       if ((total_points != 0) & (sem_grades[0] != "N")) else 0.0]
        partial_gpas.append(partial_gpa[0])
    cumul_gpa = sum(partial_gpas)
    return cumul_gpa
