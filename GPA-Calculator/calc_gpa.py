from grade_info import calculate_semgpa, calculate_cumulgpa

sem_number = int(input("Semester GPA to be calculated (1-8) : "))

sem_gpa = calculate_semgpa(sem_number)
cumul_gpa = calculate_cumulgpa()

print(f"""
Your Semester {sem_number} GPA is {sem_gpa}. 
Your Cumulative GPA is {cumul_gpa}.
""")
