#!/usr/bin/env python3

"""
    Levi D Davis

    A python script that is an interactive flowchart.
"""

from os import path

def getNums(nums):
    returning = [x.strip() for x in nums.split(",")]
    if len(returning[0]) == 0:
        returning = []
    return returning


# load the flowchart nodes
def loadFlowChart(file, flowChart):
    with open(file) as nodes:
        line = 0
        for nodeLine in nodes:
            if line == 0:
                line += 1
                continue

            # get each param as element in list (seperated by ':'), strip excess space
            nodeParams = [x.strip() for x in nodeLine.split(":")]

            # place the node in the flowchart dict, line is key, values are phrase and node list
            # everything are strings!
            flowChart[nodeParams[0]] = [nodeParams[1], getNums(nodeParams[2])]


def valCheck(output, nodeType):
    result = input(output).strip().lower()
    if result in ["q", "quit"]:
        return -1
    elif nodeType == 1 or result in ["yes", "y"]:
        return 0
    elif result in ["no", "n"]:
        return 1
    else:
        return -2


def getResponse(node):
    # print the phrase
    print(node[0])

    nodeType = len(node[1])
    val = -1
    if nodeType == 1:
        val = valCheck("Continue (or quit: q)", 1)
    elif nodeType == 2:
        val = valCheck("Yes (y) or No (n) (or quit: q)? ", 2)

    # val was never changed, or a quit was inputted, exit now
    if val == -1:
        return -1
    elif val == -2:
        print("That wasn't one of the options dummy!")
        return getResponse(node)
    else:
        return node[1][val]



def main():
    doCharts = True
    while doCharts:
        flowChart = {}
        nodeFile = ""
        while nodeFile == "":
            nodeFile = input("What flowChart do you want to use?\n")
            if nodeFile in ["quit", "q"]:
                return
            elif not path.exists(nodeFile):
                print("That flowChart doesn't exist! Try again or quit (q)")
                nodeFile = ""

        flowChart = {}
        loadFlowChart(nodeFile, flowChart)
        doFlowChart = True
        curr = '0'
        while doFlowChart:
            curr = getResponse(flowChart[curr])
            if curr == -1:  # hit an endpoint or quitting
                doFlowChart = False

        print("All done with that flowchart")
        print("\n"*5)

main()