import time

global health
health = 100
if health == 75:
    print ("You have been wounded by the beast...")
elif health == 50:
    print ("You are now heavily wounded...")
elif health == 25:
    print ("You are sevearly damaged, you are now on your last limbs...")
elif health == 0:
    print ("You have taken too much damage and have died.")

beast = 1

global bhealth
bhealth = 3

def finalfight():
    print ("You, Maynard and Barrow scramble up and head towards the exit...")
    time.sleep(5)
    print ("")
    print ("Approaching the exit you notice the storm which once settled has started to build up again...")
    time.sleep(5)
    print ("")
    print ("You exit the base..")
    time.sleep(5)
    print ("")
    print ("Your vision is heavily clouded by the brewing storm...")
    time.sleep(5)
    print ("")
    print ("You head towards the ship...")
    time.sleep(3)
    print ("")
    print ("Maynard: Hey, remember that pisol i gave you...I think this might be the time to use it.")
    print ("")
    eqpistol = ""
    eqpistol = input ("Please 'equip' your pistol. ")
    if eqpistol == ("pistol") or ("equip pistol"):
        print ("")
        print ("You equip your pistol.")
        time.sleep(3)
        print ("")
        print ("Barrow: Keep your eyes peeled guys, this beast could be anywhere...")
        time.sleep(4)
        print ("")
        print ("The storm contunies to rage around you...")
        time.sleep(3)
        print ("")
        print ("Maynard: I can barely see anything through this storm!")
        time.sleep(5)
        print ("")
        print ("Try 'shooting' in the direction of the beast")
        time.sleep(3)
        print ("")
        print ("You hear a beastly screech coming from the west.") # HERE THE PLAYER IS INFORMED VIA THE DIRECTION, BUT WILL MISS IF THEY FOLLOW.
        print ("")
        first()



def first(): #FIRST PHASE. 
    if beast == 1:
        fristshot = ""
        firstshot = input ("Which direction would you like to shoot? ")
        if firstshot == ("north"): #this is the correct going, because its where the boss will be (following counterclockwise around a compass)
            print ("")
            print ("The beast lets out a scream as if it were hit!")
            time.sleep(3)
            print ("")
            global bhealth
            bhealth = bhealth - 1 #this is the boss recieving damage and the stages of it.
            if bhealth == 2:
                print ("Barrow: Good work! I doubt it could take much more of this!")
            elif bhealth == 1:
                print ("Barrow: Nice! it must be on its last legs now!")
            elif bhealth == 0:
                print ("Barrow: That must be it!")
                print ("")
                print ("Congratulations, you have slain the beast!")
                finished()
            time.sleep(6)
            print ("")
            second()
        elif firstshot == ("south"): #This is where the player will miss.
            print ("")
            print ("Your bullet misses!")
            print ("")
            time.sleep(2)
            print ("Maynard: The beast must be circling us!")
            time.sleep(2)
            print ("")
            print ("Maynard: Try to predict its movements!")
            time.sleep(6)
            print ("")
            second()
        elif firstshot == ("west"): #this is when the player makes the same choice as the noise, they will be notificated on the direction of the boss and will have to think about its next movements via the sound
            print ("")
            print ("Your bullet just misses!")
            print ("")
            time.sleep(2)
            print ("Maynard: The beast must be circling us!")
            time.sleep(2)
            print ("")
            print ("Maynard: Try to predict its movements!")
            time.sleep(6)
            print ("")
            second()
        elif firstshot == ("east"): # this is when the player makes the complete wrong choice, they will recieve damage and eventually die.
            print ("")
            print ("The beast lunges at you from behind...")
            print ("")
            global health
            health = health - 25
            if health == 75:
                print ("You have been wounded by the beast...")
            elif health == 50:
                print ("You are now heavily wounded...")
            elif health == 25:
                print ("You are sevearly damaged, you are now on your last limbs...")
            elif health == 0:
                print ("You have taken too much damage and have died.")
                time.sleep(5)
                death()
            print ("")
            time.sleep(6)
            second()
        else: #this is a repeat if the player makes an invalid inpuit.
            fristshot1 = ""
            firstshot1 = input ("Which direction would you like to shoot? ")
            if firstshot1 == ("north"):
                print ("")
                print ("The beast lets out a scream as if it were hit!")
                time.sleep(3)
                print ("")
                bhealth = bhealth - 1
                if bhealth == 2:
                    print ("Barrow: Good work! I doubt it could take much more of this!")
                elif bhealth == 1:
                    print ("Barrow: Nice! it must be on its last legs now!")
                elif bhealth == 0:
                    print ("Barrow: That must be it!")
                    print ("")
                    print ("Congratulations, you have slain the beast!")
                    finished()
                time.sleep(6)
                print ("")
                second()
            elif firstshot1 == ("south"):
                print ("")
                print ("Your bullet misses!")
                print ("")
                time.sleep(2)
                print ("Maynard: The beast must be circling us!")
                time.sleep(2)
                print ("")
                print ("Maynard: Try to predict its movements!")
                time.sleep(5)
                print ("")
                second()
            elif firstshot1 == ("west"):
                print ("")
                print ("Your bullet just misses!")
                print ("")
                time.sleep(2)
                print ("Maynard: The beast must be circling us!")
                time.sleep(2)
                print ("")
                print ("Maynard: Try to predict its movements!")
                time.sleep(5)
                print ("")
                second()
            elif firstshot1 == ("east"):
                print ("")
                print ("The beast lunges at you from behind...")
                print ("")
                health = health - 25
                if health == 75:
                    print ("You have been wounded by the beast...")
                elif health == 50:
                    print ("You are now heavily wounded...")
                elif health == 25:
                    print ("You are sevearly damaged, you are now on your last limbs...")
                elif health == 0:
                    print ("You have taken too much damage and have died.")
                    time.sleep(5)
                    death()
                print ("")
                time.sleep(6)
                second()

