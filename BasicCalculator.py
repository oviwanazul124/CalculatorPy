
# Obtain user input for the operation character
AccountSymbol = input("Welcome, Please enter the following characters (*) Multiplication (+) Addition (-) Subtraction (/) Division : ")
# Make Spaces to good look
print(" ")
# Obtain user input for the first number
Number1 = float(input("Please enter the first number you want to make the account with: "))
# Make Spaces to good look
print(" ")
# Obtain user input for the 2nd number
Number2 = float(input("Now please enter the 2nd number with which you want to perform the operation: "))

# If user selected + perform this operation
if AccountSymbol == "+":
    Result = print("The result of the operation is ", Number1+Number2)

# If user selected * perform this operation
elif AccountSymbol == "*":
    # Make Spaces to good look
    print(" ")
    Result = print("The result of the operation is ", Number1*Number2)

# If user selected - perform this operation
elif AccountSymbol == "-":
    # Make Spaces to good look
    print(" ")
    Result = print("The result of the operation is ", Number1-Number2)

# If user selected / perform this operation
elif AccountSymbol == "/":
    # Make Spaces to good look
    print(" ")
    Result = print("The result of the operation", Number1/Number2)

# Created by Oviwanazul

