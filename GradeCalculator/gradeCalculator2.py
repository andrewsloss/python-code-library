def semesterGrade():
    gradingPeriods = int(input("How many grading periods are there: "))
    gradingPeriodGrades = []
    gradeAvg = 0
    for x in range(gradingPeriods):
        gradingPeriodGrades.append(float(input(f"Enter you grade for grading period {x + 1}: ")))
    for y in gradingPeriodGrades:
        gradeAvg += y
    grade = gradeAvg / gradingPeriods
    print(grade)

def yearGrade():
    semesterOne = float(input("Semester One Grade: "))
    semesterTwo = float(input("Semester Two Grade: "))
    grade = (semesterOne + semesterTwo) / 2
    print(grade)

while(True):
    print("1. Semester Grade")
    print("2. Year Grade")
    choice = input("> ")
    if choice == 1:
        semesterGrade()
    elif choice == 2:
        yearGrade()
    else:
        quit()