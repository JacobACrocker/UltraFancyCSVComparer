from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import functools
import pandas as pd

master = Tk()

  
@functools.lru_cache(maxsize=None)  
def findFile1():
    master.filename =  filedialog.askopenfilename(initialdir = "C:/",title = "Select file 1",filetypes = (("CSV","*.csv"),("all files","*.*")))
    print (master.filename)
    file1 = master.filename
    return file1
          
@functools.lru_cache(maxsize=None)  
def findFile2():
    master.filename =  filedialog.askopenfilename(initialdir = "C:/",title = "Select file 2",filetypes = (("CSV","*.csv"),("all files","*.*")))
    print (master.filename)
    file2 = master.filename
    return file2
       

def saveFile():
    master.filename =  filedialog.asksaveasfilename(initialdir = "C:/",title = "Save file",defaultextension=".csv",filetypes = (("CSV","*.csv"),("all files","*.*")))
    print (master.filename)
    f1 = pd.read_csv(findFile1())
    f2 = pd.read_csv(findFile2())

    with open(master.filename, 'w') as outFile:
        diff = (f2[~f2.Email.isin(f1.Email)])
        diff.to_csv (master.filename, index = None, header=True)
        messagebox.showinfo("Sucess", "File created successfully!")       

loadFile1 = Button(master, text="Load Old File", command=findFile1)
loadFile1.pack()

loadFile2 = Button(master, text="Load New File", command=findFile2)
loadFile2.pack()

start = Button(master, text="Save Updates to New File", command=saveFile)
start.pack()

master.geometry("400x100")
master.title("Ultra Fancy CSV Comparer")
 
mainloop()
