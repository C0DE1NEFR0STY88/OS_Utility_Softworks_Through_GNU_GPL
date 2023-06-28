import os

from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class Notepad:
    root = Tk()
    thisWidth = 600
    thisHeight = 400
    thisTextArea = Text(root)
    thisMenuBar = Menu(root)
    thisFileMenu = Menu(thisMenuBar, tearoff=0)
    thisEditMenu = Menu(thisMenuBar, tearoff=0)
    thisHelpMenu = Menu(thisMenuBar, tearoff=0)
    thisScrollBar = Scrollbar(thisTextArea)
    file = None
    def __init__(self, **kwargs):
        try:
            self.root.wm_iconbitmap("Notepad.ico")
        except:
            pass
        self.root.title("Major Project")
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()
        left = (screenWidth / 2) - (self.thisWidth / 2)
        top = (screenHeight / 2) - (self.thisHeight / 2)
        self.root.geometry('%dx%d+%d+%d' % (self.thisWidth, self.thisHeight, left, top))
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.thisTextArea.grid(sticky=N + E + S + W)
        self.thisFileMenu.add_command(label="New", command=self.__newFile)
        self.thisFileMenu.add_command(label="Open", command=self.__openFile)
        self.thisFileMenu.add_command(label="Save", command=self.__saveFile)
        self.thisFileMenu.add_command(label="Exit", command=self.__exitApplication)
        self.thisMenuBar.add_cascade(label="File", menu=self.thisFileMenu)
        self.thisEditMenu.add_command(label="Cut", command=self.__cut)
        self.thisEditMenu.add_command(label="Copy", command=self.__copy)
        self.thisEditMenu.add_command(label="Paste", command=self.__paste)
        self.thisMenuBar.add_cascade(label="Edit", menu=self.thisEditMenu)
        self.thisHelpMenu.add_command(label="About Notepad", command=self.__showAbout)
        self.thisMenuBar.add_cascade(label="Help", menu=self.thisHelpMenu)
        # To configure MenuBar & scrollbar of notepad
        self.root.config(menu=self.thisMenuBar)
        self.thisScrollBar.pack(side=RIGHT, fill=Y)
        self.thisScrollBar.config(command=self.thisTextArea.yview)
        self.thisTextArea.config(yscrollcommand=self.thisScrollBar.set)
    def __exitApplication(self):
        self.root.destroy()
    def __showAbout(self):
        showinfo("Notepad", "This is a Notepad Using Tkinter Module In Python")
    def __openFile(self):
        self.__file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if self.__file == "":
            self.__file = None
        else:
            self.root.title(os.path.basename(self.__file) + " - Notepad")
            self.thisTextArea.delete(1.0, END)
            file = open(self.__file, "r")
            self.thisTextArea.insert(1.0, file.read())
            file.close()
    def __newFile(self):
        self.root.title("Untitled - Notepad")
        self.__file = None
        self.thisTextArea.delete(1.0, END)
    def __saveFile(self):
        if self.__file == None:
            self.__file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
            if self.__file == "":
                self.__file = None
            else:
                file = open(self.__file, "w")
                file.write(self.thisTextArea.get(1.0, END))
                file.close()
                self.root.title(os.path.basename(self.__file) + " - Notepad")

        else:
            file = open(self.__file, "w")
            file.write(self.thisTextArea.get(1.0, END))
            file.close()
    def __cut(self):
        self.thisTextArea.event_generate("<<Cut>>")
    def __copy(self):
        self.thisTextArea.event_generate("<<Copy>>")
    def __paste(self):
        self.thisTextArea.event_generate("<<Paste>>")
    def run(self):
        self.root.mainloop()



notepad = Notepad(width=600, height=400)
notepad.run()