def second(): #Phase two....This is the same idea but here the player is informed that the boss is rotating clockwise and he needs to predict its movements.
    if beast == 1:
        print ("You hear the beast screeching from the North")
        print ("")
        time.sleep(4)
        print ("Barrow: It seems that the beast is circling us clockwise! ")
        print ("")
        time.sleep(3)
        secondshot = ""
        secondshot = input ("Which direction you like to shoot? ")
        if secondshot == ("north"):
            print ("")
            print ("Your bullet just misses!")
            print ("")
            time.sleep(2)
            print ("Maynard: The beast must be circling us!")
            time.sleep(2)
            print ("")
            print ("Maynard: Try to predict its movements, its circling us clockwise!")
            time.sleep(3)
            print ("")
            third()
        elif secondshot == ("south"):
            print ("")
            print ("The beast lunges at you from behind...")
            print ("")
            global health
            health = health - 25
            if health == 75:
                print ("You have been wounded by the beast...")
            elif health == 50:
                print ("You are now heavily wounded...")
            elif health == 25:
                print ("You are sevearly damaged, you are now on your last limbs...")
            elif health == 0:
                print ("You have taken too much damage and have died.")
                time.sleep(5)
                death()
            print ("")
            time.sleep(6)
            third()
        elif secondshot == ("east"):
            print ("")
            print ("The beast lets out a dire scream as if it were hit!")
            time.sleep(3)
            print ("")
            global bhealth
            bhealth = bhealth - 1
            if bhealth == 2:
                print ("Barrow: Good work! I doubt it could take much more of this!")
            elif bhealth == 1:
                print ("Barrow: Nice! it must be on its last legs now!")
            elif bhealth == 0:
                print ("Barrow: That must be it!")
                print ("")
                print ("Congratulations, you have slain the beast!")
                finished()
            time.sleep(6)
            print ("")
            third()
        elif secondshot == ("west"):
            print ("")
            print ("Your bullet misses!")
            print ("")
            time.sleep(2)
            print ("Maynard: The beast must be circling us!")
            time.sleep(2)
            print ("")
            print ("Maynard: Try to predict its movements, its circling us clockwise!")
            time.sleep(5)
            print ("")
        else:
            secondshot1 = ""
            secondshot1 = input ("Which direction you like to shoot? ")
            if secondshot1 == ("north"):
                print ("")
                print ("Your bullet just misses!")
                print ("")
                time.sleep(2)
                print ("Maynard: The beast must be circling us!")
                time.sleep(2)
                print ("")
                print ("Maynard: Try to predict its movements, its circling us clockwise!")
                time.sleep(3)
                print ("")
                third()
            elif secondshot1 == ("south"):
                print ("")
                print ("The beast lunges at you from behind...")
                print ("")
                health = health - 25
                if health == 75:
                    print ("You have been wounded by the beast...")
                elif health == 50:
                    print ("You are now heavily wounded...")
                elif health == 25:
                    print ("You are sevearly damaged, you are now on your last limbs...")
                elif health == 0:
                    print ("You have taken too much damage and have died.")
                    time.sleep(5)
                    death()
                print ("")
                time.sleep(6)
                third()
            elif secondshot1 == ("east"):
                print ("")
                print ("The beast lets out a dire scream as if it were hit!")
                time.sleep(3)
                print ("")
                bhealth = bhealth - 1
                if bhealth == 2:
                    print ("Barrow: Good work! I doubt it could take much more of this!")
                elif bhealth == 1:
                    print ("Barrow: Nice! it must be on its last legs now!")
                elif bhealth == 0:
                    print ("Barrow: That must be it!")
                    print ("")
                    print ("Congratulations, you have slain the beast!")
                    finished()
                time.sleep(6)
                print ("")
                third()
            elif secondshot1 == ("west"):
                print ("")
                print ("Your bullet misses!")
                print ("")
                time.sleep(2)
                print ("Maynard: The beast must be circling us!")
                time.sleep(2)
                print ("")
                print ("Maynard: Try to predict its movements, its circling us clockwise!")
                time.sleep(5)
                print ("")
                third()



