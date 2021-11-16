def dialogue1(player_name, friend, inventory, items, wrong):    
    print (player_name +"! We need your help! A crazy Sorcerer came out of nowhere and demanded our power crystal! He's headed for the Temple!")
    print ()
    print ("[1] Who're you?") 
    print ("[2] Sorcerer?")
    print ("[3] Where's the Temple?")
    print ("[4] Power crystal?")
    print ()
    while True:
        answer = input('Pick a dialogue option: ').strip()
        if answer == '1':
            print ()
            print ("What? It's me,", friend + "! What's gotten into you?")
            print ()
            print ()
            print ()
            print ("[1] Power crystal?")
            print ("[2] Sorcerer?")
            print ("[3] Where's the Temple?")
            print ("[4] Say less")
            print ()
            while True:
                answer = input('Pick a dialogue option: ').strip()
                if answer == '1':
                    print ()
                    print ("The power crystal keeps our village safe! We can't let the Sorcerer take it!")
                    print ()
                    print ()
                    print ()
                    print ("[1] Sorcerer?")
                    print ("[2] Where's the Temple?")
                    print ("[3] Say less")
                    print ()
                    while True:
                        answer = input('Pick a dialogue option: ').strip()
                        if answer == '1':
                            print ()
                            print("Yeah this crazy old guy came and started spouting about getting young again. He wants our power crystal to use our crystal for eternal youth!")
                            print ()
                            print ()
                            print ()
                            print ("[1] Where's the Temple?")
                            print ("[2] Say less")
                            print ()
                            while True:
                                answer = input('Pick a dialogue option: ').strip()
                                if (answer == '2') or (answer == '1'):
                                    print ()
                                    print ("It's over that way! Thank you for helping", player_name +", take this as well, you'll need it.")
                                    input ()
                                    print (friend, "gave you a", items[1] + "!")
                                    inventory.append(items[1]) #ITEM
                                    input ()
                                    break

                                else:
                                    print ()
                                    print (wrong)
                            break

                        elif (answer == '2') or (answer == '3'):
                            print ()
                            print ("It's over that way! Thank you for helping", player_name +", take this as well, you'll need it.")
                            input ()
                            print (friend, "gave you a", items[1] + "!")
                            inventory.append(items[1]) #ITEM
                            input ()
                            break

                        else:
                            print ()
                            print (wrong)
                    break

                elif answer == '2':
                    print ()
                    print("Yeah this crazy old guy came and started spouting about getting young again. He wants our power crystal to use our crystal for eternal youth!")
                    print ()
                    print ()
                    print ()
                    print ("[1] Power crystal?")
                    print ("[2] Where's the Temple?")
                    print ("[3] Say less")
                    print ()
                    while True:
                        answer = input('Pick a dialogue option: ').strip()
                        if (answer == '2') or (answer == '3'):
                            print ()
                            print ("It's over that way! Thank you for helping", player_name +", take this as well, you'll need it.")
                            input ()
                            print (friend, "gave you a", items[1] + "!")
                            inventory.append(items[1]) #ITEM
                            input ()
                            break

                        elif answer == '1':
                            print ()
                            print ("The power crystal keeps our village safe! We can't let the Sorcerer take it!")
                            print ()
                            print ()
                            print ()
                            print ("[1] Where's the Temple?")
                            print ("[2] Say less")
                            print ()
                            while True:
                                answer = input('Pick a dialogue option: ').strip()
                                if (answer == '1') or (answer == '2'):
                                    print ()
                                    print ("It's over that way! Thank you for helping", player_name +", take this as well, you'll need it.")
                                    input ()
                                    print (friend, "gave you a", items[1] + "!")
                                    inventory.append(items[1]) #ITEM
                                    input ()
                                    break
                                    
                                else:
                                    print ()
                                    print (wrong)                               

                            break

                        else:
                            print ()
                            print (wrong)
                    break

                elif (answer == '4') or (answer == '3'):
                    print ()
                    print ("It's over that way! Thank you for helping", player_name +", take this as well, you'll need it.")
                    input ()
                    print (friend, "gave you a", items[1] + "!")
                    inventory.append(items[1]) #ITEM
                    input ()
                    break

                else:
                    print ()
                    print (wrong)
            break


        elif answer == '2':
            print ()
            print("Yeah this crazy old guy came and started spouting about getting young again. He wants our power crystal for eternal youth!")
            print ()
            print ()
            print ()
            print ("[1] Who're you?")
            print ("[2] Power crystal?")
            print ("[3] Where's the Temple?")
            print ("[4] Say less")
            print ()
            while True:
                answer = input('Pick a dialogue option: ').strip()
                if (answer == '4') or (answer == '3'):
                    print ()
                    print ("It's over that way! Thank you for helping", player_name +", take this as well, you'll need it.")
                    input ()
                    print (friend, "gave you a", items[1] + "!")
                    inventory.append(items[1]) #ITEM
                    input ()
                    break

                elif answer == '2':
                    print ()
                    print ("The power crystal keeps our village safe! We can't let the Sorcerer take it!")
                    print ()
                    print ()
                    print ()
                    print ("[1] Who're you?")
                    print ("[2] Where's the Temple?")
                    print ("[3] Say less")
                    print ()
                    while True:
                        answer = input('Pick a dialogue option: ').strip()
                        if (answer == '3') or (answer == '2'):
                            print ()
                            print ("It's over that way! Thank you for helping", player_name +", take this as well, you'll need it.")
                            input ()
                            print (friend, "gave you a", items[1] + "!")
                            inventory.append(items[1]) #ITEM
                            input ()
                            break

                        elif answer == '1':
                            print ()
                            print("It's me", friend, +"! What's gotten into you?")
                            print ()
                            print ()
                            print ()
                            print ("[1] Where's the Temple?")
                            print ("[2] Say less")
                            print ()
                            while True:
                                answer = input('Pick a dialogue option: ').strip()
                                if (answer == '1') or (answer == '2'):
                                    print ()
                                    print ("It's over that way! Thank you for helping", player_name +", take this as well, you'll need it.")
                                    input ()
                                    print (friend, "gave you a", items[1] + "!")
                                    inventory.append(items[1]) #ITEM
                                    input ()
                                    break
                                    
                                else:
                                    print ()
                                    print (wrong)                               

                            break
                            
                        else:
                            print ()
                            print (wrong)                               

                    break
                
                elif answer == '1':
                    print ()
                    print("It's me", friend, +"! What's gotten into you?")
                    print ()
                    print ()
                    print ()
                    print ("[1] Power crystal?")
                    print ("[2] Where's the Temple?")
                    print ("[3] Say less")
                    print ()
                    while True:
                        answer = input('Pick a dialogue option: ').strip()                             
                        if answer == '1':
                            print ()
                            print ("The power crystal keeps our village safe! We can't let the Sorcerer take it!")
                            print ()
                            print ()
                            print ()
                            print ("[1] Where's the Temple?")
                            print ("[2] Say less")
                            print ()
                            while True:
                                answer = input('Pick a dialogue option: ').strip()
                                if (answer == '1') or (answer == '2'):
                                    print ()
                                    print ("It's over that way! Thank you for helping", player_name +", take this as well, you'll need it.")
                                    input ()
                                    print (friend, "gave you a", items[1] + "!")
                                    inventory.append(items[1]) #ITEM
                                    input ()
                                    break
                                    
                                else:
                                    print ()
                                    print (wrong)                               

                            break

                        elif (answer == '2') or (answer == '3'):
                            print ()
                            print ("It's over that way! Thank you for helping", player_name +", take this as well, you'll need it.")
                            input ()
                            print (friend, "gave you a", items[1] + "!")
                            inventory.append(items[1]) #ITEM
                            input ()
                            break

                        else:
                            print ()
                            print (wrong)
                    break
                    

                else:
                    print ()
                    print (wrong)
            break

        elif (answer == '3'):
            print ()
            print ("It's over that way! Thank you for helping", player_name +", take this as well, you'll need it.")
            input ()
            print (friend, "gave you a", items[1] + "!")
            inventory.append(items[1]) #ITEM
            input ()
            break

        elif answer == '4':
            print ()
            print ("The power crystal keeps our village safe! We can't let the Sorcerer take it!")
            print ()
            print ()
            print ()
            print ("[1] Sorcerer?")
            print ("[2] Who're you?")
            print ("[3] Where's the Temple?")
            print ("[4] Say less")
            print ()
            while True:
                answer = input('Pick a dialogue option: ').strip()
                if answer == '1':
                    print ()
                    print("Yeah this crazy old guy came and started spouting about getting young again. He wants our power crystal to use your crystal for eternal youth!")
                    print ()
                    print ()
                    print ()
                    print ("[1] Who're you?")
                    print ("[2] Where's the Temple?")
                    print ("[3] Say less")
                    print ()
                    while True:
                        answer = input('Pick a dialogue option: ').strip()
                        if (answer == '2') or (answer == '3'):
                            print ()
                            print ("It's over that way! Thank you for helping", player_name +", take this as well, you'll need it.")
                            input ()
                            print (friend, "gave you a", items[1] + "!")
                            inventory.append(items[1]) #ITEM
                            input ()
                            break

                        elif answer == '1':
                            print ()
                            print("It's me", friend, +"! What's gotten into you?")
                            print ()
                            print ()
                            print ()
                            print ("[1] Where's the Temple?")
                            print ("[2] Say less")
                            print ()
                            while True:
                                answer = input('Pick a dialogue option: ').strip()
                                if (answer == '1') or (answer == '2'):
                                    print ()
                                    print ("It's over that way! Thank you for helping", player_name +", take this as well, you'll need it.")
                                    input ()
                                    print (friend, "gave you a", items[1] + "!")
                                    inventory.append(items[1]) #ITEM
                                    input ()
                                    break
                                    
                                else:
                                    print ()
                                    print (wrong)                               

                            break
                            

                        else:
                            print ()
                            print (wrong)
                    break

                elif answer == '2':
                    print ()
                    print("It's me", friend, + "! What's gotten into you?")
                    print ()
                    print ()
                    print ()
                    print ("[1] Sorcerer?")
                    print ("[2] Where's the Temple?")
                    print ("[3] Say less")
                    print ()
                    while True:
                        answer = input('Pick a dialogue option: ').strip()
                        if answer == '1':
                            print ()
                            print("Yeah this crazy old guy came and started spouting about getting young again. He wants our power crystal to use our crystal for eternal youth!")
                            print ()
                            print ()
                            print ()
                            print ("[1] Where's the Temple?")
                            print ("[2] Say less")
                            print ()
                            while True:
                                answer = input('Pick a dialogue option: ').strip()
                                if (answer == '2') or (answer == '1'):
                                    print ()
                                    print ("It's over that way! Thank you for helping", player_name +", take this as well, you'll need it.")
                                    input ()
                                    print (friend, "gave you a", items[1] + "!")
                                    inventory.append(items[1]) #ITEM
                                    input ()
                                    break

                                else:
                                    print ()
                                    print (wrong)
                            break

                        elif (answer == '2') or (answer == '3'):
                            print ()
                            print ("It's over that way! Thank you for helping", player_name +", take this as well, you'll need it.")
                            input ()
                            print (friend, "gave you a", items[1] + "!")
                            inventory.append(items[1]) #ITEM
                            input ()
                            break

                        else:
                            print ()
                            print (wrong)
                    break

                elif (answer == '4') or (answer == '3'):
                    print ()
                    print ("It's over that way! Thank you for helping", player_name +", take this as well, you'll need it.")
                    input ()
                    print (friend, "gave you a", items[1] + "!")
                    inventory.append(items[1]) #ITEM
                    input ()
                    break

                else:
                    print ()
                    print (wrong)
            break

        else:
            print ()
            print (wrong)

