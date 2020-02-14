from tkinter import *


class Periodic_table(Frame):
    def __init__(self, master, file_name):
        super(Periodic_table, self).__init__(master)
        self.image_dict = {}
        text_file = open(file_name, "r")
        for line in text_file:
            el = line.strip()
            per = el.split(",")
            self.image_dict[per[0]]=per[1]

    def create_widgets(self):
        pt = self.image_dict[0]
        periodic = PhotoImage(file= 'images/' + pt.periodic)
        p = Label(self, image=periodic)
        p.photo = periodic
        p.grid(row=0, column=0, sticky=N)

root = Tk()
root.title("Periodic Table!")
root.geometry("1000x1400")
app = Periodic_table(root)
root.mainloop()