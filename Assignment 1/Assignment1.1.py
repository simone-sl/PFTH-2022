"""""
Title: Assignment 1.1 Pattern Generator
Author: Simone Lewis
Date: 09-22-2022

This script contains the solutions for problem 1 from assignment 1. 

"""""


pyramids = int(input("Enter Number of Pyramids: "))
length = 9
for k in range(pyramids):
    for i in range(1, length + 1):
        for j in range(1, i):
            print("*", end='')
        print("")
    for i in range(length - 1, 0, -1):
        for j in range(1, i):
            print("*", end='')
        print("\r")