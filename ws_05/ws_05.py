#1
#
# string_array = []
# longest = 0
# longest_string = ''
#
# while True:
#
#     string = str(input("Enter a string:"))
#     string_array.append(string)
#     if string.startswith("A"):
#         break
#
#     if len(string) > longest:
#         longest = len(string)
#         longest_string = string
#
# print("The longest was:", longest_string)

#2

# string = str(input("Enter a string:"))
# processed_string = ""
#
# for char in string:
#     if char.isdigit():
#         processed_string += '_'
#     else:
#         processed_string += char
#
# print("Output: ", processed_string)

#3

# def leap_year(year):
#     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
#
# start_year = int(input("Enter Year 1: "))
# end_year = int(input("Enter Year 2: "))
#
# days = 0
# for year in range(start_year, end_year + 1):
#     if leap_year(year):
#         days += 366
#     else:
#         days += 365
#
# print("Number of days: ", days)

#4
import math

while True:
    CARPET_WIDTH = 3.66

    dimension_1 = float(input("Enter room dimension 1(m): "))
    dimension_2 = float(input("Enter room dimension 2(m): "))

    if dimension_1 <= 0 or dimension_2 <= 0:
        break
    if dimension_1 > dimension_2:
        length = dimension_1
        width = dimension_2
    else:
        length = dimension_2
        width = dimension_1


    def lengthways(length, width):
        if width < CARPET_WIDTH:
            return math.ceil(length)
        else:
            return math.ceil(length * math.ceil(width / CARPET_WIDTH))

    def widthways(length, width):
        if length < CARPET_WIDTH:
            return math.ceil(width)
        else:
            return math.ceil(width * math.ceil(length / CARPET_WIDTH))

    print("Length: ", "{:.3f}".format(length))
    print("Width: ", "{:.3f}".format(width))

    required_length_lengthways = lengthways(length, width)
    print("Total carpet length in lengthways manner = ", required_length_lengthways)
    required_length_widthways = widthways(length, width)
    print("Total carpet length in widthways manner = ", required_length_widthways)