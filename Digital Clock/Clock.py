from tkinter import Tk, Label
import time

### create a tkinter window

master = Tk()
master.title('Digital Clock')

### create a function using "def"
### This function alows you to display timei on the label
#### %I = hour; %M = minutes; %p = AM/PM

def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(1000,get_time)

### Stylize your Label Widget
### Feel free to change : font, size, background and foreground colors!!

clock = Label(master, font=('Arial', 120),bg='#872229',fg='#DA6998')
clock.pack()

get_time()

#put it in a loop
master.mainloop()