import random


#This should all probably be in a class?
managerlevel = 0 
day = 1
gold = 1000
daystorent = 6
rentprice = 100
monsters = {
    "goblins":["Tony", "Chad", "Mikey"], 
    "orcs":["Bruk", "Druk"],
    "ogres": ["Meat"],
    "dragons": ["Sylvander"]
    } #Currently just keeping a few monsters in the lists for testing, game will start with them being empty

#global variables for total gold for each monster type- I need to figure out how to not need these
gobtotal = 0
orctotal = 0
ogretotal = 0
dragtotal = 0

#classes are not implemented yet, WIP
class Unit:
    def __init__(self, type, unithealth):
        self.type = type
        self.unithealth = unithealth

#Launches the game
def gamestart(begingame = False):
    print("Hello! Welcome to Dungeon Monster Manager! Ready to manage some monsters?")
    startgame = input("Do you want to (p)lay or go to (o)ptions?: ")
    if startgame == "p":
        pass
    elif startgame == "o":
        print("No options available") #options are a long time away; first iteration will probably be difficulty e.g. starting gold
        gamestart()
    else:
        gamestart() #loops back to the menu

#Main player turn, all players actions and info should flow through here
def playerturn():
    global daystorent
    global gold
    if daystorent == -1:
        daystorent = 6
    print("-----------------------")
    print(f"It is day {day}")
    print(f"You have {gold} gold")
    print(f"You have {len(monsters["goblins"])} goblins")
    print(f"You have {len(monsters["orcs"])} orcs")
    print(f"You have {len(monsters["ogres"])} ogres")
    print(f"You have {len(monsters["dragons"])} dragons")
    if daystorent != 0:
        print(f"You have {daystorent} days until rent is due!")
    else:
        print(f"Rent is due today! {rentprice} gold will be collected at the end of the day!")
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
    else:
        print("That's not a valid input")
        turnaction()

#allows the player to hire a monster
def hire_monster():
    playerturn()

#allows the player to fire a monster
def fire_monster():
    playerturn()

#ends the day, changing the day value, calculates/prints gold gain and potentially collecting rent
#Global vars used to update and then reset the values. I don't think the totals are actually needed as global since they should just be added to total, but I'd like to improve this anyway
def end_day():
    global day
    global daystorent
    global gobtotal
    global orctotal
    global ogretotal
    global dragtotal
    print(f"That is the end of day {day}")
    goldgain()
    for i in monsters:
        if len(monsters[i]) == 0: #if threre are no monsters of a certain type, does not tell you their gold generation
            pass
        else: #if you have monsters, tells you their daily gold generation
              #Is there a better way to loop this in case I have more monsters?
            if i == "goblins":
                print(f"Your {i} generated {gobtotal} gold today!")
            elif i == "orcs":
                print(f"Your {i} generated {orctotal} gold today!")
            elif i == "ogres":
                print(f"Your {i} generated {ogretotal} gold today!")
            elif i == "dragons":
                print(f"Your {i} generated {dragtotal} gold today!")
    gobtotal = 0
    orctotal = 0
    ogretotal = 0
    dragtotal = 0
    day += 1
    if daystorent == 0:
        global gold
        gold = gold - rentprice
    daystorent -= 1
    print()    
    playerturn() 

#Generates random gold per monster- is there a better way?
def goldgain():
    for i in monsters["goblins"]:
        global gobtotal
        gobgain = random.randint(0, 2)
        gobtotal = gobtotal + gobgain
    for i in monsters["orcs"]:
        global orctotal
        orcgain = random.randint(1, 4)
        orctotal = orctotal + orcgain
    for i in monsters["ogres"]:
        global ogretotal
        ogregain = random.randint(-10, 15)
        ogretotal = ogretotal + ogregain
    for i in monsters["dragons"]:
        global dragtotal
        draggain = random.randint(20, 50)
        dragtotal = dragtotal + draggain


#starts the game, eventual plan to run game state without functions starting other functions. I think gamestart has to be outside of this to work properly (once functions don't connect directly)?
gamestart()
if __name__ == "__main__":
    playerturn()