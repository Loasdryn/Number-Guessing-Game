#This is a simple number guessing game
import random
guess = 0 
tries = 0
Number = random.randint(1,100)

print("""
Hello, Welcome to the number guessing game!
Your job is to guess what number I'm thinking of between 1 and 100.
For each guess, I'll tell you if you're right or wrong,
and if your guess is wrong I'll tell you higher or lower.
There are three difficulty levels.
1. Easy allows 10 tries, 
2. Medium allows 5, 
3. Hard allows 3.
Please select a difficulty level (1, 2, or 3):\n
""")

while True:
    diff = input()
    if int(diff) == 1 :
        print("You have chosen Easy! You have 10 guesses.\n")
        guess = input("Ok, I have a number in mind. What is your guess?\n")
        for tries in range(1,10) :
                guess = int(guess)
                if guess == Number:
                    print("Excellent work! It took you " + str(tries) + " guesses.\n")
                    exit()
                elif guess < Number:
                    tries = tries + 1
                    guess = input("Your guess of " + str(guess) + " is too low, try again!\n")
                    continue
                elif guess > Number:
                    tries = tries + 1
                    guess = input("Your guess of " + str(guess) + " is too high, try again!\n")
                    continue
        else :
            print("You've run out of tries! The number was " + str(Number))
            exit()
    elif int(diff) == 2 :
        print("You have chosen Medium! You have 5 guesses.\n")
        guess = input("Ok, I have a number in mind. What is your guess?\n")
        for tries in range(1,5) :
            guess = int(guess)
            if guess == Number:
                print("Excellent work! It took you " + str(tries) + " guesses.\n")
                exit()
            elif guess < Number:
                tries = tries + 1
                guess = input("Your guess of " + str(guess) + " is too low, try again!\n")
                continue
            elif guess > Number:
                tries = tries + 1
                guess = input("Your guess of " + str(guess) + " is too high, try again!\n")
                continue
        else :
            print("You've run out of tries! The number was " + str(Number))
            exit()
    elif int(diff) == 3 :
        print("You have chosen Hard! You have 3 guesses.\n")
        guess = input("Ok, I have a number in mind. What is your guess?\n")
        for tries in range(1,3) :
            guess = int(guess)
            if guess == Number:
                print("Excellent work! It took you " + str(tries) + " guesses.\n")
                exit()
            elif guess < Number:
                tries = tries + 1
                guess = input("Your guess of " + str(guess) + " is too low, try again!\n")
                continue
            elif guess > Number:
                tries = tries + 1
                guess = input("Your guess of " + str(guess) + " is too high, try again!\n")
                continue
        else :
            print("You've run out of tries! The number was " + str(Number))
            exit()
    elif int(diff) > 3 :
        print("Please enter a valid number: 1, 2, or 3!")
        continue
