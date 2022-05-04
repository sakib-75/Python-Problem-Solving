# Function for nth fibonacci number

def fibonacci(n):
    n1, n2 = 0, 1

    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0

    elif n == 1:
        return n2

    else:
        for i in range(1, n):
            nth = n1 + n2
            n1 = n2
            n2 = nth
        return n2


nth_position = 14
print("fibonacci number of", nth_position, "position is:", fibonacci(nth_position))
