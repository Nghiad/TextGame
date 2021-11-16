from screens import *
from valueinput import *
from ASCII import *
from battle import *
from dialogue import *
from future import *
from present import *

#Assignments
options = ['attack', 'block' ,'stats', 'backpack', 'use']
inventory = ['left fist', 'right fist', 'rags']
items = ['rock', 'potion', 'great potion']
weapons = ['stick', 'knife', 'sword', 'great Sword']
armors = ['garbage lid', 'shield', 'knee pads', 'iron Armor', 'dark armor']
wrong = 'Invalid input, please choose an option.'
manual = "The game is designed to showcase mechanics done in python without the use of modules. All code has been written by myself excluding the ASCII art,\
which were obtained from various royalty-free sources. This game will be improved upon as more features and fixes will be patched in.\
For hard mode, when prompt for a value; input '666' (*hard mode has not been extensively tested*)."

#Player Outcome
boy = 'alive'
friendship = 'good'
timetravel = False
difficulty = 'normal'

#Extras
code = 182581
ending = 'N/A'
secret_wait = False
secret_glasses = False
secret_code = False

#Player Stats
hp = 20
attackdmg = 3
armor = 0
gold = 0

#Enemy Stats
enemy_name = 'the boy'
enemy_hp = 8
enemy_dmg = 2
enemy_weapon = 'stick'

#Misc assignments
turn = 'charging'
confronted = False
talked = False
trash_lid = False
barn_rock = False
temple = False