def grass_dialogue(boy, confronted, player_name, friend, inventory, items, wrong):
    if boy == 'alive':
        if confronted == False:
            confronted = True
            print ("You see", friend + "'s brother out in the field")
            print ()
            print ( friend + "'s brother: \"Hey", player_name + "!", "Sorry for scaring you, I saw you in the grass earlier so I came over to check up on you. I feel so bad... you can have my favourite shield! It's circular and in the barn, it will help you.\"")
            input ()
            print ()
            print ()
            print ("[1] \"What were you doing out there anyway?\"") #1:4 chance
            print ("[2] \"You shouldn't be sneaking up on people like that!\"") #1 potion
            print ("[3] \"What happened to me?\"") #1:4 chance
            print ("[4] (leave)") #0:0
            print ()
            while True:
                print ()
                answer = input('Pick a dialogue option: ').strip()
                if answer == '1':
                    print ()
                    print ("\"I saw a beam of light come from that direction so I went to check it out! By the time I got there, all I found was you.\"")
                    print ()
                    print ()
                    print ()
                    print ("[1] \"Are you alright?\"") #+1atk:2potion
                    print ("[2] \"Did you see the sorcerer?\"") #1potion
                    print ("[3] \"Did you see anything else?\"") #1potion
                    print ("[4] \"Alright stay out of trouble okay?\"")
                    print ()
                    while True:
                        print ()
                        answer = input('Pick a dialogue option: ').strip()
                        if answer == '1':
                            print ()
                            print ("\"Yeah I'm okay, Thank you for looking out for me. I want you to have this, I hope it helps you.\"")
                            print ( friend + "'s brother gave you a stick!")
                            inventory[0] = weapons[0] #+1atk
                            input ()
                            break

                        elif (answer == '3') or (answer == '2'):
                            print ()
                            print("\"No I didn't see anything else, it was just you lying on the grassfields.\"")
                            print ()
                            print ()
                            print ()
                            print ("[1] \"Okay then.\"")
                            print ()
                            while True:
                                print ()
                                answer = input ("Pick a dialogue option: ")
                                if answer == '1':
                                    print ()
                                    print ("\"I'm gonna go play somewhere else. Have this though, it'll help you more than me.\"")
                                    print (friend +"'s brother gave you a potion!")
                                    inventory.append(items[1]) #potion
                                    input ()
                                    break
                                else:
                                    print ()
                                    print (wrong)

                            break        

                        elif answer == '4':
                            print ()
                            print ("\"Okay", player_name + ",", "I'll stay safe!\"")
                            input ()
                            break

                        else:
                            print ()
                            print (wrong)

                            
                    break

                elif answer == '3':
                    print ()
                    print("\"I'm not 100% sure, I saw lights coming from over here so I came to check it out and then found you.\"")
                    print ()
                    print ()
                    print ()
                    print ("[1] \"Are you alright?\"") #1:2
                    print ("[2] \"Did you see the sorcerer?\"") #1pot
                    print ("[3] \"Did you see anything else?\"") #1pot
                    print ("[4] \"Alright stay out of trouble okay?\"")
                    print ()
                    while True:
                        print ()
                        answer = input('Pick a dialogue option: ').strip()
                        if answer == '1':
                            print ()
                            print ("\"Yeah I'm okay, Thank you for looking out for me. I want you to have this, I hope it helps you.\"")
                            print ( friend + "'s brother gave you a stick!")
                            inventory[0] = weapons[0] #+1atk
                            input ()
                            break

                        elif (answer == '3') or (answer == '2'):
                            print ()
                            print("\"No I didn't see anything else, it was just you lying on the grassfields.\"")
                            print ()
                            print ()
                            print ()
                            print ("[1] \"Okay then.\"")
                            print ()
                            while True:
                                print ()
                                answer = input ("Pick a dialogue option: ")
                                if answer == '1':
                                    print ()
                                    print ("\"I'm gonna go play somewhere else. Have this though, it'll help you more than me.\"")
                                    print (friend +"'s brother gave you a potion!")
                                    inventory.append(items[1]) #POTION
                                    input ()
                                    break
                                else:
                                    print ()
                                    print (wrong)
                            break

                        elif answer == '4':
                            print ()
                            print ("\"Okay", player_name + ",", "I'll stay safe!\"")
                            input ()
                            break

                        else:
                            print ()
                            print (wrong)
                    
                    break

                elif answer == '2':
                    print ()
                    print ("\"I'm sorry about that, I'll remember it for next time! You can have this... if it makes you feel any better.\"")
                    print ("You received a potion!")
                    inventory.append(items[1])
                    input () # POTION
                    break

                elif answer == '4':
                    print ()
                    print ("You turn around and walked away.")
                    input ()
                    print ("\"Alright see you around", player_name + "!\"")
                    input ()
                    break

                else:
                    print ()
                    print (wrong)
                    
        if confronted == True:
            print ()
            print ("You see", friend + "'s little brother in the fields playing by himself. Although he's out alone, he seem to be enjoying his time; so you leave him alone.")
            input ()

    elif boy == 'dead':
        if confronted == False:
            confronted = True
            print ("You see", friend, "in the fields crying while holding onto his poor brother's corpse.")
            input ()
            print ("\"Who could've done this?! I'll never forget this! You'll be avenged!!\"")
            input ()
            print ()
            print ()
            print ("[1] It wasn't me...")
            print ("[2] It was probably that Sorcerer!!")
            print ("[3] It was me, I'm so sorry")
            print ("[4] (leave)")
            print ()
            while True:
                print ()
                answer = input('Pick a dialogue option: ').strip()
                if answer == '1':
                    print ()
                    print ("\"Of course it wasn't you,", player_name + ",", "Only a true monster would do this! I'm sorry, can you give me some time to process this?\"")
                    input ()
                    break

                elif answer == '2':
                    print ()
                    print("\"I knew it!", player_name +",", "you have to help me defeat him and avenge my brother! I'm not very useful in a fight, so take this. I hope it'll help you slay that monster!\"")
                    input ()
                    inventory[1] = armors[0]
                    print (friend, "gave you a", armors[0] + "!")
                    armor = 1
                    input () # DEFENCE 1
                    break

                elif answer == '3':
                    print ()
                    print ("\"You? You did this?! I can't believe it... My own bestfriend! Leave, I can't stand to look at you\"")
                    input ()
                    friendship = 'bad'
                    break

                elif answer == '4':
                    print ()
                    print ("You turn around and walked away.")
                    relationship = 'neutral'
                    input ()
                    break

                else:
                    print ()
                    print (wrong)


        if confronted == True:
            print ()
            print ("You see", friend, "in the fields crying while holding onto his poor brother's corpse.", friend, "needs some space so you leave them alone.")
            input ()

