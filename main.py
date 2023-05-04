from tkinter import *
import tkinter.font as font
import final_test
import os




def start_button(t):
    final_test.app()

def read_button(t):
    os.startfile("res\\Greetings User.pdf")

def see_alphabets(t):
    os.startfile("res\\Alphabets.jpeg") 

window = Tk()

lbl = Label(window, text="PROJECT GD", fg='purple', bg='turquoise', font=("Times New Roman", 30))
lbl.place(x=30, y=45)

# declaring the common font size for all the buttons
myFont = font.Font(size=15)

# Read Instructions button
btn = Button(window, text="Read Instructions", fg='black', command=lambda t="READ Button Clicked": read_button(t))
btn['font'] = myFont
btn.place(x=70, y=135)

# Start application button
btn = Button(window, text="Start Application", fg='black', command=lambda t="START Button Clicked": start_button(t))
btn['font'] = myFont
btn.place(x=75, y=235)

# Show Gestures button
btn = Button(window, text="Show Gestures", fg='black', command=lambda t="SHOW GESTURES Button Clicked": see_alphabets(t))
btn['font'] = myFont
btn.place(x=80, y=335)

window.title('PROJECT GD')
window.geometry("300x450")
window.configure(bg='turquoise')
window.mainloop()
