from tkinter import *

class RunnerWindow:
    def __init__(self, win):#constructor
        self.echolbl1=Label(win, text='First Input Value')
        self.echolbl1.place(x=60, y=50)

        self.echolbl2=Label(win, text='Second Input Value')
        self.echolbl2.place(x=60, y=100)
        
        self.echolbl3=Label(win, text='Processed Result')
        self.echolbl3.place(x=60, y=200)
        

        self.echoinputbar1=Entry()
        self.echoinputbar1.place(x=382, y=50)
        
        self.echoinputbar2=Entry()
        self.echoinputbar2.place(x=382, y=100)
        
        self.echoiobar3=Entry()
        self.echoiobar3.place(x=382, y=200)
        
        
        self.alphab1=Button(win, text='Addition (+)', command=self.addfunc)
        #could also be self.alphab1.bind('<Button-1>', self.add)
        self.alphab1.place(x=80, y=150)

        self.bravob1=Button(win, text='Subtraction (-)', command=self.subfunc)
        self.bravob1.place(x=168, y=150)
        
        self.charlieb1=Button(win, text='Multiplication (X)', command=self.prodfunc)
        self.charlieb1.place(x=268, y=150)
                   
        self.deltab1=Button(win, text='Division (/)', command=self.divfunc)
        self.deltab1.place(x=382, y=150)

        #need a button and its () to connect adv
        
        
    def addfunc(self):
        self.echoiobar3.delete(0, 'end')
        val1=float(self.echoinputbar1.get())
        val2=float(self.echoinputbar2.get())
        result=val1+val2
        self.echoiobar3.insert(END, str(result))

        
    def subfunc(self):
        self.echoiobar3.delete(0, 'end')#to clear old display value from iobar
        val1=float(self.echoinputbar1.get())
        val2=float(self.echoinputbar2.get())
        result=val1-val2
        self.echoiobar3.insert(END, str(result))

        
    def prodfunc(self):
        self.echoiobar3.delete(0, 'end')#to clear old display value from iobar
        val1=float(self.echoinputbar1.get())
        val2=float(self.echoinputbar2.get())
        result=val1*val2
        self.echoiobar3.insert(END, str(result))    

        
    def divfunc(self):
        self.echoiobar3.delete(0, 'end')#to clear old display value from iobar
        val1=float(self.echoinputbar1.get())
        val2=float(self.echoinputbar2.get())
        if(val2==0):
            self.echoiobar3.insert(END, "ZeroDiv Error")#taken from console error log
        else:
            result=val1/val2
            self.echoiobar3.insert(END, str(result))    
        



root=Tk()
mywin=RunnerWindow(root)
root.title('calc_foxtrot')
root.geometry("600x480+80+80")
#+80+80 is displacement of window spawn from upper left corner of user screen
root.mainloop()
