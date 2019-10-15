from tkinter import *
import random

def mouse_position(event):
    global xmouse, ymouse
    xmouse = event.x
    ymouse = event.y

def noob():
    global x, y, xmouse, ymouse, total
    if xmouse >= x and xmouse <= x + 2 * R and ymouse >= y and ymouse <= y + 2 * R:
        total += 1
        e2 = Label(text=str(total), bg='white')
        e2.place(x=265, y=5)
        x = random.randint(0, 900)
        y = random.randint(30, 600)
        c.coords(ball, x, y, x + 2 * R, y + 2 * R)

def pro():
    global xmouse, ymouse, x, y
    if xmouse < x + 40 + 2*R and xmouse > x - 40  and ymouse > y - 40 and ymouse < y + 2*R + 40:
        x = random.randint(0, 900)
        y = random.randint(30, 600)
        c.coords(ball, x, y, x + 2 * R, y + 2 * R)


def mouse_click(event):
    global total
    mouse_position(event)
    if total < 20:
        noob()

def run(event):
    global xmouse, ymouse
    if total >= 20:
        xmouse = event.x
        ymouse = event.y
        pro()



root = Tk()
root.resizable(width=False, height=False)
root.config(cursor="hand1")
root.bind('<Button-1>', mouse_click)
root.bind('<Motion>', run)

c = Canvas(root, width = 1000, height = 700, bg = "white" )
c.pack()

x = random.randint(0, 1000)
y = random.randint(30, 700)
R = 10
xmouse = 1
ymouse = 1
total = 0

ball = c.create_oval(x, y , x + 2*R, y + 2*R,fill="#"+("%06x"%random.randint(0,16777215)))
c.create_text(115, 15, text =  "5 - bad, 10 - good, 15 - God, 21 - Коля")
c.create_text(250, 15, text = "Total:")
e1 = Label(text=str(total), bg='white')
e1.place(x=265, y= 5)

root.mainloop()
