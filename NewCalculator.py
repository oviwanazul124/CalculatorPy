
# This function is in charge of sending to console the welcome message

def welcome():

    print('\nWelcome to the calculator please enter the follwings symbols to make a calculation: \n "+" Use the plus symbol to do addition \n "-" Use the minus symbol to do subtraction \n "*" Use the  symbol to multiply \n "sqr" Use the string to do roots \n "**" Use the double  symbol to exponent')
    global symbolCalculation
    symbolCalculation = input("\nPlease enter the following: ")

# The inputManager function work from getting a value, from example: value = n. Meaning that n is the maximun
# number of inputs that the function can make.

def inputManager(values):
    
    match values:

        case 2:

            global inputFirstNumber
            inputFirstNumber = int(input('Please enter the first number to do the operation: '))
            global inputSecondNumber
            inputSecondNumber = int(input('Please enter the second number to do the operation: '))

        case 1:

            inputFirstNumber = int(input('Please enter the first number to do the operation: '))

        case 3:

            inputFirstNumber = int(input('Please enter the numerator to do the operation: '))
            inputSecondNumber = int(input('Please enter the denominator to do the operation: '))
            global inputThirdNumber
            inputThirdNumber = int(input('Please enter the third exponent to do the operation: '))

    pass

# The calculation() is a function that recives a value from the variable 'symbolCalculation'. From this variable
# check in match if the function is inside of the main symbol.

def calculation():

    match symbolCalculation:

        case "+":
            inputManager(2)
            print(str(inputFirstNumber + inputSecondNumber))
            welcome()

        case "-":

            inputManager(2)
            print(str(inputFirstNumber - inputSecondNumber))
            welcome()
    
        case "/":

            inputManager(2)
            print(str(inputFirstNumber / inputSecondNumber))
            welcome()

        case "*":

            inputManager(2)
            print(str(inputFirstNumber * inputSecondNumber))
            welcome()

        case "exit":
            exit()

        case "sqr":
            inputManager(3)
            print(str(sqrt(inputFirstNumber, inputSecondNumber, inputThirdNumber)))
            welcome()

        case "**":
            inputManager(2)
            print(str(inputFirstNumber ** inputSecondNumber))
            welcome()

        case _:

            print("The input you has used " + str(symbolCalculation) + " is not defined in this calculator")
            welcome()

# The function sqrt(), is a fuction that permit to use roots without the use of the library math.sqrt(), why
# I implemented this?. Why not?.

def sqrt(numerator, denominator, exponent):
    
    resultFractions = int(numerator) / int(denominator)
    mainResult = float(exponent) ** resultFractions
    return mainResult

welcome()
calculation()