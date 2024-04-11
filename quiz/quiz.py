# 1
length_large = float(input("length of the large square: "))
length_small = float(input("length of the small square: "))

area_large = length_large ** 2
area_small = length_small ** 2

difference_area = area_large - area_small

print("Difference of area", difference_area)

age = int(input("Age: "))
contract_length = int(input("Contract Length: "))

# 2
age = 20
contract_length = 8

if age == 14 and age == 15:
    weekly_salary = 343.44
elif age == 16 and age == 17:
    weekly_salary = 457.92
elif age == 18 and age == 19:
    weekly_salary = 610.56
elif age == 20 and contract_length <= 6:
    weekly_salary = 686.88
elif age == 20 and contract_length > 6:
    weekly_salary = 763.20
elif age > 20:
    weekly_salary = 850.34
else:
    print("Invalid Age")

print("Employee Age: ", age)
print("Contract Length:", contract_length)
print("Annual Salary: ", weekly_salary*52)

#3
while True:
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    try:
        if a > b and a > c:
            if b < c:
                if (a + b) > 50:
                    print("True")
                else:
                    print("False")
            elif c < b:
                if (a + c) > 50:
                    print("True")
                else:
                    print("False")
            else:
                print("Error")
        elif b > a and b > c:
            if a < c:
                if (b + a) > 50:
                    print("True")
                else:
                    print("False")
            elif c < a:
                if (b + c) > 50:
                    print("True")
                else:
                    print("False")
            else:
                print("Error")
        elif c > a and c > b:
            if a < b:
                if (c + a) > 50:
                    print("True")
                else:
                    print("False")
            elif b < a:
                if (c + b) > 50:
                    print("True")
                else:
                    print("False")
            else:
                print("Error")

    except ValueError as ve:
        print("Error: ", ve)
        print("Please put a valid number")


