from tkinter import *

class disney_princess(Frame):
    def __init__(self, master):
        super(disney_princess, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text = "Answer these questions to find which princess you are!").grid(row = 0, column = 0, columnspan = 4)

        # animal
        Label(self, text="Pick an Animal:", font = ("System", 20)).grid(row=1, column=0, sticky=W)

        self.animal = StringVar()
        self.animal.set(None)

        animals = ["shark", "cat", "dog", "horse", "lizard", "bird", "leopard"]
        column = 0

        for word in animals:
            Radiobutton(self, text=word, variable=self.animal, value=word).grid(row=2, column=column, padx = 40, sticky=W)
            column += 1

        # color
        self.color = StringVar()
        self.color.set(None)

        Label(self, text="Pick a Color:", font = ("System", 20)).grid(row=3, column=0, sticky=W)

        color = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
        column = 0
        for word in color:
            Radiobutton(self, text=word, variable=self.color, value=word).grid(row=4, column=column, padx = 40, sticky=W)
            column += 1

        # food
        self.food = StringVar()
        self.food.set(None)

        Label(self, text="Pick a Food", font = ("System", 20)).grid(row=5, column=0, sticky=W)

        food = ["apple pie", "croissant", "ice cream", "oatmeal", "cake", "lobster", "fruit"]
        column = 0
        for word in food:
            Radiobutton(self, text=word, variable=self.food, value=word).grid(row=6, column=column, padx = 40, sticky=W)
            column += 1

        # activity
        self.activity = StringVar()
        self.activity.set(None)

        Label(self, text="Pick an Activity:", font = ("System", 20)).grid(row=7, column=0, sticky=W)

        activity = ["traveling", "dancing", "swimming", "sleeping", "braiding hair", "cooking", "excercising"]
        column = 0
        for word in activity:
            Radiobutton(self, text=word, variable=self.activity, value=word).grid(row=8, column=column, padx = 40, sticky=W)
            column += 1

        # season
        self.season = StringVar()
        self.season.set(None)

        Label(self, text="Pick a Season:", font = ("System", 20)).grid(row=9, column=0, sticky=W)

        season = ["fall", "winter", "spring", "summer"]
        column = 0
        for word in season:
            Radiobutton(self, text=word, variable=self.season, value=word).grid(row=10, column=column, padx = 150, sticky=W)
            column += 1

        submit_bttn = Button(self, text="Click to See Your Result!", command=self.results)
        submit_bttn.grid(row=11, column=1, columnspan = 2)
        self.story_txt = Text(self, width=75, height=10, wrap=WORD)
        self.story_txt.grid(row=12, column=0, columnspan=4)

    def results(self):
        animal = self.animal.get()
        finalAnswer = ""
        if self.animal.get() == "dog":
            finalAnswer+= "Your Disney Princess is Aurora!"
        if self.animal.get() == "leopard":
            finalAnswer+= "Your Disney Princess is Snow White!"
        if self.animal.get() == "lizard":
            finalAnswer+= "Your Disney Princess is Rapunzel!"
        if self.animal.get() == "lobster":
            finalAnswer+= "Your Disney Princess is Ariel!"
        if self.animal.get() == "cat":
            finalAnswer+= "Your Disney Princess is Jasmine!"
        if self.animal.get() == "horse":
            finalAnswer+= "Your Disney Princess is Belle!"
        if self.animal.get() == "birds":
            finalAnswer += "Your Disney Princess is Cinderella!"
        if self.animal.get() == "shark":
            finalAnswer+= "Your Disney Princess is Ariel!"

        # display the results
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, finalAnswer)




