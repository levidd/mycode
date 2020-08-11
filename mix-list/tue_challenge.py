#!/usr/bin/env python3

icecream = ["flavors", "salty"]

icecream.append(99)

name = input("What is your name? ").strip().title()

sep = " "

print(f"{sep.join(map(str, [icecream[i] for i in (-1, 0)]))}, and {name} chooses to be {icecream[1]}.") 

