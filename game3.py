
import time


def airlockexit():
    mars_variable = ["north", "east", "west"]
    mars_choice = ""
    while mars_choice not in mars_variable:       #This will check if the user has input the correct string; if not, it will run again.
        print ("")
        print ("You exit the ship...")
        time.sleep(3)
        print ("")
        print ("Throughout the storm you manage to make out three paths ahead... ")
        time.sleep(2)
        print ("")
        print ("North leading towards the compound.")
        print ("")
        print ("East leading towards what looks like buildings generators. ")
        print ("")
        print ("West leading towards a large stack on storage containers.")

        mars_choice = str(input("Where would you like to go? "))      #here is where the player makes the choice of direciton.
    print ("")
    print ("You go " + mars_choice)     #this code will print the valid direction if the user has put the correct string in.

    if mars_choice == mars_variable[0]:      #after the users inputs a valid string we then tell the code to either run the following.
        marsnorth()
    elif mars_choice == mars_variable[1]:
        marseast()
    elif mars_choice == mars_variable[2]:
        marswest()

def marsnorth():             # Here we define the direcitons.
    print ("")
    print ("1")

def marseast():
    print ("")
    print ("2")

def marswest():
    print ("")
    print ("3")

airlockexit()
input ("please press enter to close")
