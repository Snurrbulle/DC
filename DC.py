import time
import sys
import random
import json

class Game:
    def __init__(self):
        self.inventory = {}
        self.health = 10
        self.safeness = 0

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            json.dump({"inventory": self.inventory, "health": self.health, "safeness": self.safeness}, f,
                      indent=True, sort_keys=True)

    def load_from_file(self, filename):
        with open(filename) as f:
            j = json.load(f)
        self.inventory = j["inventory"]
        self.health = j["health"]
        self.safeness = j["safeness"]

    def have_item(self, it):
        return self.inventory.get(it, 0) > 0

    def add_item(self, it, count=1):
        self.inventory.setdefault(it, 0)
        self.inventory[it] += count

    def drop_item(self, it, count=1):
        c = self.inventory.setdefault(it, 0)
        if c >= count:
            self.inventory[it] -= count
            return True
        else:
            return False

    def game_loop(self):
        while True:
            action = input("What is your next action? ")
            if action == "Cut down a tree.":
                print("Cutting. Please wait...", end="", flush=True)
                time.sleep(10)
                print(" done. You got 5 wooden logs.")
                self.add_item("wooden log", count=5)
            elif action == "Open my inventory.":
                print("Inventory: {}".format(self.inventory))
            elif action == "Quit game.":
                sys.exit()
            elif action == "Jump off a cliff.":
                self.health = self.health - 4
                print("You lost 4 health points.")
            elif action == "Check my health.":
                print("Your health is " + str(self.health) + ".")
            elif action == "Up, up, down, down, left, right, left, right, b, a, start.":
                self.add_item("wooden log", 999)
                self.health = 999
                self.safeness = 999
                self.add_item("dead cave monster", 999)
                self.add_item("stone", 999)
                self.add_item("iron", 999)
                self.add_item("cheaters pass", 999)
                self.add_item("fire potion", 999)
                self.add_item("water potion", 999)
                self.add_item("air potion", 999)
                self.add_item("earth potion", 999)
                self.add_item("gold", 999)
                self.add_item("diamond", 999)
                print("You cheater! Okay, here. Have everything you'll ever need in this game.")
            elif action == "Build a starter house.":
                if self.drop_item("wooden log", 10):
                    print("Building. Please wait...", end="", flush=True)
                    time.sleep(10)
                    print(" done. You got 3 points safer.")
                    self.safeness = self.safeness + 3
                else:
                    print("You need 10 wooden logs to build this.")
            elif action == "Check my safeness.":
                print("Your safeness is " + str(self.safeness) + " points.")
            elif action == "Enter a nearby cave.":
                print("You entered a nearby cave.")
                time.sleep(random.randint(1, 25))
                event = random.randint(0, 19)
                if event in range(10):
                    damage = str(random.randint(1, 10))
                    print("You found a cave monster. Before you killed it, it did " + damage + " damage on you.")
                    self.add_item("dead cave monster")
                    self.add_item("stone", random.randint(1, 6))
                    self.health = self.health - damage
                elif event in range(11, 16):
                    print("You found some iron.")
                    self.add_item("iron", random.randint(1, 3))
                    self.add_item("stone", random.randint(1, 6))
                elif event in range(15, 18):
                    print("You found gold!")
                    self.add_item("gold")
                    self.add_item("stone", random.randint(1, 6))
                elif event == 18:
                    if self.drop_item("fire potion"):
                        print("You fell in lava, but luckily, you had a fire potion to survive.")
                    else:
                        print("You fell in lava and died.")
                        sys.exit()
                elif event == 19:
                    treasureRandomness = random.randint(0, 5)
                    if treasureRandomness == 0:
                        self.add_item("fire potion")
                        tresure = "fire potion"
                    elif tresureRandomness == 1:
                        self.add_item("water potion")
                        tresure = "water potion"
                    elif tresureRandomness == 2:
                        self.add_item("air potion")
                        tresure = "air potion"
                    elif tresureRandomness == 3:
                        self.add_item("earth potion")
                        tresure = "earth potion"
                    print("You found a " + treasure + ".")
                elif event == 20:
                    print("You found a diamond! How lucky!")
                    self.add_item("diamond")
            elif action == "Build a stone house.":
                if self.drop_item("wooden log", 5) and self.drop_item("stone", 10):
                    print("Building. Please wait...", end="", flush=True)
                    time.sleep(20)
                    print(" done. You got 8 points safer.")
                    self.safeness = self.safeness + 8
                else:
                    print("You need 5 wooden logs and 10 stones to build this.")
            elif action == "Build a stone wall.":
                if self.drop_item("wooden log", 1) and self.drop_item("stone", 20):
                    print("Building. Please wait...", end="", flush=True)
                    time.sleep(15)
                    print(" done. You got 15 points safer.")
                    self.safeness = self.safeness + 15
                else:
                    print("You need 1 wooden log and 10 stones to build this.")
            elif action == "Build an iron wall.":
                if self.drop_item("wooden log", 1) and self.drop_item("iron", 20):
                    print("Building. Please wait...", end="", flush=True)
                    time.sleep(20)
                    print(" done. You got 42 points safer.")
                    self.safeness = self.safeness + 42
                else:
                    print("You need 1 wooden log and 20 iron to build to build this.")
            elif action == "Build a gold wall.":
                if self.drop_item("wooden log", 1) and self.drop_item("gold", 20):
                    print("Building. Please wait...", end="", flush=True)
                    time.sleep(20)
                    print(" done. You got 112 points safer.")
                    self.safeness = self.safeness + 112
                else:
                    print("You need 1 wooden log and 20 gold to build this.")
            elif action == "Build a diamond wall.":
                if self.drop_item("wooden log", 1) and self.drop_item("diamond", 20):
                    print("Building. Please wait...", end="", flush=True)
                    time.sleep(20)
                    print(" done. You got 498 points safer.")
                    self.safeness = self.safeness + 498
                else:
                    print("You need 1 wooden log and 20 diamonds to build this.")
            elif action == "Build a forge.":
                if self.drop_item("wooden log", 8) and self.drop_item("stone", 15) and self.drop_item("iron", 25):
                    print("Building. Please wait...", end="", flush=True)
                    time.sleep(30)
                    print(" done. You got 74 points safer.")
                    self.safeness = self.safeness + 74
                else:
                    print("You need 5 wooden logs, 15 stones, and 25 iron to build this.")
            elif action == "Build a mansion.":
                if self.drop_item("wooden log", 40) and self.drop_item("stone", 30) and self.drop_item("iron", 50) and self.drop_item("gold", 69) and self.drop_item("diamond", 37):
                    print("Building. Please wait...", end="", flush=True)
                    time.sleep(150)
                    print(" done. You got 1234 points safer.")
                    self.safeness = self.safeness + 1234
                else:
                    print("You need 40 wooden logs, 30 stones, 50 iron, 69 gold, and 37 diamonds to build this.")
            elif action == "Build a bank.":
                if self.drop_item("wooden log", 10) and self.drop_item("stone", 50) and self.drop_item("iron", 36) and self.drop_item("gold", 60):
                    print("Building. Please wait...", end="", flush=True)
                    time.sleep(100)
                    print(" done. You got 763 points safer.")
                    self.safeness = self.safeness + 763
                else:
                    print("You need 10 wooden logs, 50 stones, 36 iron, and 60 gold to build this.")
            elif action == "Create a save code.":
                self.save_to_file("save.json")
            
            else:
                print("There is no action called '" + action + "', please check your spelling, grammar or maybe you can't do that in this game.")

            if self.health <= 0:
                print("You died.")
                sys.exit()


g = Game()
newOrOld = input("Do you want to continue an old game? ")
if newOrOld == "Yes.":
    g.load_from_file("save.json")
g.game_loop()
