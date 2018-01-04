def airlockexit():
    time.sleep(2)
    print ("E.V.A: Doors opening...")
    time.sleep(4)
    print ("")
    print ("As the shuttle doors start to creep open; a wave of dust and stone swallows the airlock...")
    print ("")
    print ("Barrow: Put your flashlight on, we arent going to be able to see through this storm! ")
    print ("")
    flashlight = ""
    flashlight = input ("Do you want to turn your flashlight on? ")
    if flashlight == ("yes"):
        print ("")
        print ("You turn your light on.")
        print ("")
    elif flashlight == ("no"):
        print ("")
        print ("Barrow: What are you doing? You will need to be able to see through this storm!")
        print ("")
        flashlight1 = ""
        flashlight1 = input ("Do you want to turn your flashlight on? ")
        if flashlight1 == ("yes"):
            print ("")
            print ("You turn your light on.")
            print ("")
        elif flashlight1 == ("no"):
            print ("")
            print ("Barrow walks over to you and turns your light on...")
            print ("")
            print ("Barrow: You really need to start listening to orders or you could compromise this mission.")
    else:
        print ("")
        print ("Barrow: Can you hurry up and turn your lights on, we cant see through this storm!")
        print ("")
        flashlight3 = ""
        flashlight3 = input ("Do you want to turn your flashlight on? ")
        if flashlight3 == ("yes"):
            print ("")
            print ("You turn your light on.")
            print ("")
        elif flashlight3 == ("no"):
            print ("")
            print ("Barrow: What are you doing? You will need to be able to see through this storm!")
            print ("")
            flashlight4 = ""
            flashlight4 = input ("Do you want to turn your flashlight on? ")
            if flashlight4 == ("yes"):
                print ("")
                print ("You turn your light on.")
                print ("")
            elif flashlight4 == ("no"):
                print ("")
                print ("Barrow walks over to you and turns your light on...")
                print ("")
                print ("Barrow: You really need to start listening to orders or you could compromise this mission.")
                print ("")

airlockexit()
1
