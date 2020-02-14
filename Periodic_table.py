from tkinter import *


class Periodic_table(Frame):
    def __init__(self, master, file_name):
        super(Periodic_table, self).__init__(master)
        self.image_dict = {}
        text_file = open(file_name, "r")
        for line in text_file:
            dfg = line.strip()
            idek = dfg.split(",")
            self.image_dict[idek[0]] = idek[1]

    def create_widgets(self):
        per = self.image_dict[0]
        period = PhotoImage(file='images/' + per.period)
        p = Label(self, image=period)
        p.photo = period
        p.grid(row=0, column=0, sticky=N)

        w.grid(row=0, column=1, sticky=W)
        # pt = self.image_dict[0]
        # periodic = PhotoImage(file= 'images/' + pt.periodic)
        # p = Label(self, image=periodic)
        # p.photo = periodic
        # p.grid(row=0, column=0, sticky=N)

root = Tk()
root.title("Periodic Table!")
app = Periodic_table(root)
root.mainloop()