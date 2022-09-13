import functools


def calculate_addition():
    number = float(input("Enter the number: "))
    count = 0  # Total number enter
    addition = 0
    while number != 0:
        addition += number
        count += 1
        number = float(input("Enter another number: "))
    return [addition, count]


def calculate_subtraction():
    number_list = []
    value = float(input("Enter the number: "))
    if value != 0:
        number_list.append(value)
    while value != 0:
        value = float(input("Enter another number: "))
        if value != 0:
            number_list.append(value)

    subtraction = functools.reduce(lambda num1, num2: num1 - num2, number_list)
    print(number_list)
    return [subtraction, len(number_list)]


def calculate_multiplication():
    number = float(input("Enter the number: "))
    count = 0  # Total number enter
    multiplication = 1
    while number != 0:
        multiplication = multiplication * number
        count += 1
        number = float(input("Enter another number: "))
    return [multiplication, count]


def calculate_average():
    addition_result = calculate_addition()
    addition = addition_result[0]
    total_number = addition_result[1]
    average = addition / total_number
    return [average, total_number]


while True:
    ans = []
    print(" Simple Calculator in python by Malik Umer Farooq")
    print(" Enter '1' for addition")
    print(" Enter '2' for substraction")
    print(" Enter '3' for multiplication")
    print(" Enter '4' for average")
    print(" Enter 'q' for quit")

    option = input("Enter: ")

    if option == 'q':
        print("Quit...")
        break
    else:
        if option == '1':
            ans = calculate_addition()
            print("Addition = ", ans[0], " total inputs = ", ans[1])

        elif option == '2':
            ans = calculate_subtraction()
            print("Subtraction = ", ans[0], " total inputs = ", ans[1])

        elif option == '3':
            ans = calculate_multiplication()
            print("Multiplication = ", ans[0], " total inputs = ", ans[1])

        elif option == '4':
            ans = calculate_average()
            print("Average = ", ans[0], " total inputs = ", ans[1])

        else:
            print("Invalid option")

