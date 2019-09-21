# Joanna Li
# Homework 2
# Part 3
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

    print("Always switching wins:", "%9.7f" % (result2), "(", end="")
    print(win2, "games)")
    print("Never switching wins:", "%9.7f" % (result1), "(", end="")
    print(win1, "games)")

    import turtle

    # name of turtle program is "histogram"
    histogram = turtle.Turtle()

# points and coordinates scaled by 2
    # draws first line of graph
    histogram.penup()
    # starts at this point
    histogram.goto(-120, -120)
    histogram.pendown()
    # length of line
    histogram.forward(125 * 2)

    # after drawing line, pick up pen and go to where first bar starts
    histogram.penup()
    # leave 20 units of space on left
    histogram.goto(-100, -120)
    histogram.pendown()
    # will fill bar color
    histogram.begin_fill()
    # begin drawing bar outline
    histogram.left(90)
    histogram.forward((result2 * 200))
    histogram.right(90)
    histogram.forward(80)
    histogram.right(90)
    # height of bar determined by input from trials of game
    # result of switching doors
    # multiplied by 200 for scaling on graph
    histogram.forward((result2 * 200))
    # bar is filled color black
    histogram.end_fill()

    # pen up; go to center of top of bar
    # lists the result from game trials after switching doors in decimal
    histogram.penup()
    histogram.goto(-70, (result2 * 200) -120)
    histogram.pendown()
    # format the font to Arial size 10 normal
    histogram.write(result2, ("Arial", 10, "normal"))

    # label as Always
    histogram.penup()
    histogram.goto(-70, -136)
    histogram.write("Always", ("Arial", 10, "normal"))

    # pen up then move to next point
    histogram.goto(110, -120)
    # begin drawing second bar
    histogram.pendown()
    histogram.begin_fill()
    # draws and fills box
    # height of second bar based on game trial, not switching
    histogram.backward((result1 * 200))
    histogram.right(90)
    histogram.forward(80)
    histogram.left(90)
    histogram.forward((result1 * 200))
    histogram.end_fill()

    # result of game trials by not swtiching in decimal
    histogram.penup()
    histogram.goto(60, (result1 * 200)- 120)
    histogram.pendown()
    histogram.write(result1, ("Arial", 10, "normal"))

    # label as Never
    histogram.penup()
    histogram.goto(60, -136)
    histogram.write("Never", ("Arial", 10, "normal"))

    # write the title of graph, first sentence
    histogram.goto(-60, -150)
    histogram.write("The Monty Hall Problem: 100000 games", ("Arial", 10, "normal"))

    # write second sentece
    histogram.goto(-80, -160)
    histogram.write("Percentage of games won if you switch always or never", ("Arial", 10, "normal"))
    
main()
