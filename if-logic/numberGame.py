#!/usr/bin/env python3

""" 
    Author: Levi Davis
    
    A Python script to make a calculator that uses english to perform opperations

"""
from random import randint

# a function to do nothing
def nothing(target, num):
    return target

# grouping the functions together in a dict to make it easier to call
operations = {
        "add" : (lambda x, y : x + y),
        "minus" : (lambda x, y: x - y),
        "multiply" : (lambda x, y: x * y),
        "nothing" : nothing
        }

# function to get number from a string value. returns 0 if value passed was not a float
def getNum(value):
    try :
        return float(value)
    except ValueError:
        return 0

#  function to get a random list of numbers to use in the number game
def getRandomItems(num):
    returning = []
    i = 0
    while i < num:
        returning.append(float(randint(1,100)))
        i = i + 1
    return returning

# function to make a random target by applying the operator functions to the passed list
def makeTarget(items):
    total = items[0]
    for item in items[1::]:
        funChoice = randint(0,2)
        fun = list(operations.keys())[0:-1][funChoice]
        total = operations.get(fun)(total, item)
    return total

# function to check if player wants to go another round. Recursively calls
# if the user does not use the right call
def anotherRound():
    val = input("Go again? ").strip().lower()
    if val == "yes" or val == "y":
        return True
    elif val == "no" or val == "n":
        return False
    else:
        print("Please type either yes, y, no, or n")
        return anotherRound()
    
# function to get the action the user wants to do
def getAction():
    while True:
        action = input("Action ? ")
        if action != "":
            return action
        else:
            print("Please type an action")

# function to apply the action to a target, using the items in the passed list
def doAction(action, target, items):
    inputs = action.strip().lower().split(" ")
    fun = ""
    num = ""

    # check if there are actually two inputs
    if len(inputs) < 2:
        fun = "nothing" # do nothing if not enough
        num = 0
    else:
        fun = inputs[0]
        num = getNum(inputs[1])
    
    if num in items and fun in operations:
        items.remove(num)
        return operations.get(fun)(target, num)
    else:
        print(f"That wasn't a supported operation. Try one of these: {list(operations.keys())[0:-1]}") 
        return operations.get("nothing")(target, num)
    
    
""" Do the game """    
print("Welcome to the Numbers game!")
print("To play the game, you need to get to the target number by using the numbers given to you.")
print("You can add, multiply, or subtract. e.g. 'add four' or 'multiply 100'")

doRound = True

while doRound:
    items = getRandomItems(5)
    target = makeTarget(items)
    current = 0
    while current != target and len(items) != 0:
        print(f"\n\nCurrent number: {current}, target is {target}.\nItems left {items}.")
        current = doAction(getAction(), current, items)
   
    print(f"\n\nEnding value: {current}. The target was {target}")

    if current != target:
        print("Dang! You didn't get it.")
    else:
        print("WOW! Great job!")
    
    doRound = anotherRound()







