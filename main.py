#import the library for random to use functions that require random values
import random
#import the library for time for Python to count time
import time

#Function for the introduction of the story
def introduction():
    print("stranger: Wake up!")
    print("stranger: Are you dead?")
    # wait 2 seconds before continuing
    time.sleep(2)
    print("stranger: You ok? What’s your name?")

    #Get name of player
    name = input()
    time.sleep(1)
    print("stranger: Now, what’s the name of your village?")

    #Get name of village
    village = input()
    time.sleep(1)
    print("stranger: I am your best friend Johan :)")
    time.sleep(3)
    print(f"Johan: You almost reached our peaceful village {village}.")
    time.sleep(3)
    print("Johan: But somebody or something hit you in the head and you passed out for a while.")
    time.sleep(4)
    print("Johan: ...")
    time.sleep(2)
    print("Johan: Do you remember what's happening, Yes or No?")

    #Different NPC reactions for different user inputs
    ans = input()
    if ans.lower() == "yes":
        print("Johan: You look confused tho...Let me help you remember:")
    elif ans.lower() == "no":
        print("Johan: Here's what's happening:")
    else:
        print("...")

    time.sleep(3)
    print(f"Johan: {name}, you lived in {village} with your parents.")
    time.sleep(3)
    print("Johan: You and I were best friends, always doing tech and science shenanigans.")
    time.sleep(5)
    print("We both dreamed to advance in our studies of computer science and chemistry in the city.")
    time.sleep(5)
    print("One day, you were finally acknowledged and invited by a university in the city.")
    time.sleep(5)
    print("You went there for a few months, and are now visiting us again.")
    time.sleep(5)
    print("Let's go, they seem to be having a party at the village.")
    time.sleep(4)

    #Print funny list of strings that look like a running stickman
    print("    __O\n",
          "  / /\_,\n",
          "___/\\\n",
          "    /_ ")

    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("Almost there. Why does it look so bright?")
    time.sleep(2)
    print("    __O\n",
          "  / /\_,\n",
          "___/\\\n",
          "    /_ ")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("A FIRE!?!?")
    time.sleep(1)
    print("Quick, let's check out what's happening.")
    time.sleep(3)

    #List of dead people
    dead_people = ["Mrs. Smith", "Mr. Evan", "Mr. Sauce"]

    #Print dead people one by one every second
    for people in dead_people:
        print(people + "...")
        time.sleep(1)

    print("Everyone is dead...")
    time.sleep(2)
    print("You got any useful defense tools in your bag, YES or NO?")
    time.sleep(4)
    response = input()

    #Different NPC reactions for different user inputs
    if response.lower() == "yes":
        print("Let's see what you got there:")
        time.sleep(3)
    elif response.lower() == "no":
        print("At least you have a few things there:")
        time.sleep(3)
    else:
        print("Anyway, let's see what you got there:")
        time.sleep(3)

    #Items in bag
    bag = [
        "notebook",
        "metal bottle",
        "sandwich"
    ]

    #Print items in bag one by one
    for item in bag:
        print("-" + item)
        time.sleep(1)

    print("Here, I found some bandages and tape just in case.")
    time.sleep(3)

    #New items
    items = [
        "bandage",
        "tape"
    ]

    print("So now you have:")
    time.sleep(2)

    #Add items in bag and new items and print one by one
    inventory = bag + items
    for item in inventory:
        print("-" + item)
        time.sleep(1)

    print("...Here, let's pick up one of these weapons on the floor.")
    time.sleep(4)
    print("Choose a NUMBER: (1) machete, (2) axe, (3) scythe, (4) pickaxe")

    #Get player's choice of weapon and weapon's art
    def get_weapon():
        weapon = input()

        #Assign weapon picked by player according to their input number
        if weapon == "1":
            weapon = "machete"
            #Funny list of strings that look like text art of weach weapon
            weapon_art = (" _________ _______________________,",
                          "|_,-----,_).___________________.-’")
            return weapon, weapon_art
        elif weapon == "2":
            weapon = "axe"
            weapon_art = ("(>==============|====|=>",
                          "             .___|  |___.",
                          "              \ \____/ /",
                          "               `.____.’")
            return weapon, weapon_art
        elif weapon == "3":
            weapon = "scythe"
            weapon_art = ("(>========================|==|>",
                          "                          |  |",
                          "                          / ,’ ",
                          "                        <_.’")
            return weapon, weapon_art
        elif weapon == "4":
            weapon = "pickaxe"
            weapon_art = ("                    \`.",
                          "                     \\ \\",
                          "(>===================|==|>",
                          "                     / / ",
                          "                    /.’")
            return weapon, weapon_art
        #Run function again for invalid responses
        else:
            print("Choose a NUMBER from the list")
            get_weapon()

    #Call get_weapon() and return chosen weapon and weapon art
    weapon, weapon_art = get_weapon()

    time.sleep(1)
    print("Ok, so now you got:")
    time.sleep(2)

    #Add weapon to inventory
    inventory.append(weapon)
    for item in inventory:
        print(item)
        time.sleep(1)

    time.sleep(1)
    print("What's that moving thing?")
    time.sleep(3)
    print("ლ༼ ▀̿ Ĺ̯ ▀̿ ლ ༽")
    time.sleep(2)
    print('monster: "ROOAAHHRRR! ' + name.upper() + '!!!"')
    time.sleep(2)
    print("A MONSTER! It knows your name!?")
    time.sleep(3)
    print("It stole your mom's glasses!")
    time.sleep(3)
    print("Remember: ")
    time.sleep(2)
    print("press Enter to attack.")
    time.sleep(2)
    print("dodge attacks with 1, 40% chance of getting hit")
    time.sleep(4)
    print("block attacks with 2, but weapon health decreases")
    time.sleep(4)

    #Return useful variables to use outside of the function
    return name, village, weapon, weapon_art, inventory

