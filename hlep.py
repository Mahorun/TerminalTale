import os
import random
import time
import platform

def clear():
  if platform.system() == "Windows":
    os.system("cls")
  else:
    os.system("clear")
def fight(mainc, attacker):
    print(f"{attacker.name} appeard!")
    while mainc.alive and attacker.alive:
        print(f"Enemy HP:{attacker.health}")
        print(f"Your HP:{mainc.health}")
        userinput2 = input("1 for attack, 2 for health, 3 for TP, 4 for magic.")
        if userinput2 == "1":
          attack(mainc, attacker)
          print("You attacked!")
        elif userinput2 == "2":
          heal(mainc)
          if not heal(mainc):
            print("You cant heal!")
        elif userinput2 == "3":
          mainc.tp += 16
          print("You gained 16 TP")
        elif userinput2 == "4":
          magicial_input = input("""1 for xStab, requires 32TP.""")
          if magicial_input == 1:
            print()
        else:
          print("Skipping Your Turn...")
        input("Press Enter To Continue")
        clear()
        print(f"{attacker.name} attacked you!")
        attack(attacker, mainc)
    if mainc.alive and not attacker.alive:
      print("You won!")
    else:
      print("how did you lost lol")

def heal(character):
    amount = random.choice(character.healAmount)
    if character.health == character.maxhp:
      return False
    elif hasattr(character, 'shines') and character.shines:
        print("You called for somebody to heal you...")
        time.sleep(3)
        print("But nobody came.")
    elif character.health + amount > character.maxhp:
        character. health = character.health + amount - (character.health + amount - character.maxhp)
    else:
        character.health = character.health + amount
    return character.health
def attack(attacker, defenser):
    if hasattr(defenser, 'shines') and defenser.shines:
      print("But your soul shines within your name!")
      time.sleep(3)
      print("You only took one damage.")
      defenser.health -= 1
      input("Press enter to continue...")
      clear()
    elif hasattr(defenser, 'defense') and defenser.defense and defenser.defense != 0: 
        defenser.health -= (random.choice(attacker.damage) - (defenser.defense // 10 + 1)) 
    else:
        defenser.health = defenser.health - random.choice(attacker.damage)
    defenser.alive = bool(defenser.health > 0)
    return defenser.health
