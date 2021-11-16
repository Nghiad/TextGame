def future_explore(player_name, friend, inventory, items, talked, wrong):
    print ()
    print ("You charged the energy sphere only to get hit directly by the Sorcerer's energy!")
    input ()
    print ("The blast knocks you out.")
    input ()
    print ("You regain consciousness after awhile.")
    input ()
    print ("You wake up at the temple where you were knocked down. The Sorcerer is gone alone with the power crystal's energy. You have to stop him before he uses up all the energy!\
He must have returned to the woods! The energy blast that hit you has also made you feel stronger.")
    input ()
    print ("You're at the temple. The temple is old but nothing out of the ordinary. Nothing else here interests you.")
    input ()
    print ("You exit the temple to a familiar world.")
    input ()
    print ("You can proceed to the woods, or you can go to the crossroads; one way leading to the farm, one leading to the grassfields, and last path leading to the temple behind you.")
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

                    bad_temple()

                    print ()
                    print ("You're at the temple. It looks old but nothing out of the ordinary.")
                    print ()
                    input ()
                    
            elif answer == 'grassfields':
                    print ()

                    bad_grassfield()

                    print ()
                    print ("You're at the grassfields.")
                    print ("Parts of the grass are dead, while others are overgrown and lush.")
                    input ()
                    
            elif answer =='farm':
                    while True:
                            print ()
                            print ('You stand in the middle of a desolate farm. The smell of burned ash lingers.')
                            print ()
                            answer = input("Where do you want to go? (house/barn/leave) ").lower().strip()
                            if answer == 'barn':
                                    print ()
                                    print ()
                                    print ()
                                    print ()
                                    print ()

                                    bad_barn()

                                    print ()
                                    print ("You're at the barn") 
                                    print ("You see an abandoned barn. It doesn't seem to have been touched in awhile. There are large patches of holes in the ceiling, making it inhabitable.")
                                    print ()
                                    input ()
                                    
                            elif answer == 'house':
                                    print ()
                                    print ()
                                    print ()
                                    print ()
                                    print ()

                                    bad_house()

                                    print ()
                                    print ("You're at", friend + "'s house") 
                                    print ("The home is messy and disorganized; a variety of boxes, packages, and junk are scattered around the various rooms of the house. Although", friend, "is not home, you probably shouldn't be snooping around.")                                
                                    if talked == False:
                                        talked = True
                                        if boy == 'dead':
                                            
                                            if friendship == 'good':
                                                print ()
                                                print ("You see an older, matured", friend + ", it is evident that a lot of time has passed since you last seen him.")
                                                print ()
                                                print ("Wow its good to see you,", player_name + "! I thought you died at the Temple all those years ago... how long has it been? 15 years? Where have you been?")
                                                print ()
                                                print ()
                                                print ("[1] What do you mean its been 15 years?!")
                                                print ("[2] You did not age well.")
                                                print ("[3] Where's your brother?")
                                                print ("[4] How are you?")
                                                print ()
                                                while True:
                                                    answer = input('Pick a dialogue option: ').strip()
                                                    if answer == '1':
                                                        print ()
                                                        print ("The last time I saw you, you were headed towards the Temple, and that was 15 years ago. As you can see, a lot of time has passed.")
                                                        print ()
                                                        print ()
                                                        print ()
                                                        print ("[1] Where's the Sorcerer?")
                                                        print ("[2] What happened here?")
                                                        print ("[3] You look a little gray.")
                                                        print ("[4] Are you okay?")
                                                        print ()
                                                        while True:
                                                            answer = input('Pick a dialogue option: ').strip()
                                                            if answer == '1':
                                                                print ()
                                                                print ("The Sorcerer? He disappeared with you 15 years ago... ")
                                                                print ()
                                                                print ()
                                                                print ()
                                                                print ("[1] What happened here then?")
                                                                print ("[2] I'm here for a rematch.")
                                                                print ("[3] I told you I'd get rid of him!")
                                                                print ("[4] Where did he go?")
                                                                print ()
                                                                while True:
                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                    if answer == '1':
                                                                        print ()
                                                                        print ("Well since you, the sorcerer, and power crystal disappeared, our village has been vulnerable to monsters. They ravaged the land.")
                                                                        input ()
                                                                        print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
                                                                        print (friend, "gave you a", items[1] + "!")
                                                                        inventory.append(items[1]) #ITEM
                                                                        input ()
                                                                        break


                                                                    elif (answer == '2'):
                                                                        print ()
                                                                        print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
                                                                        print (friend, "gave you a", items[1] + "!")
                                                                        inventory.append(items[1]) #ITEM
                                                                        input ()
                                                                        break

                                                                    elif answer == '3':
                                                                        print ()
                                                                        print("Still got the jokes I see. Good to see you haven't changed,", player_name + ".")
                                                                        relationship = 'neutral'
                                                                        print ()
                                                                        print ()
                                                                        print ()
                                                                        print ("[1] You too,", friend)
                                                                        print ("[2] Always.")
                                                                        print ("[3] Why would I change?")
                                                                        print ("[4] I haven't changed clothes in 15 years either...")
                                                                        print ()
                                                                        while True:
                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                            if (answer == '1') or (answer == '2') or (answer == '3') or (answer == '4'):
                                                                                print ()
                                                                                print ("Listen, I'd love to stay and catch up but I have to go, the monsters are coming more and more often. Someone needs to deal with them. You being here is no coincidence.")
                                                                                print ()
                                                                                print ()
                                                                                print ()
                                                                                print ("[1] What do you mean?")
                                                                                print ("[2] What are you suggesting?")
                                                                                print ("[3] Where is the Sorcerer?")
                                                                                print ("[4] What do you need me to do?")
                                                                                print ()
                                                                                while True:
                                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                                    if (answer == '1') or (answer == '2'):
                                                                                        print ()
                                                                                        print ("You appearing 15 years later is riling them up...You or perhaps the Sorcerer has also returned?")
                                                                                        print ()
                                                                                        print ()
                                                                                        print ()
                                                                                        print ("[1] I'll take care of the Sorcerer.")
                                                                                        print ("[2] Where is he?")
                                                                                        print ("[3] I'll help you take care of all these monsters, don't you worry.")
                                                                                        print ("[4] Listen, I didn't sign up for this...")
                                                                                        print ()
                                                                                        while True:
                                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                                            if (answer == '1') or (answer =='3'):
                                                                                                print ()
                                                                                                print ("Thank you", player_name +", I'm glad you're back.")
                                                                                                input ()
                                                                                                print ("Here take this, It'll certainly help you")
                                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                                inventory.append(items[1]) #ITEM
                                                                                                input ()
                                                                                                break

                                                                                            elif answer == '2':
                                                                                                print ()
                                                                                                print("I don't know, but if I had to guess, it'd be the woods.")
                                                                                                input ()
                                                                                                print ("Be careful, take this with you, I'm sure you'll find a good use for it.")
                                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                                inventory.append(items[1]) #ITEM
                                                                                                input ()
                                                                                                break

                                                                                            elif answer == '4':
                                                                                                print ()
                                                                                                print ("No you didn't, but you're a part of this now, you must do this!")
                                                                                                input ()
                                                                                                print ("Here take this, It'll certainly help you")
                                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                                inventory.append(items[1]) #ITEM
                                                                                                input ()
                                                                                                break

                                                                                            else:
                                                                                                print ()
                                                                                                print (wrong)
                                                                                        break


                                                                                    elif (answer == '3') or (answer == '4'):
                                                                                        print ()
                                                                                        print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                                        input ()
                                                                                        print ("Here take this, It'll certainly help you")
                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                        inventory.append(items[1]) #ITEM
                                                                                        input ()
                                                                                        break

                                                                                    else:
                                                                                        print ()
                                                                                        print (wrong)
                                                                                break

                                                                            else:
                                                                                print (wrong)
                                                                        break

                                                                    elif (answer == '4'):
                                                                        print ()
                                                                        print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
                                                                        print (friend, "gave you a", items[1] + "!")
                                                                        inventory.append(items[1]) #ITEM
                                                                        input ()
                                                                        break

                                                                    else:
                                                                        print (wrong)
                                                                break


                                                            elif answer == '2':
                                                                print ()
                                                                print("He's...passed away. Monsters attacked the farm and I just couldn't stop them.")
                                                                print ()
                                                                print ()
                                                                print ()
                                                                print ("[1] I'm sorry to hear that.")
                                                                print ("[2] I'll avenge him!")
                                                                print ("[3] Do you need anything?")
                                                                print ("[4] Point me to the nearest monster!")
                                                                print ()
                                                                while True:
                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                    if (answer == '1') or (answer == '3'):
                                                                        print ()
                                                                        print ("Don't worry about me", player_name + ", but I do need your help to fight back! I believe the Sorcerer is back. Please go deal with him.")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
                                                                        print (friend, "gave you a", items[1] + "!")
                                                                        inventory.append(items[1]) #ITEM
                                                                        input ()
                                                                        break

                                                                    elif (answer == '4') or (answer == '2'):
                                                                        print ()
                                                                        print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
                                                                        print (friend, "gave you a", items[1] + "!")
                                                                        inventory.append(items[1]) #ITEM
                                                                        input ()
                                                                        break

                                                                    else:
                                                                        print ()
                                                                        print (wrong)
                                                                break


                                                            elif answer == '3':
                                                                print ()
                                                                print("Still got the jokes I see. Good to see you haven't changed,", player_name + ".")
                                                                relationship = 'neutral'
                                                                print ()
                                                                print ()
                                                                print ()
                                                                print ("[1] You too,", friend)
                                                                print ("[2] Always.")
                                                                print ("[3] Why would I change?")
                                                                print ("[4] I haven't changed clothes in 15 years either...")
                                                                print ()
                                                                while True:
                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                    if (answer == '1') or (answer == '2') or (answer == '3') or (answer == '4'):
                                                                        print ()
                                                                        print ("Listen, I'd love to stay and catch up but I have to go, the monsters are coming more and more often. Someone needs to deal with them. You being here is no coincidence.")
                                                                        print ()
                                                                        print ()
                                                                        print ()
                                                                        print ("[1] What do you mean?")
                                                                        print ("[2] What are you suggesting?")
                                                                        print ("[3] Where is the Sorcerer?")
                                                                        print ("[4] What do you need me to do?")
                                                                        print ()
                                                                        while True:
                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                            if (answer == '1') or (answer == '2'):
                                                                                print ()
                                                                                print ("You appearing 15 years later is riling them up...You or perhaps the Sorcerer has also returned?")
                                                                                print ()
                                                                                print ()
                                                                                print ()
                                                                                print ("[1] I'll take care of the Sorcerer.")
                                                                                print ("[2] Where is he?")
                                                                                print ("[3] I'll help you take care of all these monsters, don't you worry.")
                                                                                print ("[4] Listen, I didn't sign up for this...")
                                                                                print ()
                                                                                while True:
                                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                                    if (answer == '1') or (answer =='3'):
                                                                                        print ()
                                                                                        print ("Thank you", player_name +", I'm glad you're back.")
                                                                                        input ()
                                                                                        print ("Here take this, It'll certainly help you")
                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                        inventory.append(items[1]) #ITEM
                                                                                        input ()
                                                                                        break

                                                                                    elif answer == '2':
                                                                                        print ()
                                                                                        print("I don't know, but if I had to guess, it'd be the woods.")
                                                                                        input ()
                                                                                        print ("Be careful, take this with you, I'm sure you'll find a good use for it.")
                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                        inventory.append(items[1]) #ITEM
                                                                                        input ()
                                                                                        break

                                                                                    elif answer == '4':
                                                                                        print ()
                                                                                        print ("No you didn't, but you're a part of this now, you must do this!")
                                                                                        input ()
                                                                                        print ("Here take this, It'll certainly help you")
                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                        inventory.append(items[1]) #ITEM
                                                                                        input ()
                                                                                        break

                                                                                    else:
                                                                                        print ()
                                                                                        print (wrong)
                                                                                break


                                                                            elif (answer == '3') or (answer == '4'):
                                                                                print ()
                                                                                print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                                input ()
                                                                                print ("Here take this, It'll certainly help you")
                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                inventory.append(items[1]) #ITEM
                                                                                input ()
                                                                                break

                                                                            else:
                                                                                print ()
                                                                                print (wrong)
                                                                        break

                                                                    else:
                                                                        print (wrong)
                                                                break

                                                            elif answer == '4':
                                                                print ()
                                                                print ("I've been managing, ever since my brother passed, its just been me here, lost all the animals too.")
                                                                print ()
                                                                print ()
                                                                print ()
                                                                print ("[1] I'm sorry to hear that.")
                                                                print ("[2] What happened?")
                                                                print ("[3] Did the Sorcerer do this?")
                                                                print ("[4] Are you gonna be ok?")
                                                                print ()
                                                                while True:
                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                    if (answer == '1') or (answer == '4'):
                                                                        print ()
                                                                        print ("Don't worry about me", player_name + ", but I do need your help to fight back! I believe the Sorcerer is back. Please go deal with him.")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
                                                                        print (friend, "gave you a", items[1] + "!")
                                                                        inventory.append(items[1]) #ITEM
                                                                        input ()
                                                                        break

                                                                    elif answer == '2':
                                                                        print ()
                                                                        print ("Well since you, the sorcerer, and power crystal disappeared, our village has been vulnerable to monsters. They ravaged the land. But there's still hope, you!")
                                                                        input ()
                                                                        print ("I'm gonna need you to find and deal with the Sorcerer once and for all! I have a feeling all this is his doing. My guess is that he's in the mysterious woods!")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
                                                                        print (friend, "gave you a", items[1] + "!")
                                                                        inventory.append(items[1]) #ITEM
                                                                        input ()
                                                                        break

                                                                    elif answer == '3':
                                                                        print ()
                                                                        print ("Not him specifically... But I feel he's somehow the cause of it.")
                                                                        input ()
                                                                        print ("I'm gonna need you to find and deal with the Sorcerer once and for all! I have a feeling all this is his doing. My guess is that he's in the mysterious woods!")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
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
                                                        print("Still got the jokes I see. Good to see you haven't changed,", player_name + ".")
                                                        relationship = 'neutral'
                                                        print ()
                                                        print ()
                                                        print ()
                                                        print ("[1] You too,", friend)
                                                        print ("[2] Always.")
                                                        print ("[3] Why would I change?")
                                                        print ("[4] I haven't changed clothes in 15 years either...")
                                                        print ()
                                                        while True:
                                                            answer = input('Pick a dialogue option: ').strip()
                                                            if (answer == '1') or (answer == '2') or (answer == '3') or (answer == '4'):
                                                                print ()
                                                                print ("Listen, I'd love to stay and catch up but I have to go, the monsters are coming more and more often. Someone needs to deal with them. You being here is no coincidence.")
                                                                print ()
                                                                print ()
                                                                print ()
                                                                print ("[1] What do you mean?")
                                                                print ("[2] What are you suggesting?")
                                                                print ("[3] Where is the Sorcerer?")
                                                                print ("[4] What do you need me to do?")
                                                                print ()
                                                                while True:
                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                    if (answer == '1') or (answer == '2'):
                                                                        print ()
                                                                        print ("You appearing 15 years later is riling them up...You or perhaps the Sorcerer has also returned?")
                                                                        print ()
                                                                        print ()
                                                                        print ()
                                                                        print ("[1] I'll take care of the Sorcerer.")
                                                                        print ("[2] Where is he?")
                                                                        print ("[3] I'll help you take care of all these monsters, don't you worry.")
                                                                        print ("[4] Listen, I didn't sign up for this...")
                                                                        print ()
                                                                        while True:
                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                            if (answer == '1') or (answer =='3'):
                                                                                print ()
                                                                                print ("Thank you", player_name +", I'm glad you're back.")
                                                                                input ()
                                                                                print ("Here take this, It'll certainly help you")
                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                inventory.append(items[1]) #ITEM
                                                                                input ()
                                                                                break

                                                                            elif answer == '2':
                                                                                print ()
                                                                                print("I don't know, but if I had to guess, it'd be the woods.")
                                                                                input ()
                                                                                print ("Be careful, take this with you, I'm sure you'll find a good use for it.")
                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                inventory.append(items[1]) #ITEM
                                                                                input ()
                                                                                break

                                                                            elif answer == '4':
                                                                                print ()
                                                                                print ("No you didn't, but you're a part of this now, you must do this!")
                                                                                input ()
                                                                                print ("Here take this, It'll certainly help you")
                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                inventory.append(items[1]) #ITEM
                                                                                input ()
                                                                                break

                                                                            else:
                                                                                print ()
                                                                                print (wrong)
                                                                        break


                                                                    elif (answer == '3') or (answer == '4'):
                                                                        print ()
                                                                        print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
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


                                                    elif answer == '3':
                                                        print ()
                                                        print ("What do you mean? I haven't seen you in 15 years. We've both aged.")
                                                        print ()
                                                        print ()
                                                        print ()
                                                        print ("[1] I woke up at the Temple an hour ago...")
                                                        print ("[2] I don't remember anything in the last 15 years.")
                                                        print ("[3] Have you seen the Sorcerer?")
                                                        print ("[4] At least one of us aged well.")
                                                        print ()
                                                        while True:
                                                            answer = input('Pick a dialogue option: ').strip()
                                                            if (answer == '1') or (answer == '2'):
                                                                print ()
                                                                print ("That doesn't make sense...either you've been hit with a spell or you just have terrible memory...")
                                                                print ()
                                                                print ()
                                                                print ()
                                                                print ("[1] Where's the Sorcerer?")
                                                                print ("[2] My memory isn't that bad...")
                                                                print ("[3] I drank a lot of coffee as a kid.")
                                                                print ("[4] Who're you again?")
                                                                print ()
                                                                while True:
                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                    if answer == '1':
                                                                        print ()
                                                                        print ("The Sorcerer? He disappeared with you 15 years ago... ")
                                                                        print ()
                                                                        print ()
                                                                        print ()
                                                                        print ("[1] What happened here then?")
                                                                        print ("[2] I'm here for a rematch.")
                                                                        print ("[3] I told you I'd get rid of him!")
                                                                        print ("[4] Where did he go?")
                                                                        print ()
                                                                        while True:
                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                            if answer == '1':
                                                                                print ()
                                                                                print ("Well since you, the sorcerer, and power crystal disappeared, our village has been vulnerable to monsters. They ravaged the land.")
                                                                                input ()
                                                                                print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                                input ()
                                                                                print ("Here take this, It'll certainly help you")
                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                inventory.append(items[1]) #ITEM
                                                                                input ()
                                                                                break


                                                                            elif (answer == '2'):
                                                                                print ()
                                                                                print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                                input ()
                                                                                print ("Here take this, It'll certainly help you")
                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                inventory.append(items[1]) #ITEM
                                                                                input ()
                                                                                break

                                                                            elif answer == '3':
                                                                                print ()
                                                                                print("Still got the jokes I see. Good to see you haven't changed,", player_name + ".")
                                                                                relationship = 'neutral'
                                                                                print ()
                                                                                print ()
                                                                                print ()
                                                                                print ("[1] You too,", friend)
                                                                                print ("[2] Always.")
                                                                                print ("[3] Why would I change?")
                                                                                print ("[4] I haven't changed clothes in 15 years either...")
                                                                                print ()
                                                                                while True:
                                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                                    if (answer == '1') or (answer == '2') or (answer == '3') or (answer == '4'):
                                                                                        print ()
                                                                                        print ("Listen, I'd love to stay and catch up but I have to go, the monsters are coming more and more often. Someone needs to deal with them. You being here is no coincidence.")
                                                                                        print ()
                                                                                        print ()
                                                                                        print ()
                                                                                        print ("[1] What do you mean?")
                                                                                        print ("[2] What are you suggesting?")
                                                                                        print ("[3] Where is the Sorcerer?")
                                                                                        print ("[4] What do you need me to do?")
                                                                                        print ()
                                                                                        while True:
                                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                                            if (answer == '1') or (answer == '2'):
                                                                                                print ()
                                                                                                print ("You appearing 15 years later is riling them up...You or perhaps the Sorcerer has also returned?")
                                                                                                print ()
                                                                                                print ()
                                                                                                print ()
                                                                                                print ("[1] I'll take care of the Sorcerer.")
                                                                                                print ("[2] Where is he?")
                                                                                                print ("[3] I'll help you take care of all these monsters, don't you worry.")
                                                                                                print ("[4] Listen, I didn't sign up for this...")
                                                                                                print ()
                                                                                                while True:
                                                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                                                    if (answer == '1') or (answer =='3'):
                                                                                                        print ()
                                                                                                        print ("Thank you", player_name +", I'm glad you're back.")
                                                                                                        input ()
                                                                                                        print ("Here take this, It'll certainly help you")
                                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                                        inventory.append(items[1]) #ITEM
                                                                                                        input ()
                                                                                                        break

                                                                                                    elif answer == '2':
                                                                                                        print ()
                                                                                                        print("I don't know, but if I had to guess, it'd be the woods.")
                                                                                                        input ()
                                                                                                        print ("Be careful, take this with you, I'm sure you'll find a good use for it.")
                                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                                        inventory.append(items[1]) #ITEM
                                                                                                        input ()
                                                                                                        break

                                                                                                    elif answer == '4':
                                                                                                        print ()
                                                                                                        print ("No you didn't, but you're a part of this now, you must do this!")
                                                                                                        input ()
                                                                                                        print ("Here take this, It'll certainly help you")
                                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                                        inventory.append(items[1]) #ITEM
                                                                                                        input ()
                                                                                                        break

                                                                                                    else:
                                                                                                        print ()
                                                                                                        print (wrong)
                                                                                                break


                                                                                            elif (answer == '3') or (answer == '4'):
                                                                                                print ()
                                                                                                print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                                                input ()
                                                                                                print ("Here take this, It'll certainly help you")
                                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                                inventory.append(items[1]) #ITEM
                                                                                                input ()
                                                                                                break

                                                                                            else:
                                                                                                print ()
                                                                                                print (wrong)
                                                                                        break

                                                                                    else:
                                                                                        print (wrong)
                                                                                break

                                                                            elif (answer == '4'):
                                                                                print ()
                                                                                print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                                input ()
                                                                                print ("Here take this, It'll certainly help you")
                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                inventory.append(items[1]) #ITEM
                                                                                input ()
                                                                                break

                                                                            else:
                                                                                print (wrong)
                                                                        break

                                                                    elif (answer == '2') or (answer == '3'):
                                                                        print ()
                                                                        print("I think you were hit by a spell, perhaps defeating the Sorcerer will undo the spell...")
                                                                        input ()
                                                                        print ("You're gonna need to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
                                                                        print (friend, "gave you a", items[1] + "!")
                                                                        inventory.append(items[1]) #ITEM
                                                                        input ()
                                                                        break


                                                                    elif answer == '4':
                                                                        print ()
                                                                        print("Still got the jokes I see. Good to see you haven't changed,", player_name + ".")
                                                                        relationship = 'neutral'
                                                                        print ()
                                                                        print ()
                                                                        print ()
                                                                        print ("[1] You too,", friend)
                                                                        print ("[2] Always.")
                                                                        print ("[3] Why would I change?")
                                                                        print ("[4] I haven't changed clothes in 15 years either...")
                                                                        print ()
                                                                        while True:
                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                            if (answer == '1') or (answer == '2') or (answer == '3') or (answer == '4'):
                                                                                print ()
                                                                                print ("Listen, I'd love to stay and catch up but I have to go, the monsters are coming more and more often. Someone needs to deal with them. You being here is no coincidence.")
                                                                                print ()
                                                                                print ()
                                                                                print ()
                                                                                print ("[1] What do you mean?")
                                                                                print ("[2] What are you suggesting?")
                                                                                print ("[3] Where is the Sorcerer?")
                                                                                print ("[4] What do you need me to do?")
                                                                                print ()
                                                                                while True:
                                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                                    if (answer == '1') or (answer == '2'):
                                                                                        print ()
                                                                                        print ("You appearing 15 years later is riling them up...You or perhaps the Sorcerer has also returned?")
                                                                                        print ()
                                                                                        print ()
                                                                                        print ()
                                                                                        print ("[1] I'll take care of the Sorcerer.")
                                                                                        print ("[2] Where is he?")
                                                                                        print ("[3] I'll help you take care of all these monsters, don't you worry.")
                                                                                        print ("[4] Listen, I didn't sign up for this...")
                                                                                        print ()
                                                                                        while True:
                                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                                            if (answer == '1') or (answer =='3'):
                                                                                                print ()
                                                                                                print ("Thank you", player_name +", I'm glad you're back.")
                                                                                                input ()
                                                                                                print ("Here take this, It'll certainly help you")
                                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                                inventory.append(items[1]) #ITEM
                                                                                                input ()
                                                                                                break

                                                                                            elif answer == '2':
                                                                                                print ()
                                                                                                print("I don't know, but if I had to guess, it'd be the woods.")
                                                                                                input ()
                                                                                                print ("Be careful, take this with you, I'm sure you'll find a good use for it.")
                                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                                inventory.append(items[1]) #ITEM
                                                                                                input ()
                                                                                                break

                                                                                            elif answer == '4':
                                                                                                print ()
                                                                                                print ("No you didn't, but you're a part of this now, you must do this!")
                                                                                                input ()
                                                                                                print ("Here take this, It'll certainly help you")
                                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                                inventory.append(items[1]) #ITEM
                                                                                                input ()
                                                                                                break

                                                                                            else:
                                                                                                print ()
                                                                                                print (wrong)
                                                                                        break


                                                                                    elif (answer == '3') or (answer == '4'):
                                                                                        print ()
                                                                                        print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                                        input ()
                                                                                        print ("Here take this, It'll certainly help you")
                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                        inventory.append(items[1]) #ITEM
                                                                                        input ()
                                                                                        break

                                                                                    else:
                                                                                        print ()
                                                                                        print (wrong)
                                                                                break

                                                                            else:
                                                                                print (wrong)
                                                                        break
                                                                    
                                                                    else:
                                                                        print ()
                                                                        print (wrong)
                                                                break


                                                            elif answer == '3':
                                                                print ()
                                                                print ("The Sorcerer? He disappeared with you 15 years ago... ")
                                                                print ()
                                                                print ()
                                                                print ()
                                                                print ("[1] What happened here then?")
                                                                print ("[2] I'm here for a rematch.")
                                                                print ("[3] I told you I'd get rid of him!")
                                                                print ("[4] Where did he go?")
                                                                print ()
                                                                while True:
                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                    if answer == '1':
                                                                        print ()
                                                                        print ("Well since you, the sorcerer, and power crystal disappeared, our village has been vulnerable to monsters. They ravaged the land.")
                                                                        input ()
                                                                        print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
                                                                        print (friend, "gave you a", items[1] + "!")
                                                                        inventory.append(items[1]) #ITEM
                                                                        input ()
                                                                        break


                                                                    elif (answer == '2'):
                                                                        print ()
                                                                        print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
                                                                        print (friend, "gave you a", items[1] + "!")
                                                                        inventory.append(items[1]) #ITEM
                                                                        input ()
                                                                        break

                                                                    elif answer == '3':
                                                                        print ()
                                                                        print("Still got the jokes I see. Good to see you haven't changed,", player_name + ".")
                                                                        relationship = 'neutral'
                                                                        print ()
                                                                        print ()
                                                                        print ()
                                                                        print ("[1] You too,", friend)
                                                                        print ("[2] Always.")
                                                                        print ("[3] Why would I change?")
                                                                        print ("[4] I haven't changed clothes in 15 years either...")
                                                                        print ()
                                                                        while True:
                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                            if (answer == '1') or (answer == '2') or (answer == '3') or (answer == '4'):
                                                                                print ()
                                                                                print ("Listen, I'd love to stay and catch up but I have to go, the monsters are coming more and more often. Someone needs to deal with them. You being here is no coincidence.")
                                                                                print ()
                                                                                print ()
                                                                                print ()
                                                                                print ("[1] What do you mean?")
                                                                                print ("[2] What are you suggesting?")
                                                                                print ("[3] Where is the Sorcerer?")
                                                                                print ("[4] What do you need me to do?")
                                                                                print ()
                                                                                while True:
                                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                                    if (answer == '1') or (answer == '2'):
                                                                                        print ()
                                                                                        print ("You appearing 15 years later is riling them up...You or perhaps the Sorcerer has also returned?")
                                                                                        print ()
                                                                                        print ()
                                                                                        print ()
                                                                                        print ("[1] I'll take care of the Sorcerer.")
                                                                                        print ("[2] Where is he?")
                                                                                        print ("[3] I'll help you take care of all these monsters, don't you worry.")
                                                                                        print ("[4] Listen, I didn't sign up for this...")
                                                                                        print ()
                                                                                        while True:
                                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                                            if (answer == '1') or (answer =='3'):
                                                                                                print ()
                                                                                                print ("Thank you", player_name +", I'm glad you're back.")
                                                                                                input ()
                                                                                                print ("Here take this, It'll certainly help you")
                                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                                inventory.append(items[1]) #ITEM
                                                                                                input ()
                                                                                                break

                                                                                            elif answer == '2':
                                                                                                print ()
                                                                                                print("I don't know, but if I had to guess, it'd be the woods.")
                                                                                                input ()
                                                                                                print ("Be careful, take this with you, I'm sure you'll find a good use for it.")
                                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                                inventory.append(items[1]) #ITEM
                                                                                                input ()
                                                                                                break

                                                                                            elif answer == '4':
                                                                                                print ()
                                                                                                print ("No you didn't, but you're a part of this now, you must do this!")
                                                                                                input ()
                                                                                                print ("Here take this, It'll certainly help you")
                                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                                inventory.append(items[1]) #ITEM
                                                                                                input ()
                                                                                                break

                                                                                            else:
                                                                                                print ()
                                                                                                print (wrong)
                                                                                        break


                                                                                    elif (answer == '3') or (answer == '4'):
                                                                                        print ()
                                                                                        print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                                        input ()
                                                                                        print ("Here take this, It'll certainly help you")
                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                        inventory.append(items[1]) #ITEM
                                                                                        input ()
                                                                                        break

                                                                                    else:
                                                                                        print ()
                                                                                        print (wrong)
                                                                                break

                                                                            else:
                                                                                print (wrong)
                                                                        break

                                                                    elif (answer == '4'):
                                                                        print ()
                                                                        print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
                                                                        print (friend, "gave you a", items[1] + "!")
                                                                        inventory.append(items[1]) #ITEM
                                                                        input ()
                                                                        break

                                                                    else:
                                                                        print (wrong)
                                                                break

                                                            elif answer == '4':
                                                                print ()
                                                                print("Still got the jokes I see. Good to see you haven't changed,", player_name + ".")
                                                                relationship = 'neutral'
                                                                print ()
                                                                print ()
                                                                print ()
                                                                print ("[1] You too,", friend)
                                                                print ("[2] Always.")
                                                                print ("[3] Why would I change?")
                                                                print ("[4] I haven't changed clothes in 15 years either...")
                                                                print ()
                                                                while True:
                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                    if (answer == '1') or (answer == '2') or (answer == '3') or (answer == '4'):
                                                                        print ()
                                                                        print ("Listen, I'd love to stay and catch up but I have to go, the monsters are coming more and more often. Someone needs to deal with them. You being here is no coincidence.")
                                                                        print ()
                                                                        print ()
                                                                        print ()
                                                                        print ("[1] What do you mean?")
                                                                        print ("[2] What are you suggesting?")
                                                                        print ("[3] Where is the Sorcerer?")
                                                                        print ("[4] What do you need me to do?")
                                                                        print ()
                                                                        while True:
                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                            if (answer == '1') or (answer == '2'):
                                                                                print ()
                                                                                print ("You appearing 15 years later is riling them up...You or perhaps the Sorcerer has also returned?")
                                                                                print ()
                                                                                print ()
                                                                                print ()
                                                                                print ("[1] I'll take care of the Sorcerer.")
                                                                                print ("[2] Where is he?")
                                                                                print ("[3] I'll help you take care of all these monsters, don't you worry.")
                                                                                print ("[4] Listen, I didn't sign up for this...")
                                                                                print ()
                                                                                while True:
                                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                                    if (answer == '1') or (answer =='3'):
                                                                                        print ()
                                                                                        print ("Thank you", player_name +", I'm glad you're back.")
                                                                                        input ()
                                                                                        print ("Here take this, It'll certainly help you")
                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                        inventory.append(items[1]) #ITEM
                                                                                        input ()
                                                                                        break

                                                                                    elif answer == '2':
                                                                                        print ()
                                                                                        print("I don't know, but if I had to guess, it'd be the woods.")
                                                                                        input ()
                                                                                        print ("Be careful, take this with you, I'm sure you'll find a good use for it.")
                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                        inventory.append(items[1]) #ITEM
                                                                                        input ()
                                                                                        break

                                                                                    elif answer == '4':
                                                                                        print ()
                                                                                        print ("No you didn't, but you're a part of this now, you must do this!")
                                                                                        input ()
                                                                                        print ("Here take this, It'll certainly help you")
                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                        inventory.append(items[1]) #ITEM
                                                                                        input ()
                                                                                        break

                                                                                    else:
                                                                                        print ()
                                                                                        print (wrong)
                                                                                break


                                                                            elif (answer == '3') or (answer == '4'):
                                                                                print ()
                                                                                print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                                input ()
                                                                                print ("Here take this, It'll certainly help you")
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

                                                            else:
                                                                print ()
                                                                print (wrong)
                                                        break


                                                    elif answer == '4':
                                                        print ()
                                                        print ("I've been managing, ever since my brother passed, its just been me here, lost all the animals too.")
                                                        print ()
                                                        print ()
                                                        print ()
                                                        print ("[1] What happened here?.")
                                                        print ("[2] What happened to your brother?")
                                                        print ("[3] Did the Sorcerer do this?")
                                                        print ("[4] Do you need anything from me?")
                                                        print ()
                                                        while True:
                                                            answer = input('Pick a dialogue option: ').strip()
                                                            if (answer == '1') or (answer == '3'):
                                                                print ()
                                                                print ("Well since you, the sorcerer, and power crystal disappeared, our village has been vulnerable to monsters. They ravaged the land.")
                                                                input ()
                                                                print ("I need your help to deal with them! I think the Sorcerer is behind all this, my guess is that he's in the mysterious woods!")
                                                                input ()
                                                                print ("Here take this, It'll certainly help you")
                                                                print (friend, "gave you a", items[1] + "!")
                                                                inventory.append(items[1]) #ITEM
                                                                input ()
                                                                break

                                                            elif answer == '2':
                                                                print ()
                                                                print("He's...passed away. Monsters attacked the farm and I just couldn't stop them.")
                                                                print ()
                                                                print ()
                                                                print ()
                                                                print ("[1] I'm sorry to hear that.")
                                                                print ("[2] I'll avenge him!")
                                                                print ("[3] Do you need anything?")
                                                                print ("[4] Point me to the nearest monster!")
                                                                print ()
                                                                while True:
                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                    if (answer == '1') or (answer == '3'):
                                                                        print ()
                                                                        print ("Don't worry about me", player_name + ", but I do need your help to fight back! I believe the Sorcerer is back. Please go deal with him.")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
                                                                        print (friend, "gave you a", items[1] + "!")
                                                                        inventory.append(items[1]) #ITEM
                                                                        input ()
                                                                        break

                                                                    elif (answer == '4') or (answer == '2'):
                                                                        print ()
                                                                        print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
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
                                                                        print ("I'm gonna need you to find and deal with the Sorcerer once and for all! My guess is that he's in the mysterious woods!")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
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
                                                print ("The audacity you have to come back after all these years,", player_name + ".")
                                                print ()
                                                print ()
                                                print ("[1] All these years?")
                                                print ("[2] What happened here?")
                                                print ("[3] I'm not done with you yet!")
                                                print ("[4] I'm sorry!")
                                                print ()
                                                while True:
                                                    answer = input('Pick a dialogue option: ').strip()
                                                    if answer == '1':
                                                        print ()
                                                        print ("It's been 15 years since we last spoke", player_name +". I didn't think I'd ever see you again.")
                                                        print ()
                                                        print ()
                                                        print ()
                                                        print ("[1] Its good to see you,", friend) 
                                                        print ("[2] No way its been 15 years.")
                                                        print ("[3] 5 more minutes...")
                                                        print ("[4] Quit playin.")
                                                        print ()
                                                        while True:
                                                            answer = input('Pick a dialogue option: ').strip()
                                                            if answer == '1':
                                                                print ()
                                                                print ("It's good to see you too,", player_name +", It has been awhile since I've last seen someone I can call friend")
                                                                print ()
                                                                print ()
                                                                print ()
                                                                print ("[1] What happened here?") 
                                                                print ("[2] Where's the Sorcerer?") 
                                                                print ("[3] Not so fast speedy gonzales.") 
                                                                print ("[4] I'm not your friend pal.") 
                                                                print ()
                                                                while True:
                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                    if answer == '1':
                                                                        print ()
                                                                        print ("Well since you, the sorcerer, and power crystal disappeared, our village has been vulnerable to monsters. They ravaged the land.")
                                                                        input ()
                                                                        print ("I'm gonna need you to find and deal with the Sorcerer once and for all! He's behind all this, I know it! My guess is that he's in the mysterious woods!")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
                                                                        print (friend, "gave you a", items[1] + "!")
                                                                        inventory.append(items[1]) #ITEM
                                                                        input ()
                                                                        break
                                                                    
                                                                    elif answer == '2':
                                                                        print ()
                                                                        print ("The Sorcerer? He disappeared with you 15 years ago... ")
                                                                        print ()
                                                                        print ()
                                                                        print ()
                                                                        print ("[1] What happened here then?")
                                                                        print ("[2] I'm here for a rematch.")
                                                                        print ("[3] I told you I'd get rid of him!")
                                                                        print ("[4] Where did he go?")
                                                                        print ()
                                                                        while True:
                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                            if answer == '1':
                                                                                print ()
                                                                                print ("Well since you, the sorcerer, and power crystal disappeared, our village has been vulnerable to monsters. They ravaged the land.")
                                                                                input ()
                                                                                print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                                input ()
                                                                                print ("Here take this, It'll certainly help you")
                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                inventory.append(items[1]) #ITEM
                                                                                input ()
                                                                                break


                                                                            elif (answer == '2'):
                                                                                print ()
                                                                                print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                                input ()
                                                                                print ("Here take this, It'll certainly help you")
                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                inventory.append(items[1]) #ITEM
                                                                                input ()
                                                                                break

                                                                            elif answer == '3':
                                                                                print ()
                                                                                print("Still got the jokes I see. Good to see you haven't changed,", player_name + ".")
                                                                                relationship = 'neutral'
                                                                                print ()
                                                                                print ()
                                                                                print ()
                                                                                print ("[1] You too,", friend)
                                                                                print ("[2] Always.")
                                                                                print ("[3] Why would I change?")
                                                                                print ("[4] I haven't changed clothes in 15 years either...")
                                                                                print ()
                                                                                while True:
                                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                                    if (answer == '1') or (answer == '2') or (answer == '3') or (answer == '4'):
                                                                                        print ()
                                                                                        print ("Listen, I'd love to stay and catch up but I have to go, the monsters are coming more and more often. Someone needs to deal with them. You being here is no coincidence.")
                                                                                        print ()
                                                                                        print ()
                                                                                        print ()
                                                                                        print ("[1] What do you mean?")
                                                                                        print ("[2] What are you suggesting?")
                                                                                        print ("[3] Where is the Sorcerer?")
                                                                                        print ("[4] What do you need me to do?")
                                                                                        print ()
                                                                                        while True:
                                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                                            if (answer == '1') or (answer == '2'):
                                                                                                print ()
                                                                                                print ("You appearing 15 years later is riling them up...You or perhaps the Sorcerer has also returned?")
                                                                                                print ()
                                                                                                print ()
                                                                                                print ()
                                                                                                print ("[1] I'll take care of the Sorcerer.")
                                                                                                print ("[2] Where is he?")
                                                                                                print ("[3] I'll help you take care of all these monsters, don't you worry.")
                                                                                                print ("[4] Listen, I didn't sign up for this...")
                                                                                                print ()
                                                                                                while True:
                                                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                                                    if (answer == '1') or (answer =='3'):
                                                                                                        print ()
                                                                                                        print ("Thank you", player_name +", I'm glad you're back.")
                                                                                                        input ()
                                                                                                        print ("Here take this, It'll certainly help you")
                                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                                        inventory.append(items[1]) #ITEM
                                                                                                        input ()
                                                                                                        break

                                                                                                    elif answer == '2':
                                                                                                        print ()
                                                                                                        print("I don't know, but if I had to guess, it'd be the woods.")
                                                                                                        input ()
                                                                                                        print ("Be careful, take this with you, I'm sure you'll find a good use for it.")
                                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                                        inventory.append(items[1]) #ITEM
                                                                                                        input ()
                                                                                                        break

                                                                                                    elif answer == '4':
                                                                                                        print ()
                                                                                                        print ("No you didn't, but you're a part of this now, you must do this!")
                                                                                                        input ()
                                                                                                        print ("Here take this, It'll certainly help you")
                                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                                        inventory.append(items[1]) #ITEM
                                                                                                        input ()
                                                                                                        break

                                                                                                    else:
                                                                                                        print ()
                                                                                                        print (wrong)
                                                                                                break


                                                                                            elif (answer == '3') or (answer == '4'):
                                                                                                print ()
                                                                                                print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                                                input ()
                                                                                                print ("Here take this, It'll certainly help you")
                                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                                inventory.append(items[1]) #ITEM
                                                                                                input ()
                                                                                                break

                                                                                            else:
                                                                                                print ()
                                                                                                print (wrong)
                                                                                        break

                                                                                    else:
                                                                                        print (wrong)
                                                                                break

                                                                            elif (answer == '4'):
                                                                                print ()
                                                                                print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                                input ()
                                                                                print ("Here take this, It'll certainly help you")
                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                inventory.append(items[1]) #ITEM
                                                                                input ()
                                                                                break

                                                                            else:
                                                                                print (wrong)
                                                                        break

                                                                    elif answer == '3':
                                                                        print ()
                                                                        print("Still got the jokes I see. Good to see you haven't changed,", player_name + ".")
                                                                        relationship = 'neutral'
                                                                        print ()
                                                                        print ()
                                                                        print ()
                                                                        print ("[1] You too,", friend)
                                                                        print ("[2] Always.")
                                                                        print ("[3] Why would I change?")
                                                                        print ("[4] I haven't changed clothes in 15 years either...")
                                                                        print ()
                                                                        while True:
                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                            if (answer == '1') or (answer == '2') or (answer == '3') or (answer == '4'):
                                                                                print ()
                                                                                print ("Listen, I'd love to stay and catch up but I have to go, the monsters are coming more and more often. Someone needs to deal with them. You being here is no coincidence.")
                                                                                print ()
                                                                                print ()
                                                                                print ()
                                                                                print ("[1] What do you mean?")
                                                                                print ("[2] What are you suggesting?")
                                                                                print ("[3] Where is the Sorcerer?")
                                                                                print ("[4] What do you need me to do?")
                                                                                print ()
                                                                                while True:
                                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                                    if (answer == '1') or (answer == '2'):
                                                                                        print ()
                                                                                        print ("You appearing 15 years later is riling them up...You or perhaps the Sorcerer has also returned?")
                                                                                        print ()
                                                                                        print ()
                                                                                        print ()
                                                                                        print ("[1] I'll take care of the Sorcerer.")
                                                                                        print ("[2] Where is he?")
                                                                                        print ("[3] I'll help you take care of all these monsters, don't you worry.")
                                                                                        print ("[4] Listen, I didn't sign up for this...")
                                                                                        print ()
                                                                                        while True:
                                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                                            if (answer == '1') or (answer =='3'):
                                                                                                print ()
                                                                                                print ("Thank you", player_name +", I'm glad you're back.")
                                                                                                input ()
                                                                                                print ("Here take this, It'll certainly help you")
                                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                                inventory.append(items[1]) #ITEM
                                                                                                input ()
                                                                                                break

                                                                                            elif answer == '2':
                                                                                                print ()
                                                                                                print("I don't know, but if I had to guess, it'd be the woods.")
                                                                                                input ()
                                                                                                print ("Be careful, take this with you, I'm sure you'll find a good use for it.")
                                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                                inventory.append(items[1]) #ITEM
                                                                                                input ()
                                                                                                break

                                                                                            elif answer == '4':
                                                                                                print ()
                                                                                                print ("No you didn't, but you're a part of this now, you must do this!")
                                                                                                input ()
                                                                                                print ("Here take this, It'll certainly help you")
                                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                                inventory.append(items[1]) #ITEM
                                                                                                input ()
                                                                                                break

                                                                                            else:
                                                                                                print ()
                                                                                                print (wrong)
                                                                                        break


                                                                                    elif (answer == '3') or (answer == '4'):
                                                                                        print ()
                                                                                        print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                                        input ()
                                                                                        print ("Here take this, It'll certainly help you")
                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                        inventory.append(items[1]) #ITEM
                                                                                        input ()
                                                                                        break

                                                                                    else:
                                                                                        print ()
                                                                                        print (wrong)
                                                                                break

                                                                            else:
                                                                                print (wrong)
                                                                        break

                                                                    elif answer == '4':
                                                                        print ()
                                                                        print ("I'm not your pal buddy")
                                                                        print ()
                                                                        print ()
                                                                        print ()
                                                                        print ("[1] I'm not your buddy bro.")
                                                                        print ("[2] I'm not your buddy homie.")
                                                                        print ("[3] I'm not your buddy mate.")
                                                                        print ("[4] I'm not your buddy comrade.")
                                                                        print ()
                                                                        while True:
                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                            if (answer == '1') or (answer == '2') or (answer == '3') or (answer == '4'):
                                                                                print ()
                                                                                print("Still got the jokes I see. Good to see you haven't changed,", player_name + ".")
                                                                                relationship = 'neutral'
                                                                                print ()
                                                                                print ()
                                                                                print ()
                                                                                print ("[1] You too,", friend)
                                                                                print ("[2] Always.")
                                                                                print ("[3] Why would I change?")
                                                                                print ("[4] I haven't changed clothes in 15 years either...")
                                                                                print ()
                                                                                while True:
                                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                                    if (answer == '1') or (answer == '2') or (answer == '3') or (answer == '4'):
                                                                                        print ()
                                                                                        print ("Listen, I'd love to stay and catch up but I have to go, the monsters are coming more and more often. Someone needs to deal with them. You being here is no coincidence.")
                                                                                        print ()
                                                                                        print ()
                                                                                        print ()
                                                                                        print ("[1] What do you mean?")
                                                                                        print ("[2] What are you suggesting?")
                                                                                        print ("[3] Where is the Sorcerer?")
                                                                                        print ("[4] What do you need me to do?")
                                                                                        print ()
                                                                                        while True:
                                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                                            if (answer == '1') or (answer == '2'):
                                                                                                print ()
                                                                                                print ("You appearing 15 years later is riling them up...You or perhaps the Sorcerer has also returned?")
                                                                                                print ()
                                                                                                print ()
                                                                                                print ()
                                                                                                print ("[1] I'll take care of the Sorcerer.")
                                                                                                print ("[2] Where is he?")
                                                                                                print ("[3] I'll help you take care of all these monsters, don't you worry.")
                                                                                                print ("[4] Listen, I didn't sign up for this...")
                                                                                                print ()
                                                                                                while True:
                                                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                                                    if (answer == '1') or (answer =='3'):
                                                                                                        print ()
                                                                                                        print ("Thank you", player_name +", I'm glad you're back.")
                                                                                                        input ()
                                                                                                        print ("Here take this, It'll certainly help you")
                                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                                        inventory.append(items[1]) #ITEM
                                                                                                        input ()
                                                                                                        break

                                                                                                    elif answer == '2':
                                                                                                        print ()
                                                                                                        print("I don't know, but if I had to guess, it'd be the woods.")
                                                                                                        input ()
                                                                                                        print ("Be careful, take this with you, I'm sure you'll find a good use for it.")
                                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                                        inventory.append(items[1]) #ITEM
                                                                                                        input ()
                                                                                                        break

                                                                                                    elif answer == '4':
                                                                                                        print ()
                                                                                                        print ("No you didn't, but you're a part of this now, you must do this!")
                                                                                                        input ()
                                                                                                        print ("Here take this, It'll certainly help you")
                                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                                        inventory.append(items[1]) #ITEM
                                                                                                        input ()
                                                                                                        break

                                                                                                    else:
                                                                                                        print ()
                                                                                                        print (wrong)
                                                                                                break


                                                                                            elif (answer == '3') or (answer == '4'):
                                                                                                print ()
                                                                                                print ("I'm gonna need you to find and deal with him once and for all!")
                                                                                                input ()
                                                                                                print ("Here take this, It'll certainly help you")
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
                                                                            
                                                                            else:
                                                                                print ()
                                                                                print (wrong)
                                                                        break


                                                                    else:
                                                                        print ()
                                                                        print (wrong)
                                                                break


                                                            elif (answer == '2') or (answer == '4'):
                                                                print ()
                                                                print("We've both grown up, I think that's proof enough for you.")
                                                                print ()
                                                                print ()
                                                                print ()
                                                                print ("[1] Where's the Sorcerer?")
                                                                print ("[2] Where's your brother?")
                                                                print ("[3] What happened here?") 
                                                                print ("[4] What can I do?") 
                                                                print ()
                                                                while True:
                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                    if answer == '1':
                                                                        print ()
                                                                        print ("The Sorcerer? He disappeared with you 15 years ago... ")
                                                                        print ()
                                                                        print ()
                                                                        print ()
                                                                        print ("[1] What happened here then?")
                                                                        print ("[2] I'm here for a rematch.")
                                                                        print ("[3] I told you I'd get rid of him!")
                                                                        print ("[4] Where did he go?")
                                                                        print ()
                                                                        while True:
                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                            if answer == '1':
                                                                                print ()
                                                                                print ("Well since you, the sorcerer, and power crystal disappeared, our village has been vulnerable to monsters. They ravaged the land.")
                                                                                input ()
                                                                                print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                                input ()
                                                                                print ("Here take this, It'll certainly help you")
                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                inventory.append(items[1]) #ITEM
                                                                                input ()
                                                                                break


                                                                            elif (answer == '2'):
                                                                                print ()
                                                                                print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                                input ()
                                                                                print ("Here take this, It'll certainly help you")
                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                inventory.append(items[1]) #ITEM
                                                                                input ()
                                                                                break

                                                                            elif answer == '3':
                                                                                print ()
                                                                                print("Still got the jokes I see. Good to see you haven't changed,", player_name + ".")
                                                                                relationship = 'neutral'
                                                                                print ()
                                                                                print ()
                                                                                print ()
                                                                                print ("[1] You too,", friend)
                                                                                print ("[2] Always.")
                                                                                print ("[3] Why would I change?")
                                                                                print ("[4] I haven't changed clothes in 15 years either...")
                                                                                print ()
                                                                                while True:
                                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                                    if (answer == '1') or (answer == '2') or (answer == '3') or (answer == '4'):
                                                                                        print ()
                                                                                        print ("Listen, I'd love to stay and catch up but I have to go, the monsters are coming more and more often. Someone needs to deal with them. You being here is no coincidence.")
                                                                                        print ()
                                                                                        print ()
                                                                                        print ()
                                                                                        print ("[1] What do you mean?")
                                                                                        print ("[2] What are you suggesting?")
                                                                                        print ("[3] Where is the Sorcerer?")
                                                                                        print ("[4] What do you need me to do?")
                                                                                        print ()
                                                                                        while True:
                                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                                            if (answer == '1') or (answer == '2'):
                                                                                                print ()
                                                                                                print ("You appearing 15 years later is riling them up...You or perhaps the Sorcerer has also returned?")
                                                                                                print ()
                                                                                                print ()
                                                                                                print ()
                                                                                                print ("[1] I'll take care of the Sorcerer.")
                                                                                                print ("[2] Where is he?")
                                                                                                print ("[3] I'll help you take care of all these monsters, don't you worry.")
                                                                                                print ("[4] Listen, I didn't sign up for this...")
                                                                                                print ()
                                                                                                while True:
                                                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                                                    if (answer == '1') or (answer =='3'):
                                                                                                        print ()
                                                                                                        print ("Thank you", player_name +", I'm glad you're back.")
                                                                                                        input ()
                                                                                                        print ("Here take this, It'll certainly help you")
                                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                                        inventory.append(items[1]) #ITEM
                                                                                                        input ()
                                                                                                        break

                                                                                                    elif answer == '2':
                                                                                                        print ()
                                                                                                        print("I don't know, but if I had to guess, it'd be the woods.")
                                                                                                        input ()
                                                                                                        print ("Be careful, take this with you, I'm sure you'll find a good use for it.")
                                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                                        inventory.append(items[1]) #ITEM
                                                                                                        input ()
                                                                                                        break

                                                                                                    elif answer == '4':
                                                                                                        print ()
                                                                                                        print ("No you didn't, but you're a part of this now, you must do this!")
                                                                                                        input ()
                                                                                                        print ("Here take this, It'll certainly help you")
                                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                                        inventory.append(items[1]) #ITEM
                                                                                                        input ()
                                                                                                        break

                                                                                                    else:
                                                                                                        print ()
                                                                                                        print (wrong)
                                                                                                break


                                                                                            elif (answer == '3') or (answer == '4'):
                                                                                                print ()
                                                                                                print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                                                input ()
                                                                                                print ("Here take this, It'll certainly help you")
                                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                                inventory.append(items[1]) #ITEM
                                                                                                input ()
                                                                                                break

                                                                                            else:
                                                                                                print ()
                                                                                                print (wrong)
                                                                                        break

                                                                                    else:
                                                                                        print (wrong)
                                                                                break

                                                                            elif (answer == '4'):
                                                                                print ()
                                                                                print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                                input ()
                                                                                print ("Here take this, It'll certainly help you")
                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                inventory.append(items[1]) #ITEM
                                                                                input ()
                                                                                break

                                                                            else:
                                                                                print (wrong)
                                                                        break

                                                                    elif answer == '2':
                                                                        print ()
                                                                        print("He's...passed away. Monsters attacked the farm and I just couldn't stop them.")
                                                                        print ()
                                                                        print ()
                                                                        print ()
                                                                        print ("[1] I'm sorry to hear that.")
                                                                        print ("[2] I'll avenge him!")
                                                                        print ("[3] Do you need anything?")
                                                                        print ("[4] Point me to the nearest monster!")
                                                                        print ()
                                                                        while True:
                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                            if (answer == '1') or (answer == '3'):
                                                                                print ()
                                                                                print ("Don't worry about me", player_name + ", but I do need your help to fight back! I believe the Sorcerer is back. Please go deal with him.")
                                                                                input ()
                                                                                print ("Here take this, It'll certainly help you")
                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                inventory.append(items[1]) #ITEM
                                                                                input ()
                                                                                break

                                                                            elif (answer == '4') or (answer == '2'):
                                                                                print ()
                                                                                print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                                input ()
                                                                                print ("Here take this, It'll certainly help you")
                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                inventory.append(items[1]) #ITEM
                                                                                input ()
                                                                                break

                                                                            else:
                                                                                print ()
                                                                                print (wrong)
                                                                        break

                                                                    elif (answer == '3') or (answer == '4'): 
                                                                        print ()
                                                                        print ("Well since you, the sorcerer, and power crystal disappeared, our village has been vulnerable to monsters. They ravaged the land.")
                                                                        input ()
                                                                        print ("I'm gonna need you to find and deal with the Sorcerer once and for all! He's behind all this, I know it! My guess is that he's in the mysterious woods!")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
                                                                        print (friend, "gave you a", items[1] + "!")
                                                                        inventory.append(items[1]) #ITEM
                                                                        input ()
                                                                        break

                                                                    else:
                                                                        print ()
                                                                        print (wrong)
                                                                break


                                                            elif answer == '3':
                                                                print ()
                                                                print("Still got the jokes I see. Good to see you haven't changed,", player_name + ".")
                                                                relationship = 'neutral'
                                                                print ()
                                                                print ()
                                                                print ()
                                                                print ("[1] You too,", friend)
                                                                print ("[2] Always.")
                                                                print ("[3] Why would I change?")
                                                                print ("[4] I haven't changed clothes in 15 years either...")
                                                                print ()
                                                                while True:
                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                    if (answer == '1') or (answer == '2') or (answer == '3') or (answer == '4'):
                                                                        print ()
                                                                        print ("Listen, I'd love to stay and catch up but I have to go, the monsters are coming more and more often. Someone needs to deal with them. You being here is no coincidence.")
                                                                        print ()
                                                                        print ()
                                                                        print ()
                                                                        print ("[1] What do you mean?")
                                                                        print ("[2] What are you suggesting?")
                                                                        print ("[3] Where is the Sorcerer?")
                                                                        print ("[4] What do you need me to do?")
                                                                        print ()
                                                                        while True:
                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                            if (answer == '1') or (answer == '2'):
                                                                                print ()
                                                                                print ("You appearing 15 years later is riling them up...You or perhaps the Sorcerer has also returned?")
                                                                                print ()
                                                                                print ()
                                                                                print ()
                                                                                print ("[1] I'll take care of the Sorcerer.")
                                                                                print ("[2] Where is he?")
                                                                                print ("[3] I'll help you take care of all these monsters, don't you worry.")
                                                                                print ("[4] Listen, I didn't sign up for this...")
                                                                                print ()
                                                                                while True:
                                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                                    if (answer == '1') or (answer =='3'):
                                                                                        print ()
                                                                                        print ("Thank you", player_name +", I'm glad you're back.")
                                                                                        input ()
                                                                                        print ("Here take this, It'll certainly help you")
                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                        inventory.append(items[1]) #ITEM
                                                                                        input ()
                                                                                        break

                                                                                    elif answer == '2':
                                                                                        print ()
                                                                                        print("I don't know, but if I had to guess, it'd be the woods.")
                                                                                        input ()
                                                                                        print ("Be careful, take this with you, I'm sure you'll find a good use for it.")
                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                        inventory.append(items[1]) #ITEM
                                                                                        input ()
                                                                                        break

                                                                                    elif answer == '4':
                                                                                        print ()
                                                                                        print ("No you didn't, but you're a part of this now, you must do this!")
                                                                                        input ()
                                                                                        print ("Here take this, It'll certainly help you")
                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                        inventory.append(items[1]) #ITEM
                                                                                        input ()
                                                                                        break

                                                                                    else:
                                                                                        print ()
                                                                                        print (wrong)
                                                                                break


                                                                            elif (answer == '3') or (answer == '4'):
                                                                                print ()
                                                                                print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                                input ()
                                                                                print ("Here take this, It'll certainly help you")
                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                inventory.append(items[1]) #ITEM
                                                                                input ()
                                                                                break

                                                                            else:
                                                                                print ()
                                                                                print (wrong)
                                                                        break

                                                                    else:
                                                                        print (wrong)
                                                                break

                                                            else:
                                                                print ()
                                                                print (wrong)
                                                        break


                                                    elif answer == '2':
                                                        print ()
                                                        print ("Well since you, the sorcerer, and power crystal disappeared, our village has been vulnerable to monsters. They ravaged the land.")
                                                        input ()
                                                        print ("I need you to find and deal with the Sorcerer once and for all! I believe he's behind all of this! My guess is that he's in the mysterious woods!")
                                                        input ()
                                                        print ("Here take this, It'll certainly help you")
                                                        print (friend, "gave you a", items[1] + "!")
                                                        inventory.append(items[1]) #ITEM
                                                        input ()
                                                        break


                                                    elif (answer == '3'):
                                                        print ()
                                                        print ("You want to do some more damage huh? Well what more do I have to lose?")
                                                        input ()
                                                        enemy_name = friend
                                                        enemy_dmg = 7
                                                        enemy_hp = 25
                                                        enemy_weapon = weapons[1]
                                                        battle()
                                                        print (enemy_name, "dropped a", weapons[1] + "!")
                                                        input ()
                                                        print ("You've slain your now distant friend in cold blood. He put up a fight, but not much.")
                                                        attackdmg = attackdmg + 1
                                                        relationship = 'dead'

                                                        break
                            

                                                    elif answer == '4':
                                                        print ()
                                                        print ("Sorry isn't gonna bring my brother back!")
                                                        print ()
                                                        input ()
                                                        print ("-Sigh- It's been 15 years since that day,", player_name +". I've come to terms with my loss.")
                                                        print ()
                                                        print ()
                                                        print ()
                                                        print ("[1] I truly was an accident.") 
                                                        print ("[2] Really? Thats it?")
                                                        print ("[3] I'll never betray you again") 
                                                        print ("[4] Where's the Sorcerer?")
                                                        print ()
                                                        while True:
                                                            answer = input('Pick a dialogue option: ').strip()
                                                            if (answer == '1') or (answer == '3'): 
                                                                print ()
                                                                print ("Forget it... I just want to move on with my life, its been 15 years... Sorry I'm not in the mood to talk anymore.")
                                                                print ()
                                                                input ()
                                                                break

                                                            elif answer == '2':
                                                                print ()
                                                                print("What's that supposed to mean?!")
                                                                print ()
                                                                print ()
                                                                print ()
                                                                print ("[1] Nothing")
                                                                print ("[2] I guess 15 years is a long time.")
                                                                print ("[3] Come get your revenge!")
                                                                print ("[4] I thought you'd be a little more upset.")
                                                                print ()
                                                                while True:
                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                    if (answer == '1') or (answer == '2'):
                                                                        print ()
                                                                        print ("Look, It's good to see you", player_name +", but I'm gonna need a bit of time okay?")
                                                                        print ()
                                                                        print ()
                                                                        print ()
                                                                        print ("[1] Understandable, have a nice day.")
                                                                        print ("[2] I'll be around if you need me.")
                                                                        print ("[3] Say less.")
                                                                        print ("[4] Aight pce.")
                                                                        print ()
                                                                        while True:
                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                            if (answer == '1') or (answer == '2') or (answer == '3') or (answer == '4'):
                                                                                
                                                                                break

                                                                            else:
                                                                                print ()
                                                                                print (wrong)
                                                                        break


                                                                    elif (answer == '3') or (answer == '4'):
                                                                        print ()
                                                                        print ("You're pushing it,", player_name + ".")
                                                                        print ()
                                                                        print ()
                                                                        print ()
                                                                        print ("[1] I'm sorry.")
                                                                        print ("[2] Show me what you got.")
                                                                        print ("[3] Do something then.")
                                                                        print ("[4] My bad.")
                                                                        print ()
                                                                        while True:
                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                            if (answer == '1') or (answer =='4'):
                                                                                print ()
                                                                                print ("You should go,", player_name + ".")
                                                                                print ()
                                                                                print ()
                                                                                print ()
                                                                                print ("[1] Sorry I get nervous when confronted...")
                                                                                print ("[2] I'm not going anywhere.")
                                                                                print ("[3] Make me...")
                                                                                print ("[4] *leave*")
                                                                                print ()
                                                                                while True:
                                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                                    if answer == '1':
                                                                                        print ()
                                                                                        print ("Sorry I'm not in the mood for company anymore...")
                                                                                        print ()
                                                                                        input ()
                                                                                        break
                                                                                    
                                                                                    elif answer == '4':
                                                                                        break

                                                                                    elif (answer == '3') or (answer =='2'):
                                                                                        print ()
                                                                                        print ("You want to do some more damage huh? Alright then, what more do I have to lose?")
                                                                                        input ()
                                                                                        enemy_name = friend
                                                                                        enemy_dmg = 7
                                                                                        enemy_hp = 25
                                                                                        enemy_weapon = weapons[1]
                                                                                        battle()
                                                                                        print (enemy_name, "dropped a", weapons[1] + "!")
                                                                                        input ()
                                                                                        print ("You've slain your now distant friend in cold blood. He put up a fight, but not much.")
                                                                                        attackdmg = attackdmg + 1
                                                                                        relationship = 'dead'

                                                                                        break
                                                                                        
                                                                                    else:
                                                                                        print ()
                                                                                        print (wrong)
                                                                                break

                                                                            elif (answer == '2') or (answer =='3'):
                                                                                print ()                                                                                        
                                                                                print ("You want to do some more damage huh? Alright then, what more do I have to lose?")
                                                                                input ()
                                                                                enemy_name = friend
                                                                                enemy_dmg = 7
                                                                                enemy_hp = 25
                                                                                enemy_weapon = weapons[1]
                                                                                battle()
                                                                                print (enemy_name, "dropped a", weapons[1] + "!")
                                                                                input ()
                                                                                print ("You've slain your now distant friend in cold blood. He put up a fight, but not much.")
                                                                                attackdmg = attackdmg + 1
                                                                                relationship = 'dead'

                                                                                break

                                                                            else:
                                                                                print ()
                                                                                print (wrong)
                                                                        break
                                                                
                                                                    else:
                                                                        print ()
                                                                        print (wrong)
                                                                break

                                                            elif answer == '4':
                                                                print ()
                                                                print ("The Sorcerer? He disappeared with you 15 years ago... ")
                                                                print ()
                                                                print ()
                                                                print ()
                                                                print ("[1] What happened here then?")
                                                                print ("[2] I'm here for a rematch.")
                                                                print ("[3] I told you I'd get rid of him!")
                                                                print ("[4] Where did he go?")
                                                                print ()
                                                                while True:
                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                    if answer == '1':
                                                                        print ()
                                                                        print ("Well since you, the sorcerer, and power crystal disappeared, our village has been vulnerable to monsters. They ravaged the land.")
                                                                        input ()
                                                                        print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
                                                                        print (friend, "gave you a", items[1] + "!")
                                                                        inventory.append(items[1]) #ITEM
                                                                        input ()
                                                                        break


                                                                    elif (answer == '2'):
                                                                        print ()
                                                                        print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
                                                                        print (friend, "gave you a", items[1] + "!")
                                                                        inventory.append(items[1]) #ITEM
                                                                        input ()
                                                                        break

                                                                    elif answer == '3':
                                                                        print ()
                                                                        print("Still got the jokes I see. Good to see you haven't changed,", player_name + ".")
                                                                        relationship = 'neutral'
                                                                        print ()
                                                                        print ()
                                                                        print ()
                                                                        print ("[1] You too,", friend)
                                                                        print ("[2] Always.")
                                                                        print ("[3] Why would I change?")
                                                                        print ("[4] I haven't changed clothes in 15 years either...")
                                                                        print ()
                                                                        while True:
                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                            if (answer == '1') or (answer == '2') or (answer == '3') or (answer == '4'):
                                                                                print ()
                                                                                print ("Listen, I'd love to stay and catch up but I have to go, the monsters are coming more and more often. Someone needs to deal with them. You being here is no coincidence.")
                                                                                print ()
                                                                                print ()
                                                                                print ()
                                                                                print ("[1] What do you mean?")
                                                                                print ("[2] What are you suggesting?")
                                                                                print ("[3] Where is the Sorcerer?")
                                                                                print ("[4] What do you need me to do?")
                                                                                print ()
                                                                                while True:
                                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                                    if (answer == '1') or (answer == '2'):
                                                                                        print ()
                                                                                        print ("You appearing 15 years later is riling them up...You or perhaps the Sorcerer has also returned?")
                                                                                        print ()
                                                                                        print ()
                                                                                        print ()
                                                                                        print ("[1] I'll take care of the Sorcerer.")
                                                                                        print ("[2] Where is he?")
                                                                                        print ("[3] I'll help you take care of all these monsters, don't you worry.")
                                                                                        print ("[4] Listen, I didn't sign up for this...")
                                                                                        print ()
                                                                                        while True:
                                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                                            if (answer == '1') or (answer =='3'):
                                                                                                print ()
                                                                                                print ("Thank you", player_name +", I'm glad you're back.")
                                                                                                input ()
                                                                                                print ("Here take this, It'll certainly help you")
                                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                                inventory.append(items[1]) #ITEM
                                                                                                input ()
                                                                                                break

                                                                                            elif answer == '2':
                                                                                                print ()
                                                                                                print("I don't know, but if I had to guess, it'd be the woods.")
                                                                                                input ()
                                                                                                print ("Be careful, take this with you, I'm sure you'll find a good use for it.")
                                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                                inventory.append(items[1]) #ITEM
                                                                                                input ()
                                                                                                break

                                                                                            elif answer == '4':
                                                                                                print ()
                                                                                                print ("No you didn't, but you're a part of this now, you must do this!")
                                                                                                input ()
                                                                                                print ("Here take this, It'll certainly help you")
                                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                                inventory.append(items[1]) #ITEM
                                                                                                input ()
                                                                                                break

                                                                                            else:
                                                                                                print ()
                                                                                                print (wrong)
                                                                                        break


                                                                                    elif (answer == '3') or (answer == '4'):
                                                                                        print ()
                                                                                        print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                                        input ()
                                                                                        print ("Here take this, It'll certainly help you")
                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                        inventory.append(items[1]) #ITEM
                                                                                        input ()
                                                                                        break

                                                                                    else:
                                                                                        print ()
                                                                                        print (wrong)
                                                                                break

                                                                            else:
                                                                                print (wrong)
                                                                        break

                                                                    elif (answer == '4'):
                                                                        print ()
                                                                        print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
                                                                        print (friend, "gave you a", items[1] + "!")
                                                                        inventory.append(items[1]) #ITEM
                                                                        input ()
                                                                        break

                                                                    else:
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


                                            elif friendship == 'neutral':
                                                print ()
                                                print ("You see an older, matured", friend + ", it is evident that a lot of time has passed since you last seen him.")
                                                print ()
                                                print ("Wow its good to see you,", player_name + "! I thought you died at the Temple all those years ago... how long has it been? 15 years? Where have you been?")
                                                print ()
                                                print ()
                                                print ("[1] What do you mean its been 15 years?!")
                                                print ("[2] You did not age well.")
                                                print ("[3] Where's your brother?")
                                                print ("[4] How are you?")
                                                print ()
                                                while True:
                                                    answer = input('Pick a dialogue option: ').strip()
                                                    if answer == '1':
                                                        print ()
                                                        print ("The last time I saw you, you were headed towards the Temple, and that was 15 years ago. As you can see, a lot of time has passed.")
                                                        print ()
                                                        print ()
                                                        print ()
                                                        print ("[1] Where's the Sorcerer?")
                                                        print ("[2] What happened here?")
                                                        print ("[3] You look a little gray.")
                                                        print ("[4] Are you okay?")
                                                        print ()
                                                        while True:
                                                            answer = input('Pick a dialogue option: ').strip()
                                                            if answer == '1':
                                                                print ()
                                                                print ("The Sorcerer? He disappeared with you 15 years ago... ")
                                                                print ()
                                                                print ()
                                                                print ()
                                                                print ("[1] What happened here then?")
                                                                print ("[2] I'm here for a rematch.")
                                                                print ("[3] I told you I'd get rid of him!")
                                                                print ("[4] Where did he go?")
                                                                print ()
                                                                while True:
                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                    if answer == '1':
                                                                        print ()
                                                                        print ("Well since you, the sorcerer, and power crystal disappeared, our village has been vulnerable to monsters. They ravaged the land.")
                                                                        input ()
                                                                        print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
                                                                        print (friend, "gave you a", items[1] + "!")
                                                                        inventory.append(items[1]) #ITEM
                                                                        input ()
                                                                        break


                                                                    elif (answer == '2'):
                                                                        print ()
                                                                        print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
                                                                        print (friend, "gave you a", items[1] + "!")
                                                                        inventory.append(items[1]) #ITEM
                                                                        input ()
                                                                        break

                                                                    elif answer == '3':
                                                                        print ()
                                                                        print("Still got the jokes I see. Good to see you haven't changed,", player_name + ".")
                                                                        relationship = 'neutral'
                                                                        print ()
                                                                        print ()
                                                                        print ()
                                                                        print ("[1] You too,", friend)
                                                                        print ("[2] Always.")
                                                                        print ("[3] Why would I change?")
                                                                        print ("[4] I haven't changed clothes in 15 years either...")
                                                                        print ()
                                                                        while True:
                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                            if (answer == '1') or (answer == '2') or (answer == '3') or (answer == '4'):
                                                                                print ()
                                                                                print ("Listen, I'd love to stay and catch up but I have to go, the monsters are coming more and more often. Someone needs to deal with them. You being here is no coincidence.")
                                                                                print ()
                                                                                print ()
                                                                                print ()
                                                                                print ("[1] What do you mean?")
                                                                                print ("[2] What are you suggesting?")
                                                                                print ("[3] Where is the Sorcerer?")
                                                                                print ("[4] What do you need me to do?")
                                                                                print ()
                                                                                while True:
                                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                                    if (answer == '1') or (answer == '2'):
                                                                                        print ()
                                                                                        print ("You appearing 15 years later is riling them up...You or perhaps the Sorcerer has also returned?")
                                                                                        print ()
                                                                                        print ()
                                                                                        print ()
                                                                                        print ("[1] I'll take care of the Sorcerer.")
                                                                                        print ("[2] Where is he?")
                                                                                        print ("[3] I'll help you take care of all these monsters, don't you worry.")
                                                                                        print ("[4] Listen, I didn't sign up for this...")
                                                                                        print ()
                                                                                        while True:
                                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                                            if (answer == '1') or (answer =='3'):
                                                                                                print ()
                                                                                                print ("Thank you", player_name +", I'm glad you're back.")
                                                                                                input ()
                                                                                                print ("Here take this, It'll certainly help you")
                                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                                inventory.append(items[1]) #ITEM
                                                                                                input ()
                                                                                                break

                                                                                            elif answer == '2':
                                                                                                print ()
                                                                                                print("I don't know, but if I had to guess, it'd be the woods.")
                                                                                                input ()
                                                                                                print ("Be careful, take this with you, I'm sure you'll find a good use for it.")
                                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                                inventory.append(items[1]) #ITEM
                                                                                                input ()
                                                                                                break

                                                                                            elif answer == '4':
                                                                                                print ()
                                                                                                print ("No you didn't, but you're a part of this now, you must do this!")
                                                                                                input ()
                                                                                                print ("Here take this, It'll certainly help you")
                                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                                inventory.append(items[1]) #ITEM
                                                                                                input ()
                                                                                                break

                                                                                            else:
                                                                                                print ()
                                                                                                print (wrong)
                                                                                        break


                                                                                    elif (answer == '3') or (answer == '4'):
                                                                                        print ()
                                                                                        print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                                        input ()
                                                                                        print ("Here take this, It'll certainly help you")
                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                        inventory.append(items[1]) #ITEM
                                                                                        input ()
                                                                                        break

                                                                                    else:
                                                                                        print ()
                                                                                        print (wrong)
                                                                                break

                                                                            else:
                                                                                print (wrong)
                                                                        break

                                                                    elif (answer == '4'):
                                                                        print ()
                                                                        print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
                                                                        print (friend, "gave you a", items[1] + "!")
                                                                        inventory.append(items[1]) #ITEM
                                                                        input ()
                                                                        break

                                                                    else:
                                                                        print (wrong)
                                                                break


                                                            elif answer == '2':
                                                                print ()
                                                                print("He's...passed away. Monsters attacked the farm and I just couldn't stop them.")
                                                                print ()
                                                                print ()
                                                                print ()
                                                                print ("[1] I'm sorry to hear that.")
                                                                print ("[2] I'll avenge him!")
                                                                print ("[3] Do you need anything?")
                                                                print ("[4] Point me to the nearest monster!")
                                                                print ()
                                                                while True:
                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                    if (answer == '1') or (answer == '3'):
                                                                        print ()
                                                                        print ("Don't worry about me", player_name + ", but I do need your help to fight back! I believe the Sorcerer is back. Please go deal with him.")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
                                                                        print (friend, "gave you a", items[1] + "!")
                                                                        inventory.append(items[1]) #ITEM
                                                                        input ()
                                                                        break

                                                                    elif (answer == '4') or (answer == '2'):
                                                                        print ()
                                                                        print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
                                                                        print (friend, "gave you a", items[1] + "!")
                                                                        inventory.append(items[1]) #ITEM
                                                                        input ()
                                                                        break

                                                                    else:
                                                                        print ()
                                                                        print (wrong)
                                                                break


                                                            elif answer == '3':
                                                                print ()
                                                                print("Still got the jokes I see. Good to see you haven't changed,", player_name + ".")
                                                                relationship = 'neutral'
                                                                print ()
                                                                print ()
                                                                print ()
                                                                print ("[1] You too,", friend)
                                                                print ("[2] Always.")
                                                                print ("[3] Why would I change?")
                                                                print ("[4] I haven't changed clothes in 15 years either...")
                                                                print ()
                                                                while True:
                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                    if (answer == '1') or (answer == '2') or (answer == '3') or (answer == '4'):
                                                                        print ()
                                                                        print ("Listen, I'd love to stay and catch up but I have to go, the monsters are coming more and more often. Someone needs to deal with them. You being here is no coincidence.")
                                                                        print ()
                                                                        print ()
                                                                        print ()
                                                                        print ("[1] What do you mean?")
                                                                        print ("[2] What are you suggesting?")
                                                                        print ("[3] Where is the Sorcerer?")
                                                                        print ("[4] What do you need me to do?")
                                                                        print ()
                                                                        while True:
                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                            if (answer == '1') or (answer == '2'):
                                                                                print ()
                                                                                print ("You appearing 15 years later is riling them up...You or perhaps the Sorcerer has also returned?")
                                                                                print ()
                                                                                print ()
                                                                                print ()
                                                                                print ("[1] I'll take care of the Sorcerer.")
                                                                                print ("[2] Where is he?")
                                                                                print ("[3] I'll help you take care of all these monsters, don't you worry.")
                                                                                print ("[4] Listen, I didn't sign up for this...")
                                                                                print ()
                                                                                while True:
                                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                                    if (answer == '1') or (answer =='3'):
                                                                                        print ()
                                                                                        print ("Thank you", player_name +", I'm glad you're back.")
                                                                                        input ()
                                                                                        print ("Here take this, It'll certainly help you")
                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                        inventory.append(items[1]) #ITEM
                                                                                        input ()
                                                                                        break

                                                                                    elif answer == '2':
                                                                                        print ()
                                                                                        print("I don't know, but if I had to guess, it'd be the woods.")
                                                                                        input ()
                                                                                        print ("Be careful, take this with you, I'm sure you'll find a good use for it.")
                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                        inventory.append(items[1]) #ITEM
                                                                                        input ()
                                                                                        break

                                                                                    elif answer == '4':
                                                                                        print ()
                                                                                        print ("No you didn't, but you're a part of this now, you must do this!")
                                                                                        input ()
                                                                                        print ("Here take this, It'll certainly help you")
                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                        inventory.append(items[1]) #ITEM
                                                                                        input ()
                                                                                        break

                                                                                    else:
                                                                                        print ()
                                                                                        print (wrong)
                                                                                break


                                                                            elif (answer == '3') or (answer == '4'):
                                                                                print ()
                                                                                print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                                input ()
                                                                                print ("Here take this, It'll certainly help you")
                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                inventory.append(items[1]) #ITEM
                                                                                input ()
                                                                                break

                                                                            else:
                                                                                print ()
                                                                                print (wrong)
                                                                        break

                                                                    else:
                                                                        print (wrong)
                                                                break

                                                            elif answer == '4':
                                                                print ()
                                                                print ("I've been managing, ever since my brother passed, its just been me here, lost all the animals too.")
                                                                print ()
                                                                print ()
                                                                print ()
                                                                print ("[1] I'm sorry to hear that.")
                                                                print ("[2] What happened?")
                                                                print ("[3] Did the Sorcerer do this?")
                                                                print ("[4] Are you gonna be ok?")
                                                                print ()
                                                                while True:
                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                    if (answer == '1') or (answer == '4'):
                                                                        print ()
                                                                        print ("Don't worry about me", player_name + ", but I do need your help to fight back! I believe the Sorcerer is back. Please go deal with him.")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
                                                                        print (friend, "gave you a", items[1] + "!")
                                                                        inventory.append(items[1]) #ITEM
                                                                        input ()
                                                                        break

                                                                    elif answer == '2':
                                                                        print ()
                                                                        print ("Well since you, the sorcerer, and power crystal disappeared, our village has been vulnerable to monsters. They ravaged the land. But there's still hope, you!")
                                                                        input ()
                                                                        print ("I'm gonna need you to find and deal with the Sorcerer once and for all! I have a feeling all this is his doing. My guess is that he's in the mysterious woods!")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
                                                                        print (friend, "gave you a", items[1] + "!")
                                                                        inventory.append(items[1]) #ITEM
                                                                        input ()
                                                                        break

                                                                    elif answer == '3':
                                                                        print ()
                                                                        print ("Not him specifically... But I feel he's somehow the cause of it.")
                                                                        input ()
                                                                        print ("I'm gonna need you to find and deal with the Sorcerer once and for all! I have a feeling all this is his doing. My guess is that he's in the mysterious woods!")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
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
                                                        print("Still got the jokes I see. Good to see you haven't changed,", player_name + ".")
                                                        relationship = 'neutral'
                                                        print ()
                                                        print ()
                                                        print ()
                                                        print ("[1] You too,", friend)
                                                        print ("[2] Always.")
                                                        print ("[3] Why would I change?")
                                                        print ("[4] I haven't changed clothes in 15 years either...")
                                                        print ()
                                                        while True:
                                                            answer = input('Pick a dialogue option: ').strip()
                                                            if (answer == '1') or (answer == '2') or (answer == '3') or (answer == '4'):
                                                                print ()
                                                                print ("Listen, I'd love to stay and catch up but I have to go, the monsters are coming more and more often. Someone needs to deal with them. You being here is no coincidence.")
                                                                print ()
                                                                print ()
                                                                print ()
                                                                print ("[1] What do you mean?")
                                                                print ("[2] What are you suggesting?")
                                                                print ("[3] Where is the Sorcerer?")
                                                                print ("[4] What do you need me to do?")
                                                                print ()
                                                                while True:
                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                    if (answer == '1') or (answer == '2'):
                                                                        print ()
                                                                        print ("You appearing 15 years later is riling them up...You or perhaps the Sorcerer has also returned?")
                                                                        print ()
                                                                        print ()
                                                                        print ()
                                                                        print ("[1] I'll take care of the Sorcerer.")
                                                                        print ("[2] Where is he?")
                                                                        print ("[3] I'll help you take care of all these monsters, don't you worry.")
                                                                        print ("[4] Listen, I didn't sign up for this...")
                                                                        print ()
                                                                        while True:
                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                            if (answer == '1') or (answer =='3'):
                                                                                print ()
                                                                                print ("Thank you", player_name +", I'm glad you're back.")
                                                                                input ()
                                                                                print ("Here take this, It'll certainly help you")
                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                inventory.append(items[1]) #ITEM
                                                                                input ()
                                                                                break

                                                                            elif answer == '2':
                                                                                print ()
                                                                                print("I don't know, but if I had to guess, it'd be the woods.")
                                                                                input ()
                                                                                print ("Be careful, take this with you, I'm sure you'll find a good use for it.")
                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                inventory.append(items[1]) #ITEM
                                                                                input ()
                                                                                break

                                                                            elif answer == '4':
                                                                                print ()
                                                                                print ("No you didn't, but you're a part of this now, you must do this!")
                                                                                input ()
                                                                                print ("Here take this, It'll certainly help you")
                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                inventory.append(items[1]) #ITEM
                                                                                input ()
                                                                                break

                                                                            else:
                                                                                print ()
                                                                                print (wrong)
                                                                        break


                                                                    elif (answer == '3') or (answer == '4'):
                                                                        print ()
                                                                        print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
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


                                                    elif answer == '3':
                                                        print ()
                                                        print ("What do you mean? I haven't seen you in 15 years. We've both aged.")
                                                        print ()
                                                        print ()
                                                        print ()
                                                        print ("[1] I woke up at the Temple an hour ago...")
                                                        print ("[2] I don't remember anything in the last 15 years.")
                                                        print ("[3] Have you seen the Sorcerer?")
                                                        print ("[4] At least one of us aged well.")
                                                        print ()
                                                        while True:
                                                            answer = input('Pick a dialogue option: ').strip()
                                                            if (answer == '1') or (answer == '2'):
                                                                print ()
                                                                print ("That doesn't make sense...either you've been hit with a spell or you just have terrible memory...")
                                                                print ()
                                                                print ()
                                                                print ()
                                                                print ("[1] Where's the Sorcerer?")
                                                                print ("[2] My memory isn't that bad...")
                                                                print ("[3] I drank a lot of coffee as a kid.")
                                                                print ("[4] Who're you again?")
                                                                print ()
                                                                while True:
                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                    if answer == '1':
                                                                        print ()
                                                                        print ("The Sorcerer? He disappeared with you 15 years ago... ")
                                                                        print ()
                                                                        print ()
                                                                        print ()
                                                                        print ("[1] What happened here then?")
                                                                        print ("[2] I'm here for a rematch.")
                                                                        print ("[3] I told you I'd get rid of him!")
                                                                        print ("[4] Where did he go?")
                                                                        print ()
                                                                        while True:
                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                            if answer == '1':
                                                                                print ()
                                                                                print ("Well since you, the sorcerer, and power crystal disappeared, our village has been vulnerable to monsters. They ravaged the land.")
                                                                                input ()
                                                                                print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                                input ()
                                                                                print ("Here take this, It'll certainly help you")
                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                inventory.append(items[1]) #ITEM
                                                                                input ()
                                                                                break


                                                                            elif (answer == '2'):
                                                                                print ()
                                                                                print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                                input ()
                                                                                print ("Here take this, It'll certainly help you")
                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                inventory.append(items[1]) #ITEM
                                                                                input ()
                                                                                break

                                                                            elif answer == '3':
                                                                                print ()
                                                                                print("Still got the jokes I see. Good to see you haven't changed,", player_name + ".")
                                                                                relationship = 'neutral'
                                                                                print ()
                                                                                print ()
                                                                                print ()
                                                                                print ("[1] You too,", friend)
                                                                                print ("[2] Always.")
                                                                                print ("[3] Why would I change?")
                                                                                print ("[4] I haven't changed clothes in 15 years either...")
                                                                                print ()
                                                                                while True:
                                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                                    if (answer == '1') or (answer == '2') or (answer == '3') or (answer == '4'):
                                                                                        print ()
                                                                                        print ("Listen, I'd love to stay and catch up but I have to go, the monsters are coming more and more often. Someone needs to deal with them. You being here is no coincidence.")
                                                                                        print ()
                                                                                        print ()
                                                                                        print ()
                                                                                        print ("[1] What do you mean?")
                                                                                        print ("[2] What are you suggesting?")
                                                                                        print ("[3] Where is the Sorcerer?")
                                                                                        print ("[4] What do you need me to do?")
                                                                                        print ()
                                                                                        while True:
                                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                                            if (answer == '1') or (answer == '2'):
                                                                                                print ()
                                                                                                print ("You appearing 15 years later is riling them up...You or perhaps the Sorcerer has also returned?")
                                                                                                print ()
                                                                                                print ()
                                                                                                print ()
                                                                                                print ("[1] I'll take care of the Sorcerer.")
                                                                                                print ("[2] Where is he?")
                                                                                                print ("[3] I'll help you take care of all these monsters, don't you worry.")
                                                                                                print ("[4] Listen, I didn't sign up for this...")
                                                                                                print ()
                                                                                                while True:
                                                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                                                    if (answer == '1') or (answer =='3'):
                                                                                                        print ()
                                                                                                        print ("Thank you", player_name +", I'm glad you're back.")
                                                                                                        input ()
                                                                                                        print ("Here take this, It'll certainly help you")
                                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                                        inventory.append(items[1]) #ITEM
                                                                                                        input ()
                                                                                                        break

                                                                                                    elif answer == '2':
                                                                                                        print ()
                                                                                                        print("I don't know, but if I had to guess, it'd be the woods.")
                                                                                                        input ()
                                                                                                        print ("Be careful, take this with you, I'm sure you'll find a good use for it.")
                                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                                        inventory.append(items[1]) #ITEM
                                                                                                        input ()
                                                                                                        break

                                                                                                    elif answer == '4':
                                                                                                        print ()
                                                                                                        print ("No you didn't, but you're a part of this now, you must do this!")
                                                                                                        input ()
                                                                                                        print ("Here take this, It'll certainly help you")
                                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                                        inventory.append(items[1]) #ITEM
                                                                                                        input ()
                                                                                                        break

                                                                                                    else:
                                                                                                        print ()
                                                                                                        print (wrong)
                                                                                                break


                                                                                            elif (answer == '3') or (answer == '4'):
                                                                                                print ()
                                                                                                print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                                                input ()
                                                                                                print ("Here take this, It'll certainly help you")
                                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                                inventory.append(items[1]) #ITEM
                                                                                                input ()
                                                                                                break

                                                                                            else:
                                                                                                print ()
                                                                                                print (wrong)
                                                                                        break

                                                                                    else:
                                                                                        print (wrong)
                                                                                break

                                                                            elif (answer == '4'):
                                                                                print ()
                                                                                print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                                input ()
                                                                                print ("Here take this, It'll certainly help you")
                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                inventory.append(items[1]) #ITEM
                                                                                input ()
                                                                                break

                                                                            else:
                                                                                print (wrong)
                                                                        break

                                                                    elif (answer == '2') or (answer == '3'):
                                                                        print ()
                                                                        print("I think you were hit by a spell, perhaps defeating the Sorcerer will undo the spell...")
                                                                        input ()
                                                                        print ("You're gonna need to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
                                                                        print (friend, "gave you a", items[1] + "!")
                                                                        inventory.append(items[1]) #ITEM
                                                                        input ()
                                                                        break


                                                                    elif answer == '4':
                                                                        print ()
                                                                        print("Still got the jokes I see. Good to see you haven't changed,", player_name + ".")
                                                                        relationship = 'neutral'
                                                                        print ()
                                                                        print ()
                                                                        print ()
                                                                        print ("[1] You too,", friend)
                                                                        print ("[2] Always.")
                                                                        print ("[3] Why would I change?")
                                                                        print ("[4] I haven't changed clothes in 15 years either...")
                                                                        print ()
                                                                        while True:
                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                            if (answer == '1') or (answer == '2') or (answer == '3') or (answer == '4'):
                                                                                print ()
                                                                                print ("Listen, I'd love to stay and catch up but I have to go, the monsters are coming more and more often. Someone needs to deal with them. You being here is no coincidence.")
                                                                                print ()
                                                                                print ()
                                                                                print ()
                                                                                print ("[1] What do you mean?")
                                                                                print ("[2] What are you suggesting?")
                                                                                print ("[3] Where is the Sorcerer?")
                                                                                print ("[4] What do you need me to do?")
                                                                                print ()
                                                                                while True:
                                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                                    if (answer == '1') or (answer == '2'):
                                                                                        print ()
                                                                                        print ("You appearing 15 years later is riling them up...You or perhaps the Sorcerer has also returned?")
                                                                                        print ()
                                                                                        print ()
                                                                                        print ()
                                                                                        print ("[1] I'll take care of the Sorcerer.")
                                                                                        print ("[2] Where is he?")
                                                                                        print ("[3] I'll help you take care of all these monsters, don't you worry.")
                                                                                        print ("[4] Listen, I didn't sign up for this...")
                                                                                        print ()
                                                                                        while True:
                                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                                            if (answer == '1') or (answer =='3'):
                                                                                                print ()
                                                                                                print ("Thank you", player_name +", I'm glad you're back.")
                                                                                                input ()
                                                                                                print ("Here take this, It'll certainly help you")
                                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                                inventory.append(items[1]) #ITEM
                                                                                                input ()
                                                                                                break

                                                                                            elif answer == '2':
                                                                                                print ()
                                                                                                print("I don't know, but if I had to guess, it'd be the woods.")
                                                                                                input ()
                                                                                                print ("Be careful, take this with you, I'm sure you'll find a good use for it.")
                                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                                inventory.append(items[1]) #ITEM
                                                                                                input ()
                                                                                                break

                                                                                            elif answer == '4':
                                                                                                print ()
                                                                                                print ("No you didn't, but you're a part of this now, you must do this!")
                                                                                                input ()
                                                                                                print ("Here take this, It'll certainly help you")
                                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                                inventory.append(items[1]) #ITEM
                                                                                                input ()
                                                                                                break

                                                                                            else:
                                                                                                print ()
                                                                                                print (wrong)
                                                                                        break


                                                                                    elif (answer == '3') or (answer == '4'):
                                                                                        print ()
                                                                                        print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                                        input ()
                                                                                        print ("Here take this, It'll certainly help you")
                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                        inventory.append(items[1]) #ITEM
                                                                                        input ()
                                                                                        break

                                                                                    else:
                                                                                        print ()
                                                                                        print (wrong)
                                                                                break

                                                                            else:
                                                                                print (wrong)
                                                                        break
                                                                    
                                                                    else:
                                                                        print ()
                                                                        print (wrong)
                                                                break


                                                            elif answer == '3':
                                                                print ()
                                                                print ("The Sorcerer? He disappeared with you 15 years ago... ")
                                                                print ()
                                                                print ()
                                                                print ()
                                                                print ("[1] What happened here then?")
                                                                print ("[2] I'm here for a rematch.")
                                                                print ("[3] I told you I'd get rid of him!")
                                                                print ("[4] Where did he go?")
                                                                print ()
                                                                while True:
                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                    if answer == '1':
                                                                        print ()
                                                                        print ("Well since you, the sorcerer, and power crystal disappeared, our village has been vulnerable to monsters. They ravaged the land.")
                                                                        input ()
                                                                        print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
                                                                        print (friend, "gave you a", items[1] + "!")
                                                                        inventory.append(items[1]) #ITEM
                                                                        input ()
                                                                        break


                                                                    elif (answer == '2'):
                                                                        print ()
                                                                        print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
                                                                        print (friend, "gave you a", items[1] + "!")
                                                                        inventory.append(items[1]) #ITEM
                                                                        input ()
                                                                        break

                                                                    elif answer == '3':
                                                                        print ()
                                                                        print("Still got the jokes I see. Good to see you haven't changed,", player_name + ".")
                                                                        relationship = 'neutral'
                                                                        print ()
                                                                        print ()
                                                                        print ()
                                                                        print ("[1] You too,", friend)
                                                                        print ("[2] Always.")
                                                                        print ("[3] Why would I change?")
                                                                        print ("[4] I haven't changed clothes in 15 years either...")
                                                                        print ()
                                                                        while True:
                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                            if (answer == '1') or (answer == '2') or (answer == '3') or (answer == '4'):
                                                                                print ()
                                                                                print ("Listen, I'd love to stay and catch up but I have to go, the monsters are coming more and more often. Someone needs to deal with them. You being here is no coincidence.")
                                                                                print ()
                                                                                print ()
                                                                                print ()
                                                                                print ("[1] What do you mean?")
                                                                                print ("[2] What are you suggesting?")
                                                                                print ("[3] Where is the Sorcerer?")
                                                                                print ("[4] What do you need me to do?")
                                                                                print ()
                                                                                while True:
                                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                                    if (answer == '1') or (answer == '2'):
                                                                                        print ()
                                                                                        print ("You appearing 15 years later is riling them up...You or perhaps the Sorcerer has also returned?")
                                                                                        print ()
                                                                                        print ()
                                                                                        print ()
                                                                                        print ("[1] I'll take care of the Sorcerer.")
                                                                                        print ("[2] Where is he?")
                                                                                        print ("[3] I'll help you take care of all these monsters, don't you worry.")
                                                                                        print ("[4] Listen, I didn't sign up for this...")
                                                                                        print ()
                                                                                        while True:
                                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                                            if (answer == '1') or (answer =='3'):
                                                                                                print ()
                                                                                                print ("Thank you", player_name +", I'm glad you're back.")
                                                                                                input ()
                                                                                                print ("Here take this, It'll certainly help you")
                                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                                inventory.append(items[1]) #ITEM
                                                                                                input ()
                                                                                                break

                                                                                            elif answer == '2':
                                                                                                print ()
                                                                                                print("I don't know, but if I had to guess, it'd be the woods.")
                                                                                                input ()
                                                                                                print ("Be careful, take this with you, I'm sure you'll find a good use for it.")
                                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                                inventory.append(items[1]) #ITEM
                                                                                                input ()
                                                                                                break

                                                                                            elif answer == '4':
                                                                                                print ()
                                                                                                print ("No you didn't, but you're a part of this now, you must do this!")
                                                                                                input ()
                                                                                                print ("Here take this, It'll certainly help you")
                                                                                                print (friend, "gave you a", items[1] + "!")
                                                                                                inventory.append(items[1]) #ITEM
                                                                                                input ()
                                                                                                break

                                                                                            else:
                                                                                                print ()
                                                                                                print (wrong)
                                                                                        break


                                                                                    elif (answer == '3') or (answer == '4'):
                                                                                        print ()
                                                                                        print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                                        input ()
                                                                                        print ("Here take this, It'll certainly help you")
                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                        inventory.append(items[1]) #ITEM
                                                                                        input ()
                                                                                        break

                                                                                    else:
                                                                                        print ()
                                                                                        print (wrong)
                                                                                break

                                                                            else:
                                                                                print (wrong)
                                                                        break

                                                                    elif (answer == '4'):
                                                                        print ()
                                                                        print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
                                                                        print (friend, "gave you a", items[1] + "!")
                                                                        inventory.append(items[1]) #ITEM
                                                                        input ()
                                                                        break

                                                                    else:
                                                                        print (wrong)
                                                                break

                                                            elif answer == '4':
                                                                print ()
                                                                print("Still got the jokes I see. Good to see you haven't changed,", player_name + ".")
                                                                relationship = 'neutral'
                                                                print ()
                                                                print ()
                                                                print ()
                                                                print ("[1] You too,", friend)
                                                                print ("[2] Always.")
                                                                print ("[3] Why would I change?")
                                                                print ("[4] I haven't changed clothes in 15 years either...")
                                                                print ()
                                                                while True:
                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                    if (answer == '1') or (answer == '2') or (answer == '3') or (answer == '4'):
                                                                        print ()
                                                                        print ("Listen, I'd love to stay and catch up but I have to go, the monsters are coming more and more often. Someone needs to deal with them. You being here is no coincidence.")
                                                                        print ()
                                                                        print ()
                                                                        print ()
                                                                        print ("[1] What do you mean?")
                                                                        print ("[2] What are you suggesting?")
                                                                        print ("[3] Where is the Sorcerer?")
                                                                        print ("[4] What do you need me to do?")
                                                                        print ()
                                                                        while True:
                                                                            answer = input('Pick a dialogue option: ').strip()
                                                                            if (answer == '1') or (answer == '2'):
                                                                                print ()
                                                                                print ("You appearing 15 years later is riling them up...You or perhaps the Sorcerer has also returned?")
                                                                                print ()
                                                                                print ()
                                                                                print ()
                                                                                print ("[1] I'll take care of the Sorcerer.")
                                                                                print ("[2] Where is he?")
                                                                                print ("[3] I'll help you take care of all these monsters, don't you worry.")
                                                                                print ("[4] Listen, I didn't sign up for this...")
                                                                                print ()
                                                                                while True:
                                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                                    if (answer == '1') or (answer =='3'):
                                                                                        print ()
                                                                                        print ("Thank you", player_name +", I'm glad you're back.")
                                                                                        input ()
                                                                                        print ("Here take this, It'll certainly help you")
                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                        inventory.append(items[1]) #ITEM
                                                                                        input ()
                                                                                        break

                                                                                    elif answer == '2':
                                                                                        print ()
                                                                                        print("I don't know, but if I had to guess, it'd be the woods.")
                                                                                        input ()
                                                                                        print ("Be careful, take this with you, I'm sure you'll find a good use for it.")
                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                        inventory.append(items[1]) #ITEM
                                                                                        input ()
                                                                                        break

                                                                                    elif answer == '4':
                                                                                        print ()
                                                                                        print ("No you didn't, but you're a part of this now, you must do this!")
                                                                                        input ()
                                                                                        print ("Here take this, It'll certainly help you")
                                                                                        print (friend, "gave you a", items[1] + "!")
                                                                                        inventory.append(items[1]) #ITEM
                                                                                        input ()
                                                                                        break

                                                                                    else:
                                                                                        print ()
                                                                                        print (wrong)
                                                                                break


                                                                            elif (answer == '3') or (answer == '4'):
                                                                                print ()
                                                                                print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                                input ()
                                                                                print ("Here take this, It'll certainly help you")
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

                                                            else:
                                                                print ()
                                                                print (wrong)
                                                        break


                                                    elif answer == '4':
                                                        print ()
                                                        print ("I've been managing, ever since my brother passed, its just been me here, lost all the animals too.")
                                                        print ()
                                                        print ()
                                                        print ()
                                                        print ("[1] What happened here?.")
                                                        print ("[2] What happened to your brother?")
                                                        print ("[3] Did the Sorcerer do this?")
                                                        print ("[4] Do you need anything from me?")
                                                        print ()
                                                        while True:
                                                            answer = input('Pick a dialogue option: ').strip()
                                                            if (answer == '1') or (answer == '3'):
                                                                print ()
                                                                print ("Well since you, the sorcerer, and power crystal disappeared, our village has been vulnerable to monsters. They ravaged the land.")
                                                                input ()
                                                                print ("I need your help to deal with them! I think the Sorcerer is behind all this, my guess is that he's in the mysterious woods!")
                                                                input ()
                                                                print ("Here take this, It'll certainly help you")
                                                                print (friend, "gave you a", items[1] + "!")
                                                                inventory.append(items[1]) #ITEM
                                                                input ()
                                                                break

                                                            elif answer == '2':
                                                                print ()
                                                                print("He's...passed away. Monsters attacked the farm and I just couldn't stop them.")
                                                                print ()
                                                                print ()
                                                                print ()
                                                                print ("[1] I'm sorry to hear that.")
                                                                print ("[2] I'll avenge him!")
                                                                print ("[3] Do you need anything?")
                                                                print ("[4] Point me to the nearest monster!")
                                                                print ()
                                                                while True:
                                                                    answer = input('Pick a dialogue option: ').strip()
                                                                    if (answer == '1') or (answer == '3'):
                                                                        print ()
                                                                        print ("Don't worry about me", player_name + ", but I do need your help to fight back! I believe the Sorcerer is back. Please go deal with him.")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
                                                                        print (friend, "gave you a", items[1] + "!")
                                                                        inventory.append(items[1]) #ITEM
                                                                        input ()
                                                                        break

                                                                    elif (answer == '4') or (answer == '2'):
                                                                        print ()
                                                                        print ("I'm gonna need you to find and deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
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
                                                                        print ("I'm gonna need you to find and deal with the Sorcerer once and for all! My guess is that he's in the mysterious woods!")
                                                                        input ()
                                                                        print ("Here take this, It'll certainly help you")
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
                                              
                                                
                                        elif boy == 'alive':
                                            print ()
                                            print ("You see someone who resembles", friend + " but older. As you approach, you notice the similarities are uncanny...")
                                            print ()
                                            print ("\"Its good to see you\"")
                                            print ()
                                            print ()
                                            print ("[1] Who're you?")
                                            print ("[2] Where's", friend +"?")
                                            print ("[3] What happened here?")
                                            print ("[4] Are you related to", friend +"?")
                                            print ()
                                            while True:
                                                answer = input('Pick a dialogue option: ').strip()
                                                if (answer == '1') or (answer == '2') or (answer == '4'):
                                                    print ()
                                                    print ("It's me!", friend + "'s brother! We met 15 years ago.")
                                                    print ()
                                                    print ()
                                                    print ()
                                                    print ("[1] 15 years! How?!") ###
                                                    print ("[2] Where's", friend +"?")
                                                    print ("[3] What happened?")
                                                    print ()
                                                    while True:
                                                        answer = input('Pick a dialogue option: ').strip()
                                                        if answer == '1':
                                                            print ()
                                                            print ('Placeholder dialogue 1') ###
                                                            print ()
                                                            print ()
                                                            print ()
                                                            print ("[1] Where's", friend +"?")
                                                            print ("[2] What happened?")
                                                            print ()
                                                            while True:
                                                                answer = input('Pick a dialogue option: ').strip()
                                                                if answer == '1':
                                                                    print ()
                                                                    print ("Oh, actually he's not around anymore. We were attacked awhile ago and... he didn't make it, he died protecting me...")
                                                                    print ()
                                                                    print ()
                                                                    print ()
                                                                    print ("[1] What happened here?")
                                                                    print ()
                                                                    while True:
                                                                        answer = input('Pick a dialogue option: ').strip()
                                                                        if answer == '1':
                                                                            print ()
                                                                            print ("Well since you, the sorcerer, and power crystal disappeared, our village has been vulnerable to monsters. They ravaged the land.")
                                                                            print ("but you can deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                            input ()
                                                                            print ("Here take this, It'll certainly help you")
                                                                            print (friend, "gave you a", items[1] + "!")
                                                                            inventory.append(items[1]) #ITEM
                                                                            input ()
                                                                            break
                                                                        
                                                                        else:
                                                                            print (wrong)
                                                                    break


                                                                elif answer == '2':
                                                                    print ()
                                                                    print("Well since you, the sorcerer, and power crystal disappeared, our village has been vulnerable to monsters. They ravaged the land.")
                                                                    print ()
                                                                    print ()
                                                                    print ()
                                                                    print ("[1] Where's", friend +"?")
                                                                    print ()
                                                                    while True:
                                                                        answer = input('Pick a dialogue option: ').strip()
                                                                        if answer == '1':
                                                                            print ()
                                                                            print ("Oh, actually he's not around anymore. We were attacked awhile ago and... he didn't make it, he died protecting me. I'm sorry I'm still not quite over it, I need some time alone. It's good to see you though, have this.")
                                                                            print ()
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
                                                            print ("Oh, actually he's not around anymore. We were attacked awhile ago and... he didn't make it, he died protecting me...")
                                                            print ()
                                                            print ()
                                                            print ()
                                                            print ("[1] What happened here?")
                                                            print ()
                                                            while True:
                                                                answer = input('Pick a dialogue option: ').strip()
                                                                if answer == '1':
                                                                    print ()
                                                                    print ("Well since you, the sorcerer, and power crystal disappeared, our village has been vulnerable to monsters. They ravaged the land.")
                                                                    print ("but you can deal with him once and for all! My guess is that he's in the mysterious woods!")
                                                                    input ()
                                                                    print ("Here take this, It'll certainly help you")
                                                                    print (friend, "gave you a", items[1] + "!")
                                                                    inventory.append(items[1]) #ITEM
                                                                    input ()
                                                                    break
                                                                
                                                                else:
                                                                    print (wrong)
                                                            break
 
                                                        elif answer == '3':
                                                            print ()
                                                            print ("Well since you, the sorcerer, and power crystal disappeared, our village has been vulnerable to monsters. They ravaged the land.")
                                                            print ()
                                                            print ()
                                                            print ()
                                                            print ("[1] Where's", friend +"?")
                                                            print ()
                                                            while True:
                                                                answer = input('Pick a dialogue option: ').strip()
                                                                if answer == '1':
                                                                    print ()
                                                                    print ("Oh, actually he's not around anymore. We were attacked awhile ago and... he didn't make it, he died protecting me. I'm sorry I'm still not quite over it, I need some time alone. It's good to see you though, have this.")
                                                                    print ()
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

                                                elif answer == '3':
                                                    print ()
                                                    print ("Well since you, the sorcerer, and power crystal disappeared, our village has been vulnerable to monsters. They ravaged the land.")
                                                    print ()
                                                    print ()
                                                    print ()
                                                    print ("[1] Where's", friend +"?")
                                                    print ()
                                                    while True:
                                                        answer = input('Pick a dialogue option: ').strip()
                                                        if answer == '1':
                                                            print ()
                                                            print ("Oh, actually he's not around anymore. We were attacked awhile ago and... he didn't make it, he died protecting me. I'm sorry I'm still not quite over it, I need some time alone. It's good to see you though, have this.")
                                                            print ()
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

                                    if talked == True:
                                        print ()
                                        print ("No one seems to be home. Maybe you should come back later.")
                                        print ()

                                                                            
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
                    