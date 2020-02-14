from tkinter import *


class Periodic_table(Frame):
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
        periodic = PhotoImage(file="images/period_table.png")
        i = Label(self, image=periodic)
        i.photo = periodic
        i.grid(row=0, column=0)



root = Tk()
root.title("Periodic Table!")
root.geometry("1000x1400")
app = Periodic_table(root)
root.mainloop()