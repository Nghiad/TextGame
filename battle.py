import damage

def battle(hp, attackdmg, armor, enemy_name, enemy_hp, enemy_dmg, enemy_weapon, inventory, wrong, temple):
    while (hp > 0) and (enemy_hp > 0):
        print ()
        print ("HP:", hp)
        if temple == True:
            print ()
            print (enemy_name, "HP:", enemy_hp)
        print ()
        print ('[Options]')
        print ('Attack')
        if ('shield' in inventory) or ('garbage lid' in inventory):
            print ('Block')
        print ('Stats')
        print ('Backpack')
        print ('Use')
        print ()
        answer = input('what would you like to do? ').lower().strip()
        print ()

        #Attack Option

        if answer == 'attack':
            totaldamage = int(float(attackdmg) * damage.damage_multiplier(1, 10, 3))
            enemy_hp = enemy_hp - totaldamage
            hp = hp - ( enemy_dmg - armor )
            print ('You attacked with your', inventory[0] + '!', 'You did', totaldamage, 'damage!')
            print (enemy_name, 'attacked you with their', enemy_weapon + "!", 'you took', (enemy_dmg - armor), 'damage!')
            input ()

        #Block Option

        elif answer == 'block':
            if ('shield' in inventory) or ('garbage lid' in inventory):
                print ('You blocked with your shield!')
                input ()
            else:
                print (wrong)
                print ()

        #Stats Option

        elif answer == 'stats':
            print ('HP:', hp)
            print ('Attack Damage:', attackdmg)
            print ('Armor:', armor)
            print ()
            print ('Enemy name:', enemy_name)
            print ('Enemy HP:', enemy_hp)
            print ('Enemy Damage:', enemy_dmg)
            print ('Enemy Weapon:', enemy_weapon)
            input ()

        #Inventory Option

        elif answer == 'backpack':
            print ('Inventory:', inventory)

        #Use Option
            
        elif answer == 'use':
            item_use = input('What would you like to use? ').lower().strip()
            if item_use not in inventory:
                print (wrong)
                input ()

            if item_use in inventory:

    #item options
            
                if item_use == 'potion':
                    inventory.remove(item_use)
                    hp = hp + 10
                    print ('Your HP is now,', hp)
                    input ()
                    
                elif item_use == 'great potion':
                    inventory.remove(item_use)
                    hp = hp + 20
                    print ('Your HP is now,', hp)
                    input ()

                elif item_use == 'rock':
                    if enemy_name == 'One-eyed Demon':
                        inventory.remove(item_use)
                        enemy_hp = enemy_hp - 10
                        enemy_dmg = 0
                        print ("You threw a rock at", enemy_name + ",", "the rock pierced the demon's only eye!")
                        print ("The demon is blinded!")
                        input ()
                        
                    else:
                        inventory.remove(item_use)
                        enemy_hp = enemy_hp - 2
                        print ('You threw a rock at', enemy_name, 'for 2 damage!')
                        input ()

                elif item_use == 'glasses':
                    print ("You can see slightly better")
                    input ()

                else:
                    print (wrong)
                    input ()
                    
        else:
            print (wrong)
            input ()

    if ( hp <= 0 ):
        losescreen()
                        
    print ("You've slain", enemy_name + "!")
    input ()

    return (hp, inventory)

