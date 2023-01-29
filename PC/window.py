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
    new_window = Tk()
    new_window.title("List")
    new_window.resizable(0,0)
    new_window.geometry("300x300")
    
Window = Tk()
Window.title("Window")
Window.geometry("500x500")
Window.resizable(0,0)

my_list = ttk.Combobox(Window, font='Arial 11',width=15, height=5, values=['value 1', 'value 2', 'value 3', 'value 4',
                                                                         'value 5', 'value 6', 'value 7', 'value 8',])

label = Label(text = "Кількість людей яка пройшла \n повз датчик", font = ("Arial", 12))
people = Entry(Window, bg = "silver" , width = 23, font = "13", state="readonly")
button1 = Button(text="Старт", width = "20", height = "2", command = click1)
button2 = Button(text="Очистити", width = "20", height = "2", command = click_clear)
button3 = Button(text="Список", width = "20", height = "2", command = click2)
button = Button(text="Вийти", width = "20", height = "2", command = Window.destroy)
label.place(x = 138, y = 100)
people.place(x = 138,y = 150)
button1.place(x = 50, y = 350)
button2.place(x = 50, y = 420)
button3.place(x = 300, y = 350)
button.place(x = 300, y = 420)
my_list.place(x = 138, y = 180)
Window.mainloop()
