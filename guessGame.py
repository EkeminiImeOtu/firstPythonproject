# This is an awesome guessing game
print("Hello there! What is your name? ")
user_name = input().title()
print("Welcome, " + user_name + ". Guess a number between 1 to 25." )
import random
secret_number = random.randint(1,25)

for guesses in range (1,8):
    
    print("Make your guess, " + user_name)
    
    guess =int(input())
   
    if guess < secret_number:
        print("You guessed too low")
    elif guess > secret_number:
        print("You guessed too high")
    else:
        break #This condition is for the correct guess
if guess == secret_number:
    print("Good job! " + user_name + ", You guessed correctly in " + str(guesses) + " guesses.")
    
else:
    print("You did not guess right," + user_name + ", the number is " + str(secret_number))
