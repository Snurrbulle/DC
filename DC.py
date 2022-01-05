import time
import sys
import random
import json

def say(it):
    print(it)
    time.sleep(2.4563456)

def say_pause_say(first, pause_sec, second):
    print(first, end="", flush=True)
    time.sleep(pause_sec)
    print(second)

def ask(it):
    c = input(it)
    time.sleep(2.4563456)
    return c

class Game:
    def __init__(self):
        self.inventory = {}
        self.health = 10
        self.safeness = 0
        self.points = 0
        self.name = 0
        self.has_seen_intro = False

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            json.dump({"inventory": self.inventory, "health": self.health,
                       "safeness": self.safeness, "points": self.points,
                       "name": self.name, "has_seen_intro": self.has_seen_intro},
                      f, indent=True, sort_keys=True)

    def load_from_file(self, filename):
        with open(filename) as f:
            j = json.load(f)
        self.inventory = j["inventory"]
        self.health = j["health"]
        self.safeness = j["safeness"]
        self.points = j["points"]

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
        if not self.has_seen_intro:
            say("?1: Hello.")
            say("?1: My name is Kasper.")
            say("Kasper: Kasper Margit.")
            self.name = ask("Kasper: What's your name? ")
            say("Kasper: Hi, " + self.name + ".")
            say("Kasper: I just found you here.")
            say("Kasper: But you are not ready yet.")
            say("Kasper: I will put you in another world, where you'll be all alone.")
            say("Kasper: Survive to prove yourself ready.")
            say("Kasper: Return here when you have 5000 safeness and 7500 points.")
            say("Kasper: Bye for now.")
            self.has_seen_intro = True
        while True:
            action = ask("What is your next action? ")
            if action == "Cut down a tree.":
                say_pause_say("Cutting. Please wait...", 10, " done. You got 5 wooden logs.")
                self.add_item("wooden log", count=5)
                self.points = self.points + 5
            elif action == "Open my inventory.":
                say("Inventory: {}".format(self.inventory))
            elif action == "Quit game.":
                save_to_file("save.")
                sys.exit()
            elif action == "Jump off a cliff.":
                self.health = self.health - 4
                say("You lost 4 health points.")
            elif action == "Check my health.":
                say("Your health is " + str(self.health) + ".")
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
                self.points = 999
                say("You cheater! Okay, here. Have everything you'll ever need in this game.")
            elif action == "Build a starter house.":
                if self.drop_item("wooden log", 10):
                    say_pause_say("Building. Please wait...", 10, " done. You got 3 points safer.")
                    self.safeness = self.safeness + 3
                    self.points = self.points + 10
                else:
                    say("You need 10 wooden logs to build this.")
            elif action == "Check my safeness.":
                say("Your safeness is " + str(self.safeness) + " points.")
            elif action == "Enter a nearby cave.":
                say("You entered a nearby cave.")
                self.points = self.points + 10
                time.sleep(random.randint(1, 25))
                event = random.randint(0, 19)
                if event in range(10):
                    damage = str(random.randint(1, 10))
                    say("You found a cave monster. Before you killed it, it did " + damage + " damage on you.")
                    self.add_item("dead cave monster")
                    self.add_item("stone", random.randint(1, 6))
                    self.health = self.health - damage
                elif event in range(11, 16):
                    say("You found some iron.")
                    self.add_item("iron", random.randint(1, 3))
                    self.add_item("stone", random.randint(1, 6))
                elif event in range(15, 18):
                    say("You found gold!")
                    self.add_item("gold")
                    self.add_item("stone", random.randint(1, 6))
                elif event == 18:
                    if self.drop_item("fire potion"):
                        say("You fell in lava, but luckily, you had a fire potion to survive.")
                    else:
                        say("You fell in lava and died.")
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
                    say("You found a " + treasure + ".")
                elif event == 20:
                    say("You found a diamond! How lucky!")
                    self.add_item("diamond")
            elif action == "Build a stone house.":
                if self.drop_item("wooden log", 5) and self.drop_item("stone", 10):
                    say_pause_say("Building. Please wait...", 20, " done. You got 8 points safer.")
                    self.safeness = self.safeness + 8
                    self.points = self.points + 15
                else:
                    say("You need 5 wooden logs and 10 stones to build this.")
            elif action == "Build a stone wall.":
                if self.drop_item("wooden log", 1) and self.drop_item("stone", 20):
                    say_pause_say("Building. Please wait...", 15, " done. You got 15 points safer.")
                    self.safeness = self.safeness + 15
                    self.points = self.points + 15
                else:
                    say("You need 1 wooden log and 10 stones to build this.")
            elif action == "Build an iron wall.":
                if self.drop_item("wooden log", 1) and self.drop_item("iron", 20):
                    ("Building. Please wait...", 20, " done. You got 42 points safer.")
                    self.safeness = self.safeness + 42
                    self.points = self.points + 43
                else:
                    say("You need 1 wooden log and 20 iron to build to build this.")
            elif action == "Build a gold wall.":
                if self.drop_item("wooden log", 1) and self.drop_item("gold", 20):
                    say_pause_say("Building. Please wait...", 20, " done. You got 112 points safer.")
                    self.safeness = self.safeness + 112
                    self.points = self.points + 123
                else:
                    say("You need 1 wooden log and 20 gold to build this.")
            elif action == "Build a diamond wall.":
                if self.drop_item("wooden log", 1) and self.drop_item("diamond", 20):
                    say_pause_say("Building. Please wait...", 35, " done. You got 498 points safer.")
                    self.safeness = self.safeness + 498
                    self.points = self.points + 500
                else:
                    say("You need 1 wooden log and 20 diamonds to build this.")
            elif action == "Build a forge.":
                if self.drop_item("wooden log", 8) and self.drop_item("stone", 15) and self.drop_item("iron", 25):
                    say_pause_say("Building. Please wait...", 30, " done. You got 74 points safer.")
                    self.safeness = self.safeness + 74
                    self.points = self.points + 43
                else:
                    say("You need 5 wooden logs, 15 stones, and 25 iron to build this.")
            elif action == "Build a mansion.":
                if self.drop_item("wooden log", 40) and self.drop_item("stone", 30) and self.drop_item("iron", 50) and self.drop_item("gold", 69) and self.drop_item("diamond", 37):
                    say_pause_say("Building. Please wait...", 150, " done. You got 1234 points safer.")
                    self.safeness = self.safeness + 1234
                    self.points = self.points + 500
                else:
                    say("You need 40 wooden logs, 30 stones, 50 iron, 69 gold, and 37 diamonds to build this.")
            elif action == "Build a bank.":
                if self.drop_item("wooden log", 10) and self.drop_item("stone", 50) and self.drop_item("iron", 36) and self.drop_item("gold", 60):
                    say_pause_say("Building. Please wait...", 100, " done. You got 763 points safer.")
                    self.safeness = self.safeness + 763
                    self.points = self.points + 123
                else:
                    say("You need 10 wooden logs, 50 stones, 36 iron, and 60 gold to build this.")
            elif action == "Save to save file.":
                self.save_to_file("save.json")
                say("Saved your game state to 'save.json'")
            elif action == "Seach for a Danscupcaken core.":
                say_pause_say("Seaching. Please wait...", 20, " done. You got a Danscupcaken core.")
                self.add_item("Danscupcaken core.")
            elif action == "Build a Danscupcaken statue.":
                if drop_item("Danscupcaken core") and drop_item("stone", 8):
                    say_pause_say("Building. Please wait...", 20, " done. You got 9 points safer.")
                    safeness = safeness + 9
                    points = points + 10
                else:
                    say("You need 1 Danscupcaken core and 8 stones to build this.")
            else:
                say("There is no action called '" + action + "', please check your spelling, grammar or maybe you can't do that in this game.")
                
            if self.health <= 0:
                say("You died.")
                sys.exit()

g = Game()
newOrOld = ask("Do you want to continue an old game? ")
if newOrOld == "Yes.":
    g.load_from_file("save.json")
g.game_loop()
