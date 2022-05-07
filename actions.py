import helpers as h

def print_help(action):
  if action == "ALL":
    h.fileRead("text/help/all.txt")
  elif action == "HELP":
    h.fileRead("text/help/help.txt")
  elif action in ["GO","MOVE","WALK"]:
    h.fileRead("text/help/go.txt")
  elif action == "LOOK":
   h.fileRead("text/help/look.txt")
  elif action == "EQUIP":
    h.fileRead("text/help/equip.txt")
  elif action == "UNEQUIP":
    h.fileRead("text/help/unequip.txt")
  else:
    h.cprint("Invalid action. Use \"HELP\" to get a list of actions.")

def look(action):
  h.cprint("You look at the "+action+". It is very majestic.")