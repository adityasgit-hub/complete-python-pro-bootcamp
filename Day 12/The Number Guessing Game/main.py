# Number Guessing Game Objectives:

# Include an ASCII art logo.
import random
from art import logo

easy_level_turns = 16
hard_level_turns = 8

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  # Track the number of turns remaining.
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    # If they got the answer correct, show the actual answer to the player.
    print(f"You got it! The number was {answer}.")

# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return easy_level_turns
  elif level == "hard":
    return hard_level_turns
  else:
    print("Invalid Choice") 

def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 to 100")
  answer = random.randint(1, 100)
  # print(f"Pssst, the number is {answer}")
  turns = set_difficulty()
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    # Allow the player to submit a guess for a number between 1 and 100.
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)
    # If they run out of turns, provide feedback to the player.
    if turns == 0:
      print("You've run out of guesses, you lose.")
      print(f"The number was {answer}")
      return
    elif guess != answer:
      print("Guess again!")

game()
