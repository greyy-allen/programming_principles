name = input("What's your name? ")
print("Hello, ", name)

while True:
    try:
        length = float(input("Length: "))
        width = float(input("Width: "))
        volume_per_sqm = float(input("Volume per sqm: "))

        if length < 0 or width < 0 or volume_per_sqm < 0:
            raise ValueError("Only positive numbers are allowed.")

        volume_required = length * width * volume_per_sqm

        print("Volume required = ", volume_required)

    except ValueError as ve:
        print("Error: ", ve)
        print("Please put a valid number")

while True:
    try:
        hours_worked_per_day = float(input("Number of hours worked per day: "))
        days_worked_per_week = float(input("Number of days worked per week: "))
        annual_salary = float(input("Annual Salary: "))
        WEEKS_IN_A_YEAR = 52

        if hours_worked_per_day < 0 or days_worked_per_week < 0 or annual_salary < 0:
            raise ValueError("Only positive numbers are allowed.")

        hourly_wage = annual_salary/(WEEKS_IN_A_YEAR * days_worked_per_week * hours_worked_per_day)

        print("The computed hourly wage is: ", hourly_wage)

    except ValueError as ve:
        print("Error: ", ve)
        print("Please put a valid number")

while True:
    try:
        NUMBER_OF_STUDENTS = 25
        BIG_HALL_LIMIT = 45
        SMALL_HALL_LIMIT = 22
        big_exam_halls = int(input("Number of big exam halls: "))
        small_exam_halls = int(input("Number of small exam halls: "))

        if big_exam_halls < 0 or small_exam_halls < 0:
            raise ValueError("Only positive numbers are allowed.")

        number_of_classes = (big_exam_halls * BIG_HALL_LIMIT + small_exam_halls * SMALL_HALL_LIMIT) // NUMBER_OF_STUDENTS

        print("Number of classes: ", number_of_classes)

    except ValueError as ve:
        print("Error: ", ve)
        print("Please put a valid number")
