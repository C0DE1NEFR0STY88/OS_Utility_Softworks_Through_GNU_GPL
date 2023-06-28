import os
import tkinter as tk
from tkinter import ttk

key = tk.Tk()  #window name for logic access, better than doing in class
key.title('OnScreenKeyboard_golfbuild')  #title


exp = "" #global access stringdump
 

def press(num):
    global exp
    exp=exp + str(num)
    equation.set(exp)
    key.clipboard_clear()#backup fix
    key.clipboard_append(exp)#backup ()ality


def clear():
    global exp
    exp = ""
    equation.set(exp)
    #key.clipboard_clear() #commented out to serve as a backup against misinput by user



def opennump():
    exec(open("4_nump_echo_final.py").read())
#sometimes you need alpha-numeric,
#instead of copy pasting and merging from 2 sources
#you can copy from one text field
#as the input gets logged in the textfield of original spawner
#!!!osk.py should be in the same path as this file


#window size
key.geometry('1010x290')         #spawn x y size
key.maxsize(width=1080, height=360)      #maximum x y size
key.minsize(width= 1010 , height = 290)     #minimum x y size


#key.configure(bg = '')    #bg colour commented out. for now.


#entry box
equation = tk.StringVar()
Dis_entry = ttk.Entry(key,textvariable = equation)
Dis_entry.grid(rowspan= 1 , columnspan = 100, ipadx = 999 , ipady = 20)




#all buttons, row wise for better command. using windows on screen keyboard layout for reference



#First Row Buttons

q = ttk.Button(key,text = 'Q' , width = 6, command = lambda : press('Q'))
q.grid(row = 1 , column = 0, ipadx = 6 , ipady = 10)


w = ttk.Button(key,text = 'W' , width = 6, command = lambda : press('W'))
w.grid(row = 1 , column = 1, ipadx = 6 , ipady = 10)


E = ttk.Button(key,text = 'E' , width = 6, command = lambda : press('E'))
E.grid(row = 1 , column = 2, ipadx = 6 , ipady = 10)


R = ttk.Button(key,text = 'R' , width = 6, command = lambda : press('R'))
R.grid(row = 1 , column = 3, ipadx = 6 , ipady = 10)


T = ttk.Button(key,text = 'T' , width = 6, command = lambda : press('T'))
T.grid(row = 1 , column = 4, ipadx = 6 , ipady = 10)


Y = ttk.Button(key,text = 'Y' , width = 6, command = lambda : press('Y'))
Y.grid(row = 1 , column = 5, ipadx = 6 , ipady = 10)


U = ttk.Button(key,text = 'U' , width = 6, command = lambda : press('U'))
U.grid(row = 1 , column = 6, ipadx = 6 , ipady = 10)


I = ttk.Button(key,text = 'I' , width = 6, command = lambda : press('I'))
I.grid(row = 1 , column = 7, ipadx = 6 , ipady = 10)


O = ttk.Button(key,text = 'O' , width = 6, command = lambda : press('O'))
O.grid(row = 1 , column = 8, ipadx = 6 , ipady = 10)


P = ttk.Button(key,text = 'P' , width = 6, command = lambda : press('P'))
P.grid(row = 1 , column = 9, ipadx = 6 , ipady = 10)


cur = ttk.Button(key,text = '{' , width = 6, command = lambda : press('{'))
cur.grid(row = 1 , column = 10 , ipadx = 6 , ipady = 10)


cur_c = ttk.Button(key,text = '}' , width = 6, command = lambda : press('}'))
cur_c.grid(row = 1 , column = 11, ipadx = 6 , ipady = 10)


back_slash = ttk.Button(key,text = '\\' , width = 6, command = lambda : press('\\'))
back_slash.grid(row = 1 , column = 12, ipadx = 6 , ipady = 10)


clear = ttk.Button(key,text = 'Clear' , width = 6, command = clear)
clear.grid(row = 1 , column = 13, ipadx = 20 , ipady = 10)





