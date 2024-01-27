import time
from hlep import clear, fight

class Froggit: #Unhealable
    human = False
    name = "Froggit"
    health = 20
    damage = [2 ,3]
    alive = True
    name = "Froggit" 
class Frisk: #Healable
    human = True
    color = "red"
    name = ""
    health = 20
    maxhp = 20
    damage = [4 ,5]
    healAmount = [2, 3, 4, 5] 
    tp = 0
    alive = True
    defense = 0
    shines = False
Usr = input("Do you want armors to be on?(Y) ") 
if Usr == "Y":
  Frisk.defense = 5
nameQuestion = input("Give human a name.")
if nameQuestion == "Frisk":
  areYouSureAboutFrisk = input("This name will make your life hell. Are you sure?(Y/n)")
  if areYouSureAboutFrisk == "Y":
    Frisk.shines = True
    Frisk.health = 3
  else:
    print("then your name is automatically set to Q5U4EX7YY2E9N")
    Frisk.name = "Q5U4EX7YY2E9N"
else:
  print(f"Your name is {nameQuestion}")
  Frisk.name = nameQuestion
time.sleep(3)
clear()
fight(Frisk, Froggit)
