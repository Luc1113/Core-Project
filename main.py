#thing without a title
#made with love(?) by Luca and Justin
import actions as a #functions from actions file
import helpers as h

def start_loop():
  if loops==0:
    h.fileRead("text/0loop.txt")
  elif loops==1:
    h.cprint("Placeholder text for waking up after first loop")
  else:
    h.cprint("Placeholder text for waking up after subsequent loops.")



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
      h.cprint("What are you looking at?")
    
  else:
    h.cprint("Invalid action. Use \"HELP\" to get a list of actions.")
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