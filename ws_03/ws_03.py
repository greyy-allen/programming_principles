# count = 0
#
# while True:
#     try:
#         num = int(input("Enter a number: "))
#
#         if num == 0:
#             print(count, "positive numbers were entered.")
#             count = 0
#             print("=====RESET=====")
#
#         if num > 0:
#             count += 1
#
#     except ValueError as ve:
#         print("Error: ", ve)
#         print("Please put a valid mark")


#Fibonacci Sequence

# while True:
#     try:
#         f1 = 0
#         f2 = 1
#         count = 2
#         totalCount = 2
#         n = int(input("Enter a number: "))
#
#         if n == 1:
#             print(f1)
#             print("====RESET====")
#         elif n == 2:
#             print(f1, end=' ')
#             print(f2)
#             print("====RESET====")
#         else:
#             print(f1, end=' ')
#             print(f2, end=' ')
#             for i in range(2, n):
#                 fNum = f1 + f2
#                 f1 = f2
#                 f2 = fNum
#                 count += 1
#                 totalCount += 1
#
#                 if count >= 4:
#                     print(fNum)
#                     count = 0
#                 elif totalCount == n:
#                     print(fNum)
#                     print("====RESET====")
#                 else:
#                     print(fNum, end=' ')

    # except ValueError as ve:
    # print("Error: ", ve)
    # print("Please put a valid number")

#Diamond

# while True:
#     try:
#         n = int(input("Enter a number: "))
#         x = 2 * n - 1
#
#         if n <= 0:
#             raise ValueError("Only positive numbers are allowed.")
#         else:
#             j = 1
#             for i in range(x):
#                 k = round(x/2)
#                 if i < k:
#                     print(" " * (k-i), end="")
#                     print("*" * j)
#                     j += 2
#                 else:
#                     print(" " * (i - k), end="")
#                     print("*" * j)
#                     j -= 2
#
#             print("====RESET====")
#
#     except ValueError as ve:
#         print("Error: ", ve)
#         print("Please put a valid number")

#Palindrome

while True:
    try:
        n = int(input("Enter a number: "))

        if n <= 0:
            raise ValueError("Only positive numbers are allowed.")

        digits = list(map(int, str(n)))
        x = len(str(n))

        if x % 2 == 0:
            mp = len(digits) // 2
            array1 = digits[:mp]
            array2 = digits[mp:]
            array2 = array2[::-1]

            if array1 == array2:
                print(n, "is a palindrome.")
            else:
                print(n, "is not a palindrome.")
        else:
            mp = len(digits) // 2
            del digits[mp]

            array1 = digits[:mp]
            array2 = digits[mp:]
            array2 = array2[::-1]

            if array1 == array2:
                print(n, "is a palindrome.")
            else:
                print(n, "is not a palindrome.")

    except ValueError as ve:
        print("Error: ", ve)
        print("Please put a valid number")