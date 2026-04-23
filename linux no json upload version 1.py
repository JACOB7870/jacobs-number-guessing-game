import json
import os
import random
import time

print("--- Number Guessing game ---")
print("--  1-10  0 for actions  --")

data = {
    'points': 0,
    'guessed_wrong': 0,
    'easy_points': 0,
    'normal_points': 0,
    'hard_points': 0,
    'extreme_points': 0
}

difficulty = "normal"
min_num = 1
max_num = 10

#GAMEPLAY
while True:
    number_guess = int(input("\033[34mGuess: \033[0m"))

    if number_guess == 0:
        print("Select Action:\n1  No Action\n2  Save and Quit\n3  Select difficulty\n4  Show Statistics")
        action_select = int(input("Action Number: ").strip().lower())
        match action_select:
            case 1: #No Action
                continue
            case 2: #Exiting
                print("exiting and saving...")
                time.sleep(1)
                break
            case 3: #Difficulty
                print("Select difficulty:\n1  Easy 1-3\n2  Normal 1-10\n3  Hard 1-30\n4  Extreme 1-100")
                difficulty_select = int(input("Difficulty Number: "))
                match difficulty_select:
                    case 1:
                        min_num = 1
                        max_num = 3
                        print("Selected Easy 1-3...")
                        difficulty = "easy"
                        continue
                    case 2:
                        min_num = 1
                        max_num = 10
                        print("Selected Normal 1-10...")
                        difficulty = "normal"
                        continue
                    case 3:
                        min_num = 1
                        max_num = 30
                        print("Selected Hard 1-30...")
                        difficulty = "hard"
                        continue
                    case 4:
                        min_num = 1
                        max_num = 100
                        print("Selected Extreme 1-100...")
                        difficulty = "extreme"
                        continue
            case 4: #Statistics
                print(f"--- Statistics: ---\nPoints: {data['points']}\nEasy Points: {data['easy_points']}\nNormal Points: {data['normal_points']}\nHard Points: {data['hard_points']}\nExtreme Points: {data['extreme_points']}\nWrong Guesses: {data['guessed_wrong']}")
                continue

    number = random.randint(min_num, max_num)

    if number == number_guess:
        print("\033[31mguessed right!\033[0m")
        print("+1 Point")
        data["points"] += 1
        # region Difficulty Points
        if difficulty == "easy":
            data["easy_points"] += 1
        if difficulty == "normal":
            data["normal_points"] += 1
        if difficulty == "hard":
            data["hard_points"] += 1
        if difficulty == "extreme":
            data["extreme_points"] += 1
        # endregion
    else:
        print("\033[31mwrong number!\033[0m")
        data["guessed_wrong"] += 1
