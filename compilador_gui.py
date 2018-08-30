#GUI del compilador de Python en Python
import pdb 	#python debugger
from tkinter import * #se importa todo de tkinter
from tkinter.filedialog import askopenfilename
import tkinter as tk #tkinter se declara como tk
#from tkinter import messagebox #mensajes de dialogo
import sys 
import os

def mainWindow():
    w=600
    h=600
    root= tk.Tk()
    root.title("Compilador python")
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    executeSyntax()

    root.mainloop()
    sys.exit(0)


def lookForFile():
    filename = tk.filedialog.askopenfilename()
    return filename


def executeSyntax():
    os.system("python3 syntax.py")#comando para ejecutar el arhivo


def executeLexicon():
    os.system("python3 lexicon.py")#comando para ejecutar el arhivo


if __name__ == '__main__':   
	mainWindow()