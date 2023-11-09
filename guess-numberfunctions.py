import random
from art import logo1
random_number = random.randint(1,100)
should_continue = True
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5



def check_answer(guess, random_number):
    diference = abs(random_number - guess)
    if guess == random_number:
        print("You are correct!")
        return True

    elif guess != random_number and guess < random_number and diference > 7:
            print("Too low")
            
    elif guess != random_number and guess > random_number and diference > 7:
            print("Too High")
            
    elif guess != random_number and guess < random_number and diference <= 7:
            print("Little more")
            
    elif guess != random_number and guess > random_number and diference <= 7:
            print("Little less")
    print("Guess again.")

def dificulty():
    level = input("Choose a dificulty ('easy' or 'hard'):")
    if level == 'easy':
         turns = EASY_LEVEL_TURNS
         return turns
    elif level == 'hard':
          turns = HARD_LEVEL_TURNS
          return turns 

print("Welcome to the Guess Game!")
print("I'm thinking in a number between 1 and 100")


attempts = dificulty()

while should_continue:
    print(f"You have {attempts} attempts to do.")   
    guess = int(input("Make a guess:"))
    check_answer(guess,random_number)
    attempts -=1
    if attempts == 0:
        print("You are out of guess!")
        should_continue = False
    elif random_number == guess:
        should_continue = False



    
