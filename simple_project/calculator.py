# Calculator

def calculate_addition():
    print("Addition")
    number = float(input("Enter the number: "))
    count = 0  # Total number enter
    addition = 0
    while number != 0:
        addition += number
        count += 1
        number = float(input("Enter another number (0 to calculate): "))
    return [addition, count]


def calculate_subtraction():
    print("Subtraction")
    number = float(input("Enter the number: "))
    count = 0  # Total number enter
    subtraction = 0
    while number != 0:
        subtraction = subtraction - number
        count += 1
        number = float(input("Enter another number (0 to calculate): "))
    return [subtraction, count]


def calculate_multiplication():
    print("Multiplication")
    number = float(input("Enter the number: "))
    count = 0  # Total number enter
    multiplication = 1
    while number != 0:
        multiplication = multiplication * number
        count += 1
        number = float(input("Enter another number (0 to calculate): "))
    return [multiplication, count]


def calculate_average():
    addition_result = calculate_addition()
    addition = addition_result[0]
    total_number = addition_result[1]
    average = addition / total_number
    return [average, total_number]


while True:
    ans = []
    print(" My first python program!")
    print(" Simple Calculator in python by Malik Umer Farooq")
    print(" Enter '1' for addition")
    print(" Enter '2' for substraction")
    print(" Enter '3' for multiplication")
    print(" Enter '4' for average")
    print(" Enter 'q' for quit")

    option = input("Enter: ")

    if option != 'q':

        if option == '1':
            ans = calculate_addition()
            print("Ans = ", ans[0], " total inputs = ", ans[1])

        elif option == '2':
            ans = calculate_subtraction()
            print("Ans = ", ans[0], " total inputs = ", ans[1])

        elif option == '3':
            ans = calculate_multiplication()
            print("Ans = ", ans[0], " total inputs = ", ans[1])

        elif option == '4':
            ans = calculate_average()
            print("Ans = ", ans[0], " total inputs = ", ans[1])

        else:
            print("Invalid option")

    else:
        print("Quit...")
        break
