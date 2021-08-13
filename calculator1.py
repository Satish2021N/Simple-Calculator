from tkinter import *
root = Tk()
root.geometry("425x585")
root.resizable(0,0) #To disable resize button
root.title("Simple Calculator")
root.iconbitmap(r'calc.ico')

'''Entry Widget'''
e = Entry(root, width=50, borderwidth=0, font=("Comic Sans MS", 24), justify="right",bg="#FFFFFF")
e.pack(expand=True, fill="both",padx=5)


def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math="addition"
    f_num = int(first_number)
    e.delete(0,END)

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math="subtraction"
    f_num = int(first_number)
    e.delete(0,END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math="multiplication"
    f_num = int(first_number)
    e.delete(0,END)

def button_division():
    first_number = e.get()
    global f_num
    global math
    math="division"
    f_num = int(first_number)
    e.delete(0,END)

def button_equal():
    second_number = e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    elif math == "subtraction":
        e.insert(0, f_num - int(second_number))
    elif math == "multiplication":
        e.insert(0, f_num * int(second_number))
    elif math == "division":
        e.insert(0, f_num /int(second_number))

# Frames
row1 = Frame(root, bg="#A0ABA4")
row1.pack(expand = True, fill="both")

row2 = Frame(root, bg="white")
row2.pack(expand = True, fill="both")

row3 = Frame(root, bg="white")
row3.pack(expand = True, fill="both")

row4 = Frame(root, bg="white")
row4.pack(expand=True, fill="both")

#Row1
btn1 = Button(row1, text="7", font=("Comic Sans MS", 22), bg="#351288", fg="#FFFFFF",relief = GROOVE, border = 0, command=lambda:button_click(7))
btn1.pack(side=LEFT, expand= True, fill="both",)
btn1 = Button(row1, text="8", font=("Comic Sans MS", 22), bg="#351288", fg="#FFFFFF",relief = GROOVE, border = 0, command=lambda:button_click(8))
btn1.pack(side=LEFT, expand= True, fill="both",)
btn1 = Button(row1, text="9", font=("Comic Sans MS", 22), bg="#351288", fg="#FFFFFF",relief = GROOVE, border = 0, command=lambda:button_click(9))
btn1.pack(side=LEFT, expand= True, fill="both",)
btn1 = Button(row1, text="/", font=("Comic Sans MS", 22), bg="#351288", fg="#FFFFFF",relief = GROOVE, border = 0, command=lambda:button_division())
btn1.pack(side=LEFT, expand= True, fill="both",)

#Row2
btn1 = Button(row2,text="4",font=("Comic Sans MS", 22),bg="#351288",fg="#FFFFFF",relief = GROOVE,border = 0,command=lambda:button_click(4))
btn1.pack(side=LEFT, expand= True, fill="both",)
btn1 = Button(row2, text="5", font=("Comic Sans MS", 22), bg="#351288", fg="#FFFFFF",relief=GROOVE, border = 0, command=lambda:button_click(5))
btn1.pack(side=LEFT, expand= True, fill="both",)
btn1 = Button(row2, text="6", font=("Comic Sans MS", 22), bg="#351288", fg="#FFFFFF", relief = GROOVE, border = 0, command=lambda:button_click(6))
btn1.pack(side=LEFT, expand= True, fill="both",)
btn1 = Button(row2, text="-", font=("Comic Sans MS", 22), bg="#351288", fg="#FFFFFF", relief = GROOVE, border = 0, command=lambda:button_subtract())
btn1.pack(side=LEFT, expand= True, fill="both",)

#Row3
btn1 = Button(row3, text="1", font=("Comic Sans MS", 22), bg="#351288", fg="#FFFFFF",relief = GROOVE, border = 0, command=lambda:button_click(1))
btn1.pack(side=LEFT, expand= True, fill="both",)
btn1 = Button(row3, text="2", font=("Comic Sans MS", 22), bg="#351288", fg="#FFFFFF",relief = GROOVE, border = 0, command=lambda:button_click(2))
btn1.pack(side=LEFT, expand= True, fill="both",)
btn1 = Button(row3, text="3", font=("Comic Sans MS", 22), bg="#351288", fg="#FFFFFF",relief = GROOVE, border = 0, command=lambda:button_click(3))
btn1.pack(side=LEFT, expand= True, fill="both",)
btn1 = Button(row3, text="+", font=("Comic Sans MS", 22), bg="#351288", fg="#FFFFFF",relief = GROOVE, border = 0, command=lambda:button_add())
btn1.pack(side=LEFT, expand= True, fill="both",)

#Row4
btn1 = Button(row4, text="C", font=("Comic Sans MS", 22), bg="#351288", fg="#FFFFFF",relief = GROOVE, border = 0, command=lambda:button_clear())
btn1.pack(side=LEFT, expand= True, fill="both",)
btn1 = Button(row4, text="0", font=("Comic Sans MS", 22), bg="#351288", fg="#FFFFFF",relief = GROOVE, border = 0, command=lambda:button_click(0))
btn1.pack(side=LEFT, expand= True, fill="both",)
btn1 = Button(row4, text="*", font=("Comic Sans MS", 22), bg="#351288", fg="#FFFFFF",relief = GROOVE, border = 0, command=lambda:button_multiply())
btn1.pack(side=LEFT, expand= True, fill="both",)
btn1 = Button(row4, text="=", font=("Comic Sans MS", 22), bg="#ff972a", fg="#FFFFFF",relief = GROOVE, border = 0, command=lambda:button_equal())
btn1.pack(side=LEFT, expand= True, fill="both",)

root.mainloop()