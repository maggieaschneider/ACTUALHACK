import random
from tkinter import *

class meme_gen(Frame):
    def __init__(self, master):
        super().__init__(master)
        print("create meme gen")
        self.image_dict = {}
        text_file = open("image_list", "r")
        for line in text_file:
            l = line.strip()
            mem = l.split(",")
            self.image_dict[mem[0]] = mem[1]
        self.create_widgets()
        self.grid()

    def create_widgets(self):
        Button(self, text="Generate Meme", command=self.generate
               ).grid(row=0, column=0, sticky=W)

        self.i = Label(text= "")


    def generate(self):
        self.i.destroy()
        meme_num = str(random.randrange(1,31))
        image = PhotoImage(file="images/meme"+meme_num+".gif")
        self.i = Label(self, image=image)
        self.i.photo = image
        self.i.grid(row=5, column=0, sticky=W)










