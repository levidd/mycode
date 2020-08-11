#!/usr/bin/env python3

# create a list containing three items
my_list = [ "192.168.0.5", 5060, "UP" ]

# display the first item in the list
print("The first item in the list (IP): " + my_list[0] )

# display the second item in the list
print("The second item in the list (port): " + str(my_list[1]) )

# display the third item in the list
print("The last item in the list (state): " + my_list[2] )

def myPrint(subsection) :
        returning = ", ".join(list(map(str, subsection[0:-1])))
        returning += f", or {subsection[-1]}"

        return returning

new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

def doPrint(stuff) :
    print(f"When I {stuff[-1]} into IP addresses {myPrint(stuff[3:5])} I am unable to ping ports {myPrint(stuff[0:3])}.")

doPrint(new_list)




