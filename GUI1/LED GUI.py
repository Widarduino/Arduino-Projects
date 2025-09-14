from ftplib import print_line
from tkinter import *
from tkinter import ttk
import csv

# https://tkdocs.com/tutorial/widgets.html documentation
pushed = False


# RUN THIS SCRIPT FIRST

with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')
    writer.writerow(['ID/STATE'])



def test(x,y):

    global pushed
    global writer
    #OUTPUT.set("Hello World!")
    if not pushed:
        x.config(text="LED:"+ y +" : ON")
        store = (y+"1")
        print("LED" + y + ":ON")


        #turn this into function to avoid rewrites
        #instead of writing full line to cvs write first digit as LEDpin and second as binary state
        with open('output.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ')
            writer.writerow([store])

        pushed = True

#replace LED1 with the led name being inputted into the function

    else:
        x.config(text="LED:" + y + " : OFF")
        store = (y+"0")
        print("LED" + y + ":OFF")

        with open('output.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ')
            writer.writerow([store])

        pushed = False

### below is code to print screen

root = Tk()
style = ttk.Style()
style.configure("TLabel", foreground="white", background="blue")
mainframe = ttk.Frame(root, style="TLabel", padding="100 70 10 10")  # Create a frame inside root and padding
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))  # Place it in the grid

root.columnconfigure(0, weight=1)  # x axis resize refresh
root.rowconfigure(0, weight=1) # y axis resize refresh



TEST = StringVar()
TEST.set("COMPONENT CONTROL")

Title = (ttk.Label(mainframe, textvariable=TEST,style="TLabel"))   #creates title line
Title.grid(column=0, row=0, sticky=(N, E))
Title.config(padding="0 0 0 15")                    #creates padding between title and button



BUTTON1 = ttk.Button(mainframe, text="LED1 : OFF",command= lambda:test(BUTTON1,"1"))
BUTTON1.grid(column=0, row=2, sticky=(N, E))

BUTTON2 = ttk.Button(mainframe, text="LED2 : OFF",command= lambda:test(BUTTON2,"2"))
BUTTON2.grid(column=0, row=3, sticky=(N, E))
#this works for atm

#(future)replace the text to change depending on amount of LED's instead of this create for loop
#    that will initialize button at position for int var indicating led amount



root.mainloop() #loops the program so it doesn't crash immediately