import time
from functions import clear, fight
from characters import Frisk, Froggit, Clover

selected_character = input("Do you want to be yellow soul? (Y)")
if selected_character.lower() == "y":
  selected_character = Clover
  time.sleep(3)
  clear()
else:
  selected_character = Frisk
  name = input("Enter your name.")
  if name == "Frisk":
    questionMark = input("Are you sure(Y)? This name will make your life hell.")
    if questionMark.lower() == "y":
      print("Good luck.")
      time.sleep(3)
      Frisk.shines = True
    elif questionMark:
      print(f"{name} is your name right now.")
      time.sleep(3)
      clear()
    else:
      print("Well, you are now nameless lol.")
      time.sleep(3)
      clear()
fight(selected_character, Froggit)