def appr_battle(hp, attackdmg, armor, enemy_name, enemy_hp, enemy_dmg, enemy_weapon, inventory, turn, wrong):
    while (hp > 0) and (enemy_hp > 0):
        if turn == 'casting':
            turn = 'charging'
            print ()
            print ("HP:", hp)
            print ()
            print ('[Options]')
            print ('Attack')
            print ('Block')
            print ('Stats')
            print ('Backpack')
            print ('Use')
            print ()
            answer = input('what would you like to do? ').lower().strip()
            print ()

            #Attack Option

            if answer == 'attack':
                totaldamage = int(float(attackdmg) * damage.damage_multiplier(1, 10, 3))
                enemy_hp = enemy_hp - totaldamage
                hp = hp - ( enemy_dmg - armor )
                print ('You attacked with your', inventory[0] + '!', 'You did', totaldamage, 'damage!')
                print ("The Sorcerer's Apprentice casted a giant fireball! you took", ( enemy_dmg - armor )," damage!")
                input ()

            #Block Option
            
            elif answer == 'block':
                print ('You blocked with your shield! You still get burned for 1 damage')
                hp = hp - 1
                input ()

            #Stats Option

            elif answer == 'stats':
                print ('HP:', hp)
                print ('Attack Damage:', attackdmg)
                print ('Armor:', armor)
                print ()
                print ('Enemy name:', enemy_name)
                print ('Enemy Damage:', enemy_dmg)
                print ('Enemy HP:', enemy_hp)
                print ('Enemy Weapon:', enemy_weapon)
                print ('Current Turn: Casting')
                turn = 'casting'
                input ()

            #Inventory Option

            elif answer == 'backpack':
                print ('Inventory:', inventory)
                turn = 'casting'

            #Use Option
                
            elif answer == 'use':
                item_use = input('What would you like to use? ').lower().strip()
                if item_use not in inventory:
                    print (wrong)
                    turn = 'casting'
                    input ()

                if item_use in inventory:

        #item options
                
                    if item_use == 'potion':
                        inventory.remove(item_use)
                        turn = 'casting'
                        hp = hp + 10
                        print ('Your HP is now,', hp)
                        input ()

                    elif item_use == 'rock':
                        inventory.remove(item_use)
                        turn = 'casting'
                        enemy_hp = enemy_hp - 2
                        print ('You threw a rock at', enemy_name, 'for 2 damage!')
                        input ()

                    else:
                        print (wrong)
                        turn = 'casting'
                        input ()
                        
            else:
                print (wrong)
                turn = 'casting'
                input ()
                                
        elif turn == 'charging':
                turn = 'casting'
                print ()
                print ("HP:", hp)
                print ()
                print ('[Options]')
                print ('Attack')
                print ('Block')
                print ('Stats')
                print ('Backpack')
                print ('Use')
                print ()
                answer = input('what would you like to do? ').lower().strip()
                print ()

                #Attack Option

                if answer == 'attack':
                    totaldamage = int(float(attackdmg) * damage.damage_multiplier(1, 10, 3))
                    enemy_hp = enemy_hp - totaldamage
                    print ('You attacked with your', inventory[0] + '!', 'You did', totaldamage, 'damage!')
                    print ("The Sorcerer's Apprentice is casting a spell...")
                    input ()

                #Block Option
                
                elif answer == 'block':
                    print ('You blocked with your shield!')
                    input ()
                        
                #Stats Option
                    
                elif answer == 'stats':
                    print ('HP:', hp)
                    print ('Attack Damage:', attackdmg)
                    print ('Armor:', armor)
                    print ()
                    print ('Enemy name:', enemy_name)
                    print ('Enemy Damage:', enemy_dmg)
                    print ('Enemy HP:', enemy_hp)
                    print ('Enemy Weapon:', enemy_weapon)
                    print ('Current Turn: Charging')
                    turn = 'charging'
                    input ()

                #Inventory Option

                elif answer == 'backpack':
                    print ('Inventory:', inventory)
                    turn = 'charging'

                #Use Option
                    
                elif answer == 'use':
                    item_use = input('What would you like to use? ').lower().strip()
                    if item_use not in inventory:
                        print (wrong)
                        turn = 'charging'
                        input ()

                    if item_use in inventory:

            #item options
                    
                        if item_use == 'potion':
                            inventory.remove(item_use)
                            turn = 'charging'
                            hp = hp + 10
                            print ('Your HP is now,', hp)
                            input ()

                        elif item_use == 'rock':
                            inventory.remove(item_use)
                            turn = 'charging'
                            enemy_hp = enemy_hp - 5
                            print (enemy_name, "is distracted! Critical Hit for 5 damage!")
                            print ("You broke the Sorcerer's concentration!")
                            input ()

                        else:
                            print (wrong)
                            turn = 'charging'
                            input ()
                            
                else:
                    print (wrong)
                    turn = 'charging'
                    input ()
                                
    if ( hp <= 0 ):
            losescreen()

    return (hp, inventory)

