
import random
from art import logo 

print(logo)

number = random.randint(0,101)
print(f"Your Number is: {number}")

print("Welcome to the Number Guessing Game!")
print("I'm Thinking of a number between 1 and 100")

level = input("Choose a difficulty? Type 'easy' or 'hard'?: ")


def play_game():

  score = 0

  if level == "easy":
    score = 10
  elif level == "hard": 
    score = 5
  game_over = False
  while game_over == False:
    print(f"You have {score} remaining attempts, to guess the number")
    guessed_number = int(input("Make a Guess: "))
    if number < guessed_number:
      print("Too High")
      print("Guess again")
      game_over = False
      score = score - 1
    elif number > guessed_number:
      print("Too Low")
      print("Guess Again")
      score = score -1 
      game_over = False
    elif number == guessed_number:
      print(f"You made the correct guess, The corect number is {guessed_number}")
      game_over = True

    if score == 0:
      print("Sorry You ran out of chances")
      exit()

play_game()



