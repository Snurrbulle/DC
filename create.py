from tkinter import *
import tkMessageBox
import tkFont

def window():
    window = Tk()
    window.title("DC")
    window.configure(width=500, height=300)
    window.configure(bg="black")
    window.mainloop()

def background(window):
    image2 =Image.open('C:\\Users\\\\D\\titlepage\\front.gif')
    image1 = ImageTk.PhotoImage(image2)
    w = image1.width()
    h = image1.height()
    app.geometry('%dx%d+0+0' % (w,h))
