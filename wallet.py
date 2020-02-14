from tkinter import *
class wallet(Frame):
    def __init__(self):
    def create_widgets(self):
    def math(self):
            if choice == "p":
                total += 0.01
                print("New balance: $%0.2f" % (total))
            elif choice == "n":
                total += 0.05
                print("New balance: $%0.2f" % (total))
            elif choice == "d":
                total += 0.10
                print("New balance: $%0.2f" % (total))
            elif choice == "q":
                total += 0.25
                print("New balance: $%0.2f" % (total))
            # print output if there is an invalid option(reprint menu as well)
            elif choice != "e":
                print("Invalid option.")
                print("\tMENU")
                print("(p) - deposit a penny")
                print("(n) - deposit a nickel")
                print("(d) - deposit a dime")
                print("(q) - deposit a quarter")
                print("(e) - exit program and give balance")
            # print out after every input to ask user if they would like to deposit more money
            choice = input("Please press a letter to select an option: ")

        # print if the user wants to exit and leave
        if choice == "e":
            print("Final balance: $%0.2f" % (total))
            print("Goodbye.")