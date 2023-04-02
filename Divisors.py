# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.


def divisor(x):
    divisors = []
    for i in range(2, x+1):
        if (x % i) == 0:
            divisors += [i]

    print(divisors)



