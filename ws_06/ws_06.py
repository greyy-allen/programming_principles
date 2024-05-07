#1
# while True:
#     try:
#         input_string = input("Enter String: ")
#         words = input_string.split()
#         processed_words = []
#
#         if input_string == ' ' or input_string == '':
#             break
#         for word in words:
#             processed_word = word.lower()
#             processed_words.append(processed_word)
#
#         processed_words.sort(reverse=True)
#         output_string = " ".join(processed_words)
#         print(output_string)
#         print("====NEW STRING====")
#
#     except ValueError as ve:
#         print("Error: ", ve)
#         print("Please put a valid string")


#2

# while True:
#     try:
#         list_1 = input("Enter numbers: ")
#         list_2 = input("Enter numbers: ")
#
#         list_1 = list_1.split(' ')
#         list_2 = list_2.split(' ')
#
#         # print(list_1)
#         # print(list_2)
#
#         processed_list_1 = [int(d) for d in list_1]
#         processed_list_2 = [int(d) for d in list_2]
#
#         sum_1 = processed_list_1[0] + processed_list_1[-1]
#         sum_2 = processed_list_2[0] + processed_list_2[-1]
#
#         if sum_1 > sum_2:
#             print("Output:", sum_1)
#         else:
#             print("Output:", sum_2)
#
#         print("====NEW LIST====")
#
#     except ValueError as ve:
#         print("Error: ", ve)
#         print("Please put a valid number")

#3
# while True:
#     try:
#         string_input = input('Enter a string: ')
#         def is_happy(string):
#             string = string.lower()
#
#             for i in range(len(string)):
#                 if string[i] == 'g':
#                     if (i>0 and string[i-1] =='g') or (i < len(string)-1 and string[i+1] == 'g'):
#                         continue
#                     else:
#                         return False
#                 return True
#         print("Happy? ", is_happy(string_input))
#         print("====NEW STRING====")
#
#     except ValueError as ve:
#         print("Error: ", ve)
#         print("Please put a string with letter g")

#4
while True:
    try:
        student_1 = input("Student 1(courses 1-4): ")
        student_2 = input("Student 2(courses 1-4): ")
        student_3 = input("Student 3(courses 1-4): ")
        student_4 = input("Student 4(courses 1-4): ")
        student_5 = input("Student 5(courses 1-5): ")
        student_grades = [student_1, student_2, student_3, student_4, student_5]
        average_grade_list = []
        average_course_grade_list = []
        initial_course_grade_list = []

        for grades in student_grades:
            split_grades = grades.split(' ')
            initial_course_grade_list.append(split_grades)

        course_grades_list = list(zip(*initial_course_grade_list))
        def average_grade(grades_str):
            grades = grades_str.split(' ')

            grades_int = [int(num) for num in grades]
            average_grade_int = sum(grades_int) / len(grades_int)
            return average_grade_int

        def average_course_grade():
            course_grades_int = [int(num) for num in course_grades_list]
            average_course_grade_int = sum(course_grades_int) / len(course_grades_int)
            return average_course_grade_int

        for grades_str in student_grades:
            avg_grade = average_grade(grades_str)
            average_grade_list.append(avg_grade)

        for course_grades_str in course_grades_list:
            avg_course_grade = average_course_grade()
            average_course_grade_list.append(avg_course_grade)

        print("The highest average mark of student: ", max(average_grade_list))
        print("The highest average mark of course: ", max(average_course_grade_list))

    except ValueError as ve:
        print("Error: ", ve)
        print("Please put a valid grades")

