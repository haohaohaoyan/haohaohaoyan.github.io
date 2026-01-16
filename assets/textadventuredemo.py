#Game by Haoyan Li
#Made for a computer club shenanigan
#Holy cow there was a whole lot of typing.
#My fingies hurt.
#I will do my best to publish a finished, polished version on Itch.io when I can.
#PLEASE DON'T HARASS ME IF SOMETHING IS SCIENTIFICALLY INACCURATE, IT'S A LITERAL SEMI-FANTASY GAME YA DOLT

from time import sleep as wait
#OH NO SO MANY FLAGGGGGGGGGGGSSSSSSSSSSSSS
storage = []
awakened = False
stairwellOpened = False
mapFloor1 = "There is no map for this floor yet."
mapFloor2 = "There is no map for this floor yet."
room3Searched = False
room4Searched = False

def dialogue(text, sleepTime):
    print(text)
    wait(sleepTime)
    
def query():
    ans = input(">")
    return ans
    
def inventory(locationFlag):
    #simple lil inventory function
    global mapFloor1
    global mapFloor2
    dialogue("You are holding these things:", 0)
    dialogue(storage, 0.3)
    dialogue("Type an object's name to select it.", 0.3)
    ans = query()
    if ans not in storage:
        dialogue("You don't have that.", 0.3)
    else:
        if ans == "flashlight":
            dialogue("A glowing, torchlike object. It doesn't look like it will burn out anytime soon.", 0.3)
            dialogue("This object lets you see through the darkness.", 0.3)
        if ans == "paper":
            dialogue("A thing to write on, with a thing to write with.", 0.3)
            dialogue("You can view the map with this.", 0.3)
            if 1<=locationFlag<=4:
                print(mapFloor1)
        if ans == "stairwell 1 key":
            dialogue("A key you found in the storage room on floor 1.", 0.3)
            if stairwellOpened == False:
                dialogue("You can try putting this in the lock in the stairwell.", 0.3)
            else:
                dialogue("You opened the first stairwell's door with this.", 0.3)
                dialogue("It doesn't seem to have any other use. ", 0.3)
                
