import math

#Semester Avarage Calculator 1
def semester_avarage_calculator_1():
    semester_weight = float(input('Enter your grade weight: '))
    semester_weight = semester_weight * 0.01
    final_weight = float(input('Enter your final exam weight: '))
    final_weight = final_weight * 0.01
    #get the grades for the 1 grading period
    grade_period_1 = float(input('Enter grade for the 1st grading period: '))
    #avarage out the grade from the 1 grading period
    total = grade_period_1
    total = total / 1
    total_rounded = float(round(total))
    #print avarage
    print('Your avarage for the semester not including the final is ' + str(total) + ' or ' + str(total_rounded))
    #get the final exam score
    final_score_1 = float(input('Enter your score for the final exam: '))
    #get the grade avarage and final score reday to add
    final_score_2 = final_score_1 * final_weight
    new_total = total_rounded * semester_weight
    #add the grade avarage and final score to get the semester avarage
    semester_avg = new_total + final_score_2
    semester_avg_rounded = float(round(semester_avg))
    #print semester avarage
    print('Your semester avarage is ' + str(semester_avg) + ' or ' + str(semester_avg_rounded))

#Semester Avarage Calculator 2
def semester_avarage_calculator_2():
    semester_weight = float(input('Enter your grade weight: '))
    semester_weight = semester_weight * 0.01
    final_weight = float(input('Enter your final exam weight: '))
    final_weight = final_weight * 0.01
    #get the grades for the first 2 grading periods
    grade_period_1 = float(input('Enter grade for the 1st grading period: '))
    grade_period_2 = float(input('Enter grade for the 2nd grading period: '))
    #avarage out the grade from the first 2 grading periods
    total = grade_period_1 + grade_period_2
    total = total / 2
    total_rounded = float(round(total))
    #print avarage
    print('Your avarage for the semester not including the final is ' + str(total) + ' or ' + str(total_rounded))
    #get the final exam score
    final_score_1 = float(input('Enter your score for the final exam: '))
    #get the grade avarage and final score reday to add
    final_score_2 = final_score_1 * final_weight
    new_total = total_rounded * semester_weight
    #add the grade avarage and final score to get the semester avarage
    semester_avg = new_total + final_score_2
    semester_avg_rounded = float(round(semester_avg))
    #print semester avarage
    print('Your semester avarage is ' + str(semester_avg) + ' or ' + str(semester_avg_rounded))

#Semester Avarage Calculator 3
def semester_avarage_calculator_3():
    semester_weight = float(input('Enter your grade weight: '))
    semester_weight = semester_weight * 0.01
    final_weight = float(input('Enter your final exam weight: '))
    final_weight = final_weight * 0.01
    #get the grades for the first 3 grading periods
    grade_period_1 = float(input('Enter grade for the 1st grading period: '))
    grade_period_2 = float(input('Enter grade for the 2nd grading period: '))
    grade_period_3 = float(input('Enter grade for the 3rd grading period: '))
    #avarage out the grade from the first 3 grading periods
    total = grade_period_1 + grade_period_2 + grade_period_3
    total = total / 3
    total_rounded = float(round(total))
    #print avarage
    print('Your avarage for the semester not including the final is ' + str(total) + ' or ' + str(total_rounded))
    #get the final exam score
    final_score_1 = float(input('Enter your score for the final exam: '))
    #get the grade avarage and final score reday to add
    final_score_2 = final_score_1 * final_weight
    new_total = total_rounded * semester_weight
    #add the grade avarage and final score to get the semester avarage
    semester_avg = new_total + final_score_2
    semester_avg_rounded = float(round(semester_avg))
    #print semester avarage
    print('Your semester avarage is ' + str(semester_avg) + ' or ' + str(semester_avg_rounded))

#Semester Avarage Calculator 4
def semester_avarage_calculator_4():
    semester_weight = float(input('Enter your grade weight: '))
    semester_weight = semester_weight * 0.01
    final_weight = float(input('Enter your final exam weight: '))
    final_weight = final_weight * 0.01
    #get the grades for the first 4 grading periods
    grade_period_1 = float(input('Enter grade for the 1st grading period: '))
    grade_period_2 = float(input('Enter grade for the 2nd grading period: '))
    grade_period_3 = float(input('Enter grade for the 3rd grading period: '))
    grade_period_4 = float(input('Enter grade for the 4th grading period: '))
    #avarage out the grade from the first 4 grading periods
    total = grade_period_1 + grade_period_2 + grade_period_3 + grade_period_4
    total = total / 4
    total_rounded = float(round(total))
    #print avarage
    print('Your avarage for the semester not including the final is ' + str(total) + ' or ' + str(total_rounded))
    #get the final exam score
    final_score_1 = float(input('Enter your score for the final exam: '))
    #get the grade avarage and final score reday to add
    final_score_2 = final_score_1 * final_weight
    new_total = total_rounded * semester_weight
    #add the grade avarage and final score to get the semester avarage
    semester_avg = new_total + final_score_2
    semester_avg_rounded = float(round(semester_avg))
    #print semester avarage
    print('Your semester avarage is ' + str(semester_avg) + ' or ' + str(semester_avg_rounded))

def grading_periods():
    print('Press 1 for 1 grading period')
    print('Press 2 for 2 grading period')
    print('Press 3 for 3 grading period')
    print('Press 4 for 4 grading period')
    num_grading_periods = input('Enter here: ')
    if num_grading_periods == '1':
        semester_avarage_calculator_1()
    if num_grading_periods == '2':
        semester_avarage_calculator_2()
    if num_grading_periods == '3':
        semester_avarage_calculator_3()
    if num_grading_periods == '4':
        semester_avarage_calculator_4()

def year_grade():
    s1 = float(input('Enter your grade for the 1st semester: '))
    s2 = float(input('Enter your grade for the 2nd semester: '))
    year_grade_var = s1 + s2
    year_grade_var = year_grade_var / 2
    year_grade_rounded = round(year_grade_var)
    print('Your grade for the year is ' + str(year_grade_var) + ' or ' + str(year_grade_rounded))

def calculator():
    print('Press 1 to calculate your semester grade calculator')
    print('Press 2 to calculate your grade for the year')
    choice = input('Enter here: ')
    if choice == '1':
        grading_periods()
    if choice == '2':
        year_grade()

calculator()