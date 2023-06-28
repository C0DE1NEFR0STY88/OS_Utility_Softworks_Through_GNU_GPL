#echo name scheme present throughout since built on calc_echo
import math
from tkinter import *

class RunnerWindow:
    def __init__(self, win):#constructor
        self.echolbl1=Label(win, text='First Input Value')
        self.echolbl1.place(x=60, y=50)

        self.echolbl2=Label(win, text='Second Input Value')
        self.echolbl2.place(x=60, y=100)
        
        self.echolbl3=Label(win, text='Processed Result')
        self.echolbl3.place(x=60, y=300)
        

        self.echoinputbar1=Entry()
        self.echoinputbar1.place(x=382, y=50)
        
        self.echoinputbar2=Entry()
        self.echoinputbar2.place(x=382, y=100)
        
        self.echoiobar3=Entry()
        self.echoiobar3.place(x=382, y=300)
        
        
        self.alphab1=Button(win, text='1 Power 2', command=self.powfunc)
        #could also be self.alphab1.bind('<Button-1>', self.add)
        self.alphab1.place(x=80, y=150)

        self.bravob1=Button(win, text='Log(1Base2)', command=self.logfunc)
        self.bravob1.place(x=168, y=150)
        
        self.charlieb1=Button(win, text='Sin(1stval)', command=self.sinfunc)
        self.charlieb1.place(x=268, y=150)
                   
        self.deltab1=Button(win, text='Cos(1stval)', command=self.cosfunc)
        self.deltab1.place(x=382, y=150)

        self.eb1=Button(win, text='Tan(1stval)', command=self.tanfunc)
        self.eb1.place(x=80, y=200)

        self.fb1=Button(win, text='Cosec(1stval)', command=self.cosecfunc)
        self.fb1.place(x=168, y=200)

        self.eb1=Button(win, text='Sec(1stval)', command=self.secfunc)
        self.eb1.place(x=268, y=200)

        self.eb1=Button(win, text='Cot(1stval)', command=self.cotfunc)
        self.eb1.place(x=382, y=200)

        self.eb1=Button(win, text='GCD', command=self.gcdfunc)
        self.eb1.place(x=80, y=250)

        self.eb1=Button(win, text='SQRT(1stval)', command=self.sqrtfunc)
        self.eb1.place(x=168, y=250)

        self.eb1=Button(win, text='DEGtoRAD', command=self.d2rfunc)
        self.eb1.place(x=268, y=250)

        self.eb1=Button(win, text='RADtoDEG', command=self.r2dfunc)
        self.eb1.place(x=382, y=250)


        
        
    def powfunc(self):
        self.echoiobar3.delete(0, 'end')
        val1=float(self.echoinputbar1.get())
        val2=float(self.echoinputbar2.get())
        result=pow(val1,val2)
        self.echoiobar3.insert(END, str(result))

        
    def logfunc(self):
        self.echoiobar3.delete(0, 'end')#to clear old display value from iobar
        val1=float(self.echoinputbar1.get())
        val2=float(self.echoinputbar2.get())
        result=(math.log(val1,val2))
        self.echoiobar3.insert(END, str(result))

        
    def sinfunc(self):
        self.echoiobar3.delete(0, 'end')#to clear old display value from iobar
        val1=float(self.echoinputbar1.get())
        result=(round(math.sin(math.radians(val1))))#must first be converted to radian ALSO round used to fix floatingpoint error
        self.echoiobar3.insert(END, str(result))    

        
    def cosfunc(self):
        self.echoiobar3.delete(0, 'end')#to clear old display value from iobar
        val1=float(self.echoinputbar1.get())
        result=(round(math.cos(math.radians(val1))))#must first be converted to radian ALSO round used to fix floatingpoint error
        self.echoiobar3.insert(END, str(result))     


    def tanfunc(self):
        self.echoiobar3.delete(0, 'end')#to clear old display value from iobar
        val1=float(self.echoinputbar1.get())
        result=(round(math.tan(math.radians(val1))))#must first be converted to radian ALSO round used to fix floatingpoint error
        self.echoiobar3.insert(END, str(result)) 


    def cosecfunc(self):
        self.echoiobar3.delete(0, 'end')#to clear old display value from iobar
        val1=float(self.echoinputbar1.get())
        if((round(math.sin(math.radians(val1))))==0):
            self.echoiobar3.insert(END, "∞")#infinity
        else:
            result=(1/(round(math.sin(math.radians(val1)))))#must first be converted to radian ALSO round used to fix floatingpoint error
            self.echoiobar3.insert(END, str(result))


    def secfunc(self):
        self.echoiobar3.delete(0, 'end')#to clear old display value from iobar
        val1=float(self.echoinputbar1.get())
        if((round(math.cos(math.radians(val1))))==0):
            self.echoiobar3.insert(END, "∞")#infinity
        else:
            result=(1/(round(math.cos(math.radians(val1)))))#must first be converted to radian ALSO round used to fix floatingpoint error
            self.echoiobar3.insert(END, str(result)) 


    def cotfunc(self):
        self.echoiobar3.delete(0, 'end')#to clear old display value from iobar
        val1=float(self.echoinputbar1.get())
        if((round(math.tan(math.radians(val1))))==0):
            self.echoiobar3.insert(END, "∞")#infinity
        else:
            result=(1/(round(math.tan(math.radians(val1)))))#must first be converted to radian ALSO round used to fix floatingpoint error
            self.echoiobar3.insert(END, str(result)) 


    def gcdfunc(self):
        self.echoiobar3.delete(0, 'end')#to clear old display value from iobar
        val1=int(self.echoinputbar1.get())
        val2=int(self.echoinputbar2.get())
        result=(math.gcd(val1,val2))
        self.echoiobar3.insert(END, str(result))


    def sqrtfunc(self):
        self.echoiobar3.delete(0, 'end')#to clear old display value from iobar
        val1=float(self.echoinputbar1.get())
        result=(math.sqrt(val1))
        self.echoiobar3.insert(END, str(result))


    def d2rfunc(self):
        self.echoiobar3.delete(0, 'end')#to clear old display value from iobar
        val1=float(self.echoinputbar1.get())
        result=(math.radians(val1))
        self.echoiobar3.insert(END, str(result))


    def r2dfunc(self):
        self.echoiobar3.delete(0, 'end')#to clear old display value from iobar
        val1=float(self.echoinputbar1.get())
        result=(math.degrees(val1))
        self.echoiobar3.insert(END, str(result))


root=Tk()
mywin=RunnerWindow(root)
root.title('advcalcmodule_echobuild')
root.geometry("600x480+80+80")
#+80+80 is displacement of window spawn from upper left corner of user screen
root.mainloop()