def hellhound_battle(hp, attackdmg, armor, enemy_name, enemy_name2, enemy_hp, enemy_hp2, enemy_dmg, enemy_dmg2, enemy_weapon, enemy_weapon2, inventory, wrong):
    while (hp > 0) and (enemy_hp > 0) and (enemy_hp2 > 0):
        print ()
        print ("HP:", hp)
        print ()
        print (enemy_name, "HP:", enemy_hp)
        print (enemy_name2, "HP:", enemy_hp)
        print ()
        print ('[Options]')
        print ('Attack')
        print ('Block')
        print ('Stats')
        print ('Backpack')
        print ('Use')
        print ()
        answer = input('what would you like to do? ').lower().strip()
        print ()

        #Attack Option
        
        if answer == 'attack':
            while True:
                answer = input ('which Hellhound do you want to attack? (1/2) ')
                if answer.isdigit() == True:
                    answer = int(answer)
                    if answer == 1:
                        totaldamage = int(float(attackdmg) * damage.damage_multiplier(1, 10, 3))
                        enemy_hp = enemy_hp - totaldamage
                        hp = hp - ( enemy_dmg - armor )
                        hp = hp - ( enemy_dmg2 - armor )
                        print ()
                        print ('You attacked with your', inventory[0] + '!', 'You did', totaldamage, 'damage!')
                        print (enemy_name, 'attacked you with their', enemy_weapon + "!", 'you took', (enemy_dmg - armor), 'damage!')
                        print (enemy_name2, 'attacked you with their', enemy_weapon2 + "!", 'you took', (enemy_dmg2 - armor), 'damage!')
                        input ()

                        break

                    elif answer == 2:
                        totaldamage = int(float(attackdmg) * damage.damage_multiplier(1, 10, 3))
                        enemy_hp2 = enemy_hp2 - totaldamage
                        hp = hp - ( enemy_dmg - armor )
                        hp = hp - ( enemy_dmg2 - armor )
                        print ()
                        print ('You attacked with your', inventory[0] + '!', 'You did', totaldamage, 'damage!')
                        print (enemy_name, 'attacked you with their', enemy_weapon + "!", 'you took', (enemy_dmg - armor), 'damage!')
                        print (enemy_name2, 'attacked you with their', enemy_weapon2 + "!", 'you took', (enemy_dmg2 - armor), 'damage!')
                        input ()

                        break

                    else:
                        print ()
                        print (wrong)
                        print ()

                else:
                    print ()
                    print (wrong)
                    print ()

        #Block Option

        elif answer == 'block':
            if ('shield' in inventory) or ('garbage lid' in inventory):
                print ('You blocked one attack with your shield!')
                print (enemy_name2, 'attacked you with their', enemy_weapon2 + "!", 'you took', (enemy_dmg2 - armor), 'damage!')
                hp = hp - ( enemy_dmg2 - armor )
                input ()
            else:
                print (wrong)
                print ()

        #Stats Option

        elif answer == 'stats':
            print ('HP:', hp)
            print ('Attack Damage:', attackdmg)
            print ('Armor:', armor)
            print ()
            print ('Enemy name:', enemy_name)
            print ('Enemy Damage:', enemy_dmg)
            print ('Enemy HP:', enemy_hp)
            print ('Enemy Weapon:', enemy_weapon)
            print ()
            print ('Enemy 2 name:', enemy_name2)
            print ('Enemy 2 Damage:', enemy_dmg2)
            print ('Enemy 2 HP:', enemy_hp2)
            print ('Enemy 2 Weapon:', enemy_weapon2)
            input ()

        #Inventory Option

        elif answer == 'backpack':
            print ('Inventory:', inventory)

        #Use Option
            
        elif answer == 'use':
            item_use = input('What would you like to use? ').lower().strip()
            if item_use not in inventory:
                print (wrong)
                input ()

            if item_use in inventory:

    #item options
            
                if item_use == 'potion':
                    inventory.remove(item_use)
                    hp = hp + 10
                    print ('Your HP is now,', hp)
                    input ()
                    
                elif item_use == 'great potion':
                    inventory.remove(item_use)
                    hp = hp + 20
                    print ('Your HP is now,', hp)
                    input ()

                elif item_use == 'rock':
                    inventory.remove(item_use)
                    enemy_hp = enemy_hp - 2
                    print ('You threw a rock at', enemy_name, 'for 2 damage!')
                    input ()

                elif item_use == 'glasses':
                    enemy_name = 'Chihuahua 1'
                    enemy_name2 = 'Chihuahua 2'
                    print ("You can see slightly better")
                    input ()

                else:
                    print (wrong)
                    input ()
                    
        else:
            print (wrong)
            input ()

    if ( hp <= 0 ):
            losescreen()

    elif ( enemy_hp <= 0):
        print ("You have slain", enemy_name +"!", enemy_name2, "got angrier.")
        enemy_dmg2 = enemy_dmg2 + 2
        input ()
        while (hp > 0) and (enemy_hp2 > 0):
            print ()
            print ("HP:", hp)
            print ()
            print (enemy_name2, "HP:", enemy_hp2)
            print ()
            print ('[Options]')
            print ('Attack')
            print ('Block')
            print ('Stats')
            print ('Backpack')
            print ('Use')
            print ()
            answer = input('what would you like to do? ').lower().strip()
            print ()

            #Attack Option

            if answer == 'attack':
                totaldamage = int(float(attackdmg) * damage.damage_multiplier(1, 10, 3))
                enemy_hp2 = enemy_hp2 - totaldamage
                hp = hp - ( enemy_dmg2 - armor )
                print ('You attacked with your', inventory[0] + '!', 'You did', totaldamage, 'damage!')
                print (enemy_name2, 'attacked you with their', enemy_weapon2 + "!", 'you took', (enemy_dmg2 - armor), 'damage!')
                input ()

            #Block Option

            elif answer == 'block':
                print ('You blocked with your shield!')
                input ()

            #Stats Option

            elif answer == 'stats':
                print ('HP:', hp)
                print ('Attack Damage:', attackdmg)
                print ('Armor:', armor)
                print ()
                print ('Enemy name:', enemy_name2)
                print ('Enemy HP:', enemy_hp2)
                print ('Enemy Damage:', enemy_dmg2)
                print ('Enemy Weapon:', enemy_weapon2)
                input ()

            #Inventory Option

            elif answer == 'backpack':
                print ('Inventory:', inventory)

            #Use Option
                
            elif answer == 'use':
                item_use = input('What would you like to use? ').lower().strip()
                if item_use not in inventory:
                    print (wrong)
                    input ()

                if item_use in inventory:

        #item options
                
                    if item_use == 'potion':
                        inventory.remove(item_use)
                        hp = hp + 10
                        print ('Your HP is now,', hp)
                        input ()
                        
                    elif item_use == 'great potion':
                        inventory.remove(item_use)
                        hp = hp + 20
                        print ('Your HP is now,', hp)
                        input ()

                    elif item_use == 'rock':
                        inventory.remove(item_use)
                        enemy_hp2 = enemy_hp2 - 2
                        print ('You threw a rock at', enemy_name2, 'for 2 damage!')
                        input ()

                    elif item_use == 'glasses':
                        enemy_name2 ='Chihuahua'
                        print ("You can see slightly better")
                        input ()

                    else:
                        print (wrong)
                        input ()
                            
            else:
                print (wrong)
                input ()

        if ( hp <= 0 ):            
            losescreen()

        else:    
            print ("You've slain", enemy_name2 + "!")
            input ()

    elif ( enemy_hp2 <= 0):
        print ("You have slain", enemy_name2 +"!", enemy_name, "got angrier.")
        enemy_dmg = enemy_dmg + 2
        input ()
        while (hp > 0) and (enemy_hp > 0):
            print ()
            print ("HP:", hp)
            print ()
            print (enemy_name, "HP:", enemy_hp)
            print ()
            print ('[Options]')
            print ('Attack')
            print ('Block')
            print ('Stats')
            print ('Backpack')
            print ('Use')
            print ()
            answer = input('what would you like to do? ').lower().strip()
            print ()

            #Attack Option

            if answer == 'attack':
                totaldamage = int(float(attackdmg) * damage.damage_multiplier(1, 10, 3))
                enemy_hp = enemy_hp - totaldamage
                hp = hp - ( enemy_dmg - armor )
                print ('You attacked with your', inventory[0] + '!', 'You did', totaldamage, 'damage!')
                print (enemy_name, 'attacked you with their', enemy_weapon + "!", 'you took', (enemy_dmg - armor), 'damage!')
                input ()

            #Block Option

            elif answer == 'block':
                print ('You blocked with your shield!')
                input ()

            #Stats Option

            elif answer == 'stats':
                print ('HP:', hp)
                print ('Attack Damage:', attackdmg)
                print ('Armor:', armor)
                print ()
                print ('Enemy name:', enemy_name)
                print ('Enemy HP:', enemy_hp)
                print ('Enemy Damage:', enemy_dmg)
                print ('Enemy Weapon:', enemy_weapon)
                input ()

            #Inventory Option

            elif answer == 'backpack':
                print ('Inventory:', inventory)

            #Use Option
                
            elif answer == 'use':
                item_use = input('What would you like to use? ').lower().strip()
                if item_use not in inventory:
                    print (wrong)
                    input ()

                if item_use in inventory:

        #item options
                
                    if item_use == 'potion':
                        inventory.remove(item_use)
                        hp = hp + 10
                        print ('Your HP is now,', hp)
                        input ()
                        
                    elif item_use == 'great potion':
                        inventory.remove(item_use)
                        hp = hp + 20
                        print ('Your HP is now,', hp)
                        input ()

                    elif item_use == 'rock':
                        inventory.remove(item_use)
                        enemy_hp = enemy_hp - 2
                        print ('You threw a rock at', enemy_name, 'for 2 damage!')
                        input ()

                    elif item_use == 'glasses':
                        enemy_name2 ='Chihuahua'
                        print ("You can see slightly better")
                        input ()

                    else:
                        print (wrong)
                        input ()
                            
            else:
                print (wrong)
                input ()

        if ( hp <= 0 ):
            losescreen()
        else:
            print ("You've slain", enemy_name + "!")
            input ()
    return (hp, inventory)