def location(locationVar):
    #Oh man this is a lot of text, this is all the location data and input options. OH NOOOOOOOO
    #I now despise the lack of global *. Too lazy to use an all-in-one list...
    global awakened
    global mapFloor1
    global mapFloor2
    global tutorialInput
    global stairwellOpened
    global room3Searched
    global room4Searched
    #Okay. Here is the actual info. 
    if locationVar == 1:
        if awakened == False:
            dialogue("Your eyes slowly open,", 1.2)
            dialogue("as you look up", 0.6)
            dialogue("at the same ceiling that you've awoken to for an unintelligible amount of time.", 1)
            dialogue("You get up. Your back aches.", 0.8)
            awakened = True
            location(1)
        if "flashlight" not in storage:
            dialogue("A faintly lit, familiar little room.", 0.6)
            dialogue("There is a glowing device in the corner that you can TAKE.", 0.3)
            dialogue("(Input command after [>].)", 0.3)
        else:
            dialogue("A familiar little room. The faint lighting is now in your posession.", 0.6)
            dialogue("With the torch, you see a door.", 0.3)
            dialogue("The way out. The way FORWARD.", 0.6)
            dialogue("Go on. The outside beckons you.", 0.3)
        ans = query()
        if ans == "take":
            if "flashlight" not in storage:
                dialogue("You approach the glowing device, ", 0.3)
                dialogue("and grasp it. ", 0.3)
                dialogue("It's metallic and rodlike, similar to a torch.", 0.3)
                dialogue("(FLASHLIGHT was added to INVENTORY)", 0.3)
                dialogue("(You can access the INVENTORY now.)", 0.3)
                storage.append("flashlight")
            else:
                dialogue("You already took the flashlight.", 0.3)
            location(1)
        elif ans == "forward":
            if "flashlight" in storage:
                dialogue("You walk through the door.", 1)
                dialogue("You leave your past behind, in search for a new life. ", 0.3)
                location(2)
            else:
                dialogue("It's too dark to go that way.", 0.3)
        elif ans == "inventory":
            inventory(1)
            location(1)
        else:
            dialogue("You can't do that.", 0.3)
            location(1)
    if locationVar == 2:
        dialogue("You are in a larger room.", 0.6)
        dialogue("There is a decaying wooden table in the center, and the remains of furniture and belongings are scattered around.", 0.3)
        dialogue("There are doors to your left and right, leading into different rooms.", 0.3)
        if stairwellOpened == False:
            dialogue("You cannot go FORWARD to the stairwell, as it is locked.", 0.6)
            dialogue("You are able to go BACK, LEFT, and RIGHT.", 0.3)
            if "stairwell 1 key" in storage:
                dialogue("You have a KEY. It can UNLOCK the stairwell.", 0.3)
        else:
            dialogue("The stairs used to be locked, but you can scale them now.", 0.3)
            dialogue("You can go FORWARD and up the stairs, BACK, LEFT, and RIGHT.", 0.3)
        if "paper" in storage or "map" in storage:
            dialogue("You can DRAW a map of the floor from here.", 0.3)
        ans = query()
        if ans == "back":
            dialogue("You went back through the door.", 0.3)
            location(1)
        if ans == "left":
            dialogue("You went through the door on your left.", 0.3)
            location(3)
        if ans == "right":
            dialogue("You went through the door on your right.", 0.3)
            location(4)
        if ans == "forward":
            if stairwellOpened == False:
                dialogue("The stairwell is locked. Maybe a key is somewhere?", 0.9)
                location(2)
            else:
                dialogue("You went up the stairs, into the next floor.", 0.6)
                location(5)
        if ans == "unlock":
            if "stairwell 1 key" in storage:
                dialogue("You inserted the key into the lock.", 0.3)
                dialogue("You yanked it, and it popped open.", 0.3)
                dialogue("You are now able to go FORWARD.", 0.3)
                stairwellOpened = True
                location(2)
            else:
                dialogue("There's nothing to unlock the door with.", 0.3)
                location(2)
        if ans == "inventory":
            inventory(2)
            location(2)
        if ans == "draw":
            if "paper" in storage or "map" in storage:
                if mapFloor1 == "There is no map for this floor yet.":
                    dialogue("You looked around and drew the layout of the floor.", 0.9)
                    dialogue("(View the MAP in your INVENTORY)", 0.3)
                    mapFloor1 = "*pretend it's a map here, this is a placeholder*"
                else:
                    dialogue("You already drew this floor.", 0.3)
            else:
                dialogue("You don't have anything to DRAW on.", 0.3)
            location(2)
        else:
            dialogue("You can't do that", 0.3)
            location(2)
            
    if locationVar == 3:
        dialogue("You are in a dormitory.", 0.3)
        dialogue("Rusting cots are lain across the floor in an orderly fashion.", 0.3)
        if "paper" not in storage:
            dialogue("An organic white sheet and a peculiar wooden rod lay on the floor for you to TAKE.", 0.3)
        if room3Searched == False:
            dialogue("You can also SEARCH the room for something that will help with the lock.", 0.3)
        dialogue("Moving to the RIGHT will take you back into the large room.", 0.3)
        ans = query()
        if ans == "right":
            dialogue("You moved back through the door on the right.", 0.3)
            location(2)
        if ans == "take":
            if "paper" not in storage:
                dialogue("You took the pencil and paper.", 0.3)
                dialogue("(PAPER was added to INVENTORY)", 0.3)
                dialogue("(You can DRAW a layout of any floor on the paper if you are close to the floor's center)", 0.6)
                storage.append("paper")
            else:
                dialogue("There's nothing to take that you can carry.")
            location(3)
        if ans == "search":
            if room3Searched == False:
                dialogue("You searched the room.", 2)
                dialogue("...and you found nothing.", 0.3)
                dialogue("There were mice under the last bed though.", 0.3)
                room3Searched = True
                location(3)
            else:
                dialogue("You've already searched this room and found nothing.", 0.3)
                location(3)
        if ans == "inventory":
            inventory(3)
            location(3)
        else:
            dialogue("You can't do that.", 0.3)
            location(3)
    if locationVar == 4:
        dialogue("A storage room.", 0.6)
        dialogue("Barrels and crates are littered over the floor. ", 0.3)
        dialogue("It smells like dry fabric.", 0.3)
        if room4Searched == False:
            dialogue("You can SEARCH the room and boxes.", 0.3)
        dialogue("Moving LEFT will bring you back into the large room.", 0.3)
        ans = query()
        if ans == "left":
            dialogue("You moved back through the door on the left.", 0.3)
            location(2)
        if ans == "search":
            if room4Searched == False:
                dialogue("You searched the room.", 2)
                dialogue("In one of the last boxes, there's a rusted iron key!", 0.3)
                dialogue("(STAIRWELL 1 KEY was added to INVENTORY)", 0.3)
                room4Searched = True
                storage.append("stairwell 1 key")
                location(4)
            else:
                dialogue("You've already searched this room.", 0.3)
                location(4)
        if ans == "inventory":
            inventory(4)
            location(4)
        else:
            dialogue("You can't do that.", 0.3)
            location(4)
    if locationVar == 5:
        print("thanks man you finished the tiny lil demo yayaya")
        quit()
            
location(1)
print("if you are seeing this message, something may be wrong or you have finished the demo")   
    
