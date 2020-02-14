from tkinter import *

class spiritAnimal(Frame):
    def __init__(self, master):
        super(spiritAnimal, self).__init__(master)
        self.grid()
        self.create_widgets()



    def create_widgets(self):
        Label(self, text = "Answer these questions to see what your spirit animal is!").grid(row = 0, column = 1, columnspan = 2)

        # one word
        Label(self, text="Pick one word that describes yourself:", font = ("Verdana", 20)).grid(row=1, column=0, sticky=W)

        self.desc = StringVar()
        self.desc.set(None)

        desc = ["helpful", "selfless", "busy", "intelligent", "confident", "funny", "leopard"]
        column = 1

        for word in desc:
            Radiobutton(self, text=word, variable=self.desc, value=word).grid(row=2, column=column, sticky=W)
            column += 1

        # color
        self.color = StringVar()
        self.color.set(None)

        Label(self, text="Pick a Color:", font = ("Verdana", 20)).grid(row=3, column=0, sticky=W)

        color = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
        column = 1
        for word in color:
            Radiobutton(self, text=word, variable=self.color, value=word).grid(row=4, column=column, sticky=W)
            column += 1

        # drinks
        self.drink = StringVar()
        self.drink.set(None)

        Label(self, text="Pick a Food", font = ("Verdana", 20)).grid(row=5, column=0, sticky=W)

        drink = ["OJ", "coffee", "fanta", "sprite", "coca-cola", "Brisk Iced Tea", "water", "Seltzer"]
        column = 1
        for word in drink:
            Radiobutton(self, text=word, variable=self.drink, value=word).grid(row=6, column=column, sticky=W)
            column += 1

        # activity
        self.activity = StringVar()
        self.activity.set(None)

        Label(self, text="Pick an Activity", font = ("Verdana", 20)).grid(row=7, column=0, sticky=W)

        activity = ["excercise", "eat", "sleep", "cry", "hanging with friends", "reading books", "video games", "swim"]
        column = 1
        for word in activity:
            Radiobutton(self, text=word, variable=self.activity, value=word).grid(row=8, column=column, sticky=W)
            column += 1


        submit_bttn = Button(self, text="Click to See Your Result!", command=self.results)
        submit_bttn.grid(row=11, column=0, sticky=W)
        self.story_txt = Text(self, width=75, height=10, wrap=WORD)
        self.story_txt.grid(row=12, column=0, columnspan=4)


    def results(self):
        color = self.color.get()
        finalAnswer = ""
        if self.color.get() == "blue":
            finalAnswer+= "Your Spirit animal is a dolphin!"
        if self.color.get() == "orange":
            finalAnswer+= "Your Spirit animal is a otter!"
        if self.color.get() == "red":
            finalAnswer+= "Your Spirit animal is a fox!"
        if self.color.get() == "purple":
            finalAnswer+= "Your Spirit animal is a whale!"
        if self.color.get() == "pink":
            finalAnswer+= "Your Spirit animal is an anteater!"
        if self.color.get() == "yellow":
            finalAnswer+= "Your Spirit animal is a elephant!"
        if self.color.get() == "green":
            finalAnswer+= "Your Spirit animal is a giraffe"

        # display the results
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, finalAnswer)




