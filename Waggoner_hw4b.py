# File: hw4b.py
# Author: Sam Waggoner
# Date: 10/13/2020
# Section: 1006
# E-mail samuel.waggoner@maine.edu
# Description:
# Write a program that draws a box with a border and a fill symbol.
# Collaboration:
# I worked by myself.

def main():
    
    width = int(input("What is the width of the box? "))
    while width < 0:
        width = int(input("Please enter a non-negative value for width. "))
    height = int(input("What is the height of the box? "))
    while height < 0:
        height = int(input("Please enter a non-negative value for height. "))
    symbol = input("With what symbol will the box be filled? ")
    outline = input("With what symbol will the box be outlined? ")
    def drawbox():
        if height == 1:
            print(width*outline)
        elif width == 1:
            print(height*outline)
        else:
            print(width*outline)
            for i in range((height-2)):
                print(outline+(width-2)*symbol+outline)
            print(width*outline)
    drawbox()

main()