from tkinter import *
from academy import *
from basicCalc import *
from calendar import *
from click_counter import *
from color_changer import *
from color_quiz import *
from disney_princess import *
from font_change import *
from hogwarts_house import *
from mad_lib import *
from mean_median import *
from meme_gen import *
from menu import *
from Periodic_table import *
from rand_num_gen import *
from spiritAnimal import *
from surprise import *
from third_grade_quiz import *
from wallet import *



class Main(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="WELCOME TO L-CARM!", font="Helvetica, 30"
              ).grid(row=0, columnspan=8)

        # create body part radio buttons

        self.file_name = StringVar()
        self.file_name.set(None)

        file_name = ["academy.py", "Basic_calc.py", "calendar.py", "click_counter.py", "color_change.py",
                     "color_person.py", "disney_princess.py", "font_change.py", "hogwarts_house.py",
                     "mad_lib.py", "mean_median.py", "meme_gen.py", "menu.py", "Periodic_table.py", "rand_num_gen.py",
                     "spirit_animal.py", "surprise.py", "third_grade_quiz.py", "wallet.py"]
        column = 1
        row = 1


        for app in file_name:
            if column % 8 == 0:
                row += 1
                column = 1
            Radiobutton(self,
                        text = app.replace(".py","").replace("_", " ").title(),
                        variable= self.file_name,
                        value= app
                        ).grid(row=row, column=column, sticky=W)

            column += 1

        Label(self, text = " ").grid(row=row+ 1)
        self.butt = Button(self, text = "Submit", command=self.select).grid(row=row+ 2, column = 1, sticky = W)

    def select(self):
        file_name = self.file_name.get()
        if file_name == "academy.py":
            academy(self)
        if file_name == "basicCalc.py":
            basicCalc(self)
        if file_name == "click_counter.py":
            click_counter(self)
        if file_name == "calendar.py":
            calendar(self)
        if file_name == "color_changer.py":
            color_changer(self)
        if file_name == "color_quiz.py":
            color(self)
        if file_name == "disney_princess.py":
            disney_princess(self)
        if file_name == "font_change.py":
            font_change(self)
        if file_name == "hogwarts_house.py":
            hogwarts(self)
        if file_name == "mad_lib.py":
            madlib(self)
        if file_name == "mean_median.py":
            mean_median(self)
        if file_name == "meme_gen.py":
            meme_gen(self)
        if file_name == "menu.py":
            menu(self)
        if file_name == "Periodic_table.py":
            Periodic_table(self)
        if file_name == "rand_num_gen.py":
            rand_num_gen(self)
        if file_name == "spiritAnimal.py":
            spiritAnimal(self)
        if file_name == "surprise.py":
            surprise(self)
        if file_name == "third_grade_quiz.py":
            third_grade_quiz(self)
        if file_name == "wallet.py":
            wallet(self)





root = Tk()
root.title("Main screen")
root.geometry("1000x1400")
app = Main(root)
root.mainloop()