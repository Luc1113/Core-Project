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

def fileRead(file):
  temp_file = open(file, 'r')
  cprint(temp_file.read())