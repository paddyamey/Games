import random

random_list = []
user_list = []
used_number = []

index_finder = -1
random_number = str(random.randint(0, 9999))
random_list = list(random_number)
print(random_list)

while True:

    bulls = 0  # if same number wrong place
    cows = 0  # if right number and right place

    user_number = input("Guess a random four digit number")

    for index, number in enumerate(user_number):
        temp_list = random_list.copy()
        if number == random_list[index]:

            cows += 1
            print(temp_list)
            temp_list.remove(number)
            print(temp_list)

        elif number in temp_list:
            bulls += 1
            temp_list.remove(number)



    print(f"You have {bulls} bulls and {cows} cows.")
    if cows == 4:
        print("You guessed the number exactly right!")
        break
