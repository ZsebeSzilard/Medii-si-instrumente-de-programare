'''
1
--------------------------------------------
from tkinter import *
master = Tk()
def callback():
    print("click!")

theLabel = Label(master, text="This is too easy")
b = Button(master, text="OK", command=callback)
b.pack()
master.geometry("500x500")
master.title("Alma")
theLabel.pack()
mainloop()
2
--------------------------------------------
from tkinter import *
form = Tk()
form.resizable(False,False)
form.title("Project")
form.geometry("500x350+110+300")
label1 = Label(form,text="Yes").pack()
label2 = Label(form,text="Yes").pack()
label3 = Label(form,text="Yes").pack()
label4 = Label(form,text="Yes").pack()
label5 = Label(form,text="Yes").pack()
form.mainloop()
3
---------------------------------------
from tkinter import *

form = Tk()
form.title("My project")
form.resizable(False,False)

window_height = 500
window_width = 900

screen_width = form.winfo_screenwidth()
screen_height = form.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

form.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
form.mainloop()

4
----------------------------------------------

from tkinter import *

form = Tk()

form.title("Main window")

formwidth = 700
formheight = 450
x_cordonate = int((form.winfo_screenwidth()-formwidth)/2)
y_cordonate = int((form.winfo_screenheight()-formheight)/2)

form.geometry("{}x{}+{}+{}".format(formwidth,formheight,x_cordonate,y_cordonate))

topFrame = Frame(form)
topFrame.pack(side=TOP)

bottomFrame=Frame(form)
bottomFrame.pack(side=BOTTOM)

leftFrame=Frame(form)
leftFrame.pack(side=LEFT)

rightFrame = Frame(form)
rightFrame.pack(side=RIGHT)

button1 = Button(bottomFrame, text="1.Press me!", fg="red",bg="dark blue")
button2 = Button(bottomFrame,text="2.Press me!", fg="green")
button3 = Button(bottomFrame,text="3.Press me!", fg="blue")
button4 = Button(topFrame,text="4.Press me!", fg="purple",bg="orange")
button5 = Button(topFrame,text="5.Press me!", fg="Aqua")
button6 = Button(leftFrame,text="6.Press me!", fg="Orange")
button7 = Button(rightFrame,text="7.Press me!", fg="Grey")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
button5.pack(side=LEFT)
button6.pack(side=LEFT)
button7.pack(side=LEFT)

form.mainloop()


5
----------------------------------------------


from tkinter import *

form = Tk()
form.title("Main window")
formwidth = 500
formheight = 350
x_cordonate=int((form.winfo_screenwidth() - formwidth) / 2)
y_cordonate=int((form.winfo_screenheight() - formheight) / 2)
form.geometry("{}x{}+{}+{}".format(formwidth,formheight,x_cordonate,y_cordonate))

topFrame = Frame(form)
topFrame.pack(side=TOP)

bottomFrame = Frame(form)
bottomFrame.pack(side=BOTTOM)



Label1 = Label(bottomFrame, text="This is a label", bg= "Red", fg= "Black")
Label1.pack(fill=X,side = BOTTOM)

form.mainloop()
6
---------------------------------

from tkinter import *

form = Tk()
form.title("Main window")
formwidth = 500
formheight = 350
x_cordonate=int((form.winfo_screenwidth() - formwidth) / 2)
y_cordonate=int((form.winfo_screenheight() - formheight) / 2)
form.geometry("{}x{}+{}+{}".format(formwidth,formheight,x_cordonate,y_cordonate))


label1 = Label(form, text="Name:")
label2 = Label(form, text="Password:")

entry1 = Entry(form)
entry2 = Entry(form)

label1.grid(sticky=E)
label2.grid(row=1, sticky=E)

entry1.grid(row=0, column=1, sticky=E)
entry2.grid(row=1, column=1, sticky=E)

checkbox=Checkbutton(form, text="Keep me logged")
checkbox.grid(columnspan=2)

form.mainloop()


6
---------------------------------

from tkinter import *

def PrintHello():
    print("Hello World")

def PrintHi(event):
    print("Hi!")
form = Tk()
form.title("Main window")
formwidth = 500
formheight = 350
x_cordonate=int((form.winfo_screenwidth() - formwidth) / 2)
y_cordonate=int((form.winfo_screenheight() - formheight) / 2)
form.geometry("{}x{}+{}+{}".format(formwidth,formheight,x_cordonate,y_cordonate))

button1 = Button(form, text="Click me!", command=PrintHello)
button1.pack();

button2 = Button(form, text='Say "Hi!"')
button2.pack();
button2.bind("<Button-1>", PrintHi)


form.mainloop()

7
---------------------------------


from tkinter import *

form = Tk()
form.title("Main window")

def leftclick(event):
    print("Left")
def middleclick(event):
    print("Middle")
def rightclick(event):
    print("Right")

frame = Frame(form, width=300, height=200, bg="Red")
frame.bind("<Button-1>", leftclick)
frame.bind("<Button-2>", middleclick)
frame.bind("<Button-3>", rightclick)
frame.pack()

form.mainloop()

8
---------------------------------


from tkinter import *

class MyButtons:
    def __init__(self, master):
        frame = Frame(master, width=250, height=150, bg="Blue")
        frame.pack(side=TOP)

        self.button1=Button(frame, text= "Print message", command=self.PrintMessage)
        self.button1.pack(side=LEFT)

        self.button2=Button(frame, text="Quit", command=frame.quit)
        self.button2.pack(side=RIGHT)

    def PrintMessage(self):
        print("This is a message")

form = Tk()
form.geometry("300x250")


frame = Frame(form, width=250, height=150, bg="Red")

buttons = MyButtons(form)
frame.pack(side=TOP)
form.mainloop()

9
---------------------------------

from tkinter import *


def DoNothing():
    print("i did nothing")

form = Tk()

mainmenu = Menu(form)
form.config(menu=mainmenu)

submenu1=Menu(mainmenu)
mainmenu.add_cascade(label="File",menu=submenu1)
submenu1.add_command(label="New File...",command=DoNothing)
submenu1.add_command(label="Settings",command=DoNothing)
submenu1.add_separator()
submenu1.add_command(label="Quit",command=form.quit)

submenu2=Menu(mainmenu)
mainmenu.add_cascade(label="Edit",menu=submenu2)
submenu2.add_command(label="Delete", command=form.quit)

form.mainloop()

10
---------------------------------


from tkinter import *


def DoNothing():
    print("i did nothing")

form = Tk()
# ************  Main Menu  *****************
mainmenu = Menu(form)
form.config(menu=mainmenu)

submenu1=Menu(mainmenu)
mainmenu.add_cascade(label="File",menu=submenu1)
submenu1.add_command(label="New File...",command=DoNothing)
submenu1.add_command(label="Settings",command=DoNothing)
submenu1.add_separator()
submenu1.add_command(label="Quit",command=form.quit)

submenu2=Menu(mainmenu)
mainmenu.add_cascade(label="Edit",menu=submenu2)
submenu2.add_command(label="Delete", command=form.quit)

# ************  Toolbar  *****************

toolbar = Frame(form,bg="Blue")
button1 = Button(toolbar,text="Press me!",command=DoNothing)
button1.pack(side=LEFT,padx=2,pady=2)

button2 = Button(toolbar,text="Press me!",command=DoNothing)
button2.pack(side=RIGHT,padx=2,pady=2)



toolbar.pack(side=TOP,fill=X)
form.mainloop()

11
---------------------------------



from tkinter import *


def DoNothing():
    print("i did nothing")

form = Tk()
# ************  Main Menu  *****************
mainmenu = Menu(form)
form.config(menu=mainmenu)

submenu1=Menu(mainmenu)
mainmenu.add_cascade(label="File",menu=submenu1)
submenu1.add_command(label="New File...",command=DoNothing)
submenu1.add_command(label="Settings",command=DoNothing)
submenu1.add_separator()
submenu1.add_command(label="Quit",command=form.quit)

submenu2=Menu(mainmenu)
mainmenu.add_cascade(label="Edit",menu=submenu2)
submenu2.add_command(label="Delete", command=form.quit)

# ************  Toolbar  *****************

toolbar = Frame(form,bg="Blue")
button1 = Button(toolbar,text="Press me!",command=DoNothing)
button1.pack(side=LEFT,padx=2,pady=2)

button2 = Button(toolbar,text="Press me!",command=DoNothing)
button2.pack(side=RIGHT,padx=2,pady=2)

toolbar.pack(side=TOP,fill=X)

# ************  Statusbar  *****************
status = Label(form, text="Prepearing to show something...",bd=1,relief=SUNKEN,anchor=W) #relief=SOLID
status.pack(side=BOTTOM,fill=X)


form.mainloop()

12
---------------------------------


from tkinter import *
import tkinter.messagebox as msgBox

form=Tk()
msgBox.showinfo("Fact","You are ugly!")

answer = msgBox.askquestion("Question 1","Do you love chocolate?")

if answer == "yes":  # is- not work properly , USE ==
    print("Yes")
else:
    print("Hell no!")

form.mainloop()


13
---------------------------------

from tkinter import *
form = Tk()

mycanvas=Canvas(form, width=200,height=100)
mycanvas.pack()

myline1=mycanvas.create_line(10,20,0,50,fill="red")
myline2=mycanvas.create_line(10,20,170,50,fill="blue")
myrectangle=mycanvas.create_rectangle(55,25,105,85,fill="green")
mycanvas.delete(myline1)
mycanvas.delete(ALL)

form.mainloop()

14
---------------------------------


from tkinter import *
form = Tk()
form.iconbitmap("Ekko Icon.ico")

photo = PhotoImage(file="Ekko Icon.png")
label = Label(form,image=photo)
label.pack();

form.mainloop()

14++
# -----------------------

#https://www.daniweb.com/programming/software-development/threads/369823/resizing-image
# pip install Pillow !!! pip install Pil - outdated
from tkinter import *
from PIL import Image
from PIL import ImageTk

form = Tk()
form.iconbitmap("Ekko Icon.ico")

file_in = "Ekko Icon.png"
pil_image = PhotoImage(file=file_in)
#pil_image = ImageTk.PhotoImage(pil_image)
#print("image.size   = (%d, %d)" % pil_image.size)
#print("image.format = %s" % pil_image.format)
#print("image.mode   = %s" % pil_image.mode)
#image200x100 =
#pil_image.resize((200, 100), Image.ANTIALIAS)
label = Label(form,image=(pil_image))
label.pack();

form.mainloop()
'''



