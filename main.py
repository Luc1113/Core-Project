#thing without a title
#made with love(?) by Luca and Justin
import actions as a #functions from actions file
import helpers as h
import rooms

def start_loop():
  if loops==0:
    h.file_print("text/loopEvents/0loop.txt")
  elif loops==1:
    h.cprint("Placeholder text for waking up after first loop")
  else:
    h.cprint("Placeholder text for waking up after subsequent loops.")

def get_action():
  print()
  action = input("> ")
  action = action.upper().split()
  
  if action[0] == "HELP":
    if len(action) == 1:
      a.print_help("ALL")
    else:
      a.print_help(action[1])

  elif action[0] == "LOOK":
    global room
    if (len(action) >= 3) and action[1] == "AT":
      a.look(action[2], room)
    elif len(action)>=2:
      a.look(action[1], room)
    else:
      h.cprint("What are you looking at?")
    
  else:
    h.cprint("Invalid action. Use \"HELP\" to get a list of actions.")
    get_action()

def main():
  global room
  global actions_taken
  global loops
  
  room = rooms.make_rooms()[0]
  loops = 0
  actions_taken = 0
  start_loop()
  while actions_taken < 5:
    get_action()
    actions_taken += 1
  main()

global loops
global actions_taken
global room

main() 