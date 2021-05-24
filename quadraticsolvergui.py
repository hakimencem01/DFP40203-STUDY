# !/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import math
top = Tk()

def solve_equation():
    # ax2 + bx + c = 0
    # (-b + sq((b*b)-4*a*c) ) / 2*a
    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())

    x1 = (-(b) + math.sqrt((b*b)-4*a*c))/(2*a)
    x2 = (-(b) - math.sqrt((b*b)-4*a*c))/(2*a)
    x1 = str(round(x1,3))
    x2 = str(round(x2,3))
    label_result_value["text"] = "Solution x1="+x1+" , x2="+x2

    
def clear_entry():
    entry_a.delete(0, 'end')
    entry_b.delete(0, 'end')
    entry_c.delete(0, 'end')
label_title = Label(text="Quadratic Equation Solver")
label_a_value = Label(text="A Value:")
label_b_value = Label(text="B Value:")
label_c_value = Label(text="C Value:")
label_result_value = Label(text="res")

entry_a = Entry()
entry_b = Entry()
entry_c = Entry()
label_title.place(x=30,y=1)
label_a_value.place(x=15,y=30)
label_b_value.place(x=15,y=60)
label_c_value.place(x=15,y=90)
label_result_value.place(x=0,y=180)

entry_a.place(x=70,y=30)
entry_b.place(x=70,y=60)
entry_c.place(x=70,y=90)

solve_btn = Button(text="Solve",command=solve_equation)
solve_btn.place(x=60,y=150)

solve_btn = Button(text="Clear",command=clear_entry)
solve_btn.place(x=120,y=150)
top.mainloop()
