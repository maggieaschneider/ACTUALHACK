from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="CALCULATOR :)", font = ("System", 25)).grid(row=0, column=1)

        Label(self, text="Enter First Number: ", font = ("Courier New", 10)).grid(row=2, column=0)
        self.first_ent = Entry(self)
        self.first_ent.grid(row=3, column=0)

        Label(self, text="Enter Operation: ", font = ("Courier New", 10)).grid(row=2, column=1)
        self.op_ent = Entry(self)
        self.op_ent.grid(row=3, column=1)

        Label(self, text="Enter Second Number: ", font = ("Courier New", 10)).grid(row=2, column=2)
        self.second_ent = Entry(self)
        self.second_ent.grid(row=3, column=2)

        Label(self, text=" ", font=("Courier New", 10)).grid(row=4, column=1)

        self.button_calculate = Button(self, text="CALCULATE", bg="lightblue", font=("Comic Sans MS", 14))
        self.button_calculate.grid(row=5, column=1)
        self.button_calculate["command"] = self.calculate

    def calculate(self):
        first = self.first_ent.get()
        op = self.op_ent.get()
        second = self.second_ent.get()
        if op == "+":
            result = float(first) + float(second)
            Label(self, text=("Answer: %.2f" % (result)), font=("System", 12)).grid(row=7, column=1)
        elif op == "-":
            result = float(first) - float(second)
            Label(self, text=("Answer: %.2f" % (result)), font=("System", 12)).grid(row=7, column=1)
        elif op == "*":
            result = float(first) * float(second)
            Label(self, text=("Answer: %.2f" % (result)), font=("System", 12)).grid(row=7, column=1)
        elif op == "/":
            result = float(first)/float(second)
            Label(self, text=("Answer: %.2f" % (result)), font=("System", 12)).grid(row=7, column=1)

root = Tk()
root.title("Calculator!")
app = Application(root)
root.mainloop()
