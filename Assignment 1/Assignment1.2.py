"""""
Title: Assignment 1.2 Authorization Test
Author: Simone Lewis
Date: 09-22-2022

This script contains the solutions for problem 2 from assignment 1. 

"""""





def welcome_user():
    while True:
        name = input('Welcome, what is your name?')
        password = input('Welcome, ' + name + ', please enter the password.')
        if password == 'calico':
            print('That is the correct password, welcome ' + name)
            break
        elif password != 'calico':
         print('That is not the correct password, please try again.')
        continue
welcome_user()