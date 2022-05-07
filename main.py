#thing without a title
#made with love(?) by Luca and Justin
import time
import sys as sus
import actions as a #functions from actions file

def start_loop():
  if loops==0:
    a.cprint(str(fileRead("text/0loop.txt")))
  elif loops==1:
    a.cprint("Placeholder text for waking up after first loop")
  else:
    a.cprint("Placeholder text for waking up after subsequent loops.")

def fileRead(file):
  temp_file = open(file, 'r')
  return temp_file.read()

def get_action():
  print()
  action = input("> ")
  action = action.split()
  
  if action[0] == "HELP":
    if len(action) == 1:
      a.print_help("ALL")
    else:
      a.print_help(action[1])

  elif action[0] == "LOOK":
    if (len(action) >= 3) and action[1] == "AT":
      a.look(action[2])
    elif len(action)>=2:
      a.look(action[1])
    else:
      a.cprint("What are you looking at?")
    
  else:
    a.cprint("Invalid action. Use \"HELP\" to get a list of actions.")
    get_action()

def main():
  global actions_taken
  start_loop()
  while actions_taken < 20:
    get_action()
    actions_taken -= 1

global loops
global actions_taken

loops = 0
actions_taken = 0
main() 