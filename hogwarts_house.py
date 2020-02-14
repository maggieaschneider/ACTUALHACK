from tkinter import *

class hogwarts(Frame):
    def __init__(self, master):
        super(hogwarts, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text = "What Hogwart's House Do You Belong In, Based Off Of Your Ideal Date?").grid(row = 0, column = 1, columnspan = 2)

        Label(self, text="Who Are You Going On A Date With:").grid(row=1, column=0, sticky=W)
        self.person = StringVar()
        self.person.set(None)
        people = ["celebrity", "crush", "best friend", "dr. bath"]
        column = 1
        for word in people:
            Radiobutton(self, text=word, variable=self.person, value=word).grid(row=2, column=column, sticky=W)
            column += 1

        Label(self, text="Pick A Place:").grid(row=3, column=0, sticky=W)
        self.place = StringVar()
        self.place.set(None)
        places = ["movies", "dungeon", "beach", "museum"]
        column = 1
        for word in places:
            Radiobutton(self, text=word, variable=self.place, value=word).grid(row=4, column=column, sticky=W)
            column += 1

        Label(self, text="Pick An Outfit:").grid(row=5, column=0, sticky=W)
        self.outfit = StringVar()
        self.outfit.set(None)
        outfits = ["suit", "dress", "swag minecraft skin", "kilt"]
        column = 1
        for word in outfits:
            Radiobutton(self, text=word, variable=self.outfit, value=word).grid(row=6, column=column, sticky=W)
            column += 1

        Label(self, text="Pick A Gift For Your Date:").grid(row=7, column=0, sticky=W)
        self.gift = StringVar()
        self.gift.set(None)
        gifts = ["chocolate", "vacuum cleaner set", "teddy bear", "white van"]
        column = 1
        for word in gifts:
            Radiobutton(self, text=word, variable=self.gift, value=word).grid(row=8, column=column, sticky=W)
            column += 1

        Label(self, text="What Will You Pick Up Your Date In:").grid(row=9, column=0, sticky=W)
        self.ride = StringVar()
        self.ride.set(None)
        rides = ["jet", "ferrari", "tricycle", "submarine"]
        column = 1
        for word in rides:
            Radiobutton(self, text=word, variable=self.ride, value=word).grid(row=10, column=column, sticky=W)
            column += 1

        submit_bttn = Button(self, text="Click to See Your Result!", command=self.house)
        submit_bttn.grid(row=11, column=0, sticky=W)
        self.story_txt = Text(self, width=75, height=10, wrap=WORD)
        self.story_txt.grid(row=12, column=0, columnspan=4)

    def house(self):
        place = self.place.get()
        finalAnswer = ""
        if self.place.get() == "movies":
            finalAnswer += "You belong in Hufflepuff!"
        if self.place.get() == "dungeon":
            finalAnswer += "You belong in Slytherin!"
        if self.place.get() == "beach":
            finalAnswer += "You belong in Gryffindor!"
        if self.place.get() == "museum":
            finalAnswer += "You belong in Ravenclaw!"

        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, finalAnswer)


