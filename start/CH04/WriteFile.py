#!/usr/bin/env python3
# Sample script that writes to a file
# By Lynae Woody

'''
Opens the file hackme.txt and writes the content of the responses into it
'''

#The list of questions to ask the user!

questions = [
    "What is your name? ",
    "What is your favorite color? ",
    "What was your first pet's name? ",
    "What is your mother's maiden name? ",
    "What elementary school did you attend? "
]

#The list where the answers will be stored

answers = []

#Loop through the questions and save the input to the answers variable

for q in questions:
    ans = input(q)
    answers.append({ans})
print(answers)