import random
import json

with open("words.txt") as f:
    word_list = f.read().splitlines()

with open("users.json") as f:
    account_dict = json.load(f)

username = input("Enter your username:")
password = input("Enter your password:")

if username in account_dict.keys():
    if account_dict[username]["password"] == password:
        print(f"{username} logged in")

else:
    if input("No existing user found, would you like to create one?(y/n)") == "y":
        account_dict[username] = {"password": password, "score": 0}
        print(f"Account created for {username}.")

while True:
    if not word_list:
        print("Congratulations you have completed all the words!")
        break

    else:
        game_mode = input("Would you like to play (y/n):")

        if game_mode.lower() == "y":
            # list comprehension
            word_length = set([len(item) for item in word_list])

            while True:
                try:
                    length = int(input(f"How many letters would you like the word to be, you can choose from {word_length}:"))

                    if length not in word_length:
                        print("Invalid input, try again.\n")
                    else:
                        break

                except ValueError:
                    print("You must input an integer.")

            # if statement has to go after the for if there isn't an else
            possible_words = [item for item in word_list if len(item) == length]
            word = random.choice(possible_words)

            censored_word = ["_"] * len(word)
            lines = 10
            letters = list(word)
            print(f"The word has {len(word)} characters")

            while lines > 0:
                guess = input("Guess a letter: ")

                if guess in word and letters.count(guess) == 1:
                    index = word.find(guess)
                    censored_word[index] = guess
                    print(f"The letter {guess} is in the word!\n {censored_word}")

                elif guess in word and letters.count(guess) > 1:
                    index_of_guess = []
                    for characters_index in range(0, len(letters)):
                        if word[characters_index] == guess:
                            index_of_guess.append(characters_index)

                    for recurrences in index_of_guess:
                        censored_word[recurrences] = guess
                    print(f"The letter {guess} is in the word!\n {censored_word}")

                else:
                    lines = lines - 1
                    print(f"That letter is not in the word, you have {lines} guesses left.\n {censored_word}")

                if "_" not in censored_word:
                    print(f"Congratulations {username}, you have guessed the word {word} correctly!")
                    word_list.remove(word)
                    lines = 0

                    account_dict[username]["score"] += 1

        else:
            with open("hangman_saves.json", "w") as f:
                json.dump(account_dict, f)
            exit()
