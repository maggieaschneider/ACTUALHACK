from tkinter import *

class menu(Frame):
   def __init__(self, master):
       super().__init__(master)
       self.grid()
       self.total = 0
       self.create_widgets()
       self.drinks = ["water", "lemonade", "soda"]
       self.foods = ["chicken", "pasta", "salad"]
       self.desserts = ["Ice Cream", "Lava Cake", "Brownie"]
   def create_widgets(self):
       Label(self, text = "MENU!", font = "Helvetica, 20"
             ).grid(row = 0, column = 0)

       Label(self, text = "Drink:").grid(row = 1, column = 0)
       self.drink = StringVar()
       self.drink.set(None)

       self.drinks = ["water", "lemonade", "soda"]
       column = 1
       for word in self.drinks:
           dri = Radiobutton(self, text = word, variable= self.drink, value = word
                       ).grid(row = 1, column = column)
           column+=1

       Label(self, text="Entree:").grid(row=2, column=0)
       self.food= StringVar()
       self.food.set(None)

       self.foods = ["chicken", "pasta", "salad"]
       column = 1
       for word in self.foods:
           foo = Radiobutton(self, text=word, variable=self.food, value=word
                       ).grid(row=2, column=column)
           column += 1

       Label(self, text="Dessert:").grid(row=3, column=0)
       self.dessert = StringVar()
       self.dessert.set(None)

       self.desserts = ["Ice Cream", "Lava Cake", "Brownie"]
       column = 1
       for word in self.desserts:
           des = Radiobutton(self, text=word, variable=self.dessert, value=word).grid(row=3, column=column)
           column+=1


       if dri == self.drinks[0]:
           self.total += 1
       elif dri == self.drinks[1]:
           self.total += 2
       elif dri == self.drinks[2]:
           self.total += 3

       if foo == self.foods[0]:
           self.total += 9.99
       elif foo == self.foods[1]:
           self.total += 13.20
       elif foo == self.foods[2]:
           self.total += 6.88

       if des == self.desserts[0]:
            self.total += 2.50
       elif des == self.desserts[1]:
            self.total += 9.99
       elif des == self.desserts[2]:
            self.total += 4.33

       Button(self,
              text="Total",
              command=self.calculate
              ).grid(row=5, column=0)

   def calculate(self):
       if self.drink.get()== self.drinks[0]:
           self.total += 1
       elif self.drink.get() == self.drinks[1]:
           self.total += 2
       elif self.drink.get()== self.drinks[2]:
           self.total += 3

       if self.food.get() == self.foods[0]:
           self.total += 9.99
       elif self.food.get() == self.foods[1]:
           self.total += 13.20
       elif self.food.get() == self.foods[2]:
           self.total += 6.88

       if self.dessert.get() == self.desserts[0]:
            self.total += 2.50
       elif self.dessert.get() == self.desserts[1]:
            self.total += 9.99
       elif self.dessert.get()== self.desserts[2]:
            self.total += 4.33
       answer = Label(self, text = self.total).grid(row = 5, column = 2)
       answer = ("%.1f")
root = Tk()
root.title("Menu and Total Cost")
app = menu(root)
root.mainloop()