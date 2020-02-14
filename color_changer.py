from tkinter import *

class color_changer(Frame):
   def __init__(self, master):
       super().__init__(master)
       self.grid()
       self.create_widgets()
       self.create_widgets()

   def create_widgets(self):
       Label(self, text = "Enter a message: ").grid(row = 0, column = 0)
       self.message = Text(self, wrap = WORD, height = 10, width = 10)
       self.message.grid(row = 0, column = 1)
       self.color_button = Button(self,
              text="Color ",
              command=self.change
              )
       self.color_button.grid(row=1, column=0, sticky=W)
       Label(self, text = "Output"
             ).grid(row = 2, column = 0, sticky = W)
       self.output = Text(self, wrap = WORD, height = 10, width = 10, fg = "red")
       self.output.grid(row = 2, column = 1)

   def change(self):
       new_msg = self.message.get(0.0, END)
       self.output.delete(0.0, END)
       self.output.insert(0.0, new_msg)

