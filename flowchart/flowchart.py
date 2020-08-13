#!/usr/bin/env python3

"""
    Levi D Davis

    A python script that is an interactive flowchart. 
"""
import sys

class FlowChartNode:
    
    # init
    def __init__(self, phrase):
        self.phrase = phrase

    def __init__(self, phrase, nodes):
        self.phrase = phrase
        if len(nodes) > 0:
            self.setYesNode(nodes[0])
        if len(nodes) > 1:
            self.setNoNode(nodes[1])

    def setYesNode(self, yesNode):
        self.yes = yesNode

    def setNoNode(self, noNode):
        self.no = noNode

    def getChild(self, childNum):
        if childNum == 1:
            return self.yes
        else:
            return self.no

    def getPhrase(self):
        return self.phrase

    def getType(self):
        if hasattr(self, "no"):
            return 2
        elif hasattr(self, "yes"):
            return 1
        else:
            return 0

def convertToInt(item):
    try:
        return int(item)
    except ValueError:
        return []

nodeFile = "flowChartNodes.txt"
flowChart = []

# load the flowchart nodes
with open(nodeFile) as nodes:
    line = 0
    for nodeLine in nodes:
        if line == 0:
            line += 1
            continue
        # get each param as element in list (seperated by ':'), strip excess space
        nodeParams = list(map(lambda x: x.strip(), nodeLine.split(":")))
        
        # last item may be a comma seperate list, replace in list as another list
        nodeParams.append(list(map(convertToInt, nodeParams.pop().split(","))))

        flowChart.append(FlowChartNode(*nodeParams[1::]))

def valCheck(result, nodeType):
    result = result.strip().lower()
    if result == "q" or result == "quit":
        return 0
    elif nodeType == 1 or result in ["yes", "y"]:
        return 1
    elif result in ["no", "n"]:
        return 2
    else:
        print("That isn't one of the options dummy!")
        valCheck(input("yes (y) or no (n)? "), 2)

def doQuestion(node):
    print(node.getPhrase())
    response = getResponse(node)
    doQuestion(flowChart[response]) 

def getResponse(node):
    nodeType = node.getType()
    val = 0
    if nodeType == 1:
        val = valCheck(input("Continue "), 1)
    elif nodeType == 2:
        val = valCheck(input("yes (y) or no (n)? "), 2)
    else:
        print("Now do some pushups")

    # val was never changed, or a quit was inputted, exit now
    if val == 0:
        sys.exit()
    else:
        return node.getChild(val)

doQuestion(flowChart[0])


