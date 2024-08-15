grading_scale ={'A': 4.0, 'B': 3.0, 'C': 2.0, 'D':1.0, 'F': 0.0}
num_courses = int(input('enter the number of courses:'))
for i in range(num_courses):
    course_name =input(f'enter course {i +1} name:')
    credit_hours = float (input(f'enter credit hours for {course_name}:'))
    grade = input(f'enter grade for {course_name} (A-F):')
    grade_point = grading_scale[grade.upper()]* credit_hours
    total_grade_points += grade_points
    cgpa = total_grade_points / total_credit_hours
    print(F'your CGPA is:{cgpa:,2f}')