def sorc_battle(hp, attackdmg, armor, enemy_name, enemy_hp, enemy_dmg, enemy_weapon, inventory, turn, wrong, player_name):
    while (hp > 0) and (enemy_hp > 15):
        if turn == 'casting':
            turn = 'attacking'
            print ()
            print ("HP:", hp)
            print ()
            print (enemy_name, "HP:", enemy_hp)
            print ()
            print ('[Options]')
            print ('Attack')
            print ('Block')
            print ('Stats')
            print ('Backpack')
            print ('Use')
            print ()
            answer = input('what would you like to do? ').lower().strip()
            print ()

            #Attack Option

            if answer == 'attack':
                totaldamage = int(float(attackdmg) * damage.damage_multiplier(1, 10, 3))
                enemy_hp = enemy_hp - (totaldamage - 1)
                hp = hp - ( (enemy_dmg + 4) - armor )
                print ('You attacked with your', inventory[0] + '!', 'You did', (totaldamage - 1), 'damage!')
                print ("The Dark Sorcerer casted a giant fireball! you took", ( (enemy_dmg + 4) - armor )," damage!")
                input ()

            #Block Option
            
            elif answer == 'block':
                print ('You blocked with your shield! You still get burned for 2 damage')
                hp = hp - 2
                input ()

            #Stats Option

            elif answer == 'stats':
                print ('HP:', hp)
                print ('Attack Damage:', attackdmg)
                print ('Armor:', armor)
                print ()
                print ('Enemy name:', enemy_name)
                print ('Enemy Damage:', enemy_dmg)
                print ('Enemy HP:', enemy_hp)
                print ('Enemy Weapon:', enemy_weapon)
                print ('Enemy Armor: Energy Shield')
                print ('Current Turn: Casting')
                turn = 'casting'
                input ()

            #Inventory Option

            elif answer == 'backpack':
                print ('Inventory:', inventory)
                turn = 'casting'

            #Use Option
                
            elif answer == 'use':
                item_use = input('What would you like to use? ').lower().strip()
                if item_use not in inventory:
                    print (wrong)
                    turn = 'casting'
                    input ()

                if item_use in inventory:

        #item options
                
                    if item_use == 'potion':
                        inventory.remove(item_use)
                        turn = 'casting'
                        hp = hp + 10
                        print ('Your HP is now,', hp)
                        input ()

                    elif item_use == 'rock':
                        inventory.remove(item_use)
                        turn = 'casting'
                        enemy_hp = enemy_hp - 2
                        print ('You threw a rock at', enemy_name, 'for 2 damage!')
                        input ()

                    elif item_use == 'great potion':
                        inventory.remove(item_use)
                        turn = 'casting'
                        hp = hp + 20
                        print ('Your HP is now,', hp)
                        input ()

                    elif item_use == 'glasses':
                        enemy_name = ('Time-worned', player_name)
                        turn = 'casting'
                        print ("You can see slightly better")
                        input ()

                    else:
                        print (wrong)
                        turn = 'casting'
                        input ()
                            
            else:
                print (wrong)
                turn = 'casting'
                input ()
                                
        elif turn == 'charging':
            turn = 'casting'
            print ()
            print ("HP:", hp)
            print ()
            print (enemy_name, "HP:", enemy_hp)
            print ()
            print ('[Options]')
            print ('Attack')
            print ('Block')
            print ('Stats')
            print ('Backpack')
            print ('Use')
            print ()
            answer = input('what would you like to do? ').lower().strip()
            print ()

            #Attack Option

            if answer == 'attack':
                totaldamage = int(float(attackdmg) * damage.damage_multiplier(1, 10, 3))
                enemy_hp = enemy_hp - (totaldamage-1)
                print ('You attacked with your', inventory[0] + '!', 'You did', (totaldamage-1), 'damage!')
                print ("The Dark Sorcerer is casting a spell...")
                input ()

            #Block Option
            
            elif answer == 'block':
                print ('You blocked with your shield!')
                input ()
                    
            #Stats Option
                
            elif answer == 'stats':
                print ('HP:', hp)
                print ('Attack Damage:', attackdmg)
                print ('Armor:', armor)
                print ()
                print ('Enemy name:', enemy_name)
                print ('Enemy Damage:', enemy_dmg)
                print ('Enemy HP:', enemy_hp)
                print ('Enemy Weapon:', enemy_weapon)
                print ('Enemy Armor: Energy Shield')
                print ('Current Turn: Charging')
                turn = 'charging'
                input ()

            #Inventory Option

            elif answer == 'backpack':
                print ('Inventory:', inventory)
                turn = 'charging'

            #Use Option
                
            elif answer == 'use':
                item_use = input('What would you like to use? ').lower().strip()
                if item_use not in inventory:
                    print (wrong)
                    turn = 'charging'
                    input ()

                if item_use in inventory:

        #item options
                
                    if item_use == 'potion':
                        inventory.remove(item_use)
                        turn = 'charging'
                        hp = hp + 10
                        print ('Your HP is now,', hp)
                        input ()

                    elif item_use == 'rock':
                        inventory.remove(item_use)
                        enemy_hp = enemy_hp - 5
                        turn = 'attacking'
                        print (enemy_name, "is distracted! Critical Hit for 5 damage!")
                        print ("You broke the Sorcerer's concentration!")
                        input ()

                    elif item_use == 'great potion':
                        inventory.remove(item_use)
                        turn = 'charging'
                        hp = hp + 20
                        print ('Your HP is now,', hp)
                        input ()

                    elif item_use == 'glasses':
                        enemy_name = ('Time-worned', player_name)
                        turn = 'charging'
                        print ("You can see slightly better")
                        input ()

                    else:
                        print (wrong)
                        turn = 'charging'
                        input ()
                            
            else:
                print (wrong)
                turn = 'charging'
                input ()

        elif turn == 'attacking':
            turn = 'charging'
            print ()
            print ("HP:", hp)
            print ()
            print (enemy_name, "HP:", enemy_hp)
            print ()
            print ('[Options]')
            print ('Attack')
            print ('Block')
            print ('Stats')
            print ('Backpack')
            print ('Use')
            print ()
            answer = input('what would you like to do? ').lower().strip()
            print ()

            #Attack Option

            if answer == 'attack':
                totaldamage = int(float(attackdmg) * damage.damage_multiplier(1, 10, 3))
                enemy_hp = enemy_hp - (totaldamage - 1)
                hp = hp - ( enemy_dmg - armor )
                print ('You attacked with your', inventory[0] + '!', 'You did', (totaldamage - 1), 'damage!')
                print (enemy_name, 'attacked you with their', enemy_weapon + "!", 'you took', (enemy_dmg - armor), 'damage!')
                input ()

            #Block Option
            
            elif answer == 'block':
                print ('You blocked with your shield!')
                input ()
                    
            #Stats Option
                
            elif answer == 'stats':
                print ('HP:', hp)
                print ('Attack Damage:', attackdmg)
                print ('Armor:', armor)
                print ()
                print ('Enemy name:', enemy_name)
                print ('Enemy Damage:', enemy_dmg)
                print ('Enemy HP:', enemy_hp)
                print ('Enemy Weapon:', enemy_weapon)
                print ('Enemy Armor: Energy Shield')
                print ('Current Turn: Attacking')
                turn = 'attacking'
                input ()

            #Inventory Option

            elif answer == 'backpack':
                print ('Inventory:', inventory)
                turn = 'attacking'

            #Use Option
                
            elif answer == 'use':
                item_use = input('What would you like to use? ').lower().strip()
                if item_use not in inventory:
                    print (wrong)
                    turn = 'attacking'
                    input ()

                if item_use in inventory:

        #item options
                
                    if item_use == 'potion':
                        inventory.remove(item_use)
                        turn = 'attacking'
                        hp = hp + 10
                        print ('Your HP is now,', hp)
                        input ()

                    elif item_use == 'rock':
                        inventory.remove(item_use)
                        turn = 'attacking'
                        enemy_hp = enemy_hp - 2
                        print ('You threw a rock at', enemy_name, 'for 2 damage!')
                        input ()

                    elif item_use == 'great potion':
                        inventory.remove(item_use)
                        turn = 'attacking'
                        hp = hp + 20
                        print ('Your HP is now,', hp)
                        input ()

                    elif item_use == 'glasses':
                        enemy_name = ('Time-worned', player_name)
                        turn = 'attacking'
                        print ("You can see slightly better")
                        input ()

                    else:
                        print (wrong)
                        turn = 'attacking'
                        input ()
                            
            else:
                print (wrong)
                turn = 'attacking'
                input ()
                                
    if ( hp <= 0 ):
            losescreen()
        
    print ()
    print ("As the Sorcerer take damage, he becomes increasingly unstable, expelling more energy.")
    input ()

    while (hp > 0) and (enemy_hp > 0):
        if turn == 'casting':
            turn = 'casting2'
            print ()
            print ("HP:", hp)
            print ()
            print (enemy_name, "HP:", enemy_hp)
            print ()
            print ('[Options]')
            print ('Attack')
            print ('Block')
            print ('Stats')
            print ('Backpack')
            print ('Use')
            print ()
            answer = input('what would you like to do? ').lower().strip()
            print ()

            #Attack Option

            if answer == 'attack':
                totaldamage = int(float(attackdmg) * damage.damage_multiplier(1, 10, 3))
                enemy_hp = enemy_hp - (totaldamage - 2)
                hp = hp - ( (enemy_dmg + 3) - armor )
                print ('You attacked with your', inventory[0] + '!', 'You did', (totaldamage - 2), 'damage!')
                print ("The Dark Sorcerer casted a giant fireball! you took", ( (enemy_dmg + 3) - armor )," damage!")
                input ()

            #Block Option
            
            elif answer == 'block':
                print ('You blocked with your shield! You still get burned for 2 damage')
                hp = hp - 2
                input ()

            #Stats Option

            elif answer == 'stats':
                print ('HP:', hp)
                print ('Attack Damage:', attackdmg)
                print ('Armor:', armor)
                print ()
                print ('Enemy name:', enemy_name)
                print ('Enemy Damage:', enemy_dmg)
                print ('Enemy HP:', enemy_hp)
                print ('Enemy Weapon:', enemy_weapon)
                print ('Enemy Armor: Energy Shield +1')
                print ('Current Turn: Casting')
                turn = 'casting'
                input ()

            #Inventory Option

            elif answer == 'backpack':
                print ('Inventory:', inventory)
                turn = 'casting'

            #Use Option
                
            elif answer == 'use':
                item_use = input('What would you like to use? ').lower().strip()
                if item_use not in inventory:
                    print (wrong)
                    turn = 'casting'
                    input ()

                if item_use in inventory:

        #item options
                
                    if item_use == 'potion':
                        inventory.remove(item_use)
                        turn = 'casting'
                        hp = hp + 10
                        print ('Your HP is now,', hp)
                        input ()

                    elif item_use == 'rock':
                        inventory.remove(item_use)
                        turn = 'casting'
                        enemy_hp = enemy_hp - 2
                        print ('You threw a rock at', enemy_name, 'for 2 damage!')
                        input ()

                    elif item_use == 'great potion':
                        inventory.remove(item_use)
                        turn = 'casting'
                        hp = hp + 20
                        print ('Your HP is now,', hp)
                        input ()

                    elif item_use == 'glasses':
                        enemy_name = ('Time-worned', player_name)
                        turn = 'casting'
                        print ("You can see slightly better")
                        input ()

                    else:
                        print (wrong)
                        turn = 'casting'
                        input ()
                                
            else:
                print (wrong)
                turn = 'casting'
                input ()
                                    
        elif turn == 'charging':
            turn = 'casting'
            print ()
            print ("HP:", hp)
            print ()
            print (enemy_name, "HP:", enemy_hp)
            print ()
            print ('[Options]')
            print ('Attack')
            print ('Block')
            print ('Stats')
            print ('Backpack')
            print ('Use')
            print ()
            answer = input('what would you like to do? ').lower().strip()
            print ()

            #Attack Option

            if answer == 'attack':
                totaldamage = int(float(attackdmg) * damage.damage_multiplier(1, 10, 3))
                enemy_hp = enemy_hp - (totaldamage-2)
                print ('You attacked with your', inventory[0] + '!', 'You did', (totaldamage-2), 'damage!')
                print ("The Dark Sorcerer is casting a spell...")
                input ()

            #Block Option
            
            elif answer == 'block':
                print ('You blocked with your shield!')
                input ()
                    
            #Stats Option
                
            elif answer == 'stats':
                print ('HP:', hp)
                print ('Attack Damage:', attackdmg)
                print ('Armor:', armor)
                print ()
                print ('Enemy name:', enemy_name)
                print ('Enemy Damage:', enemy_dmg)
                print ('Enemy HP:', enemy_hp)
                print ('Enemy Weapon:', enemy_weapon)
                print ('Enemy Armor: Energy Shield +1')
                print ('Current Turn: Charging')
                turn = 'charging'
                input ()

            #Inventory Option

            elif answer == 'backpack':
                print ('Inventory:', inventory)
                turn = 'charging'

            #Use Option
                
            elif answer == 'use':
                item_use = input('What would you like to use? ').lower().strip()
                if item_use not in inventory:
                    print (wrong)
                    turn = 'charging'
                    input ()

                if item_use in inventory:

        #item options
                
                    if item_use == 'potion':
                        inventory.remove(item_use)
                        turn = 'charging'
                        hp = hp + 10
                        print ('Your HP is now,', hp)
                        input ()

                    elif item_use == 'rock':
                        inventory.remove(item_use)
                        enemy_hp = enemy_hp - 5
                        turn = 'charging'
                        print (enemy_name, "is distracted! Critical Hit for 5 damage!")
                        print ("You broke the Sorcerer's concentration!")
                        input ()

                    elif item_use == 'great potion':
                        inventory.remove(item_use)
                        turn = 'charging'
                        hp = hp + 20
                        print ('Your HP is now,', hp)
                        input ()

                    elif item_use == 'glasses':
                        enemy_name = ('Time-worned', player_name)
                        turn = 'charging'
                        print ("You can see slightly better")
                        input ()

                    else:
                        print (wrong)
                        turn = 'charging'
                        input ()
                            
            else:
                print (wrong)
                turn = 'charging'
                input ()

        elif turn == 'casting2':
            turn = 'charging'
            print ()
            print ("HP:", hp)
            print ()
            print (enemy_name, "HP:", enemy_hp)
            print ()
            print ('[Options]')
            print ('Attack')
            print ('Block')
            print ('Stats')
            print ('Backpack')
            print ('Use')
            print ()
            answer = input('what would you like to do? ').lower().strip()
            print ()

            #Attack Option

            if answer == 'attack':
                totaldamage = int(float(attackdmg) * damage.damage_multiplier(1, 10, 3))
                enemy_hp = enemy_hp - (totaldamage - 2)
                hp = hp - ( (enemy_dmg + 6) - armor )
                print ('You attacked with your', inventory[0] + '!', 'You did', (totaldamage - 2), 'damage!')
                print ("The Dark Sorcerer casted a giant fireball! you took", ( (enemy_dmg + 6) - armor )," damage!")
                input ()

            #Block Option
            
            elif answer == 'block':
                print ('You blocked with your shield! You still get burned for 4 damage')
                hp = hp - 4
                input ()
                    
            #Stats Option
                
            elif answer == 'stats':
                print ('HP:', hp)
                print ('Attack Damage:', attackdmg)
                print ('Armor:', armor)
                print ()
                print ('Enemy name:', enemy_name)
                print ('Enemy Damage:', enemy_dmg)
                print ('Enemy HP:', enemy_hp)
                print ('Enemy Weapon:', enemy_weapon)
                print ('Enemy Armor: Energy Shield +1')
                print ('Current Turn: Casting 2')
                turn = 'casting2'
                input ()

            #Inventory Option

            elif answer == 'backpack':
                print ('Inventory:', inventory)
                turn = 'casting2'

            #Use Option
                
            elif answer == 'use':
                item_use = input('What would you like to use? ').lower().strip()
                if item_use not in inventory:
                    print (wrong)
                    turn = 'casting2'
                    input ()

                if item_use in inventory:

        #item options
                
                    if item_use == 'potion':
                        inventory.remove(item_use)
                        turn = 'casting2'
                        hp = hp + 10
                        print ('Your HP is now,', hp)
                        input ()

                    elif item_use == 'rock':
                        inventory.remove(item_use)
                        turn = 'casting2'
                        enemy_hp = enemy_hp - 2
                        print ('You threw a rock at', enemy_name, 'for 2 damage!')
                        input ()

                    elif item_use == 'great potion':
                        inventory.remove(item_use)
                        turn = 'casting2'
                        hp = hp + 20
                        print ('Your HP is now,', hp)
                        input ()

                    elif item_use == 'glasses':
                        enemy_name = ('Time-worned', player_name)
                        turn = 'casting2'
                        print ("You can see slightly better")
                        input ()

                    else:
                        print (wrong)
                        turn = 'casting2'
                        input ()
                            
            else:
                print (wrong)
                turn = 'casting2'
                input ()
                                    
    if ( hp <= 0 ):
            losescreen()
    return (hp, inventory, enemy_name)