#Second Row Buttons

A = ttk.Button(key,text = 'A' , width = 6, command = lambda : press('A'))
A.grid(row = 2 , column = 0, ipadx = 6 , ipady = 10)


S = ttk.Button(key,text = 'S' , width = 6, command = lambda : press('S'))
S.grid(row = 2 , column = 1, ipadx = 6 , ipady = 10)


D = ttk.Button(key,text = 'D' , width = 6, command = lambda : press('D'))
D.grid(row = 2 , column = 2, ipadx = 6 , ipady = 10)


F = ttk.Button(key,text = 'F' , width = 6, command = lambda : press('F'))
F.grid(row = 2 , column = 3, ipadx = 6 , ipady = 10)


G = ttk.Button(key,text = 'G' , width = 6, command = lambda : press('G'))
G.grid(row = 2 , column = 4, ipadx = 6 , ipady = 10)


H = ttk.Button(key,text = 'H' , width = 6, command = lambda : press('H'))
H.grid(row = 2 , column = 5, ipadx = 6 , ipady = 10)


J = ttk.Button(key,text = 'J' , width = 6, command = lambda : press('J'))
J.grid(row = 2 , column = 6, ipadx = 6 , ipady = 10)


K = ttk.Button(key,text = 'K' , width = 6, command = lambda : press('K'))
K.grid(row = 2 , column = 7, ipadx = 6 , ipady = 10)


L = ttk.Button(key,text = 'L' , width = 6, command = lambda : press('L'))
L.grid(row = 2 , column = 8, ipadx = 6 , ipady = 10)


semi_co = ttk.Button(key,text = ';' , width = 6, command = lambda : press(';'))
semi_co.grid(row = 2 , column = 9, ipadx = 6 , ipady = 10)


d_colon = ttk.Button(key,text = '"' , width = 6, command = lambda : press('"'))
d_colon.grid(row = 2 , column = 10, ipadx = 6 , ipady = 10)


open_b = ttk.Button(key,text = '(' , width = 6, command = lambda : press('('))
open_b.grid(row = 2 , column = 11 , ipadx = 6 , ipady = 10)


close_b = ttk.Button(key,text = ')' , width = 6, command = lambda : press(')'))
close_b.grid(row = 2 , column = 12 , ipadx = 6 , ipady = 10)




#Third Row Buttons

Z = ttk.Button(key,text = 'Z' , width = 6, command = lambda : press('Z'))
Z.grid(row = 3 , column = 0, ipadx = 6 , ipady = 10)


X = ttk.Button(key,text = 'X' , width = 6, command = lambda : press('X'))
X.grid(row = 3 , column = 1, ipadx = 6 , ipady = 10)


C = ttk.Button(key,text = 'C' , width = 6, command = lambda : press('C'))
C.grid(row = 3 , column = 2, ipadx = 6 , ipady = 10)


V = ttk.Button(key,text = 'V' , width = 6, command = lambda : press('V'))
V.grid(row = 3 , column = 3, ipadx = 6 , ipady = 10)


B = ttk.Button(key, text= 'B' , width = 6 , command = lambda : press('B'))
B.grid(row = 3 , column = 4 , ipadx = 6 ,ipady = 10)


N = ttk.Button(key,text = 'N' , width = 6, command = lambda : press('N'))
N.grid(row = 3 , column = 5, ipadx = 6 , ipady = 10)


M = ttk.Button(key,text = 'M' , width = 6, command = lambda : press('M'))
M.grid(row = 3 , column = 6, ipadx = 6 , ipady = 10)


left = ttk.Button(key,text = '<' , width = 6, command = lambda : press('<'))
left.grid(row = 3 , column = 7, ipadx = 6 , ipady = 10)


right = ttk.Button(key,text = '>' , width = 6, command = lambda : press('>'))
right.grid(row = 3 , column = 8, ipadx = 6 , ipady = 10)


slas = ttk.Button(key,text = '/' , width = 6, command = lambda : press('/'))
slas.grid(row = 3 , column = 9, ipadx = 6 , ipady = 10)


