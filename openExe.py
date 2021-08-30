# Import Library
from tkinter import *
import os
from tkinter.filedialog import askopenfilename

# Create Object
root = Tk()

# Set geometry
root.geometry('200x200')


def open_file():
    #file = askopenfilename()
    #os.system('F:\jogos\MK11\MK11\Binaries\Retail\MK11.exe')
    #os.system('F:\jogos\guitar\GH3.exe')
    os.system('C:/Windows/System32/notepad.exe')



Button(root, text='Open',
       command=open_file).pack(side=TOP,
                               pady=10)

# Execute Tkinter
root.mainloop()