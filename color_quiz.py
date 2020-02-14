from tkinter import *

class color(Frame):
    def __init__(self, master):
        super(color, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text = "Which Color Represents Your Personality?").grid(row = 0, column = 1, columnspan = 2)

        Label(self, text="Pick A Dessert:").grid(row=1, column=0, sticky=W)
        self.dessert = StringVar()
        self.dessert.set(None)
        desserts = ["chocolate cupcake", "caramel apple", "snickerdoodle cookie", "chocolate bar", "vanilla ice cream", "brownie", "macaron"]
        column = 1
        for word in desserts:
            Radiobutton(self, text=word, variable=self.dessert, value=word).grid(row=2, column=column, sticky=W)
            column += 1

        Label(self, text="Pick A Job:").grid(row=3, column=0, sticky=W)
        self.job = StringVar()
        self.job.set(None)
        jobs = ["doctor", "teacher", "mailman", "carpenter", "chef", "electrician", "software engineer"]
        column = 1
        for word in jobs:
            Radiobutton(self, text=word, variable=self.job, value=word).grid(row=4, column=column, sticky=W)
            column += 1

        Label(self, text="Pick A Game:").grid(row=5, column=0, sticky=W)
        self.game = StringVar()
        self.game.set(None)
        games = ["hide-and-seek", "tag", "checkers", "pac-man", "simon says", "hopscotch", "jump-rope"]
        column = 1
        for word in games:
            Radiobutton(self, text=word, variable=self.game, value=word).grid(row=6, column=column, sticky=W)
            column += 1

        Label(self, text="Pick A Fantasy Character:").grid(row=7, column=0, sticky=W)
        self.fantasy = StringVar()
        self.fantasy.set(None)
        fantasies = ["centaur", "princess", "dragon", "unicorn", "fairy godmother",
                    "prince charming", "wizard"]
        column = 1
        for word in fantasies:
            Radiobutton(self, text=word, variable=self.fantasy, value=word).grid(row=8, column=column, sticky=W)
            column += 1

        Label(self, text="Pick A Holiday:").grid(row=9, column=0, sticky=W)
        self.holiday = StringVar()
        self.holiday.set(None)
        holidays = ["christmas", "halloween", "valentine's day", "easter", "hanukkah",
                     "kwanzaa", "diwali"]
        column = 1
        for word in holidays:
            Radiobutton(self, text=word, variable=self.holiday, value=word).grid(row=10, column=column, sticky=W)
            column += 1

        submit_bttn = Button(self, text="Click to See Your Result!", command=self.color)
        submit_bttn.grid(row=11, column=0, sticky=W)
        self.story_txt = Text(self, width=75, height=10, wrap=WORD)
        self.story_txt.grid(row=12, column=0, columnspan=4)

    def color(self):
        dessert = self.dessert.get()
        finalAnswer = ""
        if self.dessert.get() == "chocolate cupcake":
            finalAnswer += "Your color is red!"
        if self.dessert.get() == "caramel apple":
            finalAnswer += "Your color is orange!"
        if self.dessert.get() == "snickerdoodle cookie":
            finalAnswer += "Your color is yellow!"
        if self.dessert.get() == "chocolate bar":
            finalAnswer += "Your color is green!"
        if self.dessert.get() == "vanilla ice cream":
            finalAnswer += "Your color is blue!"
        if self.dessert.get() == "brownie":
            finalAnswer += "Your color is purple!"
        if self.dessert.get() == "macaron":
            finalAnswer += "Your color is pink!"

        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, finalAnswer)


