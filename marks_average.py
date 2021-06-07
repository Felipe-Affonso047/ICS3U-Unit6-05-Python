#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: June 2021
# This program get marks in porcentage and shows the average


def average(list_of_numbers):
    # this function gets the average
    average = 0

    for counter in range(0, len(list_of_numbers)):
        average += list_of_numbers[counter]

    average = float(average / len(list_of_numbers))

    return average


def main():
    # This function is the main function
    marks = []
    temp_mark = 0
    boolean = True

    print("Enter one mark at a time in percentage. If you are done, enter -1.")

    print()

    while boolean:
        try:
            while temp_mark != -1:
                temp_mark = float(input("Enter your mark(%): "))
                if temp_mark != -1:
                    marks.append(temp_mark)
                    boolean = False
        except Exception:
            print("\nThis input is invalid, please, insert a number.")
            boolean = True

    result = average(marks)

    print("\nThe average is: {}%".format(result))

    print("\nDone.")


if __name__ == "__main__":
    main()
