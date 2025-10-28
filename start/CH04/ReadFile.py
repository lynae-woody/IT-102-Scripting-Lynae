#!/usr/bin/env python3
# Sample script that reads from a file
# By Lynae Woody

'''
A script to open the file and read the contents
'''

with open("hackme.txt", "r") as test:
    content = test.read()
    print("Here is someone to hack - " + "\n" + content)
