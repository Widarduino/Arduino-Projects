from tkinter import *
from tkinter import ttk      #imports tkinter

def calculate(*args):    #conversion function
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()     #initialises the window to root using Tk() function then assigns to name root
root.title("Feet to Meters")



mainframe = ttk.Frame(root, padding="3 3 12 12")   # creates frame in root and creates padding coming from (left,top,right,bottom)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) # grid tells where to place widget
root.columnconfigure(0, weight=1)   #tells tk to expand to fill if window is adjusted
root.rowconfigure(0, weight=1)


feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)  #creates entry widget
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))   #creates text widget

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W) #creates button to call function

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)   #creates text widget
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)   #creates text widget
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W) #creates text widget

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5) # for every element adds a spacer using grid function

feet_entry.focus() #places cursor on prompt
root.bind("<Return>", calculate)    # binds keystroke in root to call function

root.mainloop()