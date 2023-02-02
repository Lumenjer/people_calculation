from tkinter import *
from tkinter.messagebox import *
import random
from tkinter import ttk

def click1():
    people.config(state="normal")
    people.delete(0, END)
    people.insert(0, random.randint(0, 1000000))
    people.config(state="readonly")

def click_clear():
    people.config(state="normal")
    if askyesno(title="Close", message="Ви впевнені, що хочете очистити?"):
        people.delete(0, END)
    people.config(state="readonly")
    
def click2():
    my_list.delete(0, END)
    

Window = Tk()
Window.title("Window")
Window.geometry("500x500")
Window.resizable(0,0)

my_list = ttk.Combobox(Window, font='Arial 11',width=15, height=5, value = [1, 2])

label = Label(text = "Кількість людей яка пройшла \n повз датчик", font = ("Arial", 12))
people = Entry(Window, bg = "silver" , width = 23, font = "13", state="readonly")
button1 = Button(text="Старт", width = "20", height = "2", command = click1)
button2 = Button(text="Очистити", width = "20", height = "2", command = click_clear)
button3 = Button(text="Оновити", width = "20", height = "2", command = click2)
button = Button(text="Вийти", width = "20", height = "2", command = Window.destroy)
label.place(x = 138, y = 100)
people.place(x = 138,y = 150)
button1.place(x = 50, y = 350)
button2.place(x = 50, y = 420)
button3.place(x = 300, y = 350)
button.place(x = 300, y = 420)
my_list.place(x = 0, y = 0)
Window.mainloop()
