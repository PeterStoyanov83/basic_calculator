
def intro():
    return '''    #############################################
    #    welcome to the calculator machine!!!   # 
    #         prepare to calculate              #
    #                                           #
    #       PLEASE CHOOSE AN OPTION:            #
    #    created by P. Stoyanov                 #
    #   Inspired by SoftUni Fundamentals        #
    #    lecturer M. Zahariev                   #
    #                                           #
    #############################################'''


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def add(a, b):
    return a + b
print(intro())
while True:
    choice = input(' 1 - add \n 2 - subtract \n 3 - multiply \n 4 - divide \n 5 - Exit \n What is your choice? :')
    if choice == '5':
        print("thank you for using the machine")
        break

    n1 = float(input("input your first number: "))
    n2 = float(input("input your second number: "))

    if choice == "1":
        print("the result is", add(n1, n2))
    elif choice == "2":
        print("the result is", subtract(n1, n2))
    elif choice == "3":
        print("the result is", multiply(n1, n2))
    elif choice == "4":
        print("the result is", divide(n1, n2))