def ending_dialogue(secret_glasses, ending, timetravel, wrong):
    print ()
    print ("You defeated the Dark Sorcerer!")
    print ()
    input ()
    print ("The Sorcerer loses control of the energy inside him and erupts!")
    input ()

    #Ending 2
    if (secret_glasses == True):
        ending = '2'
        print ()
        print ("You examine the Sorcerer's body only to realize that the sorcerer you've been fighting is yourself, but older. An aged", player_name, "corrupted by the power and driven mad by time, lies lifeless in front of you. Nevertheless, you've brought peace back to the village!")
        input ()

    #Ending 3

        if (secret_wait == True):
            if timetravel == True:
                while True:
                    print ()
                    answer = input ("Use the energy from the sorcerer to go home? (yes/no) ").lower().strip()
                    if answer == 'yes':
                        ending = '3'
                        print ("You absorb the energy from the sorcerer to create a way home. You dont have enough control the vast amount of energy inside you to create a stable rift home.")
                        print ()
                        input ()
                        print ("The rift you open is wild and unpredictable but manage to successfully sends you back home.")
                        print ()
                        input ()
                        print ("You arrive in the Sorcerer's lair only to find yourself, but younger; and looking for a fight.")
                        input ()
                        break

                    elif answer == 'no':
                        ending = '3'
                        print ("After defeating the threat, you return to life in the village...")
                        print ()
                        input ()
                        print ("...")
                        print ()
                        input ()
                        print ("........")
                        print ()
                        input ()
                        print ("...........................")
                        print ()
                        input ()
                        print ("After some time, you start to notice something...")
                        print ()
                        input ()
                        print ("The blast that struck you stayed inside you. The energy that reside inside you gives you the ability to cast magic, but it also made you vulnerable to the flow of time.")
                        print ()
                        input ()
                        print ("As time pass, you start to age as everyone around you stay young and healthy. Growing envious and bitter,you isolate yourself from them; delving deeper into dark magic in search for answers.")
                        print ()
                        input ()
                        print ("You cast a powerful time spell that will undo the effects of time on yourself. The spell hit you with a beam of light making you feel dazed. You figure you dont have enough energy to fully cast the spell.")
                        print ()
                        input ()
                        print ("Now where can you find a powerful energy source?")
                        print ()
                        input ()
                        break

                    else:
                        print ()
                        print (wrong)

            elif timetravel == False:
                ending = '3'
                print ("After defeating the threat, you return to life in the village...")
                print ()
                input ()
                print ("...")
                print ()
                input ()
                print ("........")
                print ()
                input ()
                print ("...........................")
                print ()
                input ()
                print ("After some time, you start to notice something...")
                print ()
                input ()
                print ("The blast that struck you stayed inside you. The energy that reside inside you gives you the ability to cast magic, but it also made you vulnerable to the flow of time.")
                print ()
                input ()
                print ("As time pass, you start to age as everyone around you stay young and healthy. Growing envious and bitter,you isolate yourself from them; delving deeper into dark magic in search for answers.")
                print ()
                input ()
                print ("You cast a powerful time spell that will undo the effects of time on yourself. The spell hit you with a beam of light making you feel dazed. You figure you dont have enough energy to fully cast the spell.")
                print ()
                input ()
                print ("Now where can you find a powerful energy source?")
                print ()
                input ()
