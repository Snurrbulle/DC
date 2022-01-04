import time
import sys

inventory = {}
health = 10
safeness = 0

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
        print("You cheater! Okay, here. Have evrything you need like ever in this game.")
    elif action == "Build a starter house.":
        if drop_item("wooden log", 10):
            print("Building. Please wait...", end="", flush=True)
            time.sleep(10)
            print(" done. You got 3 points safer.")
            safeness = safeness + 3
        else:
            print("You need 10 wooden logs to build this.")
    elif action == "Check my safeness.":
        print("Your safeness is " + str(safeness) + " points.")
    else:
        print("'There is no action called '" + action + "', please check your spelling, grammar or maybe you can't do that in the game.")

    if health <= 0:
        print("You died.")
        sys.exit()
