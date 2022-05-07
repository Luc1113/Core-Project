import helpers as h
import 

def print_help(action):
  if action == "ALL":
    h.file_print("text/help/all.txt")
  elif action == "HELP":
    h.file_print("text/help/help.txt")
  elif action in ["GO","MOVE","WALK"]:
    h.file_print("text/help/go.txt")
  elif action == "LOOK":
   h.file_print("text/help/look.txt")
  elif action == "EQUIP":
    h.file_print("text/help/equip.txt")
  elif action == "UNEQUIP":
    h.file_print("text/help/unequip.txt")
  else:
    h.cprint("Invalid action. Use \"HELP\" to get a list of actions.")

def equip(item):
  

def look(action, room):
  for object in room.objects:
    if object.name == action:
      h.cprint(object.description)
      return
  h.cprint("You don't see any "+action+" in this room.")