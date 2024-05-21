#1

# count = 0
#
# while True:
#
#     string = str(input("Enter a string:"))
#     count += 1
#     if string.endswith('.'):
#         break
#
# print(count, "strings were entered")

#2

# def mytest(chars, option):
#     if option is None:
#         option = 'Alpha'
#
#     if option == 'alpha':
#         return chars.alpha()
#     elif option == 'digit':
#         return chars.isdigit()
#     else:
#         return chars.isspace()
#
# print(mytest("123", option="Alpha"))

#3
sourcefile = open(input("Enter the source file: "), mode='r')
targetfile = open(input("Enter the target file: "), mode='w')

for line in sourcefile:
    if not line[0].isdigit():
        targetfile.write(line)

sourcefile.close()
targetfile.close()

#4
# while True:
#     test_list = input("List 1: ")
#
#     def unique_list(input_list):
#         array_list = input_list.split()
#         set_list = set(array_list)
#
#         set_list = sorted(set_list)
#         array_list = sorted(array_list)
#
#         if set_list == array_list:
#             return True
#         else:
#             return False
#
#     print(unique_list(test_list))

def mytest(chars, option):
    if option is None:
        option = 'alpha'

    if option == 'alpha':
        return chars.isalpha()
    elif option == 'digit':
        return chars.isdigit()
    else:
        return chars.isspace()