#Get random Attack Damage between 5 and 10
def damage():
    return random.randint(5, 10)

#Get player's choice of defense
def defend():
    print("\nThe monster is attacking!")
    time.sleep(2)
    print("Choose your move: (1) Dodge, (2) Block")
    choice = input()
    return choice

#Main gameplay and storyline function
def main():
    #Starting HP of characters and weapon
    player_hp = 20
    monster_hp = 40
    weapon_hp = 20

    #Return useful variables from introduction() function for later use
    player_name, village_name, weapon_name, weapon_art, inventory_items = introduction()

    #Loop turn-based gameplay continuously as long as Player and Monster HP are above 0
    while player_hp > 0 and monster_hp > 0:
        print(f"\nYour HP: {player_hp} | Monster HP: {monster_hp} | Weapon HP: {weapon_hp}")
        time.sleep(5)
        print("Press ENTER to attack!")
        input()

        #Call damage() and assign the function's returned value to the player's damage
        player_damage = damage()

        #Subtract player's damage from the Monster's HP
        monster_hp -= player_damage

        #Print the "items" in the list of weapon's art one by one to look like the weapon
        for x in weapon_art:
            print(x)

        time.sleep(2)
        print(f"You use your {weapon_name} and deal {player_damage} damage!")
        time.sleep(3)

        #Ending of story triggered if Monster HP becomes less than or equal to 8
        if monster_hp <= 8:
            print("The monster is in pain.")
            time.sleep(2)
            print("It seems to have noticed something...")
            time.sleep(3)
            #More funny text art
            print(" ༽☉_☉༼")
            time.sleep(2)
            print('monster: "...J-Jo..."')
            time.sleep(2)
            print('monster: "JOHAN!!"')
            time.sleep(2)
            print('monster: "MONSTAAA!"')
            time.sleep(2)
            print(" ༽◺‸◿༼")
            time.sleep(2)
            print("\nPress ENTER to finish the monster!")
            input()

            #Print weapon art for final attack
            for x in weapon_art:
                print(x)

            time.sleep(2)
            print('monster: "AAARRRGGHHH!!!')
            time.sleep(2)
            print("Monster HP: 0")
            time.sleep(2)
            print(f'monster: "my child...Orproja..."')
            time.sleep(3)
            print(" ༽ಥ_ಥ༼")
            time.sleep(2)
            print('monster: "must...run..."')
            time.sleep(3)
            print('monster: "monster...Johan......"')
            time.sleep(3)

            #Text art simulating heartbeat
            print("     /\    /\     ",
                  "\n____/  \  /  \  ______",
                  "\n        \/    \/")
            time.sleep(2)
            print("     /\    /\     ",
                  "\n____/  \  /  \  ______",
                  "\n        \/    \/")
            time.sleep(2)
            print("           ",
                  "\n_________________________",
                  "\n         ")
            time.sleep(2)

            print('The "monster" passes away, with tears of anguish and concern...')
            time.sleep(3)
            print("TO BE CONTINUED...")
            time.sleep(2)

            #End the code
            break

        #Call defend() and return user's choice of defense
        move = defend()

        #Dodge if player's input is 1
        if move == "1":
            #Get random float number between 0.0 and 1.0
            dodge_chance = random.random()

            #Dodge success if random number is equal or less than 0.6 (60% chance)
            if dodge_chance <= 0.6:
                print("You dodged the monster's attack!")
                time.sleep(2)
                #Continue code
                continue
            #Dodge failed for any other random number (40% chance)
            else:
                #Call damage() and assign the function's returned value to the monster's damage
                monster_damage = damage()
                #Subtract monster's damage from the Player's HP
                player_hp -= monster_damage
                print(f"You failed to dodge and received {monster_damage} damage!")
                time.sleep(2)

        #Block if player input is 2
        elif move == "2":
            #Weapon health decreases by 5 when blocking
            weapon_hp -= 5

            #End battle and story if Weapon HP become equal or less than 0
            if weapon_hp <= 0:
                print("Your weapon breaks! You receive an undodgeable blow and lose.")
                time.sleep(3)
                print("Next time, stop the skill issues, and don't break your weapon.")
                #End the code
                break
            #Block success
            else:
                print("You block the monster's attack with your weapon!")
                time.sleep(3)
                print("But your weapon has been damaged!")
                time.sleep(2)

        #Player stand still if input is invalid
        else:
            print("Invalid move. You stand still.")
            time.sleep(2)
            monster_damage = damage()
            player_hp -= monster_damage
            print(f"You got hit and received {monster_damage} damage!")
            time.sleep(3)

        if player_hp <= 10 and "bandage" in inventory_items:
            print("You're bleeding a lot!")
            time.sleep(2)
            print("Press ENTER to use your bandages and heal!")
            input()
            time.sleep(2)
            player_hp += 10
            print("You recover 10 HP.")
            inventory_items.remove("bandage")
            print("Inventory left:")
            time.sleep(1)
            for x in inventory_items:
                print(x)
                time.sleep(1)
            time.sleep(1)

        if player_hp <= 0:
            print("Do you...")
            time.sleep(1)
            print("perhaps...")
            time.sleep(1)
            print("Have skill issues?")
            time.sleep(2)
            print("I guess reincarnating you wasn't a good idea...")
            time.sleep(3)
            print("Try again!")
            time.sleep(1)
            break

if __name__ == "__main__":
    main()