while True:
    try:
        MAX_GRADE = 100
        GRADE_6 = 85
        GRADE_5 = 75
        GRADE_4 = 65
        GRADE_F = 50

        mark = float(input("Mark: "))

        if mark >= GRADE_6:
            print("Grade: ", 7)
        elif mark < GRADE_6 and mark >= GRADE_5:
            print("Grade: ", 6)
        elif mark < GRADE_5 and mark >= GRADE_4:
            print("Grade: ", 5)
        elif mark < GRADE_4 and mark >= GRADE_F:
            print("Grade: ", 4)
        else:
            print("Grade: ", F)

    except ValueError as ve:
        print("Error: ", ve)
        print("Please put a valid mark")

distance < 250km, no discount
if 250km ≤ distance < 500km, 10% discount
500km ≤ distance < 1000km, 15% discount
1000km ≤ distance < 2000km, 20% discount
2000km ≤ distance < 3000km, 35% discount
3000km ≤ distance, 50% discount

while True:
    try:
        distance1 = 250
        distance2 = 500
        distance3 = 1000
        distance4 = 2000
        distance5 = 3000

        base_price = float(input("Base Price: "))
        weight = float(input("Weight: "))
        distance = float(input("Distance: "))

        if distance >= distance1 and distance < distance2:
            discount = 0.1
        elif distance >= distance2 and distance < distance3:
            discount = 0.15
        elif distance >= distance3 and distance < distance4:
            discount = 0.20
        elif distance >= distance4 and distance < distance5:
            discount = 0.35
        elif distance >= distance5:
            discount = 0.50

        cost = base_price * weight * distance*(1 - discount)

        print("Total Cost: ", round(cost, 1))
        print("=========ENTER NEW TRANSACTION=========")

    except ValueError as ve:
        print("Error: ", ve)
        print("Please put a valid input")

while True:
    try:
        integer_1 = int(input("Integer 1: "))
        integer_2 = int(input("Integer 2: "))
        integer_3 = int(input("Integer 3: "))

        sort = [integer_1, integer_2, integer_3]

        desc_sort = sorted(sort, reverse=True)

        print(desc_sort)
        print("========NEW SET=========")

    except ValueError as ve:
        print("Error: ", ve)
        print("Please put a valid number")

while True:
    try:
        BASE_HOURS = 37
        BASE_CAR_SALE = 5
        BASE_WAGE = 36.25
        BONUS = 200

        hours = float(input("Hours: "))
        sold_cars = float(input("Sold Cars: "))

        if hours > BASE_HOURS:
            overtime = hours - BASE_HOURS
            hours = BASE_HOURS
        else:
            overtime = 0

        if sold_cars > BASE_CAR_SALE:
            extra_sales = sold_cars - BASE_CAR_SALE
            sold_cars = BASE_CAR_SALE
        else:
            extra_sales = 0

        salary = hours * BASE_WAGE + overtime * 1.5 * BASE_WAGE + extra_sales * BONUS

        print("Salary: ", salary)
        print("=====   NEW SALARY REPORT   =====")

    except ValueError as ve:
        print("Error: ", ve)
        print("Please put a valid number")