from tkinter import *

def WriteSomething():
    print("Something")


form = Tk()
form.title("Main window")
x = int(form.winfo_screenwidth()/2-400/2)
y = int(form.winfo_screenheight()/2-500/2)
form.geometry("400x500+{}+{}".format(x,y))
form.resizable(True,False)

mainmenu = Menu(form)
form.config(menu=mainmenu)

submenu1=Menu(mainmenu)
mainmenu.add_cascade(label="File",menu=submenu1)
submenu1.add_command(label="New File...",command=WriteSomething)
submenu1.add_command(label="Settings",command=WriteSomething)
submenu1.add_separator()


submenu2=Menu(mainmenu)
mainmenu.add_cascade(label="Edit",menu=submenu2)
submenu2.add_command(label="Delete...",command=WriteSomething)
submenu2.add_separator()
submenu2.add_command(label="Quit",command=form.quit)
submenu1.add_cascade(label="File",menu=submenu2)




status = Label(form, text="Prepearing to show something...",bd=1,relief=SUNKEN,anchor=W) #relief=SOLID
status.pack(side=BOTTOM,fill=X)


toolbar = Frame(form,bg="Blue")
toolbar.pack(anchor=W, fill=X)
button11 = Button(toolbar,text="Press me!",command=WriteSomething)
button11.pack(side=LEFT,padx=2,pady=2)

button21 = Button(toolbar,text="Press me!",command=WriteSomething)
button21.pack(side=LEFT,padx=2,pady=2)

#photo = PhotoImage(file="Ekko Icon.png")
#label = Label(form,image=photo)
#label.pack();

mycanvas=Canvas(form, width=200,height=100)
mycanvas.pack()

myline1=mycanvas.create_line(10,20,0,50,fill="red")
myline2=mycanvas.create_line(10,20,170,50,fill="blue")
myrectangle=mycanvas.create_rectangle(55,25,105,85,fill="green")
#mycanvas.delete(myline1)
mycanvas.delete(ALL)

form.mainloop()

