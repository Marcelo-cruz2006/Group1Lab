from rps import play_rps
from guessing import play_guessing_game


# Lab 1: Rock, Paper, Scissors and Guessing Game
# Author: Marcelo Cruz
# Date: 10/23/2026

def main():
      print("Hello, welcome to the Rock, Paper, Scissors game! or guessing game!")
      while True:
          print("\nPlease choose a game to play:")
          print("1. Rock, Paper, Scissors")
          print("2. Guessing Game")
          print("3. Exit")

          choice = input("Enter the number of your choice: ")

          if choice == '1':
              from rps import play_rps
              play_rps()
          elif choice == '2':
              from guessing import play_guessing_game
              play_guessing_game()
          elif choice == '3':
              print("Thank you for playing! Goodbye!")
              break
          else:
              print("Invalid choice. Please enter 1, 2, or 3.")
         
if __name__ == "__main__":
    main()