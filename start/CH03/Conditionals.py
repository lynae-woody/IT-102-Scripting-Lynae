#!/usr/bin/env python3
# example workign with conditionals
#By Lynae Woody

#First, I am going to ask the user if their day is good or bad
question = input("Is your day good? Answer y or n: ")

#Second, I will analyze the value and will respond accordingly
if question == 'y':
    print("Yes it is.")
elif question == 'n':
    print("Aww that's okay! Tomorrow will be a better day.")
elif question == 'idk':
    print("That's alright.")
else:
    print("Please enter a valid answer of y for yes and n for no.")