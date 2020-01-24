from tkinter import *
import math

root=Tk()
#put title on the window
root.title('simple calculator')
#creating a label widget
"""mylabel1=Label(root, text="Hello World!").grid(row=0, column=0)
mylabel2=Label(root, text="How are you?").grid(row=2, column=10)
mylabel3=Label(root, text="+").grid(row=2, column=1)"""

#showing it on to the screen
"""mylabel1.grid(row=0, column=0)
mylabel2.grid(row=2, column=10)
mylabel3.grid(row=1, column=1)"""

e=Entry(root, width=35, borderwidth=5)
#will put buttons accordingly
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#e.pack()
#e.insert(0)




#defining every function of buttons
def button_equal():
    number2=e.get()
    e.delete(0, END)
    #if statement for calc functions
    if calc == 'addition':
        e.insert(0, n_number + float(number2))
    if calc == 'subtraction':
        e.insert(0, n_number - float(number2))
    if calc == 'multiplication':
        e.insert(0, n_number * float(number2))
    if calc == 'division':
        e.insert(0, n_number / float(number2))
    if calc == 'square':
        e.insert(0, math.pow(number2,2))
    if calc == 'cube':
        e.insert(0, math.pow(number2,3))
    if calc == 'square root':
        e.insert(0, math.sqrt(number2))

def button_add():
    number1=e.get()
    global n_number
    global calc
    calc='addition'
    n_number=float(number1)
    e.delete(0, END)

def button_press(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))

def button_clear():
    e.delete(0, END)

def button_sub():
    number1 = e.get()
    global n_number
    global calc
    calc = 'subtraction'
    n_number = float(number1)
    e.delete(0, END)

def button_mult():
    number1 = e.get()
    global n_number
    global calc
    calc = 'multiplication'
    n_number = float(number1)
    e.delete(0, END)

def button_div():
    number1 = e.get()
    global n_number
    global calc
    calc = 'division'
    n_number = float(number1)
    e.delete(0, END)

"""def button_sq():
    number1 = e.get()
    global n_number
    global calc
    calc = 'square'
    n_number = float(number1)
    e.delete(0, END)
def button_cube():
    number1 = e.get()
    global n_number
    global calc
    calc = 'cube'
    n_number = float(number1)
    e.delete(0, END)
def button_sqr():
    number1 = e.get()
    global n_number
    global calc
    calc = 'square root'
    n_number = float(number1)
    e.delete(0, END)"""

#below will define buttons
button_1=Button(root, text='1', padx=40, pady=20, command=lambda: button_press('1'))
button_2=Button(root, text='2', padx=40, pady=20, command=lambda: button_press('2'))
button_3=Button(root, text='3', padx=40, pady=20, command=lambda: button_press('3'))
button_4=Button(root, text='4', padx=40, pady=20, command=lambda: button_press('4'))
button_5=Button(root, text='5', padx=40, pady=20, command=lambda: button_press('5'))
button_6=Button(root, text='6', padx=40, pady=20, command=lambda: button_press('6'))
button_7=Button(root, text='7', padx=40, pady=20, command=lambda: button_press('7'))
button_8=Button(root, text='8', padx=40, pady=20, command=lambda: button_press('8'))
button_9=Button(root, text='9', padx=40, pady=20, command=lambda: button_press('9'))
button_0=Button(root, text='0', padx=40, pady=20, command=lambda: button_press('0'))
button_add=Button(root, text='+', padx=39, pady=20, command=button_add)
button_subtraction=Button(root, text='-', padx=42, pady=20, command=button_sub)
button_multiplication=Button(root, text='*', padx=40, pady=20, command=button_mult)
button_division=Button(root, text='/', padx=42, pady=20, command=button_div)
"""button_square=Button(root, text='x2', padx=36, pady=20, command=button_sq)
button_cube=Button(root, text='x3', padx=36, pady=20, command=button_cube)
button_sqr=Button(root, text='sqr', padx=36, pady=20, command=button_sqr)"""
button_equals=Button(root, text='=', padx=40, pady=20, command=button_equal)
button_clear=Button(root, text='clear', padx=132, pady=20, command=button_clear)

#below will show buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_add.grid(row=4, column=1)
button_subtraction.grid(row=4, column=2)
button_multiplication.grid(row=5, column=0)
button_division.grid(row=5, column=1)
"""button_square.grid(row=5, column=2)
button_cube.grid(row=6, column=0)
button_sqr.grid(row=6, column=1)"""
button_equals.grid(row=5, column=2)
button_clear.grid(row=6, column=0, columnspan=3)


#loop it
root.mainloop()
