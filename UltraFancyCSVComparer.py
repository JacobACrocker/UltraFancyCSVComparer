from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import functools
import pandas as pd
import numpy as np

master = Tk()

#obtain the original file  
@functools.lru_cache(maxsize=None)  
def findFile1():
    master.filename =  filedialog.askopenfilename(initialdir = "C:/",title = "Select file 1",filetypes = (("CSV","*.csv"),("all files","*.*")))
    print (master.filename)
    file1 = master.filename
    return file1
  
#obtain the most recent file containing updates and changes          
@functools.lru_cache(maxsize=None)  
def findFile2():
    master.filename =  filedialog.askopenfilename(initialdir = "C:/",title = "Select file 2",filetypes = (("CSV","*.csv"),("all files","*.*")))
    print (master.filename)
    file2 = master.filename
    return file2


#choose a directory and file name for new file. Rename column to 'Email'.       
@functools.lru_cache(maxsize=None)
def saveFile():
    master.filename =  filedialog.asksaveasfilename(initialdir = "C:/",title = "Save file",defaultextension=".csv",filetypes = (("CSV","*.csv"),("all files","*.*")))
    newDoc = master.filename
    print (newDoc)
    file1 = pd.read_csv(findFile1())
    f1 = file1.rename(columns={'Contact Email': 'Email'})
    file2 = pd.read_csv(findFile2())
    f2 = file2.rename(columns={'Contact Email': 'Email'})
    
#open new file and populate it with the updates and changes only. Then, assign the Product Representative name and ID# to the appropriate entry based on State.
    with open(master.filename, 'w') as outFile:
        pd.options.mode.chained_assignment = None
        diff = (f2[~f2.Email.isin(f1.Email)])
        conditions = [
            (diff['State'] == 'TX') | (diff['State'] == 'LA') | (diff['State'] == 'FL'),
            (diff['State'] == 'AK') | (diff['State'] == 'AZ') | (diff['State'] == 'CA') | (diff['State'] == 'CT') | (diff['State'] == 'DE') | (diff['State'] == 'HI') | (diff['State'] == 'ID') | (diff['State'] == 'ME') | (diff['State'] == 'MD') | (diff['State'] == 'MA') | (diff['State'] == 'MT') | (diff['State'] == 'NV') | (diff['State'] == 'NH') | (diff['State'] == 'NJ') | (diff['State'] == 'NY') | (diff['State'] == 'OR') | (diff['State'] == 'RI') | (diff['State'] == 'VT') | (diff['State'] == 'WA') | (diff['State'] == 'WY'),
            (diff['State'] == 'CO') | (diff['State'] == 'DC') | (diff['State'] == 'GA') | (diff['State'] == 'IL') | (diff['State'] == 'IA') | (diff['State'] == 'KS') | (diff['State'] == 'KY') | (diff['State'] == 'MO') | (diff['State'] == 'NE') | (diff['State'] == 'NC') | (diff['State'] == 'SC') | (diff['State'] == 'UT') | (diff['State'] == 'VA') | (diff['State'] == 'WV'),
            (diff['State'] == 'AL') | (diff['State'] == 'AR') | (diff['State'] == 'IN') | (diff['State'] == 'MI') | (diff['State'] == 'MN') | (diff['State'] == 'MS') | (diff['State'] == 'NM') | (diff['State'] == 'ND') | (diff['State'] == 'OH') | (diff['State'] == 'OK') | (diff['State'] == 'PA') | (diff['State'] == 'SD') | (diff['State'] == 'TN') | (diff['State'] == 'WI'),
        ]
        choices = ['Bryan', 'Marilyn', 'Ryan', 'Tom']
        diff['Product Rep'] = np.select(conditions, choices, default='Bryan')
        conditions = [
            (diff['State'] == 'TX') | (diff['State'] == 'LA') | (diff['State'] == 'FL'),
            (diff['State'] == 'AK') | (diff['State'] == 'AZ') | (diff['State'] == 'CA') | (diff['State'] == 'CT') | (diff['State'] == 'DE') | (diff['State'] == 'HI') | (diff['State'] == 'ID') | (diff['State'] == 'ME') | (diff['State'] == 'MD') | (diff['State'] == 'MA') | (diff['State'] == 'MT') | (diff['State'] == 'NV') | (diff['State'] == 'NH') | (diff['State'] == 'NJ') | (diff['State'] == 'NY') | (diff['State'] == 'OR') | (diff['State'] == 'RI') | (diff['State'] == 'VT') | (diff['State'] == 'WA') | (diff['State'] == 'WY'),
            (diff['State'] == 'CO') | (diff['State'] == 'DC') | (diff['State'] == 'GA') | (diff['State'] == 'IL') | (diff['State'] == 'IA') | (diff['State'] == 'KS') | (diff['State'] == 'KY') | (diff['State'] == 'MO') | (diff['State'] == 'NE') | (diff['State'] == 'NC') | (diff['State'] == 'SC') | (diff['State'] == 'UT') | (diff['State'] == 'VA') | (diff['State'] == 'WV'),
            (diff['State'] == 'AL') | (diff['State'] == 'AR') | (diff['State'] == 'IN') | (diff['State'] == 'MI') | (diff['State'] == 'MN') | (diff['State'] == 'MS') | (diff['State'] == 'NM') | (diff['State'] == 'ND') | (diff['State'] == 'OH') | (diff['State'] == 'OK') | (diff['State'] == 'PA') | (diff['State'] == 'SD') | (diff['State'] == 'TN') | (diff['State'] == 'WI'),
        ]
        choices = ['13', '301876', '87942', '301874']
        diff['PR ID'] = np.select(conditions, choices, default='13')
        diff.to_csv (newDoc, index = None, header=True)
        messagebox.showinfo("Sucess", "File created successfully!")
        return newDoc

    

loadFile1 = Button(master, text="Load Old File", command=findFile1)
loadFile1.pack()

loadFile2 = Button(master, text="Load New File", command=findFile2)
loadFile2.pack()

start = Button(master, text="Save Updates to New File", command=saveFile)
start.pack()

master.geometry("400x100")
master.title("Ultra Fancy CSV Comparer")
 
mainloop()
