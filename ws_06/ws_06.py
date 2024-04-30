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

