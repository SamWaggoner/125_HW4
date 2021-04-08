# File: hw4c.py
# Author: Sam Waggoner
# Date: 10/13/2020
# Section: 1006
# E-mail samuel.waggoner@maine.edu
# Description:
# Write a program that draws a box with a border and a fill symbol.
# Collaboration:
# I got a piece of general advice from Zach during his office hours.

# I basically did this without lists, since I tried it with lists but it wasn't working out.
# This code is ugly, bulky, redundant, and inefficient. :)
def main():
    park1 = (input("What is one of your favorite parks in Maine? "))
    visitors1 = (int(input("How many thousands of people visited "+str(park1)+" in a year? ")))
    park2 = (input("What is one of your favorite parks in Maine? "))
    visitors2 = (int(input("How many thousands of people visited "+str(park2)+" in a year? ")))
    park3 = (input("What is one of your favorite parks in Maine? "))
    visitors3 = (int(input("How many thousands of people visited "+str(park3)+" in a year? ")))    
    park4 = (input("What is one of your favorite parks in Maine? "))
    visitors4 = (int(input("How many thousands of people visited "+str(park4)+" in a year? ")))    
    park5 = (input("What is one of your favorite parks in Maine? "))
    visitors5 = (int(input("How many thousands of people visited "+str(park5)+" in a year? ")))
    def attendMinpark():
        minpark = ""
        minvisitors = int(999999999999999999)
        if visitors1 < minvisitors:
            minvisitors = visitors1
        if visitors2 < minvisitors:
            minvisitors = visitors2
        if visitors3 < minvisitors:
            minvisitors = visitors3
        if visitors4 < minvisitors:
            minvisitors = visitors4
        if visitors5 < minvisitors:
            minvisitors = visitors5
        if minvisitors == visitors1:
            minpark = str(park1)
        if minvisitors == visitors2:
            minpark = str(park2)
        if minvisitors == visitors3:
            minpark = str(park3)
        if minvisitors == visitors4:
            minpark = str(park4)
        if minvisitors == visitors5:
            minpark = str(park5)
        return str(minpark)
    def attendMinvisitors():
        minpark = ""
        minvisitors = int(999999999999999999)
        if visitors1 < minvisitors:
            minvisitors = visitors1
        if visitors2 < minvisitors:
            minvisitors = visitors2
        if visitors3 < minvisitors:
            minvisitors = visitors3
        if visitors4 < minvisitors:
            minvisitors = visitors4
        if visitors5 < minvisitors:
            minvisitors = visitors5
        return int(minvisitors*1000)
    def attendMaxpark():
        maxpark = ""
        maxvisitors = int(0)
        if visitors1 > maxvisitors:
            maxvisitors = visitors1
        if visitors2 > maxvisitors:
            maxvisitors = visitors2
        if visitors3 > maxvisitors:
            maxvisitors = visitors3
        if visitors4 > maxvisitors:
            maxvisitors = visitors4
        if visitors5 > maxvisitors:
            maxvisitors = visitors5
        if maxvisitors == visitors1:
            maxpark = str(park1)
        if maxvisitors == visitors2:
            maxpark = str(park2)
        if maxvisitors == visitors3:
            maxpark = str(park3)
        if maxvisitors == visitors4:
            maxpark = str(park4)
        if maxvisitors == visitors5:
            maxpark = str(park5)
        return str(maxpark)
    def attendMaxvisitors():
        maxpark = ""
        maxvisitors = int(0)
        if visitors1 > maxvisitors:
            maxvisitors = visitors1
        if visitors2 > maxvisitors:
            maxvisitors = visitors2
        if visitors3 > maxvisitors:
            maxvisitors = visitors3
        if visitors4 > maxvisitors:
            maxvisitors = visitors4
        if visitors5 > maxvisitors:
            maxvisitors = visitors5
        return int(maxvisitors*1000)
    def attendTotal():
        total = 0
        total = (visitors1 + visitors2 + visitors3 + visitors4 + visitors5)*1000
        return int(total)
    def attendAvg():
        total = visitors1 + visitors2 + visitors3 + visitors4 + visitors5
        average = (total/5)*1000
        return float(average)
    print("The park with the fewest visitors is "+str(attendMinpark())+" at "+str(attendMinvisitors())+" people.")
    print("The park with the most visitors is "+str(attendMaxpark())+" at "+str(attendMaxvisitors())+" people.")
    print("The total number of visitors at these parks is "+str(attendTotal())+".")
    print("The average number of visitors is "+str(attendAvg())+".")
main()

# Below is a version of the code that doesn't use lists or functions. It is much
# more simple, although it doesn't follow the prompt like the one above.

"""
def main():
    total = 0
    maxvisitors = 0
    for i in range(5):
        park = (input("What is one of your favorite parks in Maine? "))
        visitors = (int(input("How many thousands of people visited "+str(park)+" in a year? ")))
        if visitors > maxvisitors:
            maxvisitors = visitors
            maxpark = str(park)
        total += visitors
    average = total/5

    def print_results():
        print("The park with the most visitors is "+str(maxpark)+" at "+str(maxvisitors)+" people.")
        print("The total number of visitors at these parks is "+str(total)+".")
        print("The average number of visitors is "+str(average)+".")
    print_results()
main()
"""


# I tried using lists and tuples, but then decided to try it a simpler way.
# I couldn't find how to match the name of the park with the max and min values.
# Below are my failed and or unfinished attempts.

"""
def main():

    park_visitors_list = [["park1","visitors1"],["park2","visitors2"],["park3","visitors3"],["park4","visitors4"],["park5","visitors5"]]
    for i in range(5):
        park_visitors_list[i][0] = (input("What is one of your favorite parks in Maine? "))
        park_visitors_list[i][1] = (int(input("How many thousands of people visited "+park_visitors_list[i][0]+" in a year? ")))
    park_visitors_tuple = tuple(park_visitors_list)
    def attendMin():
        return min(park_visitors_tuple)
    def attendMax():
        return max(park_visitors_tuple)
    def attendTotal():
        for i in range(5):
            total += park_visitors_list[i][1]
        return total
    def attendAvg():
        for i in range(5):
            total += park_visitors_list[i][1]
        average = total/5
        return average
    maximum = attendMax()
    print(maximum)
    minimum = attendMin()
    print(minmum)
    total = attendTotal()
    print(total)
    average = attendAvg()
    print(average)
    print("The park with the most visitors in a year is "+",")
main()

"""
"""
def main():

    visitors = []
    parklist = []
    for i in range(5):
        parklist.append(input("What is one of your favorite parks in Maine? "))
        visitors.append(int(input("How many thousands of people visited "+parklist[i]+" in a year? ")))
    parklist_tup = tuple(parklist)
    visitors_tup = tuple(visitors)
    def attendMin():
        return min(visitors_tup)
    def attendMax():
        return max(visitors_tup)
    def attendTotal():
        for i in range(len(visitors)):
            total += visitors[i]
        return total
    def attendAvg():
        for i in range(len(visitors)):
            total += visitors[i]
        average = total/len(parklist)
    maximum = attendmax()
    minimum = attendmin()
    total = attendtotal()
    average = attendAvg()
    print("The park with the most visitors in a year is "+)
main()
"""