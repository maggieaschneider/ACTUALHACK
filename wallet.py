from tkinter import *


class wallet(Frame):
    def __init__(self, master):
        super(wallet, self).__init__(master)
        self.grid()
        self.total = 0
        # self.penny = 0.01
        # self.nickel = 0.05
        # self.dime = 0.10
        # self.quarter = 0.25
        self.create_widgets()

    def create_widgets(self):
        Label(self,text = "Insert money:"
              ).grid(row=0, column = 0)
        self.p = Button(self,text="Add Penny:", command = self.penny)
        self.p.grid(row=1, column = 0)
        self.n = Button(self, text= "Add Nickel:", command = self.nickel)
        self.n.grid(row=2, column = 0)
        self.d = Button(self, text="Add Dime:", command=self.dime)
        self.d.grid(row=3, column=0)
        self.q = Button(self, text="Add Quarter:", command=self.quarter)
        self.q.grid(row=4, column=0)
        self.tota = Label(self, text = self.total)
        self.tota.grid(row = 6, column = 0)

    def penny(self):
        self.total += 0.01
        self.tota["text"] = "%.2f" % self.total
    def nickel(self):
        self.total+=0.05
        self.tota["text"] = "%.2f" % self.total
    def dime(self):
        self.total+= 0.1
        self.tota["text"] = "%.2f" % self.total
    def quarter(self):
        self.total+= 0.25
        self.tota["text"] = "%.2f" % self.total

    # def end(self):
    #     new_msg = self.math(self.output.get(0.0))
    #     self.output.delete(0.0)




