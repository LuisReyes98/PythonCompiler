from tkinter import *
import sys 
import os
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
import tkinter as tk #tkinter se declara como tk
import syntax as sy
import lexicon as lx

global input_text1
global input_text2
global input_text3
global filename

def main():	
	global input_text1
	global input_text2
	global input_text3
	# Parent window delaration and configure 
	w=700
	h=700
	root = Tk()
	ws = root.winfo_screenwidth()
	hs = root.winfo_screenheight()	
	x = (ws/2) - (w/2)    
	y = (hs/2) - (h/2)    
	root.geometry('%dx%d+%d+%d' % (w, h, x, y))    

	root.title("Analizador Lexico y Sintactico (PYTHON)")
	#root.geometry("600x700")

	root.configure(background="#B22222")
	root.resizable(0,990)

	# Labels
	principal_label = Label(root, text="COMPILADOR PYTHON", font="Arial", bg="#B22222", fg="white").place(x=230, y=20)
	principal_code_label = Label(root, text="CODIGO FUENTE", bg="#B22222", fg="white").place(x=250, y=140)
	lexico_analysis_label = Label(root, text="ANALISIS LEXICO", bg="#B22222", fg="white").place(x=110, y=375)
	syntactic_analysis_label = Label(root, text="ANALISIS SINTACTICO", bg="#B22222", fg="white").place(x=370, y=375)

	#Butons
	import_button = Button(root, text="Importar archivo (.py)", bg="#4682B4", cursor="hand1", fg="white", borderwidth='10', command=lookForFile)
	import_button.place(x=20, y=70)

	delete_button = Button(root, text="Borrar", cursor="hand1", bg="red", fg="white", command=eraseCode)
	delete_button.place(x=220, y=70)

	lexico_analysis_button = Button(root, text="Analisis Léxico", bg="#FF8C00", cursor="hand1", fg="white", borderwidth='10', command=executeLexicon)
	lexico_analysis_button.place(x=75, y=610)

	syntactic_analysis_button = Button(root, text="Analisis Sintáctico", bg="#228B22", cursor="hand1", fg="white", borderwidth='10', command=executeSyntax)
	syntactic_analysis_button.place(x=375, y=610)

	prepare_button= Button(root, text="Preparar Codigo", bg="#228B22", cursor="hand1", fg="white", borderwidth='10', command=prepareFile)
	prepare_button.place(x=200, y=320)

	#Inputs
	input_text1 = Text(root, width=80, height=8)
	input_text1.place(x=20,y=170)

	input_text2 = Text(root, width=38, height=12)
	input_text2.place(x=20,y=400)

	input_text3 = Text(root, width=38, height=12)
	input_text3.place(x=310,y=400)
	
	#import_button.pack()

	root.mainloop()
	sys.exit(0)#para que el programa se cierre una vez se cierra la ventana



def lookForFile():
	global filename
	global input_text1
	filename = tk.filedialog.askopenfilename()
	#print(filename)	
	try:
		if filename.endswith(".py"):
			file = open(filename,'r')
			code = file.read()
			file.close()
			input_text1.delete('1.0', END)
			input_text1.insert(END,code)
		elif filename:					
			tk.messagebox.showwarning("Error", "Debe escogerse un archivo .py")
			lookForFile()

	except Exception as e:
		pass	

def prepareFile():
	global input_text1
	fileWrite = open('input.py','w')
	fileWrite.write(input_text1.get("1.0",END))
	fileWrite.close()	
	return filename

def eraseCode():
	global input_text1
	input_text1.delete('1.0', END)


def executeSyntax():
	global input_text3
	texto=sy.main()	
	input_text3.delete('1.0', END)
	input_text3.insert(END,texto)
	
    #os.system("python3 syntax.py ")#comando para ejecutar el arhivo


def executeLexicon():
	global input_text2	
	texto=lx.main()
	
	input_text2.delete('1.0', END)
	input_text2.insert(END,texto)

	#os.system("python3 lexicon.py")#comando para ejecutar el arhivo

if __name__ == '__main__':   
	main()