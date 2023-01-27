from tkinter import *

def click():
    people.delete(0, END)




Window = Tk()
Window.title("Window")
Window.geometry("500x500")
Window.resizable(0,0)
label = Label(text = "Кількість людей яка пройшла \n повз датчик", font = ("Arial", 12))
people = Entry(Window, bg = "silver" , width = 25, font = "13")

button1 = Button(text="Старт", width = "20")
button2 = Button(text="Очистити", width = "20", command = click)
button3 = Button(text="Пауза", width = "20")
button = Button(text="Вийти", width = "20", command = Window.destroy)
label.place(x = 150, y = 100)
people.place(x = 150,y = 150)
button1.place(x = 50, y = 350)
button2.place(x = 50, y = 400)
button3.place(x = 300, y = 350)
button.place(x = 300, y = 400)
Window.mainloop()
