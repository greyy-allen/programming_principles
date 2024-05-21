#1
# print("Welcome to the Adder REPL: ")
# command=input("??? ").strip()
# mydict={}
# def input_func(input_var, input_val):
#     mydict[input_var] = input_val
#
# def print_func(print_var):
#     print(print_var, 'equals', mydict[print_var])
#
# def gets_func(gets_var, gets_val):
#     mydict[gets_var] = gets_val
#
# def adds_func(adds_var, adds_val):
#     mydict[adds_var] = mydict[adds_var] + adds_val
#
# while command != 'quit':
#     cmd=command.split()
#     if len(cmd) == 2 and cmd[0] == 'print':
#         print_var = cmd[1]
#         print_func(print_var)
#
#     elif len(cmd) == 2 and cmd[0] == 'input':
#         input_var = cmd[1]
#         input_statement = 'Enter a value for ' + input_var + ':'
#         input_val = input(input_statement)
#
#         input_func(input_var, input_val)
#
#     elif len(cmd) == 3 and cmd[1] == 'adds':
#         adds_var = cmd[0]
#         adds_val = cmd[2]
#
#         adds_func(adds_var, adds_val)
#         print(mydict)
#
#     elif len(cmd) == 3 and cmd[1] == 'gets':
#         gets_var = cmd[0]
#         gets_val = cmd[2]
#
#         gets_func(gets_var, gets_val)
#         print(mydict)
#
#     else:
#         print("Syntax Error")
#
#     command = input("??? ").strip()
# print("Goodbye")

print("Welcome to the Adder REPL: ")
command = input("??? ").strip()
mydict = {}

def input_func(input_var, input_val):
    mydict[input_var] = input_val

def print_func(print_var):
    if print_var in mydict:
        print(print_var, 'equals', mydict[print_var])
    elif print_var.isdigit():
        print(print_var)
    else:
        print(f"'{print_var}' is not defined")

def gets_func(gets_var, gets_val):
    if gets_val.isalpha() and gets_val in mydict:
        mydict[gets_var] = mydict[gets_val]
    elif gets_val.isalpha() and gets_val not in mydict:
        print("Syntax Error")
    elif gets_val.isdigit():
        mydict[gets_var] = int(gets_val)
    else:
        print("Syntax Error")

def adds_func(adds_var, adds_val):
    if adds_val.isdigit():
        if adds_var in mydict and str(mydict[adds_var]).isdigit():
            mydict[adds_var] = mydict[adds_var] + int(adds_val)
        else:
            print("Syntax Error")
    elif adds_val.isalpha():
        if adds_val in mydict and str(mydict[adds_val]).isdigit():
            mydict[adds_var] = int(mydict[adds_var]) + int(mydict[adds_val])
        else:
            print("Syntax Error")
    else:
        print("Syntax Error")


while command != 'quit':
    cmd = command.split()
    if len(cmd) == 2 and cmd[0] == 'print':
        print_var = cmd[1]
        print_func(print_var)

    elif len(cmd) == 2 and cmd[0] == 'input':
        input_var = cmd[1]
        input_statement = 'Enter a value for ' + input_var + ':'
        input_val = input(input_statement)

        input_func(input_var, input_val)

    elif len(cmd) == 3 and cmd[1] == 'adds':
        adds_var = cmd[0]
        adds_val = cmd[2]

        adds_func(adds_var, adds_val)

    elif len(cmd) == 3 and cmd[1] == 'gets':
        gets_var = cmd[0]
        gets_val = cmd[2]

        gets_func(gets_var, gets_val)

    else:
        print("Syntax Error")

    command = input("??? ").strip()

print("Goodbye")
