#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

def getThing(adapter, thing):
    return netifaces.ifaddresses(adapter)[thing][0]['addr']

def getMAC(adapter):
    return getThing(adapter, netifaces.AF_LINK)

def getIP(adapter):
    return getThing(adapter, netifaces.AF_INET)


for i in netifaces.interfaces():
    print('\n****** details of interface - ' + i + ' ******')
    try:
        print('MAC:', getMAC(i))
        print('IP:', getIP(i))
    except:          # This is a new line
        print('Could not collect adapter information') # Print an error message

