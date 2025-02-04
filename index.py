import random


#This should all probably be in a class?
managerlevel = 0 
day = 1
gold = 1000
days_to_rent = 6
rent_price = 100
monsters = {
    "goblins":[], 
    "orcs":[],
    "ogres": [],
    "dragons": []
    } #Currently just keeping a few monsters in the lists for testing, game will start with them being empty


#Unit class sets params for fired/dead- future functions to delete objects when either is set to true
class Unit:
    def __init__(self, fired=False, dead=False):

        self.is_fired = fired
        self.is_dead = dead

        if self.is_fired:
            pass
        if self.is_dead:
            pass

# Classes for all monster types
class Goblin(Unit):
    name = "Jasongob"
    type = "Goblin"
    max_health = 5
    current_health = max_health
    gold_low = 0
    gold_high = 2

class Orc(Unit):
    name = "Jasorc"
    type = "Orc"
    max_health = 15
    current_health = max_health
    gold_low = 1
    gold_high = 4

class Ogre(Unit):
    name = "Jasogre"
    type = "Ogre"
    max_health = 30
    current_health = max_health
    gold_low = -10
    gold_high = 15

class Dragon(Unit):
    name = "Jason eyes white dragon"
    type = "Dragon"
    max_health = 75
    current_health = max_health
    gold_low = 20
    gold_high = 50
      

#Launches the game
def gamestart():
    print("Hello! Welcome to Dungeon Monster Manager! Ready to manage some monsters?")
    start_game = input("Do you want to (p)lay or go to (o)ptions?: ")
    if start_game == "p":
        pass
    elif start_game == "o":
        print("No options available") #options are a long time away; first iteration will probably be difficulty e.g. starting gold
        gamestart()
    else:
        gamestart() #loops back to the menu

#Main player turn, all players actions and info should flow through here
def playerturn():
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
    turnaction()

#Gives the player their actions and takes in the input of their selected action and runs the correct function
def turnaction():
    choice = input("Would you like to (h)ire a monster, (f)ire a monster, or (e)nd the day?: ").strip().lower()
    if choice == "h":
        hire_monster()
    elif choice == "f":
        fire_monster()
    elif choice == "e":
        end_day()
    elif choice == 'test':
        getgold()
        turnaction()

    else:
        print("That's not a valid input")
        turnaction()

#allows the player to hire a monster
def hire_monster():
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
        playerturn()
    else:
        print("That's not a valid choice!")
        hire_monster()

#allows the player to fire a monster
def fire_monster():
    playerturn()

#ends the day, changing the day value, calculates/prints gold gain and potentially collecting rent
#Global vars used to update and then reset the values. I don't think the totals are actually needed as global since they should just be added to total, but I'd like to improve this anyway
def end_day():
    global day
    global gold
    global days_to_rent
    print(f"That is the end of day {day}")
    gold += getgold()
    day += 1
    if days_to_rent == 0:
        gold = gold - rent_price
        if gold < 0:
            print("You lose you fucking loser")
            gamestart()
    days_to_rent -= 1
    print()    
    playerturn() 
    
def getgold():
    allearned = 0
    for i in monsters:
        if len(monsters[i]) == 0: #if threre are no monsters of a certain type, does not tell you their gold generation
            pass
        else:
            typeearned = 0
            for j in monsters[i]:
                earned = random.randint(j.gold_low, j.gold_high)
                typeearned += earned
            print(f"Your {i} earned {typeearned} gold!")
            allearned +=typeearned
    return allearned

#starts the game, eventual plan to run game state without functions starting other functions.
if __name__ == "__main__":
    try:
        gamestart()
        playerturn()
    except Exception as e:
        print(e)
        print("This didn't work but at least I didn't die")