if __name__=="__main__":
    start_screen()

    print ("This is a simple text-based adventure game. The game only require a keyboard for input. To proceed through the dialogue and menus,\
    press enter. When asked for an input, the game will display all the available options; dialogue options will be a number. This game does not have a saving\
    feature and will take about 10 minutes. Don't worry, the game is designed to be easy.")
    input ()
    while True:
        print ()
        answer = input("Would you like to read the manual? (yes/no) ")
        if answer == 'yes':
            print (manual)
            input ()
            break
        
        elif answer == 'no':
            break
        
        else:
            print ()
            print (wrong)
    print ()
    print ()
    print ("Alright before we get started, I just need your name and a friend's name.")
    print () 
    player_name = input("What is your name? ").strip()
    print ()
    friend = input("Who is your friend? ").strip()
    print ()
    print ()
    print ("Alright Let's get started!")
    print ()
    input ()

    transition()

    #Adventure start

    first_grassfield()

    print ()
    print ()
    print ("You wake up in the middle of a grass field not knowing how you got there; you're dazed and confused at what's going on and how you got there.\
    Someone is standing over you holding a stick. Your adrenaline spikes and your fight or flight response kicks in.")
    input ()

    while True:
        answer = input("what do you do? (fight/run) ").lower().strip()
        if answer == 'fight': #Battle 0
            print ()
            print ("You run at the figure filled with adrenaline swinging your fists wildly .")
            input ()
            print ()

            print_boy()

            result = battle(hp, attackdmg, armor, enemy_name, enemy_hp, enemy_dmg, enemy_weapon, inventory, wrong, temple)
            hp, inventory = result
            inventory[0] = weapons[0]
            inventory.append(items[0])
            attackdmg = attackdmg + 1
            print (enemy_name, "dropped a", weapons[0] + "!")
            print (enemy_name, "dropped a", items[0] + "!")
            input ()
            boy = 'dead'
            print ()
            print ("You've calmed down enough to see what you just did. You can't help but feel like a bully for it... but oh well, what's done is done.")
            print ("You're at a grassfield you don't recognize. You see a dirt path near you. You can stay on the grassfield next to the evidence until somebody comes by or travel down the dirt path.")
            
            first_wait(code, wrong, difficulty, secret_code, secret_wait)
                    
            break

        elif answer == 'run':
            print ()
            print ("You turn to your right and sprint as fast as you can.")
            print ("You keep running until you feel safe, losing track of how far you've ran.")
            input ()
            break
                    
        else:
            print ()
            print (wrong)
            print ()

    #TRANSITION    

    transition()

    #Farm Area

    good_farm()

    #DIALOGUE 1
    input ()

    dialogue1(player_name, friend, inventory, items, wrong)
            
    #Explore farm

    print (friend, "left so you're alone on the farm now. The farm is old but functional. Theres a large barn and a house on the farm, along with dozens of farm animals. With this many friends, no wonder", friend, "is never lonely.")
    while True:
        print ()
        answer = input("Where do you want to go? (house/barn/leave) ").lower().strip()
        if answer == 'barn':
            print ()

            good_barn()

            print ()
            print ("You're at the barn")
            if barn_rock == False:
                barn_rock = True
                print ("You see a few cows roaming in the barn. There are many haybells, some being enjoyed by a few happy cows. They seem content.")
                print ("You find a rock!")
                inventory.append(items[0])
                print ()
                input ()
            else:
                print ("You see a few cows roaming in the barn. There are many haybells, some being enjoyed by a few happy cows. They seem content. Other than the cows, there isn't much of interest to you here.")
                print ()
                input ()
                
        elif answer == 'house':
            print ()

            good_house()

            print ()
            print ("You're at the house")
            print ("The house is nice and tidy. There's a fireplace being used to keep the house warm. The light of the fire illuminate the cozy home. You can relax for awhile before heading out.")
            print ()

            second_wait(code, wrong, difficulty, secret_code, secret_wait) 
                    
                
        elif answer == 'leave':
                break
        else:
                print ()
                print (wrong)
                    
    print ()
    print ("You're at a crossroad; one way leading to the temple, another back to the grassfield which you came from, and last path leading to the farm behind you.")

    #Explore the rest
    while True:
        print ()
        answer = input("Where do you want to go? (grassfields/temple/farm) ").lower().strip()
        if answer == 'temple':
            print ()
            print ("You start heading towards the temple.")
            input ()
            break
                
        elif answer == 'grassfields':
            print ()

            good_grassfield()

            print ()
            print ("You're at the grassfields")

            grass_dialogue(boy, confronted, player_name, friend, inventory, items, wrong)
        
        elif answer =='farm':
            while True:
                print ()
                print ("You're at", friend +"'s farm.", friend +"'s companions are lively.")
                print ()
                answer = input("Where do you want to go? (house/barn/leave) ").lower().strip()
                if answer == 'barn':
                    print ()
                    print ()
                    print ()
                    print ()
                    print ()

                    good_barn()

                    print ()
                    print ("You're at the barn")
                    if (boy == 'alive') and (confronted == True) and (trash_lid == False):
                        trash_lid = True
                        print ("You see a few cows roaming in the barn. There are many haybells, some being enjoyed by a few happy cows. They seem content. You look around for the round shield ", friend +"'s brother was talking. You find what you think he was talking about.")
                        print ("You received", armors[0])
                        inventory[1] = armors[0]
                        armor = 1
                        print ()
                        input ()
                    
                    if barn_rock == False:
                        barn_rock = True
                        print ("You see a few cows roaming in the barn. There are many haybells, some being enjoyed by a few happy cows. They seem content.")
                        print ("You find a rock!")
                        inventory.append(items[0])
                        print ()
                        input ()
                        
                    else:
                        print ("You see a few cows roaming in the barn. There are many haybells, some being enjoyed by a few happy cows. They seem content. Other than the cows, there isn't much of interest to you here.")
                        print ()
                        input ()

                elif answer == 'house':
                    print ()
                    print ()
                    print ()
                    print ()
                    print ()

                    good_house()

                    print ()
                    print ("You're at the house")
                    print ("The house is nice and tidy. There's a fireplace being used to keep the house warm. The light of the fire illuminate the cozy home. You can relax for awhile before heading out.")
                    print ()
                    second_wait(code, wrong, difficulty, secret_code, secret_wait)
                        
                elif answer == 'leave':
                        break
                    
                else:
                        print ()
                        print (wrong)
                                
        else:
            print ()
            print (wrong)
                    
                    
    #TRANSITION  

    transition()

    #Enemy1
    if difficulty == 'hard':
        enemy_name = 'Goblin'
        enemy_hp = 20
        enemy_dmg =  5
        enemy_weapon = 'shiv'
    else:
        enemy_name = 'Goblin'
        enemy_hp = 15
        enemy_dmg =  4
        enemy_weapon = 'shiv'

    #Temple Dungeon
    print ()

    good_temple()

    input ()

    #Temple Intro
    print ()
    print ("You arrive at the temple. ", end=' ')
    if secret_wait == True:
        print ("(about time...)", end=' ')
    print ("and a group of goblins hanging around by the entrance. Goblins are known for doing dirty work in exchange for gold. You dont see another way around the gob squad.")
    print ()
    input ()

    goblin()

    print ("The first of the goblins rush at you!")
    print ('A new challenger has arrived!', enemy_name + "!")
    input ()

    #Fight1
    result = battle(hp, attackdmg, armor, enemy_name, enemy_hp, enemy_dmg, enemy_weapon, inventory, wrong, temple)
    hp, inventory = result

    print (enemy_name, "dropped a", items[0] + "!")
    print (enemy_name, "dropped a", items[1] + "!")
    print (enemy_name, "dropped a", armors[1] + "!")
    inventory.append(items[1])
    inventory.append(items[0])
    inventory[1] = armors[1]
    armor = armor + 3

    #Enemy 2
    if difficulty == 'hard':
        enemy_name = 'Goblin Leader'
        enemy_hp = 25
        enemy_dmg =  7
        enemy_weapon = 'sword'
    else:
        enemy_name = 'Goblin Leader'
        enemy_hp = 20
        enemy_dmg =  5
        enemy_weapon = 'sword'

    input ()
    print ("The group of goblins gasp at the sight of one of their brother slain. The crowd clears infront of you as you see their leader approach you.")
    print ()
    input ()

    goblin_leader()

    print ()
    print ("Their leader charge at you!")
    print ('A new challenger has arrived!', enemy_name + "!")
    input ()


    #Fight 2
    result = battle(hp, attackdmg, armor, enemy_name, enemy_hp, enemy_dmg, enemy_weapon, inventory, wrong, temple)
    hp, inventory = result

    print (enemy_name, "dropped a", armors[3] + "!")
    print (enemy_name, "dropped a", weapons[2] + "!")
    inventory[0] = weapons[2]
    inventory[2] = armors[3]
    armor = armor + 2
    attackdmg = attackdmg + 5

    #Enemy 3
    if difficulty == 'hard':
        enemy_name = "Sorcerer's Apprentice"
        enemy_hp = 35
        enemy_dmg =  13
        enemy_weapon = "Magic"
    else:
        enemy_name = "Sorcerer's Apprentice"
        enemy_hp = 25
        enemy_dmg =  10
        enemy_weapon = "magic"

    input ()
    print ("All the goblins yell as they run and scatter out. With their leader down, the goblins all run home. There's a mysterious man standing on the other side of the chaotic crowd.")
    print ()
    input ()

    sorc_appr()

    print ()
    print ("The shadowy figure is ready to fight you!")
    print ('A new challenger has arrived!', enemy_name + "!")
    print ()
    input ()

    #Fight 3

    result = appr_battle(hp, attackdmg, armor, enemy_name, enemy_hp, enemy_dmg, enemy_weapon, inventory, turn, wrong)
    hp, inventory = result

    #Temple cleared
    print ("You've slain", enemy_name + "!")
    input ()
    print (enemy_name, "dropped a", items[0] + "!")
    print (enemy_name, "dropped a", items[2] + "!") #Great potion
    print (enemy_name, "dropped a pair of glasses!")
    inventory.append(items[2])
    inventory.append(items[0])
    inventory.append('glasses')
    print ("You can see slightly better.")

    temple = True

    input ()
    print ()
    print ("You defeated the Sorcerer's henchmen and can finally give chase. You run into the temple looking for the Sorcerer or the crystal.")
    input ()
    print ()
    print ("You enter the Grand Hall and see the Dark Sorcerer approach the power crystal in the center of the room. The dark figure stops and look at you for a moment before charging toward the power crystal.\
    He gets to the crystal before you can even react and grabs it.")
    input ()
    print ()
    print ("In an instant, the energy in the crystal is absorbed by the Sorcerer, enclosing himself in a massive shroud of energy. The aura radiates energy, seemingly unstable.")
    print ()

    #Ending 4
    if (secret_wait == True) and (secret_code == True):
        ending = '4'
        print ("You remember this is the nexus point, the event that split you up. If there was ever a time to break the time loop, its now.")
        print ()
        input ()
        print ("Unfortunately I'm not done writing out the story so this is where it ends!")
        print ()
        input ()
        winscreen()
        
    #Timeline split
    while True:
        jump = input("What do you do? (fight/run) ").lower().strip()
        if jump == 'fight':
            timetravel = True
            break
        
        if jump == 'run':
            break
            
        else:
            print ()
            print (wrong)
            print ()

    #present exploration
    if timetravel == False:
        present_explore(player_name, friend, inventory, items, talked, wrong)

    #future exploration
    if timetravel == True:
        future_explore(player_name, friend, inventory, items, talked, wrong)

    #DIALOGUE 2

    #TRANSITION
    transition()

    #Maybe custom stats for difficulty change
    if difficulty == 'hard':
        hp = 25
    else:
        hp = 30

    #Woods start
    print ()

    woods()

    print ()
    print ()
    print ("You arrive at the Woods.")
    print ("There are monsters roaming the woods, it seems like there's no way of getting to the Sorcerer without a fight!")
    input ()

    #Enemy 1
    if difficulty == 'hard':
        enemy_name = 'Skeleton'
        enemy_hp = 30
        enemy_dmg =  10
        enemy_weapon = 'bone club'
    else:
        enemy_name = 'Skeleton'
        enemy_hp = 20
        enemy_dmg =  8
        enemy_weapon = 'bone club'

    print ()

    skeleton()

    print ()
    print ('A new challenger has arrived!', enemy_name + "!")
    input ()

    #Fight 1
    result = battle(hp, attackdmg, armor, enemy_name, enemy_hp, enemy_dmg, enemy_weapon, inventory, wrong, temple)
    hp, inventory = result

    print (enemy_name, "dropped a", items[0] + "!")
    print (enemy_name, "dropped a", items[1] + "!")
    inventory.append(items[0])
    inventory.append(items[1])
    input ()
                                       
    demon1()

    print ()
    print ("As you proceed deeper, you start to feel uneasy from the ominous woods.")
    print ('A new challenger has arrived!', enemy_name + "!")
    input ()


    #enemy 2   SPECIAL FIGHT
    if difficulty == 'hard':
        enemy_name = 'One-eyed Demon'
        enemy_hp = 35
        enemy_dmg =  15
        enemy_weapon = 'crossbow'
    else:
        enemy_name = 'One-eyed Demon'
        enemy_hp = 25
        enemy_dmg =  13
        enemy_weapon = 'crossbow'

    #Fight 2
    result = battle(hp, attackdmg, armor, enemy_name, enemy_hp, enemy_dmg, enemy_weapon, inventory, wrong, temple)
    hp, inventory = result

    print (enemy_name, "dropped a", armors[4] + "!")
    inventory[2] = armors[4]
    armor = armor + 3
    input ()

    hellhound()

    print ()
    print ("You hear the trembling roars of incoming beasts.")
    print ('A new challenger has arrived!', enemy_name + "!")
    input ()

    #enemy 3  DOUBLE BATTLE? 18/18, 10/10
    if difficulty == 'hard':
        enemy_name = 'Hellhound 1'
        enemy_hp = 30
        enemy_dmg =  14
        enemy_weapon = 'nasty fangs'
        enemy_name2 = 'Hellhound 2'
        enemy_hp2 = 30
        enemy_dmg2 =  13
        enemy_weapon2 = 'nasty fangs'
    else:
        enemy_name = 'Hellhound 1'
        enemy_hp = 20
        enemy_dmg =  11
        enemy_weapon = 'nasty fangs'
        enemy_name2 = 'Hellhound 2'
        enemy_hp2 = 20
        enemy_dmg2 =  10
        enemy_weapon2 = 'not as nasty fangs'

    #Fight 3
    result = hellhound_battle(hp, attackdmg, armor, enemy_name, enemy_name2, enemy_hp, enemy_hp2, enemy_dmg, enemy_dmg2, enemy_weapon, enemy_weapon2, inventory, wrong)
    hp, inventory = result
    
    print (enemy_name, "dropped a", items[0] + "!")
    print (enemy_name2, "dropped a", items[0] + "!")
    print (enemy_name, "dropped a", items[1] + "!")
    inventory.append(items[1])
    inventory.append(items[0])
    inventory.append(items[0])
    input ()

    demon2()

    print ()
    print ("The earth starts to shake as you sense incoming danger.")
    print ('A new challenger has arrived!', enemy_name + "!")
    input ()

    #enemy 4     TOUGH FIGHT
    if difficulty == 'hard':
        enemy_name = 'Two-eyed Demon'
        enemy_hp = 40
        enemy_dmg =  16
        enemy_weapon = 'great sword'
    else:
        enemy_name = 'Two-eyed Demon'
        enemy_hp = 30
        enemy_dmg =  13
        enemy_weapon = 'great sword'

    #Fight 4
    result = battle(hp, attackdmg, armor, enemy_name, enemy_hp, enemy_dmg, enemy_weapon, inventory, wrong, temple)
    hp, inventory = result

    print (enemy_name, "dropped a", weapons[3] + "!")
    inventory[0] = weapons[3]
    attackdmg = attackdmg + 2
    input ()

    #TRANSITION
    print ()
    print ("You get through the mob of monsters and escaped the woods. you can finally proceed to the Sorcerer's Lair.")
    input ()
    transition()

    lair()

    print ()
    print ()
    print ()
    print ()

    print ("You arrive at the Sorcerer's Lair. A rift opens in front of you and expels massive amounts of energy. The sorcerer appears before you with an energy shield.")
    input ()
    print ("It's time to settle things with this fool")
    input ()

    sorc()

    #enemy 5 LAST BOSS
    if difficulty == 'hard':
        enemy_name = 'Dark Sorcerer'
        enemy_hp = 60
        enemy_dmg =  18
        enemy_weapon = 'Magic'
    else:
        enemy_name = 'Dark Sorcerer'
        enemy_hp = 45
        enemy_dmg =  14
        enemy_weapon = 'Magic' 

    print ()
    print ('The last challenger has arrived!', enemy_name + "!")
    input ()

    #Fight 5
    result = sorc_battle(hp, attackdmg, armor, enemy_name, enemy_hp, enemy_dmg, enemy_weapon, inventory, turn, wrong, player_name)
    hp, inventory, enemy_name = result

    ending = '1'
            
    if enemy_name == ('Time-worned', player_name):
            secret_glasses = True

    #Ending 1
    ending_dialogue(secret_glasses, ending, timetravel, wrong)
                    
    winscreen()