def third():
    if beast == 1:
        print ("You hear the beast screeching from the South")
        print ("")
        time.sleep(4)
        print ("Barrow: Remember that the beast is circling us clockwise! ")
        time.sleep(2)
        print ("")
        print ("Maynard: Its just too fast, try and predict its movemeants!")
        print ("")
        thirdshot = ""
        thirdshot = input ("Which direction would you like to shoot? ")
        if thirdshot == ("north"):
            print ("")
            print ("The beast lunges at you from behind...")
            print ("")
            global health
            health = health - 25
            if health == 75:
                print ("You have been wounded by the beast...")
            elif health == 50:
                print ("You are now heavily wounded...")
            elif health == 25:
                print ("You are sevearly damaged, you are now on your last limbs...")
            elif health == 0:
                print ("You have taken too much damage and have died.")
                time.sleep(5)
                death
            print ("")
            time.sleep(6)
            fourth()
        elif thirdshot == ("south"):
            print ("")
            print ("Your bullet just misses!")
            print ("")
            time.sleep(2)
            print ("Maynard: The beast must be circling us!")
            time.sleep(2)
            print ("")
            print ("Maynard: Try to predict its movements, its circling us clockwise!")
            time.sleep(3)
            print ("")
            fourth()
        elif thirdshot == ("east"):
            print ("")
            print ("Your bullet misses!")
            print ("")
            time.sleep(2)
            print ("Maynard: The beast must be circling us!")
            time.sleep(2)
            print ("")
            print ("Maynard: Try to predict its movements, its circling us clockwise!")
            time.sleep(5)
            print ("")
            fourth()
        elif thirdshot == ("west"):
            print ("")
            print ("The beast lets out a dying screech as if it were hit!")
            time.sleep(3)
            print ("")
            global bhealth
            bhealth = bhealth - 1
            if bhealth == 2:
                print ("Barrow: Good work! I doubt it could take much more of this!")
            elif bhealth == 1:
                print ("Barrow: Nice! it must be on its last legs now!")
            elif bhealth == 0:
                print ("Barrow: That must be it!")
                print ("")
                print ("Congratulations, you have slain the beast!")
                finished()
            time.sleep(6)
            print ("")
            fourth()
        else:
            thirdshot1 = ""
            thirdshot1 = input ("Which direction would you like to shoot? ")
            if thirdshot1 == ("north"):
                print ("")
                print ("The beast lunges at you from behind...")
                print ("")
                health = health - 25
                if health == 75:
                    print ("You have been wounded by the beast...")
                elif health == 50:
                    print ("You are now heavily wounded...")
                elif health == 25:
                    print ("You are sevearly damaged, you are now on your last limbs...")
                elif health == 0:
                    print ("You have taken too much damage and have died.")
                    time.sleep(5)
                    death()
                print ("")
                time.sleep(6)
                fourth()
            elif thirdshot1 == ("south"):
                print ("")
                print ("Your bullet just misses!")
                print ("")
                time.sleep(2)
                print ("Maynard: The beast must be circling us!")
                time.sleep(2)
                print ("")
                print ("Maynard: Try to predict its movements, its circling us clockwise!")
                time.sleep(3)
                print ("")
                fourth()
            elif thirdshot1 == ("east"):
                print ("")
                print ("Your bullet misses!")
                print ("")
                time.sleep(2)
                print ("Maynard: The beast must be circling us!")
                time.sleep(2)
                print ("")
                print ("Maynard: Try to predict its movements, its circling us clockwise!")
                time.sleep(5)
                print ("")
                fourth()
            elif thirdshot1 == ("west"):
                print ("")
                print ("The beast lets out a dying screech as if it were hit!")
                time.sleep(3)
                print ("")
                bhealth = bhealth - 1
                if bhealth == 2:
                    print ("Barrow: Good work! I doubt it could take much more of this!")
                elif bhealth == 1:
                    print ("Barrow: Nice! it must be on its last legs now!")
                elif bhealth == 0:
                    print ("Barrow: That must be it!")
                    print ("")
                    print ("Congratulations, you have slain the beast!")
                    finished()
                time.sleep(6)
                print ("")
                fourth()



