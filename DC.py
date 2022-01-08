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
    print(it, end="", flush=True)
    c = input("")
    return c

class Game:
    def __init__(self):
        self.inventory = {}
        self.health = 10
        self.safeness = 0
        self.points = 0
        self.name = 0
        self.has_seen_intro = False
        self.has_been_back_to_kasper = False
        self.has_danscupcaken_statue = False
        self.has_seen_danscupcaken = False
        self.have_team_temple = False
        self.team = "none yet"
        self.has_seen_snurrbulle = False
        self.hate_kasper = False

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            json.dump({"inventory": self.inventory, "health": self.health,
                       "safeness": self.safeness, "points": self.points,
                       "name": self.name, "has_seen_intro": self.has_seen_intro,
                       "has_been_back_to_kasper": self.has_been_back_to_kasper,
                       "has_danscupcaken_statue": self.has_danscupcaken_statue,
                       "has_seen_danscupcaken": self.has_seen_danscupcaken,
                       "have_team_temple": self.have_team_temple,
                       "team": self.team, "has_seen_snurrbulle":
                       self.has_seen_snurrbulle, "hate_kasper": self.hate_kasper},
                      f, indent=True, sort_keys=True)

    def load_from_file(self, filename):
        try:
            with open(filename) as f:
                j = json.load(f)
        except (OSError, json.decoder.JSONDecodeError) as e:
            print(f"Failed to load saved game: {e}")
            sys.exit()
        self.inventory = j.get("inventory", {})
        self.health = j.get("health", 10)
        self.safeness = j.get("safeness", 0)
        self.points = j.get("points", 0)
        self.name = j.get("name", "Player")
        self.has_seen_intro = j.get("has_seen_intro", False)
        self.has_been_back_to_kasper = j.get("has_been_back_to_kasper", False)
        self.has_danscupcaken_statue = j.get("has_danscupcaken_statue", False)
        self.has_seen_danscupcaken = j.get("has_seen_danscupcaken", False)
        self.have_team_temple = j.get("have_team_temple", False)
        self.team = j.get("team", "none yet")
        self.has_seen_snurrbulle = j.get("has_seen_snurrbulle", False)
        self.hate_kasper = j.get("hate_kasper", False)

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

    def back_to_kasper(self):
        say("Kasper: Hello.")
        if not self.has_been_back_to_kasper:
            say("Kasper: You have proved yoursef ready, by getting 7500 points and 5000 safeness without dying.")
            say("Kasper: Until this day, you have been mortal.")
            say("Kasper: I will now give you a respawn orb.")
            say("Kasper: You are now part of the imortals.")
            self.add_item("respawn orb")
            self.team = "the immortals"
            say("Kasper: Bye!")
        else:
            say("Kasper: I don't have time for you right now.")
            say("Kasper: See you later.")
        self.game_loop()

    def kill_player(self):
        if have_item("respawn orb"):
            say("You respawned.")
            inventory = {}
            self.add_item("respawn orb")
            self.add_item("cell phone")
            health = 10
            points = 0
        else:
            say("You died and lost all of your progress.")
            self.inventory = {}
            self.health = 10
            self.safeness = 0
            self.points = 0
            self.name = 0
            self.has_seen_intro = False
            self.has_been_back_to_kasper = False
            self.has_seen_snurrbulle = False
            self.has_danscupcaken_statue = False
            self.team = "none yet"
            self.have_team_temple = False
            self.hate_kasper = False
        game_loop()

    def meet_danscupcaken(self):
        if not self.has_seen_danscupcaken:
            say("?2: Hello, my name is Danscupcaken.")
            say("Danscupcaken: I am a member of the immortals.")
            saidName = ask("Danscupcaken: What is your name? ")
            if not saidName == self.name:
                say("Danscupcaken: Nah, I know you real name.")
                say(f"Danscupcaken: Kasper told me that it's {self.name}.")
            ask("Danscupcaken: What did you want to tell me, anyways? ")
            say("Danscupcaken: Whatever, I don't have time for you anyways.")
            say("Danscupcaken: Bye bye.")
        else:
            say("Danscupcaken: I don't have time for you now either.")
            say("Danscupcaken: Bye bye.")
        game_loop()

    def damage_player(self, damage):
        self.health = self.health - damage
        if self.health <= 0:
            kill_player()

    def meet_snurrbulle(self):
        say("Snurrbulle: Hello, fellow being.")
        if not self.has_seen_snurrbulle:
            saidTeam = ask("Snurrbulle: Which team are you on? ")
            if not saidTeam == self.team:
                say("Snurrbulle: You look more like a " + self.team + ".")
            say("Snurrbulle: I'm a god.")
            say("Snurrbulle: And I know that you do not belong to this realm.")
            say("Snurrbulle: None of the worlds.")
        else:
            say("Snurrbulle: Hello, fellow being.")
        if self.team == "the immortals":
            say("Kasper: That can't be true.")
            say("Snurrbulle: Kasper, how many times must I tell you to not use your team leader powers to eavesdrop on me?")
            say("Kasper: Sorry, Snurrbulle.")
            say("Snurrbulle: For you who probably don't understand this right now, " + self.name + "...")
            say("Kasper: Team leaders can travel between worlds without calling for their owners.")
            say("Snurrbulle: Yeah.")
            say("Kasper: But how isn't " + self.name + " from this realm?")
            say("Kasper: I though other realms was just a fairy tale.")
            say("Snurrbulle: I though so too, until I saw a portal to one.")
            say("Snurrbulle: It was 2 years ago.")
            say("Snurrbulle: I was doing stuff in my world 'til a portal opened up.")
            say("Snurrbulle: And somone got thrown out of it.")
            say("Kasper: Was it " + self.name + "?")
            say("Snurrbulle: Yes.")
            say("Kasper ran away from this world.")
            say("Your phone says 'emergency meeting @ my place - Kasper'.")
            say("Snurrbulle: But it was supposed to be a secret...")
            say("You got over to Kaspers world.")
            say("Kasper: Snurrbulle said that " + self.name + " was from another dimension.")
            say("Kapser: We got to kick them out.")
            say("Danscupcaken: That can't be true.")
            say("NerdyNerd: Well, that's true.")
            say("Danscupcaken: I didn't go here for fairy tales!")
            say("NerdyNerd: Me neither!")
            say("Kasper: Okay, okay.")
            say("The guests start to move towards the exit.")
            say("NerdyNerd: Don't listen to Kasper.")
            say("Danscupcaken: Yeah, he's a big liar.")
            say("You all went home.")
            self.hate_kasper = True
        else:
            say("Snurrbulle: But it's not a big thing.")
            say("Bye, fellow being.")
        self.game_loop()


    def game_loop(self):
        if not self.has_seen_intro:
            say("?1: Hello.")
            say("?1: My name is Kasper.")
            say("Kasper: Kasper Margit.")
            self.name = ask("Kasper: What's your name? ")
            say(f"Kasper: Hi, {self.name}.")
            say("Kasper: I just found you here.")
            say("Kasper: But you are not ready yet.")
            say("Kasper: I will put you in another world, where you'll be all alone.")
            say("Kasper: Survive to prove yourself ready.")
            say("Kasper: Return here when you have 5000 safeness and 7500 points.")
            say("Kasper: Here, take a cell phone.")
            self.add_item("cell phone")
            say("Kasper: Bye for now.")
            self.has_seen_intro = True

        while True:
            action = ask("What is your next action? ")
            if action == "Cut down a tree.":
                say_pause_say("Cutting. Please wait...", 10, " done. You got 5 wooden logs.")
                self.add_item("wooden log", count=5)
                self.points = self.points + 5
            elif action == "Open my inventory.":
                say(f"Inventory: {self.inventory}")
            elif action == "Quit game.":
                self.save_to_file("save.json")
                sys.exit()
            elif action == "Jump off a cliff.":
                self.damage_player(4)
                say("You lost 4 health points.")
            elif action == "Check my health.":
                say(f"Your health is {self.health}.")
            elif action == "Up, up, down, down, left, right, left, right, b, a, start.":
                much = 999 * 999
                self.add_item("wooden log", much)
                self.health = much
                self.safeness = much
                self.add_item("dead cave monster", much)
                self.add_item("stone", much)
                self.add_item("iron", much)
                self.add_item("cheaters pass", much)
                self.add_item("fire potion",much)
                self.add_item("water potion", much)
                self.add_item("air potion", much)
                self.add_item("earth potion", much)
                self.add_item("gold", much)
                self.add_item("diamond", much)
                self.points = much
                self.add_item("respawn orb", much)
                self.add_item("Dancupcaken core", much)
                say("You cheater! Okay, here. Have everything you'll ever need in this game.")
            elif action == "Build a starter house.":
                if self.drop_item("wooden log", 10):
                    say_pause_say("Building. Please wait...", 10, " done. You got 3 points safer.")
                    self.safeness = self.safeness + 3
                    self.points = self.points + 10
                else:
                    say("You need 10 wooden logs to build this.")
            elif action == "Check my safeness.":
                say(f"Your safeness is {self.safeness} points.")
            elif action == "Enter a nearby cave.":
                say("You entered a nearby cave.")
                self.points = self.points + 10
                time.sleep(random.randint(1, 25))
                event = random.randint(0, 19)
                if event in range(10):
                    damage = random.randint(1, 10)
                    self.damage_player(damage)
                    say(f"You found a cave monster. Before you killed it, it did {damage} damage on you.")
                    self.add_item("dead cave monster")
                    self.add_item("stone", random.randint(1, 6))
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
                        kill_player()
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
                    say(f"You found a {treasure}.")
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
            elif action == "Save game.":
                self.save_to_file("save.json")
                say("Saved your game state to 'save.json'")
            elif action == "Search for a Danscupcaken core.":
                say_pause_say("Searching. Please wait...", 20, " done. You got a Danscupcaken core.")
                self.add_item("Danscupcaken core", 1)
            elif action == "Build a Danscupcaken statue.":
                if self.drop_item("Danscupcaken core") and self.drop_item("stone", 8):
                    say_pause_say("Building. Please wait...", 20, " done. You got 9 points safer.")
                    self.has_danscupcaken_statue = True
                    self.safeness = safeness + 9
                    self.points = points + 10
                else:
                    say("You need 1 Danscupcaken core and 8 stones to build this.")
            elif action == "Call for Kasper.":
                if self.points >= 7500 and self.safeness >= 5000:
                    self.back_to_kasper()
                else:
                    say("Nothing happned.")
            elif action == "Call for Danscupcaken.":
                if self.has_danscupcaken_statue:
                    self.meet_danscupcaken()
                else:
                    say("Nothing happened.")
            elif action == "Build a temple of the immortals.":
                if drop_item("stone", 99) and drop_item("diamond", 10) and have_item("respawn orb") and not have_team_temple:
                    say_pause_say("Building. Please wait...", 42, " done. You got 3500 points safer.")
                    self.points = points + 1
                    self.safeness = safeness + 3500
                    self.have_team_temple = True
                else:
                    say("You need 99 stones, 10 diamonds and a immortals membership to build this. And you can only build one.")
            elif action == "Load game.":
                say("You will now load another game state.")
                self.load_from_file("save.json")
            elif action == "Call for Snurrbulle.":
                if not self.have_item("cheaters pass"):
                    self.meet_snurrbulle()
                else:
                    say("Snurrbulle: You are just a cheater.")
                    say("Snurrbulle: Never disturb me ever again.")
            else:
                say(f"There is no action called {action!r}, please check your spelling, grammar or maybe you can't do that in this game.")

g = Game()
newOrOld = ask("Do you want to continue an old game? ")
if newOrOld == "Yes.":
    g.load_from_file("save.json")
g.game_loop()
