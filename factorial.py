#!/usr/bin/env python3
# Created By: Tony Tran
# Date: Nov. 3, 2023
# This program will give you the sum of your number.


def main():
    user_num = str(input("Enter your Factorial Number:\n"))

    try:
        user_num = int(user_num)
    except ValueError:
        print(f"{user_num} is invalid.")
    else:
        if user_num >= 0:
            sum = 1
            list_num = ""
            counter = 0
            while True:
                counter = counter + 1
                sum = sum * counter
                if counter == user_num:
                    list_num = list_num + f"{counter}"
                else:
                    list_num = list_num + f"{counter} * "
                if user_num <= counter:
                    break
            print(f"{user_num}! = {list_num}\n= {sum}")
        else:
            print(f"{user_num} cannot be a negative number.")


if __name__ == "__main__":
    main()