def fourth():
    if beast == 1:
        print ("You hear the beast screeching from the East")
        print ("")
        time.sleep(4)
        print ("Barrow: Damn he must be getting tired! ")
        time.sleep(2)
        print ("")
        print ("Maynard: Just remember to predict, and shoot ahead of him.")
        print ("")
        fourthshot = ""
        fourthshot = input ("Which direction would you like to shoot? ")
        if fourthshot == ("north"):
            print ("")
            print ("Your bullet misses!")
            print ("")
            time.sleep(2)
            print ("Maynard: The beast must be circling us!")
            time.sleep(2)
            print ("")
            print ("Maynard: Try to predict its movements, its circling us clockwise!")
            time.sleep(5)
            print ("")
            first()
        elif fourthshot == ("south"):
            print ("")
            print ("The beast lets out its last breaths...")
            time.sleep(3)
            print ("")
            global bhealth
            bhealth = bhealth - 1
            if bhealth == 2:
                print ("Barrow: Good work! I doubt it could take much more of this!")
            elif bhealth == 1:
                print ("Barrow: Nice! it must be on its last legs now!")
            elif bhealth == 0:
                print ("Barrow: That must be it!")
                print ("")
                print ("Congratulations, you have slain the beast!")
                finished()
            time.sleep(6)
            print ("")
            first()
        elif fourthshot == ("west"):
            print ("")
            print ("The beast lunges at you from behind...")
            print ("")
            global health
            health = health - 25
            if health == 75:
                print ("You have been wounded by the beast...")
            elif health == 50:
                print ("You are now heavily wounded...")
            elif health == 25:
                print ("You are sevearly damaged, you are now on your last limbs...")
            elif health == 0:
                print ("You have taken too much damage and have died.")
                time.sleep(5)
                death()
            print ("")
            time.sleep(6)
            first()
        elif fourthshot == ("east"):
            print ("")
            print ("Your bullet misses!")
            print ("")
            time.sleep(2)
            print ("Maynard: The beast must be circling us!")
            time.sleep(2)
            print ("")
            print ("Maynard: Try to predict its movements, its circling us clockwise!")
            time.sleep(5)
            print ("")
            first()
        else:
            fourthshot1 = ""
            fourthshot1 = input ("Which direction would you like to shoot? ")
            if fourthshot1 == ("north"):
                print ("")
                print ("Your bullet misses!")
                print ("")
                time.sleep(2)
                print ("Maynard: The beast must be circling us!")
                time.sleep(2)
                print ("")
                print ("Maynard: Try to predict its movements, its circling us clockwise!")
                time.sleep(5)
                print ("")
                first()
            elif fourthshot1 == ("south"):
                print ("")
                print ("The beast lets out a dire scream as if it were hit!")
                time.sleep(3)
                print ("")
                bhealth = bhealth - 1
                if bhealth == 2:
                    print ("Barrow: Good work! I doubt it could take much more of this!")
                elif bhealth == 1:
                    print ("Barrow: Nice! it must be on its last legs now!")
                elif bhealth == 0:
                    print ("Barrow: That must be it!")
                    print ("")
                    print ("Congratulations, you have slain the beast!")
                    finished()
                time.sleep(6)
                print ("")
                first()
            elif fourthshot1 == ("west"):
                print ("")
                print ("The beast lunges at you from behind...")
                print ("")
                health = health - 25
                if health == 75:
                    print ("You have been wounded by the beast...")
                elif health == 50:
                    print ("You are now heavily wounded...")
                elif health == 25:
                    print ("You are sevearly damaged, you are now on your last limbs...")
                elif health == 0:
                    print ("You have taken too much damage and have died.")
                    time.sleep(5)
                    death()
                print ("")
                time.sleep(6)
                first()
            elif fourthshot1 == ("east"):
                print ("")
                print ("Your bullet misses!")
                print ("")
                time.sleep(2)
                print ("Maynard: The beast must be circling us!")
                time.sleep(2)
                print ("")
                print ("Maynard: Try to predict its movements, its circling us clockwise!")
                time.sleep(5)
                print ("")
                first()



def finished():
    print ("")
    print ("Barrow: Really good work team!")
    time.sleep(4)
    print ("")
    print ("Barrow: I couldnt have asked for a better squad for the mission.")
    time.sleep(4)
    print ("")
    print ("You enter the ship and rejoin your team.")
    time.sleep(6)
    print ("")
    print ("THANK YOU FOR PLAYING.")

def death():
    print ("")
    print ("You have died, please restart.")


finalfight()
input ("")
