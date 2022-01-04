import time
import sys

inventory = {}
health = 10

def have_item(it):
    return inventory.get(it, 0) > 0

def add_item(it, count=1):
    inventory.setdefault(it, 0)
    inventory[it] += count

while True:
    action = input("What is your next action? ")
    if action == "Cut down a tree.":
        print("Cutting. Please wait...", end="", flush=True)
        time.sleep(10)
        print(" done.")
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
        add_item("wooden log", 99)
        health = 99
        print("You cheater! Okay, here. Have evrything you need like ever in this game.")
    else:
        print("There is no action called " + action + ", please check your spelling, grammar or maybe you can't do that in the game.")
