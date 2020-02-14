import random
from tkinter import *

class meme_gen(Frame):
    def __init__(self, master, file_name):
        super(meme_gen, self).__init__(master)
        self.image_dict = {}
        text_file = open(file_name, "r")
        for line in text_file:
            l = line.strip()
            mem = l.split(",")
            self.image_dict[mem[0]] = mem[1]

    def create_widgets(self):
        Button(text="Generate Meme", command=self.generate
               ).grid(row=0, column=0, sticky=N)

    def generate(self):
        meme_num = random.randrange(1, 31)
        meme = PhotoImage(file="meme" + meme_num + ".txt")
        m = Label(self, image=meme)
        m.photo = meme
        m.grid(row=1, column=0, sticky=N)

root = Tk()
root.title("Meme Generator!")
root.geometry("1000x1400")
app = meme_gen(root)
root.mainloop()






