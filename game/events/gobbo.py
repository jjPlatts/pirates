import game.event as event
import random
import game.combat as combat
import game.superclasses as superclasses
from game.display import announce

class Gobbo (event.Event):

    def __init__ (self):
        self.name = "Gobbo"

    def process (self, world):
        result = {}
        result["message"] = "Gobbo has lost the battle!"
        monsters = []
        if random.randrange(2) == 0:
            monsters.append(combat.Gobbo("Gobbo"))
            monsters[0].speed = 1.2*monsters[0].speed
            monsters[0].health = 2*monsters[0].health
        announce ("Gobbo spawns in!")
        combat.Combat(monsters).combat()
        result["newevents"] = [ self ]
        return result
