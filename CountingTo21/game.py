import random


def check_factor(number, factor):
    """
    :param number: integer
    :param factor: integer
    :return: boolean
    """
    if number % factor == 0:
        return True
    else:
        return False


def closest_multiple(number, number_m):
    """
    :param number: integer
    :param number_m: integer
    :return: integer
    """

    while number % number_m != 0:
        number += 1

    return number


def validate_user_input(numbers_entered, user_input_list):

    #  check no more than three numbers have been entered
    if len(user_input_list) > 3:
        return False

    #  the input should all be separated by comas if they are not the input will be split incorrectly
    number_checker = [item.isnumeric() for item in user_input_list]
    if False in number_checker:
        return False

    #  check for 1-3 consecutive numbers
    if len(user_input_list) == 3:
        if int(user_input_list[2]) - int(user_input_list[0]) != 2:
            return False
    elif len(user_input_list) == 2:
        if int(user_input_list[1]) - int(user_input_list[0]) != 1:
            return False

    # the input must start after the previous output
    if int(user_input_list[0]) - int(numbers_entered[-1]) != 1:
        return False

    return True




# coin_toss = random.randint(1, 2)
coin_toss = 2
number_list = list(range(1,22))
numbers_entered = []
#TODO: create list to keep note of every number used so far

if  coin_toss == 1:

    # the first choice can only be 1, 2 or 3
    number = random.randint(1, 3)

    # keep the game going until a player says 21
    while True:

        if number < 4:
            difference = number

        else:
            difference = number - user_number

        if difference == 1:
            print(f"Computer: {number}")
            numbers_entered.append(number)

        elif difference == 2:
            print(f"Computer: {number-1},{number}")
            numbers_entered.append(number - 1)
            numbers_entered.append(number)

        else:
            print(f"Computer: {number-2},{number-1},{number}")
            numbers_entered.append(number - 2)
            numbers_entered.append(number - 1)
            numbers_entered.append(number)

        # verify player has not entered a number with a difference greater than 3
        while True:

            user_number_list = input("Input your number separated by comas:").split(",")

            try:
                if validate_user_input(numbers_entered, user_number_list):
                    user_number = int(user_number_list[-1])
                    number = user_number
                    numbers_entered.extend([int(value) for value in user_number_list])

                    break
                else:
                    print("Invalid input, you must enter three consecutive numbers separated by comas.")


            except ValueError:
                print("You must enter a number.")

        for value in user_number_list:
            if value == str(21):
                print("You have been defeated by the computer.")
                exit()


        if number == 21:
            print("You have been defeated by the computer.")
            break

        elif number == 20:
            print("Computer: 21")
            print("Congratulations, you have won.")
            break

        elif number < 4:
            number = 4

        elif check_factor(number, 4):
            number += random.randint(1, 3)

        else:
            number = closest_multiple(number, 4)

else:
    while True:

        # verify player has not entered a number with a difference greater than 3
        while True:
            user_number_list = input("Input your number separated by comas:").split(",")

            try:
                if int(user_number_list[-1]) < 4:
                    user_number = int(user_number_list[-1])
                    number = user_number
                    numbers_entered.extend([int(value) for value in user_number_list])
                    break

                elif validate_user_input(numbers_entered, user_number_list):
                    user_number = int(user_number_list[-1])
                    number = user_number
                    numbers_entered.extend([int(value) for value in user_number_list])
                    break

                else:
                    print("Invalid input, you must enter three consecutive numbers separated by comas.")


            except ValueError:
                print("You must enter a number.")
            except NameError:
                print("You can only go up 3 numbers.")


        for value in user_number_list:
            if value == str(21):
                print("You have been defeated by the computer.")
                exit()

        if number == 21:
            print("You have been defeated by the computer.")
            break

        elif number == 20:
            print("Computer: 21")
            print("Congratulations, you have won.")
            break

        elif number < 4:
            number = 4

        elif check_factor(number, 4):
            number += random.randint(1, 3)

        else:
            number = closest_multiple(number, 4)

        if number < 4:
            difference = number

        else:
            difference = number - user_number

        if difference == 1:
            print(f"Computer: {number}")
            numbers_entered.append(number)

        elif difference == 2:
            print(f"Computer: {number-1},{number}")
            numbers_entered.append(number - 1)
            numbers_entered.append(number)

        else:
            print(f"Computer: {number-2},{number-1},{number}")
            numbers_entered.append(number - 2)
            numbers_entered.append(number - 1)
            numbers_entered.append(number)



