import time
import sys
import random

inventory = {}
health = 10
safeness = 0
points = 0

def have_item(it):
    return inventory.get(it, 0) > 0

def add_item(it, count=1):
    inventory.setdefault(it, 0)
    inventory[it] += count

def drop_item(it, count=1):
    c = inventory.setdefault(it, 0)
    if c >= count:
        inventory[it] -= count
        return True
    else:
        return False

while True:
    action = input("What is your next action? ")
    if action == "Cut down a tree.":
        print("Cutting. Please wait...", end="", flush=True)
        time.sleep(10)
        print(" done. You got 5 wooden logs.")
        add_item("wooden log", count=5)
        points = points + 5
    elif action == "Open my inventory.":
        print("Inventory: {}".format(inventory))
    elif action == "Quit game.":
        sys.exit()
    elif action == "Jump off a cliff.":
        health = health - 4
        print("You lost 4 health points.")
    elif action == "Check my health.":
        print("Your health is " + str(health) + ".")
    elif action == "Up, up, down, down, left, right, left, right, b, a, start.":
        add_item("wooden log", 999)
        health = 999
        safeness = 999
        add_item("dead cave monster", 999)
        add_item("stone", 999)
        add_item("iron", 999)
        add_item("cheaters pass", 999)
        add_item("fire potion", 999)
        add_item("water potion", 999)
        add_item("air potion", 999)
        add_item("earth potion", 999)
        add_item("gold", 999)
        add_item("diamond", 999)
        points = 999
        add_item("Danscupcaken core", 999)
        print("You cheater! Okay, here. Have everything you'll ever need in this game.")
    elif action == "Build a starter house.":
        if drop_item("wooden log", 10):
            print("Building. Please wait...", end="", flush=True)
            time.sleep(10)
            print(" done. You got 3 points safer.")
            safeness = safeness + 3
            points = points + 10
        else:
            print("You need 10 wooden logs to build this.")
    elif action == "Check my safeness.":
        print("Your safeness is " + str(safeness) + " points.")
    elif action == "Enter a nearby cave.":
        print("You entered a nearby cave.")
        time.sleep(random.randint(1, 25))
        event = random.randint(0, 19)
        if event in range(10):
            damage = str(random.randint(1, 10))
            print("You found a cave monster. Before you killed it, it did " + damage + " damage on you.")
            add_item("dead cave monster")
            add_item("stone", random.randint(1, 6))
            health = health - damage
            points = points + 7
        elif event in range(11, 16):
            print("You found some iron.")
            add_item("iron", random.randint(1, 3))
            add_item("stone", random.randint(1, 6))
            points = points + 12
        elif event in range(15, 18):
            print("You found gold!")
            add_item("gold")
            add_item("stone", random.randint(1, 6))
            points = points + 24
        elif event == 18:
            if drop_item("fire potion"):
                print("You fell in lava, but luckily, you had a fire potion to survive.")
            else:
                print("You fell in lava and died.")
                sys.exit()
        elif event == 19:
            treasureRandomness = random.randint(0, 5)
            if treasureRandomness == 0:
                add_item("fire potion")
                tresure = "fire potion"
            elif tresureRandomness == 1:
                add_item("water potion")
                tresure = "water potion"
            elif tresureRandomness == 2:
                add_item("air potion")
                tresure = "air potion"
            elif tresureRandomness == 3:
                add_item("earth potion")
                tresure = "earth potion"
            print("You found a " + treasure + ".")
            points = points + 34
        elif event == 20:
            print("You found a diamond! How lucky!")
            add_item("diamond")
            points = points + 35
    elif action == "Build a stone house.":
        if drop_item("wooden log", 5) and drop_item("stone", 10):
            print("Building. Please wait...", end="", flush=True)
            time.sleep(20)
            print(" done. You got 8 points safer.")
            safeness = safeness + 8
            points = points + 9
        else:
            print("You need 5 wooden logs and 10 stones to build this.")
    elif action == "Build a stone wall.":
        if drop_item("wooden log", 1) and drop_item("stone", 20):
            print("Building. Please wait...", end="", flush=True)
            time.sleep(15)
            print(" done. You got 15 points safer.")
            safeness = safeness + 15
            points = points + 9
        else:
            print("You need 1 wooden log and 10 stones to build this.")
    elif action == "Build an iron wall.":
        if drop_item("wooden log", 1) and drop_item("iron", 20):
            print("Building. Please wait...", end="", flush=True)
            time.sleep(20)
            print(" done. You got 42 points safer.")
            safeness = safeness + 42
            points = points + 42
        else:
            print("You need 1 wooden log and 20 iron to build to build this.")
    elif action == "Build a gold wall.":
        if drop_item("wooden log", 1) and drop_item("gold", 20):
            print("Building. Please wait...", end="", flush=True)
            time.sleep(20)
            print(" done. You got 112 points safer.")
            safeness = safeness + 112
            points = points + 113
        else:
            print("You need 1 wooden log and 20 gold to build this.")
    elif action == "Build a diamond wall.":
        if drop_item("wooden log", 1) and drop_item("diamond", 20):
            print("Building. Please wait...", end="", flush=True)
            time.sleep(20)
            print(" done. You got 498 points safer.")
            safeness = safeness + 498
            points = points + 500
        else:
            print("You need 1 wooden log and 20 diamonds to build this.")
    elif action == "Build a forge.":
        if drop_item("wooden log", 8) and drop_item("stone", 15) and drop_item("iron", 25):
            print("Building. Please wait...", end="", flush=True)
            time.sleep(30)
            print(" done. You got 74 points safer.")
            safeness = safeness + 74
            points = points + 42
        else:
            print("You need 5 wooden logs, 15 stones, and 25 iron to build this.")
    elif action == "Build a mansion.":
        if drop_item("wooden log", 40) and drop_item("stone", 30) and drop_item("iron", 50) and drop_item("gold", 69) and drop_item("diamond", 37):
            print("Building. Please wait...", end="", flush=True)
            time.sleep(150)
            print(" done. You got 1234 points safer.")
            safeness = safeness + 1234
            points = points + 500
        else:
            print("You need 40 wooden logs, 30 stones, 50 iron, 69 gold, and 37 diamonds to build this.")
    elif action == "Build a bank.":
        if drop_item("wooden log", 10) and drop_item("stone", 50) and drop_item("iron", 36) and drop_item("gold", 60):
            print("Building. Please wait...", end="", flush=True)
            time.sleep(100)
            print(" done. You got 763 points safer.")
            safeness = safeness + 763
            points = points + 113
        else:
            print("You need 10 wooden logs, 50 stones, 36 iron, and 60 gold to build this.")
    elif action == "Check my level.":
        print("You have " + str(points) +  ".")
    elif action == "Seach for a Danscupcaken core."
        print("Seaching. Please wait...", end="", flush=True)
        time.sleep(20)
        print(" done. You got a Danscupcaken core.")
        self.add_item("Danscupcaken core.")
    elif action == "Build a Danscupcaken statue.":
        if drop_item("Danscupcaken core") and drop_item("stone", 8):
            print("Building. Please wait...", end="", flush=True)
            time.sleep(20)
            print(" done. You got 9 points safer.")
            safeness = safeness + 9
            points = points + 10
        else:
            print("You need 1 Danscupcaken core and 8 stones to build this.")
            
    else:
        print("There is no action called '" + action + "', please check your spelling, grammar or maybe you can't do that in this game.")

    if health <= 0:
        print("You died.")
        sys.exit()
