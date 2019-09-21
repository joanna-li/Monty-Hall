# Joanna Li
# Homework 2
# Part 1
#

# import library "random" to choose random number
import random

# create definition to pick random number to represent door with prize
def numberRandom():
    prize = random.randint(1,3)
    #print(prize)
    return prize

# create definition to pick random number that represents player's door choice
def initial():
    pick = random.randint(1,3)
    #print(pick)
    return pick

# user never changes pick after gag gift door removed
def montenever():
    # call first 2 definitions
    prize = numberRandom()
    pick = initial()
    # player chose the prize door
    # doesn't switch choice
    # will always be True
    # otherwise will be False
    if prize == pick:
       print(True)
    else:
        print(False)

# user changes choise after gag gift is revealed
def montealways():
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
            # must be converted from string to integer in order to subtract
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
    # so True will be printed
    if pick != prize:
        print(True)
    # the picked door is the same as prize door
    # but player switches door
    # resulting in wrong choice and False as answer
    else:
        print(False)

# calls both definitions
# runs game
def main():
    montenever()
    montealways()

main()
