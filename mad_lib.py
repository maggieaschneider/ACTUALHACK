
from tkinter import *

class madlib(Frame):

   """ GUI application that creates a story based on user init. """

   def __init__(self, master):
       """Initialize Frame"""
       super(madlib, self).__init__(master)
       self.grid()
       self.create_widgets()
       #self.madLib_call()

   def create_widgets(self):
       # create instruction label
       Label(self,
             text="Enter information for a new story"
             ).grid(row=0, column=0, sticky=W)

       # create a label and text entry for the name of a person
       Label(self,
             text="Female Name:"
             ).grid(row=1, column=0, sticky=W)
       self.femaleName_ent = Entry(self)
       self.femaleName_ent.grid(row=1, column=1, sticky=W)

       # create label and text entry for a plural noun 1
       Label(self,
             text="Noun 1:"
             ).grid(row=2, column=0, sticky=W)
       self.noun1_ent = Entry(self)
       self.noun1_ent.grid(row=2, column=1, sticky=W)

       # create label and text entry for a plural noun 2
       Label(self,
             text="Noun 2:"
             ).grid(row=3, column=0, sticky=W)
       self.noun2_ent = Entry(self)
       self.noun2_ent.grid(row=3, column=1, sticky=W)

       # create label and text entry for a plural noun 3
       Label(self,
             text="Noun 3:"
             ).grid(row=4, column=0, sticky=W)
       self.noun3_ent = Entry(self)
       self.noun3_ent.grid(row=4, column=1, sticky=W)

       # create label and text entry for a plural noun 4
       Label(self,
             text="Noun 4:"
             ).grid(row=5, column=0, sticky=W)
       self.noun4_ent = Entry(self)
       self.noun4_ent.grid(row=5, column=1, sticky=W)

       # create label and text entry for a plural noun 5
       Label(self,
             text="Noun 5:"
             ).grid(row=6, column=0, sticky=W)
       self.noun5_ent = Entry(self)
       self.noun5_ent.grid(row=6, column=1, sticky=W)

       # create a label and text entry for a verb
       Label(self,
             text="Verb 1:"
             ).grid(row=7, column=0, sticky=W)
       self.verb1_ent = Entry(self)
       self.verb1_ent.grid(row=7, column=1, sticky=W)

       # create a label and text entry for a verb
       Label(self,
             text="Verb 2 (singular):"
             ).grid(row=8, column=0, sticky=W)
       self.verb2_ent = Entry(self)
       self.verb2_ent.grid(row=8, column=1, sticky=W)

       # create a label and text entry for adjective 1
       Label(self,
             text="Adjective 1:"
             ).grid(row=9, column=0, sticky=W)
       self.adjOne_ent = Entry(self)
       self.adjOne_ent.grid(row=9, column=1, sticky=W)

       # create a label and text entry for adjective 2
       Label(self,
             text="Adjective 2:"
             ).grid(row=10, column=0, sticky=W)
       self.adjTwo_ent = Entry(self)
       self.adjTwo_ent.grid(row=10, column=1, sticky=W)

       # create a label and text entry for adjective 3
       Label(self,
             text="Adjective 3:"
             ).grid(row=11, column=0, sticky=W)
       self.adjThree_ent = Entry(self)
       self.adjThree_ent.grid(row=11, column=1, sticky=W)

       # create a label and text entry for adjective 4
       Label(self,
             text="Adjective 4:"
             ).grid(row=12, column=0, sticky=W)
       self.adjFour_ent = Entry(self)
       self.adjFour_ent.grid(row = 12, column = 1, sticky=W)

       # create a label and text entry for adjective 5
       Label(self,
             text="Adjective 5:"
             ).grid(row=13, column=0, sticky=W)
       self.adjFive_ent = Entry(self)
       self.adjFive_ent.grid(row = 13, column = 1, sticky=W)

       # create a label and text entry for adjective 6
       Label(self,
             text="Adjective 6:"
             ).grid(row=14, column=0, sticky=W)
       self.adjSix_ent = Entry(self)
       self.adjSix_ent.grid(row=14, column=1, sticky=W) #####14!

       # create a label and text entry for BODY PART
       Label(self,
             text="Body Part:"
             ).grid(row=15, column=0, sticky=W)
       self.body_part_ent = Entry(self)
       self.body_part_ent.grid(row=15, column=1, sticky=W)

       # create label for a specific place
       Label(self,
             text="Place:"
             ).grid(row=16, column=0, sticky=W)
       self.place_ent = Entry(self)
       self.place_ent.grid(row=16, column=1, sticky=W)

       # create a submit button
       Button(self,
              text="Click for story",
              command=self.tell_story
              ).grid(row=17, column=0, sticky=W)

       self.story_txt = Text(self, width=75, height=20, wrap=WORD)
       self.story_txt.grid(row=18, column=0, columnspan=4)

   def tell_story(self):
       femaleName = self.femaleName_ent.get()
       noun1 = self.noun1_ent.get()
       noun2 = self.noun2_ent.get()
       noun3 = self.noun3_ent.get()
       noun4 = self.noun4_ent.get()
       noun5 = self.noun5_ent.get()
       verb1 = self.verb1_ent.get()
       verb2 = self.verb2_ent.get()
       adjOne = self.adjOne_ent.get()
       adjTwo = self.adjTwo_ent.get()
       adjThree = self.adjThree_ent.get()
       adjFour = self.adjFour_ent.get()
       adjFive = self.adjFive_ent.get()
       adjSix = self.adjSix_ent.get()
       bodyPart = self.body_part_ent.get()
       place = self.place_ent.get()

       # create the story
       story = "Once upon a time, there was a/an "
       story += adjOne
       story += " young girl named "
       story += femaleName
       story += " who lived in a little wooden "
       story += noun1
       story += " by the "
       story += place + "."
       story += "She was a/an "
       story += adjTwo
       story += " child, always willing to lend a/an "
       story += bodyPart
       story += " to the "
       story += adjThree + " villagers. "
       story += "She was small and " + adjFour + " but worked very hard. "
       story += "Then, one day, she happened upon a/an " + adjFive
       story += " frog. To her suprise, this little slimy " + noun2
       story += " could talk! In a deep, croaky voice, it said, “"
       "I will grant you three wishes but then you must give me a/an "
       story += verb1 + " on the lips. She agreed. And for her first wish, "
       "she asked for a new "
       story += noun3 + " for her parents to live in. For her second, she wished to be able to "
       story += verb2 + " like a bird. For her final wish, she asked for all the "
       story += noun4 + " in he world! And it all came to pass just as the frog said. " \
                        "The girl kissed the frog and he suddenly turned into a handsome, young "
       story += noun5 + " . She couldn't believe her " + adjSix + " luck!"

       # display the story
       self.story_txt.delete(0.0, END)
       self.story_txt.insert(0.0, story)


