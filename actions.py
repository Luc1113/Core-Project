import time
import sys as sus

def cprint(str):
  for char in str:
    if char=="#":
      sus.stdout.write("\n")
    else:
      sus.stdout.write(char)
    sus.stdout.flush()
    time.sleep(0.02)
  print()
"""
prints string out but cooler
str: string to be printed, but cooler
return null
"""

def print_help(action):
  if action == "ALL":
    cprint("HELP")
    cprint("GO")
    cprint("LOOK")
    cprint("EQUIP")
    cprint("UNEQUIP")
  if action == "HELP":
    cprint("HELP")
    cprint("Prints out a list of valid actions.")
    cprint("HELP [action]")
    cprint("Prints a description for the action.")
  if action in ["GO","MOVE","WALK"]:
    cprint("GO [location]#Go to the location listed, if you can access it from#your current location.#Synonyms: GO, MOVE, WALK")
  if action == ["LOOK"]:
    cprint("LOOK [object]#Looks at the object listed, if you can access it from#your current location.#")