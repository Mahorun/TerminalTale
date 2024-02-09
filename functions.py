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
    clear()
    print(f"Enemy HP:{attacker.health}")
    print(f"Your HP:{mainc.health}, Your TP: {mainc.tp}")
    if mainc.color == "red":
      userinput2 = input("1 for attack, 2 for health, 3 for TP, 4 for magic.")
    elif mainc.color == "yellow":
      userinput2 = input("1 for heal, 2 for TP, 3 for magic.(Shot, req. 8 tp, Big Shot, req 32 tp.)")
    if mainc.color == "red":
      actions = {
        "1": lambda: attack(mainc, attacker, "0"),
        "2": lambda: heal(mainc),
        "3": lambda: (
          setattr(mainc, 'tp', mainc.tp + 16),
          print("You gained 16 TP.") if mainc.tp > 0 else None),
        "4": lambda: magic(mainc, attacker)
      }
    if mainc.color == "yellow":
      actions = {
        "1": lambda: heal(mainc),
        "2": lambda: (
          setattr(mainc, 'tp', mainc.tp + 16),
          print("You gained 16 TP.") if mainc.tp > 0 else None),
        "3": lambda: magic(mainc, attacker)
      }
    try:
      if actions[userinput2]() == "Continue":
        continue
    except KeyError:
      print("Skipping your turn!..")
    input("Press Enter To Continue")
    clear()
    print(f"{attacker.name} attacked you!")
    attack(attacker, mainc, "0")
  if mainc.alive and not attacker.alive:
    print("You won!")
  else:
    print("how did you lost lol")


def heal(character):
  amount = random.choice(character.healAmount)
  if character.health == character.maxhp:
    print("You can't heal!")
    return False
  elif hasattr(character, 'shines') and character.shines:
    print("You called for somebody to heal you...")
    time.sleep(3)
    print("But nobody came.")
  elif character.health + amount > character.maxhp:
    character.health = character.health + amount - (character.health + amount - character.maxhp)
  else:
    character.health = character.health + amount
  return character.health


def attack(attacker, defenser, magicial, damage=None):
  if attacker.human and magicial == "0":
    print("You attacked!")
  if magicial == "0" or magicial == "2":
    if hasattr(defenser, 'shines') and defenser.shines:
      print("But your soul shines within your name!")
      time.sleep(3)
      print("You only took one damage.")
      defenser.health -= 1
    elif hasattr(defenser, 'defense') and defenser.defense and defenser.defense != 0:
      if not damage:
        damage = random.choice(attacker.damage)
      defenser.health -= (damage) - (defenser.defense // 10 + 1)
    else:
      if not damage:
        damage = random.choice(attacker.damage)
      defenser.health = defenser.health - damage
  elif magicial == "1":
    print("You attacked to enemy two times!")
    attack(attacker, defenser, "2")
    attack(attacker, defenser, "2")
  elif magicial == "3":
    print("You shot the enemy.")
    attack(attacker, defenser, "2", attacker.normalShotDamage)
  elif magicial == "4":
    print("You big shotted the enemy.")
    attack(attacker, defenser, "2", attacker.BIGshotDamage)
  defenser.alive = bool(defenser.health >= 0)


def magic(mainc, attacker):
  if mainc.color == "red":
    magicial_input = input("1 for XStab, req 24 TP or 2 to go back to fight menu.")
    if magicial_input == "2":
      return "Continue"
  elif mainc.color == "yellow":
    magicial_input = input("1 for shot, req 8 TP; 2 for big shot, req 32 TP or 3 to go back.")
    if magicial_input == "3":
      return "Continue"
  if magicial_input == "1" and mainc.color == "red":
    print("You are using Xstab...")
    time.sleep(3)
    if mainc.tp >= 24:
      attack(mainc, attacker, "1")
      mainc.tp -= 24
    else:
      print("Your tp isn't enough! Skipping your turn...")
  elif magicial_input == "1" and mainc.color == "yellow":
    if mainc.tp >= 8:
      mainc.tp -= 8
      attack(mainc, attacker, "3")
    else:
      print("You dont have anough tp! Skipping your turn!..")
  elif magicial_input == "2" and mainc.color == "yellow":
    if mainc.tp >= 32:
      mainc.tp -= 32
      attack(mainc, attacker, "4")
    else:
      print("You dont have anough tp! Skipping your turn!..")
  else:
    print(f"{magicial_input} does not mean anything! Skipping your turn...  ")
