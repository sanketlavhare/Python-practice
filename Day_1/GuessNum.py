
#Write a program to guess a no. 1 to 10 Accept number from user if guesses correct print congrats
import random

number = random.randint(1,10)

guess = int(input("Guess a number from 1 to 10: "))

if guess == number:
    print("Congrats!! You guessed correctly")
else:
    print("Wrong Guess, The correct number was",number)