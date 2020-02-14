from tkinter import *
class surprise(Frame):
    def __init__(self, master, file_name):
        super(surprise, self).__init__(master)
        self.image_dict = {}
        text_file = open(file_name, "r")
        for line in text_file:
            ap = line.strip()
            baj = ap.split(",")
            self.image_dict[baj[0]]=baj[1]

    def create_widgets(self):
        drbaj= self.image_dict[0]
        bajwa = PhotoImage(file= 'images/' + drbaj.bajwa)
        b = Label(self, image= bajwa)
        b.photo = bajwa
        b.grid(row=0, column=0, sticky=N)


root = Tk()
root.title("Surprise!")
root.geometry("1000x1400")
app = surprise(root)
root.mainloop()