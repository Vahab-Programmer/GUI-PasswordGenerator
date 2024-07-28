from tkinter import *
from tkinter import messagebox
import sys
import random
letters_full = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890123456789!#@$%&()*+-{}|~[]^_?!#@$%&()*+-{}|~[]^_?"
upcase_full = "ABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890123456789!#@$%&()*+-{}|~[]^_?!#@$%&()*+-{}|~[]^_?"
lowcase_full = "abcdefghijklmnopqrstuvwxyz01234567890123456789!#@$%&()*+-{}|~[]^_?!#@$%&()*+-{}|~[]^_?"
letters_with_symbol = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#@$%&()*+-{}|~[]^_?!#@$%&()*+-{}|~[]^_?"
upcase_with_symbol = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!#@$%&()*+-{}|~[]^_?!#@$%&()*+-{}|~[]^_?"
lowcase_with_symbol = "abcdefghijklmnopqrstuvwxyz!#@$%&()*+-{}|~[]^_?!#@$%&()*+-{}|~[]^_?"
letters_with_digits = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890123456789"
upcase_with_digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890123456789"
lowcase_with_digits = "abcdefghijklmnopqrstuvwxyz01234567890123456789"
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowcase = "abcdefghijklmnopqrstuvwxyz"
upcase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def Exit():
    sys.exit()
def About():
    Root.attributes("-disabled",1)
    aboutwin = Tk()
    aboutwin.protocol("WM_DELETE_WINDOW",lambda:[Root.attributes("-disabled",0),
    aboutwin.destroy()])
    aboutwin.grab_set()
    aboutwin.title("About")
    aboutwin.geometry("234x85")
    aboutwin.resizable(False,False)
    Label(aboutwin,font=("Tahoma",10),text="A Simple Python Password Generator").place(x=5,y=0)
    text = Text(aboutwin,width=31,height=1,font=("Tahoma",10))
    text.insert(END,"Github: Github.com/Vahab-Programer")
    text.place(x=5,y=28)
    text2 = Text(aboutwin,width=31,height=1,font=("Tahoma",10))
    text2.insert(END,"Email: Vahabgamer.1390@Gmail.com")
    text2.place(x=5,y=56)
def PasswdGen(Method):
    output.set("".join(random.choices(Method,k=lenght.get())))
def Generate():
    output.set("")
    up = upp.get()
    lo = low.get()
    sm = smy.get()
    nu = num.get()
    if lenght.get() >= 8 and lenght.get() <=128:
        if up or lo :
            if up and lo and nu and sm:
                PasswdGen(letters_full)
            elif up and nu and sm and not lo:
                PasswdGen(upcase_full)
            elif lo and nu and sm and not up:
                PasswdGen(lowcase_full)
            elif up and lo and sm and not nu:
                PasswdGen(letters_with_symbol)
            elif up and sm and not lo and not nu:
                PasswdGen(upcase_with_symbol)
            elif lo and sm and not up and not nu:
                PasswdGen(lowcase_with_symbol)
            elif up and lo and nu and not sm:
                PasswdGen(letters_with_digits)
            elif up and nu and not lo and not sm:
                PasswdGen(upcase_with_digits)
            elif lo and nu and not up and not sm:
                PasswdGen(lowcase_with_digits)
            elif up and lo and not nu and not sm:
                PasswdGen(letters)
            elif up and not lo and not nu and not sm:
                PasswdGen(upcase)
            elif lo and not up and not nu and not sm:
                PasswdGen(lowcase)
            else:
                messagebox.showerror("Error","You need to select option!")
        else:
            messagebox.showerror("Error","You need to select Upper or Lower case Letters!")
    elif lenght.get() >= 129:
        messagebox.showerror("Error","Lenght cannot be Upper than 128")
    else:
        messagebox.showerror("Error","Lenght Cannot be Lower than 8")
Root = Tk()
Root.title("PasswdGen V2")
Root.geometry("250x300")
Root.resizable(False,False)
menubar = Menu(Root)
menubar.add_command(label="About",command=About)
menubar.add_command(label="Exit",command=Exit)
Root.config(menu=menubar)
output = StringVar()
upp = IntVar()
low = IntVar()
smy= IntVar()
num= IntVar()
lenght = IntVar()
display = Entry(Root,textvariable=output,width=25,bd=10,background="blue",foreground="white").place(x=40,y=25)
Label(Root,text="Options",font=("Tahoma",11)).place(x=100,y=75)
Label(Root,text="Lenght",font=("Tahoma",12)).place(x=55,y=195)
Checkbutton(Root,text="Upper Case",font=("Tahoma",10),variable=upp,onvalue=1,offvalue=0).place(x=35,y=100)
Checkbutton(Root,text="Lower Case",font=("Tahoma",10),variable=low,onvalue=1,offvalue=0).place(x=135,y=100)
Checkbutton(Root,text="Symbols",font=("Tahoma",10),variable=smy,onvalue=1,offvalue=0).place(x=35,y=150)
Checkbutton(Root,text="Numbers",font=("Tahoma",10),variable=num,onvalue=1,offvalue=0).place(x=135,y=150)
Lenght = Spinbox(Root,textvariable=lenght,from_=8,to=128,width=12,).place(x=130,y=200)
Button(Root,text="Generate",width=18,font=("Tahoma",13),command=Generate).place(x=40,y=250)
Root.mainloop()