def main():
    problem1()
    # problem2()
    # problem3()
    # problem4()

# Create a function in your program that counts from 0 to [NUMBER]
def problem1():

    userInput = int(input("Enter a number "))
    # for number in range(10):
    #     print(number)
    count(userInput)
def count(userInput):
    for something in range (0,userInput):
        print (something)


# Create a function that has a loop that quits with ‘q’. If the user doesn't enter 'q', ask them to input another string.
def problem2():
    userInput = ""
    loop(userInput)
def loop(userInput):
    while userInput.lower() != 'q':
        userInput = input("Enter something, Enter q to quit! ")


#Create 4 functions called add, subtract, multiply, and divide.
# Create them to allow a user to perform the name of the function to the two numbers and return the result.
def problem3():
    num1 = int(input("Enter a number "))
    num2 = int(input("Enter another number "))
    print(add(num1,num2))
    print(subtract(num1,num2))
    print(multiply(num1,num2))
    print(divide(num1,num2))
def add(num1, num2):
    sum = num1 + num2
    return(sum)
def subtract(num1,num2):
    diff = num1 - num2
    return(diff)
def multiply(num1,num2):
    prod = num1 * num2
    return (prod)
def divide(num1,num2):
    quot = (num1//num2)
    return(quot)


# Create a function that will ask the user for a number. Use the function to get two numbers, then pass the two numbers to a function and ask a user if they want to add, subtract, multiple, or divide them. Return a string that prints the two numbers, which operation it did, and the result.
def problem4():
    num1 = int(input("Enter a number "))
    num2 = int(input("Enter another number "))
    op = input("Enter operation: add, subtract, divide, or multiply ")
    print(userOp(num1,num2,op))
def userOp(num1,num2, op):
    if op == "add":
       return (f'{num1} + {num2}= {num1 + num2}')
    elif op == "subtract":
        return(f'{num1}-{num2}= {num1 - num2}')
    elif op == "divide":
        return(f'{num1}/{num2}={num1/num2}')
    elif op == "multiply":
        return(f'{num1}*{num2}={num1*num2}')



#     def main():
#         problem1()
#
# def problem1():
#     favTeacher = "Kenn"
#     favTeacherFunction(favTeacher)
#
# def favTeacherFunction(favTeacher):
#     print(favTeacher)




if __name__ == '__main__':
    main()
