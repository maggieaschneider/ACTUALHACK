from tkinter import *

class academy(Frame):
    def __init__(self, master):
        super(academy, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text = "Answer the following questions to discover what BCA academy you belong in!").grid(row = 0, column = 1, columnspan = 2)

        # animals
        Label(self, text="Pick an Animal:").grid(row=1, column=0, sticky=W)
        self.animal = StringVar()
        self.animal.set(None)

        animals = ["snake", "owl", "mouse", "beaver", "parrot", "hummingbird", "peacock", "bee", "dolphin"]
        column = 1

        for word in animals:
            Radiobutton(self, text=word, variable=self.animal, value=word).grid(row=2, column=column, sticky=W)
            column += 1

        # sports
        Label(self, text="Pick a Sport:").grid(row=3, column=0, sticky=W)

        self.sport = StringVar()
        self.sport.set(None)

        sports = ["basketball", "ping-pong", "tennis", "baseball", "fencing", "golf", "volleyball", "track", "lacrosse"]
        column = 1
        for word in sports:
            Radiobutton(self, text=word, variable=self.sport, value=word).grid(row=4, column=column, sticky=W)
            column += 1

        Label(self, text="Pick a Color:").grid(row=5, column=0, sticky=W)

        self.color = StringVar()
        self.color.set(None)

        colors = ["maroon", "pink", "green", "gray", "orange", "blue", "purple", "yellow", "red"]
        column = 1
        for word in colors:
            Radiobutton(self, text=word, variable=self.color, value=word).grid(row=6, column=column, sticky=W)
            column += 1

        Label(self, text="Pick a Place:").grid(row=7, column=0, sticky=W)
        self.place = StringVar()
        self.place.set(None)
        places = ["museum", "arcade", "movies", "hiking", "club", "festival", "beach", "restaurant", "picnic"]
        column = 1
        for word in places:
            Radiobutton(self, text=word, variable=self.place, value=word).grid(row=8, column=column, sticky=W)
            column += 1

        submit_bttn = Button(self, text="Click to See Your Result!", command=self.academy)
        submit_bttn.grid(row=9, column=0, sticky=W)
        self.story_txt = Text(self, width=75, height=10, wrap=WORD)
        self.story_txt.grid(row=10, column=0, columnspan=4)

    def academy(self):
        animal = self.animal.get()
        finalAnswer = ""
        if self.animal.get() == "snake":
            finalAnswer += "You belong in ABF (Academy for Business and Finance)!"
        if self.animal.get() == "owl":
            finalAnswer += "You belong in ATCS (Academy for Technology and Computer Science)!"
        if self.animal.get() == "mouse":
            finalAnswer += "You belong in AAST (Academy for Advancement of Science and Technology)!"
        if self.animal.get() == "beaver":
            finalAnswer += "You belong in AEDT (Academy for Engineering and Design Technology)!"
        if self.animal.get() == "beaver":
            finalAnswer += "You belong in AVPA-T (Academy for Visual and Performing Arts - Theater)!"
        if self.animal.get() == "hummingbird":
            finalAnswer += "You belong in AVPA-M (Academy for Visual and Performing Arts - Music)!"
        if self.animal.get() == "peacock":
            finalAnswer += "You belong in AVPA-V (Academy for Visual and Performing Arts - Visual)!"
        if self.animal.get() == "bee":
            finalAnswer += "You belong in ACAHA (Academy for Culinary Arts and Hospitality Administration)!"
        if self.animal.get() == "dolphin":
            finalAnswer += "You belong in AMST (Academy for Medical Science Technology)!"

        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, finalAnswer)



