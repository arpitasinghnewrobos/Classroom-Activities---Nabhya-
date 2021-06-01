# REGISTRATION FORM
from tkinter import *

win = Tk()
win.geometry('500x500')          # for Geometry of app
win.title("Registration Form")   # Creation Of title

a=StringVar()
b=StringVar()

def firstbutton():
    print('Welcome to NewRobos')
    A=a.get()
    B=b.get()
    print('Your name is', A)
    print('Your Registered Number is ', B)
    
def secondbuton():
    exit()
    
#Create 1st 2nd and 3rd   Label,Relif - provide box 
l1=Label(win,text='Registration Form',relief="solid",font=('arial',19,"bold"))
l1.place(x=90,y=60)


l2=Label(win,text='Name :',font=('arial',10,"bold"))
l2.place(x=90,y=120)

e1=Entry(win,textvar=a)
e1.place(x=200,y=120)

l3=Label(win,text='Mobile Number:',font=('arial',10,"bold"))
l3.place(x=90,y=160)

e2=Entry(win,textvar=b)
e2.place(x=200,y=160)

B1=Button(win,text='Login',bg='brown',font=('arial',19,"bold"), fg='White',command=firstbutton)
B1.place(x=90,y=200)

B2=Button(win,text=' Exit ',bg='brown',font=('arial',19,"bold"), fg='White',command=secondbuton)
B2.place(x=220,y=200)