q_mark = ttk.Button(key,text = '?' , width = 6, command = lambda : press('?'))
q_mark.grid(row = 3 , column = 10, ipadx = 6 , ipady = 10)


coma = ttk.Button(key,text = ',' , width = 6, command = lambda : press(','))
coma.grid(row = 3 , column = 11, ipadx = 6 , ipady = 10)


dot = ttk.Button(key,text = '.' , width = 6, command = lambda : press('.'))
dot.grid(row = 3 , column = 12, ipadx = 6 , ipady = 10)




#Fourth Row Button

space = ttk.Button(key,text = 'Space' , width = 6, command = lambda : press(' '))
space.grid(row = 4 , columnspan = 14 , ipadx = 160 , ipady = 10)





#Fifth Row Buttons; special characters and symbols here. extracted using character map app on windows
#using character map app-> press alt and then hit required numpad keys, or copy within app

equalt = ttk.Button(key,text = '=' , width = 6, command = lambda : press('='))
equalt.grid(row = 5 , column = 0 , ipadx = 6 , ipady = 10)

copyrightsign = ttk.Button(key,text = '©' , width = 6, command = lambda : press('©'))
copyrightsign.grid(row = 5 , column = 1 , ipadx = 6 , ipady = 10)

regsign = ttk.Button(key,text = '®' , width = 6, command = lambda : press('®'))
regsign.grid(row = 5 , column = 2 , ipadx = 6 , ipady = 10)

tmsign = ttk.Button(key,text = '™' , width = 6, command = lambda : press('™'))
tmsign.grid(row = 5 , column = 3 , ipadx = 6 , ipady = 10)

sectionsign = ttk.Button(key,text = '§' , width = 6, command = lambda : press('§'))
sectionsign.grid(row = 5 , column = 4 , ipadx = 6 , ipady = 10)

plus = ttk.Button(key,text = '+' , width = 6, command = lambda : press('+'))
plus.grid(row = 5 , column = 5 , ipadx = 6 , ipady = 10)

minus = ttk.Button(key,text = '-' , width = 6, command = lambda : press('-'))
minus.grid(row = 5 , column = 6 , ipadx = 6 , ipady = 10)

hashsign = ttk.Button(key,text = '#' , width = 6, command = lambda : press('#'))
hashsign.grid(row = 5 , column = 7 , ipadx = 6 , ipady = 10)

at = ttk.Button(key,text = '@' , width = 6, command = lambda : press('@'))
at.grid(row = 5 , column = 8 , ipadx = 6 , ipady = 10)

micro = ttk.Button(key,text = 'µ' , width = 6, command = lambda : press('µ'))
micro.grid(row = 5 , column = 9 , ipadx = 6 , ipady = 10)

degree = ttk.Button(key,text = '°' , width = 6, command = lambda : press('°'))
degree.grid(row = 5 , column = 10 , ipadx = 6 , ipady = 10)

inr = ttk.Button(key,text = '₹' , width = 6, command = lambda : press('₹'))
inr.grid(row = 5 , column = 11 , ipadx = 6 , ipady = 10)

dollar = ttk.Button(key,text = '$' , width = 6, command = lambda : press('$'))
dollar.grid(row = 5 , column = 12 , ipadx = 6 , ipady = 10)

infinity = ttk.Button(key,text = '∞' , width = 6, command = lambda : press('∞'))
infinity.grid(row = 5 , column = 13 , ipadx = 6 , ipady = 10)


#connecting to nump file now
#sometimes you need alpha-numeric,
#instead of copy pasting and merging from 2 sources
#you can copy from one text field
#as the input gets logged in the textfield of original spawner
opennumpad = ttk.Button(key,text = 'NUMP' , width = 6, command = opennump)
opennumpad.grid(row = 2 , column = 13, ipadx = 20 , ipady = 10)
#row 2 so that it is right below clear spec button


key.mainloop()
