"""
Note: To allow duplicates, do not enter an argument for lastElement
Note: Feel free to customize to colors and limbs lists!
"""
#AAAAAAAAAAAA

import random

colors = ["red", "blue", "green", "tan", "any color"]
limbs = ["right hand", "left hand", "right foot", "left foot", "anything"]
steps = []

#picks a random element from a given list
def pickElement(list, lastElement = None):
    element = random.choice(list)
    #Checks if it's a new element
    if element != lastElement:
        return element
    #If duplicates allowed, returns a duplicate
    if lastElement == None:
        return element
    #If dpulicates NOT allowed, recurses until a non-duplicate is found
    else:
        return pickElement(list, element)

#Creates a starting position for each a limb (colors are randomized)
def firstFour():
    steps.append(("right hand", pickElement(colors)))
    steps.append(("left hand", pickElement(colors)))
    steps.append(("right foot", pickElement(colors)))
    steps.append(("left foot", pickElement(colors)))

#Prints out a list of random steps
def printSteps():
    firstFour()
    for i in range(30):
        steps.append((pickElement(limbs, steps[-1][0]), pickElement(colors, steps[-1][1])))
    for x in steps: print(x)

printSteps()