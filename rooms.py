import helpers as h

class Character:
  def __init__(self, inventory):
    self.inventory = []

class Room:
  def __init__(self,name,objects):
    self.name = name
    self.objects = objects

class Object:
  def __init__(self,name):
    self.name = name
    self.description = h.file_get("text/objects/"+self.name.lower+".txt")

def make_rooms():
  rooms = []
  rooms.append(Room("REACTOR_ROOM", [
    Object("PIPES"),
    Object("WIRES"),
    Object("TABLES"),
    Object("WATCH")
  ]))
  