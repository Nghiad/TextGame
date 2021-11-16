def first_wait(code, wrong, difficulty, secret_code, secret_wait):
    while True:
        print ()
        answer = input("What do you want to do? (wait/leave) ").lower().strip()
        if answer == 'leave':
            break
        
        elif answer == 'wait':
            while True:
                answer = input("How long do you want to wait? (number of hours) ")
                if answer.isdigit() == True:
                    answer = int(answer)
                    if (answer == code):
                        print ()
                        print ("Secret unlocked") #SECRET UNLOCKED
                        secret_code = True
                        input ()
                        break

                    elif (answer == 666):
                        print ()
                        if difficulty == 'normal':
                            difficulty = 'hard'
                            print ("Hard mode activated")
                        if difficulty == 'hard':
                            difficulty = 'normal'
                            print ("Hard mode deactivated")
                        input ()
                        break
                    
                    elif (answer > 9999):
                        print ()
                        print ("You wait for an eternity for lord knows what, and notice that time is irrelevant here.")
                        secret_wait = True
                        input ()
                        break
                        
                    elif (1000 <= answer <= 9999):
                        print ()
                        print ("You okay bro?")
                        input ()
                        break

                    elif (answer == 420):
                        print ()
                        print ("nice")
                        input ()
                        break

                    elif (answer == 69):
                        print ()
                        print ("nice")
                        input ()
                        break

                    elif (answer == 1337):
                        print ()
                        print ("nice")
                        input ()
                        break

                    elif (answer == 69420):
                        print ()
                        print ("nice")
                        input ()
                        break

                    elif (answer == 42069):
                        print ()
                        print ("nice")
                        input ()
                        break

                    elif ( 100 <= answer <= 999):
                        print ()
                        print ("You keep waiting and waiting for some cosmic sign from above to tell you to go down the dirt path... please.")
                        input ()
                        break
                        
                    elif ( 50 <= answer <= 99):
                        print ()
                        print ("You keep waiting for days for some sign on what to do next.")
                        input ()
                        break
                        
                    elif ( 24 <= answer <= 49):
                        print ()
                        print ("You wait for over a day! You keep waiting for someone or something to happen but nothing shows up.")
                        input ()
                        break

                    elif ( 11 <= answer <= 23):
                        print ()
                        print ("You wait most of the day unsure of who or what you're waiting for.")
                        input ()
                        break
                    
                    elif ( 4 <= answer <= 10):
                        print ()
                        print ("You wait for", answer, "hours because apparently you don't have anything better to do.")
                        input ()
                        break

                    elif ( 1 <= answer <= 3):
                        print ()
                        print ("You wait for", answer, "hours hoping for someone to show up but no one arrives.")
                        input ()
                        break
                        
                    elif (answer <= 0 ):
                        print ()
                        print (wrong)

                else:
                    print ()
                    print (wrong)
                                
        else:
            print ()
            print (wrong)

def second_wait(code, wrong, difficulty, secret_code, secret_wait):
    answer = input("Do you want to relax? (yes/no) ").lower().strip()
    if answer == 'yes':
        answer = input("How long do you want to relax? (number of hours) ")
        if answer.isdigit() == True:
            answer = int(answer)
            if (answer == code):
                print ()
                print ("Secret unlocked") #SECRET UNLOCKED
                secret_code = True
                input ()
                
            elif (answer == 666):
                print ()
                if difficulty == 'normal':
                    difficulty = 'hard'
                    print ("Hard mode activated")
                if difficulty == 'hard':
                    difficulty = 'normal'
                    print ("Hard mode deactivated")
                input ()
                
            elif (answer > 9999):
                print ()
                print ("You relax for an eternity, and notice that time is irrelevant in this world.")
                secret_wait = True #SECRET UNLOCKED
                input ()
                
            elif (1000 <= answer <= 9999):
                print ()
                print ("You okay bro?")
                input ()
                
            
            elif (answer == 420):
                print ()
                print ("nice")
                input ()
                

            elif (answer == 69):
                print ()
                print ("nice")
                input ()
                

            elif (answer == 69420):
                print ()
                print ("nice")
                input ()
                

            elif (answer == 42069):
                print ()
                print ("nice")
                input ()

            elif ( 101 <= answer <= 999):
                print ()
                print ("The outside world isn't that bad... I promise.")
                input ()    
                
            elif ( 24 <= answer <= 100):
                print ()
                print ("You relax for more than a day without a care in the world.")
                input ()
                
            
            elif ( 4 <= answer <= 23):
                print ()
                print ("You relax for most of the day.")
                input ()
                

            elif ( 1 <= answer <= 3):
                print ()
                print ("You relax for a few hours.")
                input ()
                
                
            elif (answer <= 0 ):
                print ()
                print (wrong)


        else:
            print ()
            print (wrong)
            print ()

    elif answer == 'no':
        print ()
        print ("You turn around and leave the house, you have more pressing matters to attend.")
        input ()
                        
    else:
        print ()
        print (wrong)