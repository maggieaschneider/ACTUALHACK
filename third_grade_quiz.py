from tkinter import *

class third_grade_quiz(Frame):
   def __init__(self, master):
       super(third_grade_quiz, self).__init__(master)
       self.grid()
       self.create_widgets()

   def create_widgets(self):
       Label(self, text = "Answer these questions to find out if you are smarter than a third grader!").grid(row = 0, column = 1, columnspan = 2)

       # animal
       Label(self, text="What color do you get when you mix yellow and blue?").grid(row=1, column=0, sticky=W)

       self.color = StringVar()
       self.color.set(None)

       colors = ["red", "orange", "purple", "green"]
       column = 1

       for word in colors:
           Radiobutton(self, text=word, variable=self.color, value=word).grid(row=2, column=column, sticky=W)
           column += 1

       # color
       self.spell = StringVar()
       self.spell.set(None)

       Label(self, text="Which of these is the correct spelling:").grid(row=3, column=0, sticky=W)

       spelling = ["receive", "recieve", "recive", "receeve", "reseive", "reseve", "resieve"]
       column = 1
       for word in spelling:
           Radiobutton(self, text=word, variable=self.spell, value=word).grid(row=4, column=column, sticky=W)
           column += 1

       # food
       self.animal = StringVar()
       self.animal.set(None)

       Label(self, text="Which of the following is a reptile?").grid(row=5, column=0, sticky=W)

       animals = ["Whale", "Lion", "Snake", "Giraffe", "Hedgehog", "Lobster", "Cow"]
       column = 1
       for word in animals:
           Radiobutton(self, text=word, variable=self.animal, value=word).grid(row=6, column=column, sticky=W)
           column += 1

       # activity
       self.continents = StringVar()
       self.continents.set(None)

       Label(self, text="How many continents are there?").grid(row=7, column=0, sticky=W)

       continent = ["7", "32", "206", "54", "4", "70", "153"]
       column = 1
       for word in continent:
           Radiobutton(self, text=word, variable=self.continents, value=word).grid(row=8, column=column, sticky=W)
           column += 1

       # season
       self.math = StringVar()
       self.math.set(None)

       Label(self, text="What is the solution to the following math problem? 2*2+2/2-2+9").grid(row=9, column=0, sticky=W)

       season = ["10", "15", "12", "11"]
       column = 1
       for word in season:
           Radiobutton(self, text=word, variable=self.math, value=word).grid(row=10, column=column, sticky=W)
           column += 1

       self.countries = StringVar()
       self.countries.set(None)

       Label(self, text="What countries border the USA?").grid(row=11, column=0, sticky=W)

       countries = ["Canada and England", "Mexico and Spain", "Canada and Mexico", "Italy and Greece"]
       column = 1
       for word in countries:
           Radiobutton(self, text=word, variable=self.countries, value=word).grid(row=12, column=column, sticky=W)
           column += 1

       self.crust = StringVar()
       self.crust.set(None)

       Label(self, text="What is the outermost layer of the Earth called?").grid(row=13, column=0, sticky=W)

       layers = ["Mantle", "Core", "Grass", "Crust"]
       column = 1
       for word in layers:
           Radiobutton(self, text=word, variable=self.crust, value=word).grid(row=14, column=column, sticky=W)
           column += 1

       self.percent = StringVar()
       self.percent.set(None)

       Label(self, text="What is 50% of 8?").grid(row=15, column=0, sticky=W)

       numbs = ["4", "7", "58", "1"]
       column = 1
       for word in numbs:
           Radiobutton(self, text=word, variable=self.percent, value=word).grid(row=16, column=column, sticky=W)
           column += 1

       self.planet = StringVar()
       self.planet.set(None)

       Label(self, text="What is the first planet from the sun?").grid(row=17, column=0, sticky=W)

       planets = ["Mars", "Mercury", "Earth", "Jupiter"]
       column = 1
       for word in planets:
           Radiobutton(self, text=word, variable=self.planet, value=word).grid(row=18, column=column, sticky=W)
           column += 1

       self.president = StringVar()
       self.president.set(None)

       Label(self, text="Who was the first president of the United States?").grid(row=19, column=0, sticky=W)

       presidents = ["Abraham Lincoln", "Donald Trump", "Michele Obama", "George Washington"]
       column = 1
       for word in presidents:
           Radiobutton(self, text=word, variable=self.president, value=word).grid(row=20, column=column, sticky=W)
           column += 1
       submit_bttn = Button(self, text="Click to See Your Result!", command=self.results)
       submit_bttn.grid(row=21, column=0, sticky=W)
       self.story_txt = Text(self, width=75, height=10, wrap=WORD)
       self.story_txt.grid(row=22, column=0, columnspan=4)

   def results(self):
       score = 0
       if self.color.get() == "green":
           score += 1
       else:
           pass
       if self.spell.get() == "receive":
           score += 1
       else:
           pass
       if self.animal.get() == "Snake":
           score += 1
       else:
           pass
       if self.continents.get() == "7":
           score += 1
       else:
           pass
       if self.math.get() == "12":
           score += 1
       else:
           pass
       if self.countries.get() == "Canada and Mexico":
           score += 1
       else:
           pass
       if self.crust.get() == "Crust":
           score += 1
       else:
           pass
       if self.percent == "4":
           score += 1
       else:
           pass
       if self.planet == "Mercury":
           score += 1
       else:
           pass
       if self.president == "George Washington":
           score += 1
       else:
           pass


       if score > 5:
           Label(text = "You're smarter than a third grader! Your score was" + str(score) + "/10! Good job!"
                 ).grid(row = 21, column = 0, columnspan = 2)
       else:
           Label(text = "Maybe you should take a trip back to third grade! Your score was " + str(score) + "/10! Nice try! "
                 ).grid(row = 21, column = 0, columnspan = 2)
       # display the results
       self.story_txt.delete(0.0, END)
      # self.story_txt.insert(0.0, finalAnswer)





