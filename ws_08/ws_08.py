#1
# list_of_numbers = input("Enter list of numbers: ")
# var_array = list_of_numbers.split()
#
# def out_n_in(array_numbers):
#
#     while True:
#         first_number = array_numbers.pop(0)
#         array_numbers.append(first_number)
#         result_string = ' '.join(array_numbers)
#         print(result_string)
#
#         if result_string == list_of_numbers:
#             return ''
#             break
#
# print(out_n_in(var_array))


#2
# while True:
#     list_1 = input("List 1: ")
#     if list_1 == ' ':
#         break
#     list_2 = input("List 2: ")
#
#     first_array = list_1.split()
#     second_array = list_2.split()
#
#     def common_numbers(array_1, array_2):
#         set1 = set(array_1)
#         set2 = set(array_2)
#
#         result_list = list(set1.intersection(set2))
#         return result_list
#
#     print("Output:", common_numbers(first_array, second_array))

#3
sourcefile = input("Enter source file: ")
def arithmetic_progression(numbers):
    difference = numbers[1] - numbers[0]

    for i in range(1, len(numbers) - 1):
        if numbers[i+1]-numbers[i] != difference:
            return False

    return True

with open(sourcefile, 'r') as f1:
    for line in f1:
        numbers = line.split()
        array_numbers = [int(x) for x in numbers]
        if arithmetic_progression(array_numbers):
            print(numbers, "True")
        else:
            print(numbers, "False")
