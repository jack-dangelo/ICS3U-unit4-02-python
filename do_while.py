#!/usr/bin/env python3

# Created by: Jack D'Angelo
# Created on: October 2019
# This program shows the factorial(%) of a number


def main():
    while True:
        # input
        multiplied_number = 1
        total_number = 1
        number = input("Input a number: ")
        print()

        try:
            number_as_number = int(number)
            while number_as_number > multiplied_number:
                # process
                print("x{0}".format(multiplied_number))
                multiplied_number += 1
                total_number = multiplied_number * total_number
            # output
            print("x{0}".format(number_as_number))
            print("The answer is {0}".format(total_number))

        except ValueError:
            print("Invalid Input")
            print()
            continue

        else:
            break


if __name__ == "__main__":
    main()
