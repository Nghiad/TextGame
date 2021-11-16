from random import randint

def damage_multiplier(x, y, tries):
    hit = randint(x, y)
    print("Guess a number between", x, "and", y)
    for num in range(tries):
        print ()
        try:
            guess = int(input())
            if guess < hit:
                if (guess + 2) > hit:
                    print ("a little low")
                elif (guess + 4) > hit:
                    print ("too low")
                elif (guess + 5) > hit:
                    print ("way too low")
                else:
                    print ("way way too low")
            elif guess > hit:
                if (guess - 2) < hit:
                    print ("a little high")
                elif (guess - 4) < hit:
                    print ("too high")
                elif (guess - 5) < hit:
                    print ("way too high")
                else:
                    print ("way way too high")
            elif guess == hit:
                print ("critical hit")
                return 2
            
        except:
            print("invalid input")
    print ("number: ", hit)
    if (hit - 1) < guess and guess < (hit + 1):
        return 1.5
    else:
        return 1

if __name__=='__main__':
    print(damage_multiplier(1,10,3))
