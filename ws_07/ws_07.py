#1

# sourcefile = open(input("Enter the source file: "), mode='r')
# targetfile = open(input("Enter the target file: "), mode='w')
# count = 0
#
# for line in sourcefile:
#     if line != '\n':
#         targetfile.write(line)
#     else:
#         count +=1
#
# print("Lines removed: ", count)


# sourcefile = open(input("Enter the source file: "), mode='r')
# lines = sourcefile.readlines()
# line1 = lines[0]
# line2 = lines[1]
# line3 = lines[-2]
# line4 = lines[-1]
#
# print("Output:")
# print(line1)
# print(line2)
# print(line3)
# print(line4)

# sourcefile = open(input("Enter the source file: "), mode='r')
# lines = sourcefile.readlines()
#
# def line_average(x):
#     array_of_lines = lines[x].split(" ")
#     average_of_lines = sum(int(x) for x in array_of_lines)/len(array_of_lines)
#     return average_of_lines
#
# print("The average of line 1 is: ", line_average(0))
# print("The average of line 2 is: ", line_average(1))
# print("The average of line 3 is: ", line_average(2))
# print("The average of line 4 is: ", line_average(3))

with open(input("Enter the file name: ")) as f1:
    line_numbers=0
    word_numbers=0
    char_numbers=0

    for line in f1:
        line_numbers += 1
        word_numbers += len(line.split())
        char_numbers += len(line)

    print("Characters: ", char_numbers)
    print("Words: ", word_numbers)
    print("Lines: ", line_numbers)

