from tkinter import *


class surprise(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.image_dict = {}
        text_file = open("image_list", "r")
        for line in text_file:
            l = line.strip()
            mem = l.split(",")
            self.image_dict[mem[0]] = mem[1]
        self.create_widgets()
        self.grid()

    def create_widgets(self):
        bajwa = PhotoImage(file="images/bajwa.gif")
        b = Label(self, image=bajwa)
        b.photo = bajwa
        b.grid(row=0, column=0)



root = Tk()
root.title("Surprise!")
root.geometry("375x650")
app = surprise(root)
root.mainloop()