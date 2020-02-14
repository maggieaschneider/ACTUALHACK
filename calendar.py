from tkinter import *


class calendar(Frame):
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
        cal = PhotoImage(file="images/calendar.gif")
        c = Label(self, image=cal)
        c.photo = cal
        c.grid(row=0, column=0)



root = Tk()
root.title("Calendar!")
root.geometry("600x500")
app = calendar(root)
root.mainloop()