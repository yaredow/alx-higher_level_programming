#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("{}".format("Fizzbuzz", end=""))
        elif number % 3 == 0:
            print("{}".format("Buzz", end=""))
        elif number % 5 == 0:
            print("{}".format("Fizz", end=""))
        else:
            print(number)
