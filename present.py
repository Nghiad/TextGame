def present_explore(player_name, friend, inventory, items, talked, wrong):
    print ()
    print ("You turn around and jump backwards. The Sorcerer's energy implodes and destroys everything around him. Your jump narrowly avoided a direct impact with the blast.")
    input ()
    print ("The shockwave knocks you down briefly but you quickly shake it off. The Sorcerer is gone along with the power crystal's energy! You have to stop him before he uses up all the energy!\
He must have returned to the woods! You absorbed the energy that radiated earlier and has made you stronger.")
    input ()
    print ("You're at the temple. The temple is well maintained, but nothing else here interests you.")
    input ()
    print ("You exit the temple.")
    input ()
    print ("You can proceed to the woods, or you can return to the crossroads; one way leading to the farm, one leading to the grassfields, and last path leading to the temple behind you.")
    while True:
            print ()
            answer = input("Where do you want to go? (woods/farm/grassfields/temple) ").lower().strip()
            if answer == 'woods':
                    print ()
                    answer = input("This is the point of no return, do you want to proceed? (yes/no) ").lower().strip()
                    if answer == 'yes':
                        print ()
                        print ("You start heading towards the Mysterious Woods.")
                        input ()
                        break

            elif answer == 'temple':

                    good_temple()

                    print ()
                    print ("You're at the temple. The temple is well maintained, but nothing else here interests you.")
                    print ()
                    input ()
                    
                    
            elif answer == 'grassfields':
                    print ()

                    good_grassfield()

                    print ()
                    print ("You're at the grassfields")
                    print ("The field is empty. The gentle breeze of the winds is calming, but nothing else here interests you.")
                    input ()
            
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
                                    if boy == 'dead':
                                        print ("You see many cows resting in the barn with mounds of hay scattered around the room. You see an occupied casket on the side of the room, you probably shouldn't be here.")
                                        input ()
    
                                    elif (boy == 'alive') and (confronted == True) and (trash_lid == False):
                                        trash_lid = True
                                        print ("You see a few cows roaming in the barn. There are many haybells, some being enjoyed by a few happy cows. They seem content. You look around for the round shield ", friend +"'s brother was talking. You find what you think he was talking about.")
                                        print ("You received", armors[0])
                                        armor = armor +1
                                        input ()
                                    
                                    elif boy == 'alive':
                                        if barn_rock == False:
                                            barn_rock = True
                                            print ("You see a few cows roaming in the barn. There are many haybells, some being enjoyed by a few happy cows. They seem content.")
                                            print ("You find a rock!")
                                            inventory.append(items[0])
                                            print ()
                                            input ()
                                        else:
                                            print ("You see many cows resting in the barn with mounds of hay scattered around the room. They seem content. Other than the cows, there isn't much of interest to you here.")
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
                                    if talked == False:
                                        talked = True
                                        if friendship == 'good':
                                            print ("The house is nice and tidy. There's a fireplace being used to keep the house warm. The light of the fire illuminate the cozy home. You can relax for awhile before heading out, but you have an urgent mission!")
                                            if boy == 'dead':
                                                print ("You see", friend, "grieving over their deceased brother.")
                                                print ()
                                                print ()
                                                print ("[1] How are you doing?") 
                                                print ("[2] I'll avenge him!") 
                                                print ("[3] The Sorcerer got away...")
                                                print ("[4] I'm sorry...") 
                                                print ()
                                                while True:
                                                    answer = input('Pick a dialogue option: ').strip()
                                                    if answer == '1':
                                                        print ()
                                                        print ("I'm okay, it's tough being home all alone now... but I guess I'll have to get used to it.")
                                                        print ()
                                                        print ()
                                                        print ("[1] Hang in there...")
                                                        print ("[2] Time heals all wounds")
                                                        print ("[3] It gets easier.")
                                                        print ("[4] I'm sorry for your loss.")
                                                        print ()
                                                        while True: 
                                                            answer = input('Pick a dialogue option: ').strip()
                                                            if (answer == '1') or (answer == '2') or (answer == '3') or (answer == '4'):
                                                                print ()
                                                                print ("Thank you,", player_name + ", you have been a great friend to me in these troubling times... I want you to have this, it'll keep you safe")
                                                                input ()
                                                                print (friend, "gave you a", items[1] + "!")
                                                                inventory.append(items[1]) #ITEM
                                                                input ()
                                                                print ("Can you excuse me? I'd like some time to grieve.")
                                                                input ()
                                                                break

                                                            else:
                                                                print (wrong)
                                                        break

                                                    elif (answer == '2'):
                                                        print ()
                                                        print("Thank you for the sentiment", player_name + ", I appreciate it. You'll defeat that Sorcerer! I know it!")
                                                        print ()
                                                        print ()
                                                        print ("[1] Hang in there, things will get better.")
                                                        print ("[2] I'll T-bag him for you.")
                                                        print ("[3] I have no doubt I'll avenge your brother!")
                                                        print ("[4] He wont get away with this!")
                                                        print ()
                                                        while True: 
                                                            answer = input('Pick a dialogue option: ').strip()
                                                            if (answer == '1') or (answer == '2') or (answer == '3') or (answer == '4'):
                                                                print ()
                                                                print ("Thank you,", player_name + ", you have been a great friend to me in these troubling times... I want you to have this, it'll keep you safe")
                                                                input ()
                                                                print (friend, "gave you a", items[1] + "!")
                                                                inventory.append(items[1]) #ITEM
                                                                input ()
                                                                print ("Can you excuse me? I'd like some time to grieve.")
                                                                input ()
                                                                break

                                                            else:
                                                                print (wrong)
                                                        break

                                                    elif answer == '3':
                                                        print ()
                                                        print ("I... it's okay, I can't blame you for trying. You'll get him next time, I believe in you!")
                                                        print ()
                                                        print ()
                                                        print ()
                                                        print ("[1] He won't get away next time!")
                                                        print ("[2] He's got magic...")
                                                        print ("[3] I don't know... He's pretty strong.")
                                                        print ("[4] Placeholder reply4")
                                                        print ()
                                                        while True: 
                                                            answer = input('Pick a dialogue option: ').strip()
                                                            if (answer == '1') or (answer == '4'):
                                                                print ()
                                                                print ("Thank you,", player_name + ", you have been a great friend to me in these troubling times... I want you to have this, it'll keep you safe")
                                                                input ()
                                                                print (friend, "gave you a", items[1] + "!")
                                                                inventory.append(items[1]) #ITEM
                                                                input ()
                                                                print ("Can you excuse me? I'd like some time to grieve.")
                                                                input ()
                                                                break

                                                            elif (answer == '2') or (answer == '3'):
                                                                print ()
                                                                print ("Thank you,", player_name + ", you have been a great friend to me in these troubling times... I want you to have this, it'll keep you safe")
                                                                input ()
                                                                print (friend, "gave you a", items[1] + "!")
                                                                inventory.append(items[1]) #ITEM
                                                                input ()
                                                                print ("Can you excuse me? I'd like some time to grieve.")
                                                                input ()
                                                                break

                                                            else:
                                                                print (wrong)
                                                        
                                                        break

                                                    elif answer == '4':
                                                        print ()
                                                        print ("It's okay", player_name + ", it's not your fault, but thank you for being here with me.")
                                                        print ()
                                                        print ()
                                                        print ()
                                                        print ("[1] Of course I'll be here for you.")
                                                        print ("[2] If you ever need to talk, I'm here for you.")
                                                        print ("[3] It was me, I killed him...")
                                                        print ("[4] If you need anything, let me know.")
                                                        print ()
                                                        while True:
                                                            answer = input('Pick a dialogue option: ').strip()
                                                            if (answer == '1') or (answer == '2') or (answer == '4'):
                                                                print ()
                                                                print ("Thank you,", player_name + ", you have been a great friend to me in these troubling times... I want you to have this, it'll keep you safe")
                                                                input ()
                                                                print (friend, "gave you a", items[1] + "!")
                                                                inventory.append(items[1]) #ITEM
                                                                input ()
                                                                print ("Can you excuse me? I'd like some time to grieve.")
                                                                input ()
                                                                break

                                                            elif answer == '3':
                                                                print ()
                                                                print ("That's a cruel joke", player_name + ".")
                                                                print ()
                                                                print ()
                                                                print ()
                                                                print ("[1] I'm sorry I didn't mean that...")
                                                                print ("[2] It's not a joke.")
                                                                print ("[3] My bad, not the time and place.")
                                                                print ()
                                                                while True:
                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                    if (answer == '1') or (answer == '3'):
                                                                        print ()
                                                                        print ("That's okay, I know you're just trying to help. Can you excuse me? I'd like some time to grieve.")
                                                                        input ()
                                                                        break

                                                                    elif answer == '2':
                                                                        print ()
                                                                        print ("What?! I can't believe what I'm hearing... I don't know what to say or think.")
                                                                        print ()
                                                                        print ()
                                                                        print ()
                                                                        print ("[1] I'm kidding!!")
                                                                        print ("[2] DATTEBAYO ( Believe it! )")
                                                                        print ("[3] It was an accident! He scared me!")
                                                                        print ("[4] I'm so sorry.")
                                                                        print ()
                                                                        while True:
                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                            if answer == '1':
                                                                                print ()
                                                                                print ("This is not the time and place for jokes", player_name + ", you should go...")
                                                                                input ()
                                                                                relationship = 'neutral'
                                                                                break

                                                                            elif answer == '2':
                                                                                print ()
                                                                                print("I'LL KILL YOU!!! SQUARE UP!")
                                                                                input ()
                                                                                print ()
                                                                                print ()
                                                                                print ("[1] Don't make me do this...")
                                                                                print ("[2] You're gonna regret this.")
                                                                                print ("[3] I'll slay you just like your brother.")
                                                                                print ("[4] I'm not fighting you.")
                                                                                print ()
                                                                                while True:
                                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                                    if (answer == '2') or (answer == '3'):
                                                                                        print ()
                                                                                        print ("You're not leaving here alive old friend.")
                                                                                        input ()
                                                                                        enemy_name = friend
                                                                                        enemy_dmg = 5
                                                                                        enemy_hp = 20
                                                                                        enemy_weapon = weapons[1]
                                                                                        battle()
                                                                                        print (enemy_name, "dropped a", weapons[1] + "!")
                                                                                        input ()
                                                                                        print ("You've slain your friend in cold blood rather easily. You stand over your friend's body with mixed feelings of victory and regret... or perhaps not.")
                                                                                        attackdmg = attackdmg + 1
                                                                                        relationship = 'dead'

                                                                                        break

                                                                                    elif (answer == '1') or (answer == '4'):
                                                                                        print ()
                                                                                        print ("Kill me like you killed my brother in cold blood!")
                                                                                        print ()
                                                                                        print ()
                                                                                        print ()
                                                                                        print ("[1] I didn't mean to...")
                                                                                        print ("[2] It was an accident, I'm sorry.")
                                                                                        print ("[3] You're gonna need a lot of potions for this...")
                                                                                        print ("[4] Come and get some then!")
                                                                                        print ()
                                                                                        while True:
                                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                                            if (answer == '4') or (answer == '3'):
                                                                                                print ()
                                                                                                print ("You're not leaving here alive old friend.")
                                                                                                input ()
                                                                                                enemy_name = friend
                                                                                                enemy_dmg = 5
                                                                                                enemy_hp = 20
                                                                                                enemy_weapon = weapons[1]
                                                                                                battle()
                                                                                                print (enemy_name, "dropped a", weapons[1] + "!")
                                                                                                input ()
                                                                                                print ("You've slain your friend in cold blood rather easily. You stand over your friend's body with mixed feelings of power and regret... or perhaps not.")
                                                                                                attackdmg = attackdmg + 1
                                                                                                relationship = 'dead'
                                                                                                break

                                                                                            elif (answer == '1') or (answer == '2'):
                                                                                                print ()
                                                                                                print ("I...! I can't even look at you,", player_name + ", leave me...please.")
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

                                                                            elif (answer == '3') or (answer == '4'):
                                                                                print ()
                                                                                print ("I'm... I can't...")
                                                                                input ()
                                                                                print ("I can't fully blame you for his death, he was always clueless... but still.")
                                                                                input ()
                                                                                print ("Can you excuse me? I'd like some time to grieve.")
                                                                                input ()
                                                                                relationship = 'neutral'
                                                                                break
                                                                            
                                                                            else:
                                                                                print ()
                                                                                print (wrong)
                                                                        break

                                                                        

                                                                    else:
                                                                        print ()
                                                                        print (wrong)
                                                                break


                                                            else:
                                                                print ()
                                                                print (wrong)
                                                                
                                                        break

                                                    else:
                                                        print ()
                                                        print (wrong)
                                                break

                                                
                                            elif boy == 'alive':
                                                print ()
                                                print ("You see", friend, "and their brother lounging.")
                                                print ("Hey", player_name + ", did you defeat the Sorcerer?")
                                                print ()
                                                print ()
                                                print ()
                                                print ("[1] Not yet...but soon!")
                                                print ("[2] It's harder than it looks...")
                                                print ("[3] The Sorcerer got away...")
                                                print ("[4] Easily!") 
                                                print ()
                                                while True: 
                                                    answer = input('Pick a dialogue option: ').strip()
                                                    if answer == '1':
                                                        print ()
                                                        print ("Alright, we're counting on you", player_name + "! Here have this, it will help you beat the sorcerer.")
                                                        input ()
                                                        print (friend, "gave you a", items[1] + "!")
                                                        inventory.append(items[1]) #ITEM
                                                        input ()
                                                        break

                                                    elif answer == '2':
                                                        print ()
                                                        print("I believe you! I wouldn't want to be fighting a magic weilder either! Here have this, it will help you beat the sorcerer.")
                                                        input ()
                                                        print (friend, "gave you a", items[1] + "!")
                                                        inventory.append(items[1]) #ITEM
                                                        input ()
                                                        break

                                                    elif answer == '3':
                                                        print ()
                                                        print ("Damn him! are you going after him?")
                                                        print ()
                                                        print ()
                                                        print ()
                                                        print ("[1] Of course.")
                                                        print ("[2] I'm just relaxing for now.")
                                                        print ("[3] He'll come to me.")
                                                        print ("[4] I'm going right now!")
                                                        print ()
                                                        while True:
                                                            answer = input('Pick a dialogue option: ').strip()
                                                            if (answer == '2') or (answer == '3'):
                                                                print ()
                                                                print ("Confident, I like it! but take this, You'll need it.")
                                                                input ()
                                                                print (friend, "gave you a", items[1] + "!")
                                                                inventory.append(items[1]) #ITEM
                                                                input ()
                                                                break

                                                            elif (answer == '4') or (answer == '1'):
                                                                print ()
                                                                print ("Alright, but take this! You'll need it.")
                                                                input ()
                                                                print (friend, "gave you a", items[1] + "!")
                                                                inventory.append(items[1]) #ITEM
                                                                input ()
                                                                break

                                                            else:
                                                                print (wrong)
                                                        break


                                                    elif answer == '4':
                                                        print ()
                                                        print ("Wow awesome, didn't doubt you! I was gonna give you this item but it doesn't look like you'll need it.")
                                                        print ()
                                                        print ()
                                                        print ()
                                                        print ("[1] I was kidding... He's still out there.")
                                                        print ("[2] Yeah I won't be needing it.")
                                                        print ("[3] Consider it my reward.")
                                                        print ("[4] Oh.... Please?")
                                                        print ()
                                                        while True:
                                                            answer = input('Pick a dialogue option: ').strip()
                                                            if (answer == '1'):
                                                                print ()
                                                                print ("I knew it, you may be good... but you're not THAT good!")
                                                                print ()
                                                                print ()
                                                                print ("[1] I'll get him next time!")
                                                                print ("[2] What's that supposed to mean?")
                                                                print ("[3] I'm EXACTLY that good!")
                                                                print ("[4] I just need a little more time.")
                                                                print ()
                                                                while True:
                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                    if answer == '1':
                                                                        print ()
                                                                        print ("I believe you, you haven't let me down yet... well I guess this time you did.")
                                                                        print ()
                                                                        print ()
                                                                        print ()
                                                                        print ("[1] It wont happen again.")
                                                                        print ("[2] I'll try harder next time.")
                                                                        print ("[3] I'm sorry.")
                                                                        print ("[4] You can go and fight him if you want.")
                                                                        print ()
                                                                        while True:
                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                            if (answer == '3') or (answer == '1') or (answer == '2') or (answer == '4'):
                                                                                print ()
                                                                                print ("Ahaha I'm kidding, you're doing great! Here have this, it will help you beat the sorcerer.")
                                                                                input ()
                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                inventory.append(items[1]) #ITEM
                                                                                input ()
                                                                                break

                                                                            else:
                                                                                print ()
                                                                                print (wrong)
                                                                        break


                                                                    elif (answer == '2') or (answer == '4'):
                                                                                print ()
                                                                                print ("Ahaha I'm kidding, you're good", player_name + "! The best! you'll beat the sorcerer. Here have this, consider it my contribution to your battle.")
                                                                                input ()
                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                inventory.append(items[1]) #ITEM
                                                                                input ()
                                                                                break

                                                                    elif (answer == '3'):
                                                                        print ()
                                                                        print ("Riiiight, that's why we have a magic weilding terrorist in the area.")
                                                                        print ()
                                                                        print ()
                                                                        print ("[1] Point taken")
                                                                        print ("[2] I'm gonna handle it!")
                                                                        print ("[3] Okay fine, but im trying my best!")
                                                                        print ("[4] Consider your problem solved.")
                                                                        print ()
                                                                        while True:
                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                            if (answer == '1') or (answer == '3'):
                                                                                print ()
                                                                                print ("Ahaha alright alright. Here, you can have this, hopefully you won't need it.")
                                                                                input ()
                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                inventory.append(items[1]) #ITEM
                                                                                input ()
                                                                                break

                                                                            elif (answer == '2') or (answer == '4'):
                                                                                print ()
                                                                                print ("We're counting on it! Here, take this, it will help you on your journey.")
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


                                                            elif (answer == '2'):
                                                                print ()
                                                                print ("Confident, I like it! I don't have a use for this anyway so you can have it regardless.")
                                                                input ()
                                                                print (friend, "gave you a", items[1] + "!")
                                                                inventory.append(items[1]) #ITEM
                                                                input ()
                                                                break

                                                            elif (answer == '3') or (answer == '4'):
                                                                print ()
                                                                print ("Ahaha alright alright here, you can have it.")
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

                                            
                                        elif friendship == 'bad':
                                            print ()
                                            print ("As you approach the door, you feel a sense of guilt and unwelcomed.", friend, "probably doesn't want to see you right now...")
                                            input ()
                                            
                                            
                                        elif friendship == 'neutral':
                                            print ("The house is nice and tidy. There's a fireplace being used to keep the house warm. The light of the fire illuminate the cozy home. You can relax for awhile before heading out, but you have an urgent mission!")
                                            if boy == 'dead':
                                                print ()
                                                print ("You see", friend, "grieving over their deceased brother.")
                                                print ()
                                                print ()
                                                print ("[1] How are you doing?") #potion/1atk
                                                print ("[2] I'll avenge him!") 
                                                print ("[3] The Sorcerer got away...")
                                                print ("[4] I'm sorry...") 
                                                print ()
                                                while True:
                                                    answer = input('Pick a dialogue option: ').strip()
                                                    if answer == '1':
                                                        print ()
                                                        print ("I'm okay, it's tough being home all alone now... but I guess I'll have to get used to it.")
                                                        print ()
                                                        print ()
                                                        print ("[1] Hang in there...")
                                                        print ("[2] Time heals all wounds")
                                                        print ("[3] It gets easier.")
                                                        print ("[4] I'm sorry for your loss.")
                                                        print ()
                                                        while True: 
                                                            answer = input('Pick a dialogue option: ').strip()
                                                            if (answer == '1') or (answer == '2') or (answer == '3') or (answer == '4'):
                                                                print ()
                                                                print ("Thank you,", player_name + ", you have been a great friend to me in these troubling times... I want you to have this, it'll keep you safe")
                                                                input ()
                                                                print (friend, "gave you a", items[1] + "!")
                                                                inventory.append(items[1]) #ITEM
                                                                relationship = 'good'
                                                                input ()
                                                                print ("Can you excuse me? I'd like some time to grieve.")
                                                                input ()
                                                                break

                                                            else:
                                                                print ()
                                                                print (wrong)
                                                        break

                                                    elif (answer == '2'):
                                                        print ()
                                                        print("Thank you for the sentiment", player_name + ", I appreciate it. You'll defeat that Sorcerer! I know it!")
                                                        print ()
                                                        print ()
                                                        print ("[1] Hang in there, things will get better.")
                                                        print ("[2] I'll T-bag him for you.")
                                                        print ("[3] I have no doubt I'll avenge your brother!")
                                                        print ("[4] He wont get away with this!")
                                                        print ()
                                                        while True: 
                                                            answer = input('Pick a dialogue option: ').strip()
                                                            if (answer == '1') or (answer == '2') or (answer == '3') or (answer == '4'):
                                                                print ()
                                                                print ("Thank you,", player_name + ", you have been a great friend to me in these troubling times... I want you to have this, it'll keep you safe")
                                                                input ()
                                                                print (friend, "gave you a", items[1] + "!")
                                                                inventory.append(items[1]) #ITEM
                                                                relationship = 'good'
                                                                input ()
                                                                print ("Can you excuse me? I'd like some time to grieve.")
                                                                input ()
                                                                break

                                                            else:
                                                                print ()
                                                                print (wrong)
                                                        break

                                                    elif answer == '3':
                                                        print ()
                                                        print ("I... it's okay, I can't blame you for trying. You'll get him next time, I believe in you!")
                                                        print ()
                                                        print()
                                                        print ()
                                                        print ("[1] He won't get away next time!")
                                                        print ("[2] He's got magic...")
                                                        print ("[3] I don't know... He's pretty strong.")
                                                        print ("[4] Placeholder reply4")
                                                        print ()
                                                        while True: 
                                                            answer = input('Pick a dialogue option: ').strip()
                                                            if (answer == '1') or (answer == '4'):
                                                                print ()
                                                                print ("Thank you,", player_name + ", you have been a great friend to me in these troubling times... I want you to have this, it'll keep you safe")
                                                                input ()
                                                                print (friend, "gave you a", items[1] + "!")
                                                                inventory.append(items[1]) #ITEM
                                                                relationship = 'good'
                                                                input ()
                                                                print ("Can you excuse me? I'd like some time to grieve.")
                                                                input ()
                                                                break

                                                            if (answer == '2') or (answer == '3'):
                                                                print ()
                                                                print ("Thank you,", player_name + ", you have been a great friend to me in these troubling times... I want you to have this, it'll keep you safe")
                                                                input ()
                                                                print (friend, "gave you a", items[1] + "!")
                                                                inventory.append(items[1]) #ITEM
                                                                relationship = 'good'
                                                                input ()
                                                                print ("Can you excuse me? I'd like some time to grieve.")
                                                                input ()
                                                                break

                                                            else:
                                                                print ()
                                                                print (wrong)
                                                        
                                                        break

                                                    elif answer == '4':
                                                        print ()
                                                        print ("It's okay", player_name + ", it's not your fault, but thank you for being here with me.")
                                                        print ()
                                                        print ()
                                                        print ()
                                                        print ("[1] Of course I'll be here for you.")
                                                        print ("[2] If you ever need to talk, I'm here for you.")
                                                        print ("[3] It was me, I killed him...")
                                                        print ("[4] If you need anything, let me know.")
                                                        print ()
                                                        while True:
                                                            answer = input('Pick a dialogue option: ').strip()
                                                            if (answer == '1') or (answer == '2') or (answer == '4'):
                                                                print ()
                                                                print ("Thank you,", player_name + ", you have been a great friend to me in these troubling times... I want you to have this, it'll keep you safe")
                                                                input ()
                                                                print (friend, "gave you a", items[1] + "!")
                                                                inventory.append(items[1]) #ITEM
                                                                relationship = 'good'
                                                                input ()
                                                                print ("Can you excuse me? I'd like some time to grieve.")
                                                                input ()
                                                                break

                                                            elif answer == '3':
                                                                print ()
                                                                print ("That's a cruel joke", player_name + ".")
                                                                print ()
                                                                print ()
                                                                print ()
                                                                print ("[1] I'm sorry I didn't mean that...")
                                                                print ("[2] It's not a joke.")
                                                                print ("[3] My bad, not the time and place.")
                                                                print ()
                                                                while True:
                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                    if (answer == '1') or (answer == '3'):
                                                                        print ()
                                                                        print ("That's okay, I know you're just trying to help. Can you excuse me? I'd like some time to grieve.")
                                                                        input ()
                                                                        break

                                                                    elif answer == '2':
                                                                        print ()
                                                                        print ("What?! I can't believe what I'm hearing... I don't know what to say or think.")
                                                                        print ()
                                                                        print ()
                                                                        print ()
                                                                        print ("[1] I'm kidding!!")
                                                                        print ("[2] DATTEBAYO ( Believe it! )")
                                                                        print ("[3] It was an accident! He scared me!")
                                                                        print ("[4] I'm so sorry.")
                                                                        print ()
                                                                        while True:
                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                            if answer == '1':
                                                                                print ()
                                                                                print ("This is not the time and place for jokes", player_name + ", you should go...")
                                                                                relationship = 'bad'
                                                                                input ()
                                                                                break

                                                                            elif answer == '2':
                                                                                print ()
                                                                                print("I'LL KILL YOU!!! SQUARE UP!")
                                                                                input ()
                                                                                print ()
                                                                                print ()
                                                                                print ("[1] Don't make me do this...")
                                                                                print ("[2] You're gonna regret this.")
                                                                                print ("[3] I'll slay you just like your brother.")
                                                                                print ("[4] I'm not fighting you.")
                                                                                print ()
                                                                                while True:
                                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                                    if (answer == '2') or (answer == '3'):
                                                                                        print ()
                                                                                        print ("You're not leaving here alive old friend.")
                                                                                        input ()
                                                                                        enemy_name = friend
                                                                                        enemy_dmg = 5
                                                                                        enemy_hp = 20
                                                                                        enemy_weapon = weapons[1]
                                                                                        battle()
                                                                                        print (enemy_name, "dropped a", weapons[1] + "!")
                                                                                        input ()
                                                                                        print ("You've slain your friend in cold blood rather easily. You stand over your friend's body with mixed feelings of victory and regret... or perhaps not.")
                                                                                        attackdmg = attackdmg + 1
                                                                                        relationship = 'dead'

                                                                                        break

                                                                                    elif (answer == '1') or (answer == '4'):
                                                                                        print ()
                                                                                        print ("Kill me like you killed my brother in cold blood!")
                                                                                        print ()
                                                                                        print ()
                                                                                        print ()
                                                                                        print ("[1] I didn't mean to...")
                                                                                        print ("[2] It was an accident, I'm sorry.")
                                                                                        print ("[3] You're gonna need a lot of potions for this...")
                                                                                        print ("[4] Come and get some then!")
                                                                                        print ()
                                                                                        while True:
                                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                                            if (answer == '4') or (answer == '3'):
                                                                                                print ()
                                                                                                print ("You're not leaving here alive old friend.")
                                                                                                input ()
                                                                                                enemy_name = friend
                                                                                                enemy_dmg = 5
                                                                                                enemy_hp = 20
                                                                                                enemy_weapon = weapons[1]
                                                                                                battle()
                                                                                                print (enemy_name, "dropped a", weapons[1] + "!")
                                                                                                input ()
                                                                                                print ("You've slain your friend in cold blood rather easily. You stand over your friend's body with mixed feelings of power and regret... or perhaps not.")
                                                                                                attackdmg = attackdmg + 1
                                                                                                relationship = 'dead'
                                                                                                break

                                                                                            elif (answer == '1') or (answer == '2'):
                                                                                                print ()
                                                                                                print ("I...! I can't even look at you,", player_name + ", leave me...please.")
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

                                                                            elif (answer == '3') or (answer == '4'):
                                                                                print ()
                                                                                print ("I'm... I can't...")
                                                                                input ()
                                                                                print ("I can't fully blame you for his death, he was always clueless... but still.")
                                                                                input ()
                                                                                print ("Can you excuse me? I'd like some time to grieve.")
                                                                                input ()
                                                                                relationship = 'bad'
                                                                                break
                                                                            
                                                                            else:
                                                                                print ()
                                                                                print (wrong)
                                                                        break

                                                                        

                                                                    else:
                                                                        print ()
                                                                        print (wrong)
                                                                break


                                                            else:
                                                                print ()
                                                                print (wrong)
                                                                
                                                        break

                                                    else:
                                                        print ()
                                                        print (wrong)
                                                break
                                                                                            
                                            elif boy == 'alive':
                                                print ()
                                                print ("You see", friend, "and their brother lounging.")
                                                print ("Hey", player_name + ", did you defeat the Sorcerer?")
                                                print ()
                                                print ()
                                                print ()
                                                print ("[1] Not yet...but soon!")
                                                print ("[2] It's harder than it looks...")
                                                print ("[3] The Sorcerer got away...")
                                                print ("[4] Easily!") 
                                                print ()
                                                while True: 
                                                    answer = input('Pick a dialogue option: ').strip()
                                                    if answer == '1':
                                                        print ()
                                                        print ("Alright, we're counting on you", player_name + "! Here have this, it will help you beat the sorcerer.")
                                                        input ()
                                                        print (friend, "gave you a", items[1] + "!")
                                                        inventory.append(items[1]) #ITEM
                                                        input ()
                                                        break

                                                    elif answer == '2':
                                                        print ()
                                                        print("I believe you! I wouldn't want to be fighting a magic weilder either! Here have this, it will help you beat the sorcerer.")
                                                        input ()
                                                        print (friend, "gave you a", items[1] + "!")
                                                        inventory.append(items[1]) #ITEM
                                                        input ()
                                                        break

                                                    elif answer == '3':
                                                        print ()
                                                        print ("Damn him! are you going after him?")
                                                        print ()
                                                        print ()
                                                        print ()
                                                        print ("[1] Of course.")
                                                        print ("[2] I'm just relaxing for now.")
                                                        print ("[3] He'll come to me.")
                                                        print ("[4] I'm going right now!")
                                                        print ()
                                                        while True:
                                                            answer = input('Pick a dialogue option: ').strip()
                                                            if (answer == '2') or (answer == '3'):
                                                                print ()
                                                                print ("Confident, I like it! but take this, You'll need it.")
                                                                input ()
                                                                print (friend, "gave you a", items[1] + "!")
                                                                inventory.append(items[1]) #ITEM
                                                                input ()
                                                                break

                                                            elif (answer == '4') or (answer == '1'):
                                                                print ()
                                                                print ("Alright, but take this! You'll need it.")
                                                                input ()
                                                                print (friend, "gave you a", items[1] + "!")
                                                                inventory.append(items[1]) #ITEM
                                                                input ()
                                                                break

                                                            else:
                                                                print ()
                                                                print (wrong)
                                                        break


                                                    elif answer == '4':
                                                        print ()
                                                        print ("Wow awesome, didn't doubt you! I was gonna give you this item but it doesn't look like you'll need it.")
                                                        print ()
                                                        print ()
                                                        print ()
                                                        print ("[1] I was kidding... He's still out there.")
                                                        print ("[2] Yeah I won't be needing it.")
                                                        print ("[3] Consider it my reward.")
                                                        print ("[4] Oh.... Please?")
                                                        print ()
                                                        while True:
                                                            answer = input('Pick a dialogue option: ').strip()
                                                            if (answer == '1'):
                                                                print ()
                                                                print ("I knew it, you may be good... but you're not THAT good!")
                                                                print ()
                                                                print ()
                                                                print ("[1] I'll get him next time!")
                                                                print ("[2] What's that supposed to mean?")
                                                                print ("[3] I'm EXACTLY that good!")
                                                                print ("[4] I just need a little more time.")
                                                                print ()
                                                                while True:
                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                    if answer == '1':
                                                                        print ()
                                                                        print ("I believe you, you haven't let me down yet... well I guess this time you did.")
                                                                        print ()
                                                                        print ()
                                                                        print ()
                                                                        print ("[1] It wont happen again.")
                                                                        print ("[2] I'll try harder next time.")
                                                                        print ("[3] I'm sorry.")
                                                                        print ("[4] You can go and fight him if you want.")
                                                                        print ()
                                                                        while True:
                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                            if (answer == '3') or (answer == '1') or (answer == '2') or (answer == '4'):
                                                                                print ()
                                                                                print ("Ahaha I'm kidding, you're doing great! Here have this, it will help you beat the sorcerer.")
                                                                                input ()
                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                inventory.append(items[1]) #ITEM
                                                                                input ()
                                                                                break

                                                                            else:
                                                                                print ()
                                                                                print (wrong)
                                                                        break


                                                                    elif (answer == '2') or (answer == '4'):
                                                                                print ()
                                                                                print ("Ahaha I'm kidding, you're good", player_name + "! The best! you'll beat the sorcerer. Here have this, consider it my contribution to your battle.")
                                                                                input ()
                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                inventory.append(items[1]) #ITEM
                                                                                input ()
                                                                                break

                                                                    elif (answer == '3'):
                                                                        print ()
                                                                        print ("Riiiight, that's why we have a magic weilding terrorist in the area.")
                                                                        print ()
                                                                        print ()
                                                                        print ("[1] Point taken")
                                                                        print ("[2] I'm gonna handle it!")
                                                                        print ("[3] Okay fine, but im trying my best!")
                                                                        print ("[4] Consider your problem solved.")
                                                                        print ()
                                                                        while True:
                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                            if (answer == '1') or (answer == '3'):
                                                                                print ()
                                                                                print ("Ahaha alright alright. Here, you can have this, hopefully you won't need it.")
                                                                                input ()
                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                inventory.append(items[1]) #ITEM
                                                                                input ()
                                                                                break

                                                                            elif (answer == '2') or (answer == '4'):
                                                                                print ()
                                                                                print ("We're counting on it! Here, take this, it will help you on your journey.")
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


                                                            elif (answer == '2'):
                                                                print ()
                                                                print ("Confident, I like it! I don't have a use for this anyway so you can have it regardless.")
                                                                input ()
                                                                print (friend, "gave you a", items[1] + "!")
                                                                inventory.append(items[1]) #ITEM
                                                                input ()
                                                                break

                                                            elif (answer == '3') or (answer == '4'):
                                                                print ()
                                                                print ("Ahaha alright alright here, you can have it.")
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
                                            
                                        print ()
                                        input ()

                                    if talked == True:
                                        print ()
                                        print (friend, "is occupied right now, maybe you should come back later.")
                                        input ()
                                
                            elif answer == 'leave':
                                    break
                            else:
                                    print ()
                                    print (wrong)
                                    print ()
                                    
            else:
                print ()
                print (wrong)
                print ()