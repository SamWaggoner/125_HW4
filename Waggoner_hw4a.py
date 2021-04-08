# File: hw4a.py
# Author: Sam Waggoner
# Date: 10/13/2020
# Section: 1006
# E-mail samuel.waggoner@maine.edu
# Description:
# Write a program that gives students advice about choosing a major, using at
# least one function.
# Collaboration:
# I went to Zach's office hours to find out how to not print "None", he directed me
# to return an empty string.
def main():

    print("Hello, I will help you to pick a major.")
    print("Please type yes or no for the following questions.")
    problems = input("Do you like problem solving? ") # cs, social work
    helping = input("Do you like to help others? ") # cs, social work, teaching
    create = input("Do you like to create? ") # cs, art
    money = input("Is money a large consideration in choosing a major? ") # cs, business, NOT social work, teaching, art
    # options = cs, social work, teaching, art, business
    def art():
        if money != "yes" and create == "yes":
            return "and art"
        return ""
    def social_work():
        if money != "yes" and problems == "yes" or helping == "yes":
            return "social work"
        return ""
    def teaching():
        if money != "yes" and helping == "yes":
            return "teaching"
        return ""
    def cs():
        cslist = []
        if problems == "yes":
            cslist.append(problems)
        if helping == "yes":
            cslist.append(helping)
        if create == "yes":
            cslist.append(create)
        if money == "yes":
            cslist.append(money)
        if len(cslist) > 2:
            return "computer science"
        return ""
    def business():
        if money == "yes":
            return "business"
        return ""
    say_and2 = ""
    say_and3 = ""
    say_and4 = ""
    say_and5 = ""
    say_and2 = "and"
    if social_work() == "":
        say_and2 == ""
    say_and3 == "and"
    if teaching() == "":
        say_and3 == ""
    say_and4 == "and"
    if cs() == "":
        say_and4 == ""
    say_and5 == "and"
    if business() == "":
        say_and5 == ""
    if cs() == "" and business() == "" and teaching() == "" and art() == "":
        print("Sorry, I don't know of any great majors for you right now.")
    else:
        print("Based off your answers, the major/s that may fit you is/are", \
        str(art()), say_and2, str(social_work()), say_and3, str(teaching()), say_and4,  \
        str(cs()), say_and5, str(business())+".")

main()

# If I were doing this earlier and had more time I would fix the print statement, 
# fixing the is/are, major/s, the spacing, and the "and"s between the majors.
