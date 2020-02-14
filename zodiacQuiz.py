
from tkinter import *

class zodiac(Frame):
    def __init__(self, master):
        super(zodiac, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text = "We can guess your zodiac based off of your Ice Cream Decisions!").grid(row = 0, column = 1, columnspan = 2)

        # flavor
        Label(self, text="Pick a Flavor:").grid(row=1, column=0, sticky=W)

        self.flavor = StringVar()
        self.flavor.set(None)

        flavor = ["vanilla", "chocolate", "cookies 'n' cream", "mint chocolate chip", "another flavor is better",
                  "cookie dough", "cotton candy", "butter pecan", "blueberry", "raspberry", "moose tracks", "cotton candy","strawberry"]
        column = 1
        row = 1
        for word in flavor:
            Radiobutton(self, text=word, variable=self.flavor, value=word).grid(row=row, column=column, sticky=W)
            if column == 6:
                row +=1
                column = (column % 6)-1
            column += 1


        # toppings
        self.topping = StringVar()
        self.topping.set(None)

        Label(self, text="Pick a Topping:").grid(row=3, column=0, sticky=W)

        topping = ["choco syrup", "choco chips", "gummy worms", "rainbow sprinkles", "choco sprinkles", "whipped cream",
                 "m&m's", "cherries", "caramel syrup", "peanuts", "strawberries", "oreos"]
        column = 1
        row =3
        for word in topping:
            Radiobutton(self, text=word, variable=self.topping, value=word).grid(row=row, column=column, sticky=W)
            if column == 6:
                row +=1
                column = (column % 6)-1
            column += 1

        # scoops
        self.scoops = StringVar()
        self.scoops.set(None)

        Label(self, text="Pick the number of Scoops").grid(row=5, column=0, sticky=W)

        scoops = ["one", "two", "three", "four", "i don't like ice cream", "five"]
        column = 1
        for word in scoops:
            Radiobutton(self, text=word, variable=self.scoops, value=word).grid(row=6, column=column, sticky=W)
            column += 1

        # where
        self.where = StringVar()
        self.where.set(None)

        Label(self, text="Pick where you would like your ice cream").grid(row=7, column=0, sticky=W)

        where = ["bowl", "waffle cup", "cone", "choco-covered cone", "sprinkled-covered cone", "kids cup"]
        column = 1
        for word in where:
            Radiobutton(self, text=word, variable=self.where, value=word).grid(row=8, column=column, sticky=W)
            column += 1

        submit_bttn = Button(self, text="Click to See Your Result!", command=self.results)
        submit_bttn.grid(row=11, column=0, sticky=W)
        self.story_txt = Text(self, width=75, height=10, wrap=WORD)
        self.story_txt.grid(row=12, column=0, columnspan=4)

    def results(self):
        print("hi")
        topping = self.topping.get()
        finalAnswer = ""
        print(self.topping.get())
        if self.topping.get() == "choco syrup":
            finalAnswer+= "Your zodiac is aries!"
        if self.topping.get() == "rainbow sprinkles":
            finalAnswer+= "Your zodiac is leo!"
        if self.topping.get() == "strawberries":
            finalAnswer += "Your zodiac is cancer!"
        if self.topping.get() == "choco chips":
            finalAnswer+= "Your zodiac is pisces!"
        if self.topping.get() == "gummy worms":
            finalAnswer+= "Your zodiac is scorpio!"
        if self.topping.get() == "whipped cream":
            finalAnswer+= "Your zodiac is taurus!"
        if self.topping.get() == "cherries":
            finalAnswer+= "Your zodiac is sagittarious!"
        if self.topping.get() == "caramel syrup":
            finalAnswer += "Your zodiac is gemini!"
        if self.topping.get() == "chocolate sprinkles":
            finalAnswer += "Your zodiac is virgo!"
        if self.topping.get() == "peanuts":
            finalAnswer += "Your zodiac is libro!"
        if self.topping.get() == "oreos":
            finalAnswer += "Your zodiac is capricorn!"
        if self.topping.get() == "m&m's":
            finalAnswer += "Your zodiac is aquarius!"

        # display the results
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, finalAnswer)

root = Tk()
root.title("Zodiac QUiz!")
app = zodiac(root)
root.mainloop()