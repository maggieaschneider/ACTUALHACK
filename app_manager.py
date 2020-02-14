from tkinter import *
from appChoices import Main
class App_Manager (object):
    def __init__(self):
        """initialize a new application manager by loading a list of apps from the file and by initializing tkinter"""
        self.character_choices = Main("ACTUALHACK3.py")
        self.root = tkinter()

        self.app_choices = ("mad_lib.py")
        self.app_choices = ("basicCalc.py")
        self.app_choices = ("calendar.py")
        self.app_choices = ("Periodic_table.py")
        self.app_choices = ("surprise.py")
        self.app_choices = ("meme_gen.py")
        self.app_choices = ("academy.py")
        self.app_choices = ("click_counter.py")
        self.app_choices = ("color_changer.py")
        self.app_choices = ("color_quiz.py")
        self.app_choices = ("disney_princess.py")
        self.app_choices = ("font_change.py")
        self.app_choices = ("hogwarts_house.py")
        self.app_choices = ("mean_median.py")
        self.app_choices = ("menu.py")
        self.app_choices = ("rand_num_gen.py")
        self.app_choices = ("wallet.py")
        self.app_choices = ("appChoices.py")
        self.app_choices = ("ZodiacQuiz.py")


    def setup_app_selector(self):
        self.root.title("L-CARM")


def main():
    appl = App_Manager()
    appl.setup_app_selector()
    appl.root.mainloop()


main()



