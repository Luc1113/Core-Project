import time
import sys as sus

def cprint(str):
  global actions_taken
  for char in str:
    if char=="#":
      sus.stdout.write("\n")
    elif char=="⌚":
      sus.stdout.write(str(20-actions_taken))
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

def file_get(file):
  temp_file = open(file, 'r')
  temp = temp_file.read()
  temp_file.close()
  return temp

def file_print(file):
  cprint(file_get(file))