#!/usr/bin/env python3
# example workign with Loops
#By Lynae Woody

#First, I am going to ask the user if their day is good or bad
question = input("Is your day good? Answer y or n: ").lower()

#Create a function called send_message for the "yes it is" loop
def send_message():
    if question == 'y':
    #Creates a loop that prints "Yes it is" 10 times when the user types 'y'
        number = 1
        while number < 11:
            print("Yes it is.")
            number += 1
    #Second, I will analyze the value and will respond accordingly
    elif question == 'n':
            print("Aww that's okay! Tomorrow will be a better day.")
    elif question == 'idk':
        print("That's alright.")
    else:
        print("Please enter a valid answer of y for yes and n for no.")


send_message()