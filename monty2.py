# Joanna Li
# Homework 2
# Part 2
#
    
# import library "random" to choose random number
import random

# create definition to pick random number to represent door with prize
def numberRandom():
    prize = random.randint(1,3)
    #print(prize)
    return prize

# create definition to pick random number
# represents player's door choice
def initial():
    pick = random.randint(1,3)
    #print(pick)
    return pick

# user never changes pick after gag gift door removed
def montenever(win1):
    # call first 2 definitions
    prize = numberRandom()
    pick = initial()
    # player chose the prize door
    # doesn't switch choice
    # will always be True
    # otherwise will be False
    if prize == pick:
        win1 = True
    return win1       
    #else:
        #print(False)

# user changes choise after gag gift is revealed
def montealways(win2):
    # calls first 2 definitions again
    prize = numberRandom()
    pick = initial()
    # make list of doors according to number to remove gag door
    doors = ["1", "2", "3"]
    while True:
        # chooses a door to remove at random
        remove = random.choice(doors)
        # if number chosen is same number as prize or pick
        # continue until third number choice is found
        if remove == prize or remove == pick:
            continue
        else:
            # remove the gag door based on the randomly selected number
            # works because it is not prize door or picked door
            # must be converted from string to integer
            # in order to subtract values
            remove = int(remove)
            # index number is 1 less than number on door
            # because index starts at 0
            index = remove - 1
            # removes gag door from list
            doors.pop(index)
            #print(doors)
            break
    # if chosen door is not the same as prize door
    # it means player is switching to door with prize
    # and new choice is the prize door
    # so True will be returned
    if pick != prize:
        win2 = True
    return win2
    # the picked door is the same as prize door
    # but player switches door
    # resulting in wrong choice and False as answer
    #else:
        #print(False)

# calls both definitions
# runs game

def main():
    # user enter input: number of games to play
    z = input("Number of games to play:")

    # make sure user enters a positive integer
    try:
        z = int(z) # must be integer
    except:
        print("Please enter a positive number:")
        exit()
    if z < 0: # must be positive
        print("Please enter a positive number:")
        exit()

    # wins to start game with
    win1 = 0
    win2 = 0
    # loops through games
    for z in range(1, z + 1):
        if montenever(win1) == True:
            # each time player wins without switching
            # add 1 to total wins
            win1 += 1
        # find the part of wins out of total
        result1 = win1 / z
            
        if montealways(win2) == True:
            # number of wins added
            # each time player switches and wins
            win2 += 1
        # how much wins out of total games played
        result2 = win2 / z

    print("Out of", z, "games:")
    print("Always switching wins:", "%9.7f" % (result2), "(", end="")
    print(win2, "games)")
    print("Never switching wins:", "%9.7f" % (result1), "(", end="")
    print(win1, "games)")

main()
