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
    cprint()
  elif action == "HELP":
    cprint("HELP")
    cprint("Prints out a list of valid actions.")
    cprint("HELP [action]")
    cprint("Prints a description for the action.")
    cprint("Neither of these actions takes any time.")
  elif action in ["GO","MOVE","WALK"]:
    cprint("GO [location]#Go to the location listed, if you can access it from#your current location.#Synonyms: GO, MOVE, WALK")
  elif action == "LOOK":
    cprint("LOOK [object]#Looks at the object listed, if you can access it from#your current location.#LOOK EQUIPPED#Prints a list of your equipped objects.#Synonyms: LOOK, LOOK AT")
  elif action == "EQUIP":
    cprint("EQUIP [object]#Equips the object listed, if you can access it from#your current location.")
  elif action == "UNEQUIP":
    cprint("UNEQUIP [object]#Uniequips the object listed.")
  else:
    cprint("Invalid action. Use \"HELP\" to get a list of actions.")

def look(action):
  cprint("You look at the "+action+". It is very majestic.")