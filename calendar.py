from tkinter import *

class calendar(Frame):
    def __init__(self, master, file_name):
        super(calendar, self).__init__(master)
        self.image_dict = {}
        text_file = open(file_name, "r")
        for line in text_file:
            gd = line.strip()
            bruh = gd.split(",")
            self.image_dict[bruh[0]]=bruh[1]

    def create_widgets(self):
        cal = self.image_dict[0]
        calend = PhotoImage(file= 'images/' + cal.calend)
        c = Label(self, image=calend)
        c.photo = calend
        c.grid(row=0, column=0, sticky=N)

root = Tk()
root.title("Calendar!")
root.geometry("1000x1400")
app = calendar(root)
root.mainloop()