import random
import names as name_gen

#This should all probably be in a class?
manager_level = 0 
day = 1
gold = 1000
days_to_rent = 6
rent_price = 100
monsters = {
    "goblins":[], 
    "orcs":[],
    "ogres": [],
    "dragons": []
    }

class Unit:
    """Unit class sets params for fired/dead- future functions to delete objects when either is set to true."""
    def __init__(self):
        pass
            


# Classes for all monster types
class Goblin(Unit):
    """Creates a goblin."""
    type = "Goblin"
    def __init__(self):
        super().__init__()
        self.max_health = 5
        self.current_health = self.max_health
        self.name = name_gen.goblin_names()
        self.gold_low = 0
        self.gold_high = 2
        self.injury_chance = 25

class Orc(Unit):
    """Creates an orc."""
    type = "Orc"
    def __init__(self):
        super().__init__()
        self.max_health = 15
        self.current_health = self.max_health
        self.name = name_gen.orc_names()
        self.gold_low = 1
        self.gold_high = 4
        self.injury_chance = 10

class Ogre(Unit):
    """Creates an ogre."""
    type = "Ogre"
    def __init__(self):
        super().__init__()
        self.max_health = 30
        self.current_health = self.max_health
        self.name = name_gen.ogre_names()
        self.gold_low = -10
        self.gold_high = 15
        self.injury_chance = 15

class Dragon(Unit):
    """Creates a dragon."""
    type = "Dragon"
    def __init__(self):
        super().__init__()
        self.max_health = 75
        self.current_health = self.max_health
        self.name = name_gen.dragon_names()
        self.gold_low = 20
        self.gold_high = 50
        self.injury_chance = 5
      

def game_start():
    """Launches the game."""
    print("Hello! Welcome to Dungeon Monster Manager! Ready to manage some monsters?")
    start_game = input("Do you want to (p)lay or go to (o)ptions?: ").strip().lower()
    if start_game == "p":
        pass
    elif start_game == "o":
        print("No options available") #options are a long time away; first iteration will probably be difficulty e.g. starting gold
        game_start()
    else:
        game_start() #loops back to the menu

def player_turn():
    """Provides insights and then runs turn_action function"""
    global days_to_rent
    global gold
    if days_to_rent == -1:
        days_to_rent = 6
    print("-----------------------")
    print(f"It is day {day}")
    print(f"You have {gold} gold")
    print(f"You have {len(monsters["goblins"])} goblins")
    print(f"You have {len(monsters["orcs"])} orcs")
    print(f"You have {len(monsters["ogres"])} ogres")
    print(f"You have {len(monsters["dragons"])} dragons")
    if days_to_rent != 0:
        print(f"You have {days_to_rent} days until rent is due!")
    else:
        print(f"Rent is due today! {rent_price} gold will be collected at the end of the day!")
    turn_action()


def turn_action():
    """Provides player choices and takes their input to go to the correct function."""
    choice = input("Would you like to (h)ire a monster, (f)ire a monster, or (e)nd the day?: ").strip().lower()
    if choice == "h":
        hire_monster()
    elif choice == "f":
        fire_monster()
    elif choice == "e":
        end_day()
    elif choice == 'test':
        for i in monsters:
            for j in monsters[i]:
                print(j.name)
        turn_action()

    else:
        print("That's not a valid input")
        turn_action()


def hire_monster():
    """Allows the player to hire monsters."""
    global gold
    print("-----------------------")
    print("Time to add more workers!")
    print(f"You have {gold} gold")
    print("Goblins cost 10 gold")
    print("Orcs cost 25 gold")
    print("Ogres cost 35 gold")
    print("Dragons cost 750 gold")
    choice = input("Would you like to hire a (g)oblin, (o)rc, og(r)e or (d)ragon? Type (b) to go back: ").strip().lower()
    if choice == "g":
        gold -= 10
        monsters["goblins"].append(Goblin())
        hire_monster()
    elif choice == "o":
        gold -= 25
        monsters["orcs"].append(Orc())
        hire_monster()
    elif choice == "r":
        gold -= 35
        monsters["ogres"].append(Ogre())
        hire_monster()
    elif choice == "d":
        gold -= 750
        monsters["dragons"].append(Dragon())
        hire_monster()
    elif choice == "b":
        player_turn()
    else:
        print("That's not a valid choice!")
        hire_monster()

def fire_monster():
    """Will allow the player to fire a monster, currently not working."""
    player_turn()


def end_day():
    """Ends the day, changing the day value, calculates/prints gold gain and potentially collecting/increasing rent."""
    global day
    global gold
    global days_to_rent
    global rent_price
    print(f"That is the end of day {day}")
    gold += get_gold()
    day += 1
    if days_to_rent == 0:
        gold = gold - rent_price
        rent_price += 50
        if gold < 0:
            print("You lose you fucking loser")
            quit()
    days_to_rent -= 1
    random_event()
    death_turn()   
    player_turn() 
    
def random_event():
    """
    
    """
    for i in monsters:
        if len(monsters[i]) == 0: #if threre are no monsters of a certain type, skips running it
            pass
        else:
            for j in monsters[i]:
                injury_roll = random.randint(1, 100)
                if injury_roll <= j.injury_chance:
                    damage_taken = random.randint(1, 10)
                    j.current_health -= damage_taken
                    print(f"{j.name} took {damage_taken} damage from a workplace injury!")
                    

def death_turn():
    for i in monsters:
        if len(monsters[i]) == 0: #if threre are no monsters of a certain type, skips running it
            pass
        else:
            for j in monsters[i]:
                if j.current_health <= 0:
                    print(f"{j.name} has died :(")
                    monsters[i].remove(j)

def get_gold():
    """Calculates gold for every monster and monster type, based one each individual monster's gold stats"""
    all_earned = 0
    for i in monsters:
        if len(monsters[i]) == 0: #if threre are no monsters of a certain type, does not tell you their gold generation
            pass
        else:
            type_earned = 0
            for j in monsters[i]:
                earned = random.randint(j.gold_low, j.gold_high)
                type_earned += earned
            print(f"Your {i} earned {type_earned} gold!")
            all_earned +=type_earned
    return all_earned

#starts the game, eventual plan to run game state without functions starting other functions.
if __name__ == "__main__":
    try:
        game_start()
        player_turn()
    except Exception as e:
        print(e)
        print("This didn't work but at least I didn't die")