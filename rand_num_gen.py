from tkinter import *
import random

class rand_num_gen(Frame):
    def __init__(self, master):
        super(rand_num_gen, self).__init__(master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        Button(self, text = "Click for a random random number 1-100", command = self.randomness).grid(row = 0, column = 0)
        self.margaret = Label(self, text="",font = "Helvetica, 40")
        self.margaret.grid(row=1, column=0)

    def randomness(self):
        self.margaret["text"] = random.randrange(1,100,1)
