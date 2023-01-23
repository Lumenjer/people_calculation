from tkinter import *

Window = Tk()
Window.title("Window")
Window.geometry("500x500")
Window.resizable(0,0)
button = Button(text="Exit", width = "15", command = Window.destroy)
button.pack()
Window.mainloop()
