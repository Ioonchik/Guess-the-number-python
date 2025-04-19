import random
import time
import os
import json

BEST_SCORE_FILE = "best_score.json"

def load_best_score():
    if os.path.exists(BEST_SCORE_FILE):
        try:
            with open(BEST_SCORE_FILE) as f:
                data = json.load(f)
                return data
        except (json.JSONDecodeError, KeyError):
            return {}
    return {}

def save_best_score(new_best, diff):
    best_scores = load_best_score()

    if str(diff) not in best_scores or new_best < best_scores[str(diff)]:
        best_scores[str(diff)] = new_best
        with open(BEST_SCORE_FILE, "w") as f:
            json.dump(best_scores, f)
        print(f"New best in this difficulty: {new_best}")
        return None
    print(f"The best time remains in this difficulty: {best_scores[str(diff)]}")


def start():
    print("You need to select a difficulty:\nEasy (10 chances) [1]\nMedium (5 chances) [2]\nHard (3 chances) [3]\n")
    flag = False
    while flag == False:
        try:
            difficulty = int(input("Just type digit in the brackets [] to choose the difficulty: "))
            flag = True
            
        except:
            print("Write only digits 1-3")
        
    print()

    if difficulty == 1:
        print("Ok, you chose the easy difficulty. That's all you got?")
    elif difficulty == 2:
        print("Hey, you chose the meium difficulty!")
    elif difficulty == 3:
        print("I am impressed, you chose the hard difficulty!")
    
    chances = [10, 5, 3]
    print(f"You have {chances[difficulty-1]} chances. Better use them carefully ;)")
    return chances[difficulty-1], difficulty


def game(chances, number, diff):
    print("\nLet's start! I am thinking of a number. Guess it!")
    start_time = time.time()
    attempts = 0
    while chances > 0:
        while True:
            try:
                guess = int(input("Enter your number: "))
                break
            except:
                print("Write only numbers!")
        attempts += 1
        print()
        if guess > number:
            print("The number is less than your guess!\n")
        elif guess < number:
            print("The number is greater than your guess!\n")

        else:
            time_taken = round(time.time() - start_time, 2)
            print(f"Congratulations! You guessed the number {number} in {attempts} attempts!")
            print(f"It took you {time_taken} seconds to find the number!")

            save_best_score(time_taken, diff)
            return True
        
        chances -= 1
        print(f"You have {chances} chances left")
    else:
        print("You lose!")
        return False


def main(wins):
    print("Welcome to the number guessing game!")
    chances, diff = start()
    number = random.randint(1, 100)
    
    if game(chances, number, diff):
        wins += 1
    
    while True:
        new_game = input("Do you want to try again? (Y/N) ").upper()
        if new_game == 'Y':
            main(wins)
            break
        elif new_game == 'N':
            print(f"You won {wins} times! Goodbye!")
            break
        else:
            print("Enter only Y or N")

main(0)