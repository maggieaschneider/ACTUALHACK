from tkinter import *
class mean_median(Frame):
    def __init__(self, master):
        super(mean_median, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        self.b = Label(self,
              text="Numbers:"
              ).grid(row=0, column=0, sticky=W)
        self.num_ent = Entry(self)
        self.num_ent.grid(row=0, column=1, sticky=W)
        self.mean = Button(text = "Calculate mean:", command = self.mean)
        self.mean.grid(row = 2, column = 0)
        self.median = Button(text = "Calculate median:", command = self.median)
        self.median.grid(row = 2, column = 1)

        self.answer = Label(text="")
        self.answer.grid(row=3, column=0, columnspan=2)


    def median(self):
        numlist = self.num_ent.get()
        numlist = numlist.split()
        if len(numlist) % 2 == 0:
            lc_pos = len(numlist) // 2 - 1
            lc_pos = int(numlist[lc_pos])
            rc_pos = len(numlist) // 2
            rc_pos = int(numlist[rc_pos])
            w= ((lc_pos + rc_pos) / 2)
            self.answer["text"] = w
        else:
            center_pos = len(numlist) // 2

            self.answer["text"]= numlist[center_pos]
    def mean(self):
        numlist = self.num_ent.get()
        numlist = numlist.split()
        self.total = 0
        for num in numlist:
            self.num = float(num)
            self.total += self.num
        mean = self.total/len(numlist)
        self.answer["text"] = mean

root = Tk()
root.title("Mean & Median!")
app = mean_median(root)
root.mainloop()