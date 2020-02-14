from tkinter import *
class click_counter(Frame):
    def __init__(self, master):
        super(click_counter, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widget()
    def create_widget(self):
        self.bttn = Button(self)
        self.bttn["text"] = "Total Clicks: 0"
        self.bttn["command"] = self.update_count
        self.bttn.grid()
    def update_count(self):
        self.bttn_clicks +=1
        self.bttn["text"] = "Total Clicks: " + str(self.bttn_clicks)
root = Tk()
root.title("Clicker Counter!")
app = click_counter(root)
root.mainloop()