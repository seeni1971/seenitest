from tkinter import * 
from tkinter.ttk import * 
#from tkinter.dnd import Tester as DragWindow,Icon as Dragable
from time import strftime 
  
# creating tkinter window 
root = Tk() 
root.title('Menu Demonstration') 
root.geometry('1000x1000')

def add_button():
    Button(root, text='New Button', command=None).pack()


# Creating Menubar 
menubar = Menu(root) 
  
# Adding File Menu and commands 
file = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New File', command = None)
file.add_command(label ='Open...', command = None) 
file.add_command(label ='Save', command = None) 
file.add_separator() 
file.add_command(label ='Exit', command = root.destroy) 
  
# Adding Edit Menu and commands 
edit = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Edit', menu = edit) 
edit.add_command(label ='Cut', command = None) 
edit.add_command(label ='Copy', command=add_button) 
edit.add_command(label ='Paste', command=None)
edit.add_command(label ='Select All', command = None) 
edit.add_separator() 
edit.add_command(label ='Find...', command = None) 
edit.add_command(label ='Find again', command = None) 
  
# Adding Help Menu 
help_ = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Help', menu = help_) 
help_.add_command(label ='Tk Help', command = None) 
help_.add_command(label ='Demo', command = None) 
help_.add_separator() 
help_.add_command(label ='About Tk', command = None) 
  
# display Menu 
root.config(menu = menubar) 
def button_click(t):
    rect=c.create_rectangle(150, 50, 200, 100,
                                outline = "black", fill = t,
                                width = 2)
c = Canvas(root, width=330, height=400, bg="grey")
c.place(x=50, y=50)
rect= c.create_rectangle(150, 50, 200, 100,
                                outline = "black", fill = "lightgrey",
                                width = 2)

btn1 = Button(c, text='on', command=lambda:button_click("lightgreen"))
btn2 = Button(c, text='off', command=lambda:button_click("red"))
btn1.place(x=50, y=200)
btn2.place(x=200, y=200)
mainloop() 