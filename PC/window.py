from tkinter import *
from tkinter.messagebox import *
import random
from tkinter import ttk

def click_start():
    people_in.config(state="normal")
    people_in.delete(0, END)
    people_in.insert(0, random.randint(0, 1000000))
    people_in.config(state="readonly")
    people_out.config(state="normal")
    people_out.delete(0, END)
    people_out.insert(0, random.randint(0, 1000000))
    people_out.config(state="readonly") 

def click_clear():
    people_in.config(state="normal")
    if askyesno(title="Close", message="Ви впевнені, що хочете очистити?"):
        people_in.delete(0, END)
    people_in.config(state="readonly")
    people_out.config(state="normal")
    if askyesno(title="Close", message="Ви впевнені, що хочете очистити?"):
        people_out.delete(0, END)
    people_out.config(state="readonly")

def click_refresh():
    my_list["values"] = [3, 4]
    my_list.delete(0, END)


Window = Tk()
Window.title("Window")
Window.geometry("500x500")
Window.resizable(0,0)

my_list = ttk.Combobox(Window, font='Arial 11',width=15, height=5, value = [1, 2])

label = Label(text = "Кількість людей які:", font = ("Arial", 12))
label_in = Label(text = "Зайшли в приміщення", font = ("Arial", 12))
label_out = Label(text = "Вийшли з приміщення", font = ("Arial", 12))

people_in = Entry(Window, bg = "silver" , width = 13, font = "13", state="readonly")
people_out = Entry(Window, bg = "silver" , width = 13, font = "13", state="readonly")

button_start = Button(text="Старт", width = "17", height = "2", command = click_start)
button_click = Button(text="Очистити", width = "17", height = "2", command = click_clear)
button_refresh = Button(text="Оновити", width = "10", height = "1", command = click_refresh)
button_exit = Button(text="Вийти", width = "20", height = "2", command = Window.destroy)


label.place(x = 180, y = 140)
label_in.place(x = 58,y = 185)
label_out.place(x = 278,y = 185)

people_in.place(x = 66,y = 210)
people_out.place(x = 285,y = 210)

button_start.place(x = 260, y = 270)
button_click.place(x = 118, y = 270)
button_refresh.place(x = 143, y = 0)
button_exit.place(x = 178, y = 400)

my_list.place(x = 0, y = 2)

Window.mainloop()
