#methods/storylines here
# import package src.main
#help = https://docs.python-guide.org/writing/structure/

location = 2.0 
if location == 2.0:
    castle()
def castle():#(2,0) Emerald Jewel no riddle
    # check if they possess the emerald jewel, if so display something else
    response = input("You are now outside of the castle and see a shiny item under a stick")
    if response.lower() in ['p', 'peer']:
        response = input("Obtained Emerald Jewel")
        #add emerald Jewel to sql database
        if response.lower() in ['left', 'l']:
            location = 3.1
            bridge()
        elif response.lower() in ['straight', 's']:
            location = 2.1
            waterfall()
        else:
            print("Please use commands, or another command")
            castle()
    elif response.lower() in ['left', 'l']:
        location = 3.1
        bridge()
    elif response.lower() in ['straight', 's']:
        location = 2.1
        waterfall()
    else:
        print("Please use commands, or another command")
        castle()
def bridge():#(3,1) 
    response = input("The bridge has writing that says 'Keep going straight' but has a weak spot in the middle")
    if response.lower() in ['j', 'jump']:
        location = 3.3
        underbridge()
    elif response.lower() in ['straight', 's']:
        location = 4.1
        trail()
    elif response.lower() in ['back', 'b']:
        location = 2.0
        castle()
    else:
        print("Please use commands, or another command")
        bridge()
def waterfall():#(2,1)
    response = input("You slip and fall into a waterfall. You start to slow down and see a blue door going into the hillside")
    if response.lower() in ['p', 'peer']:
        location = 2.5
        blueDoor()
    else:
        print("Please use commands, or another command")
        waterfall()
def trail():#(4,1)
    response = input("The trail breaks into a fork. Straight up the hill you see what could be the top of a building, but the trail also takes a right turn")
    if response.lower() in ['s', 'straight']:
        location = 5.0
        rustedCastle()
    elif response.lower() in ['r', 'right']:
        location = 5.4
        grassA()
    else:
        print("Please use commands, or another command")
        trail()
def rustedCastle():#(5,0) Diamond Jewel
    # check if they possess the diamond jewel, if so display something else
    response = input("The door appears to have a riddle ")
def grassA():#(5,4)

def grassB():#(5,6)

def grassC():#(5,8)

def miniCastle():#(4,8) Aquamarine Jewel
    # check if they possess the aquamarine jewel, if so display something else
def tallCastle():#(4,9) Tanzanite Jewel
    # check if they possess the tanzanite jewel, if so display something else
def underbridge():#(3,3)

def waterA():#(3,5)

def waterB():#(3,6)

def waterC():#(2,11) Sapphire Jewel no riddle
    # check if they possess the sapphire jewel, if so display something else
def blueDoor():#(2,5) Peridot Jewel
    # check if they possess the peridot jewel, if so display something else
def darkCastle():#(2,6) Moonstone
    # check if they possess the moonstone jewel, if so display something else
def trashTrail():#(2,8)

def fork():#(1,8)

def ladderA():#(1,9)

def waterGrass():#(0,7)

def mushroom():#(1,5) Topaz Jewel 
    # check if they possess the topaz jewel, if so display something else
def windyCastle():#(1,11) Ruby Jewel
    # check if they possess the ruby jewel, if so display something else
def ladderB():#(0,11)

def tallGrass():#(0,9) Onyx no riddle
    # check if they possess the onyx jewel, if so display something else