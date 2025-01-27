#!/bin/python

def menu() :
    print("1) Read and display names")
    print("2) Add a new name")
    print("3) Exit")

def read_and_display() :
    with open("names.txt", "r") as file:
        for name in file:
            print("Hello,", name.strip() )
            
def writeName() :
    with open("names.txt", "a") as file:
        file.write("\n" + input("Enter a new name: ") )
writeName ()      

