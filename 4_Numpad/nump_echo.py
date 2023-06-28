import os
import tkinter as tk
from tkinter import ttk

key = tk.Tk()  #window name for logic access, better than doing in class
key.title('Numpad_echobuild_final')  #title



expnump = "" #global access stringdump
 


def press(num):
    global expnump
    expnump=expnump + str(num)
    equationnump.set(expnump)
    key.clipboard_clear()#backup fix
    key.clipboard_append(expnump)#backup ()ality



def clear():
    global expnump
    expnump = ""
    equationnump.set(expnump)
    #key.clipboard_clear() #commented out to serve as a backup against misinput by user



def openosk():
    exec(open("osk.py").read())
#sometimes you need alpha-numeric,
#instead of copy pasting and merging from 2 sources
#you can copy from one text field
#as the input gets logged in the textfield of original spawner
#!!!osk.py should be in the same path as this file



#entry box
equationnump = tk.StringVar()
Dis_entry = ttk.Entry(key,textvariable = equationnump)
Dis_entry.grid(rowspan= 1 , columnspan = 10, ipadx = 10 , ipady = 10)



#buttons
one = ttk.Button(key,text = '1' , width = 6, command = lambda : press('1'))
one.grid(row = 1 , column = 0, ipadx = 6 , ipady = 10)

two = ttk.Button(key,text = '2' , width = 6, command = lambda : press('2'))
two.grid(row = 1 , column = 1, ipadx = 6 , ipady = 10)

three = ttk.Button(key,text = '3' , width = 6, command = lambda : press('3'))
three.grid(row = 1 , column = 2, ipadx = 6 , ipady = 10)

four = ttk.Button(key,text = '4' , width = 6, command = lambda : press('4'))
four.grid(row = 2 , column = 0, ipadx = 6 , ipady = 10)

five = ttk.Button(key,text = '5' , width = 6, command = lambda : press('5'))
five.grid(row = 2 , column = 1, ipadx = 6 , ipady = 10)

six = ttk.Button(key,text = '6' , width = 6, command = lambda : press('6'))
six.grid(row = 2 , column = 2, ipadx = 6 , ipady = 10)

seven = ttk.Button(key,text = '7' , width = 6, command = lambda : press('7'))
seven.grid(row = 3 , column = 0, ipadx = 6 , ipady = 10)

eight = ttk.Button(key,text = '8' , width = 6, command = lambda : press('8'))
eight.grid(row = 3 , column = 1, ipadx = 6 , ipady = 10)

nine = ttk.Button(key,text = '9' , width = 6, command = lambda : press('9'))
nine.grid(row = 3 , column = 2, ipadx = 6 , ipady = 10)

zero = ttk.Button(key,text = '0' , width = 6, command = lambda : press('0'))
zero.grid(row = 4 , column = 1, ipadx = 6 , ipady = 10)




#spec buttons
clear = ttk.Button(key,text = 'Clear' , width = 6, command = clear)
clear.grid(row = 4 , column = 0, ipadx = 6 , ipady = 10)


#sometimes you need alpha-numeric,
#instead of copy pasting and merging from 2 sources
#you can copy from one text field
#as the input gets logged in the textfield of original spawner
openonscreen = ttk.Button(key,text = 'OSK' , width = 6, command = openosk)
openonscreen.grid(row = 4 , column = 2, ipadx = 6 , ipady = 10)


key.mainloop()
