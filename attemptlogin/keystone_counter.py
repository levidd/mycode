#!/usr/bin/env python3

loginfail = 0

with open("keystone.common.wsgi", "r") as keystone_lines:
    for line in keystone_lines:
        if "- - - -] Authorization failed" in line:
            loginfail += 1

print("The unmber of failed log in attempts is", loginfail)

