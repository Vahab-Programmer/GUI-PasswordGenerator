from tkinter import Tk,Spinbox,Label,StringVar,Entry,IntVar,Menu,Checkbutton,Button
from tkinter.messagebox import showerror
from string import ascii_lowercase,ascii_uppercase,digits,punctuation
from sys import exit
from random import choices
__author__="Vahab Programmer https://Github.com/Vahab-Programmer"
__version__="0.0.3"
def About()->None:
    Root.attributes("-disabled",1)
    aboutwin = Tk()
    aboutwin.protocol("WM_DELETE_WINDOW",lambda:[Root.attributes("-disabled",0),
    aboutwin.destroy()])
    aboutwin.grab_set()
    aboutwin.title("About")
    aboutwin.geometry("234x85")
    aboutwin.resizable(False,False)
    Label(aboutwin,font=("Tahoma",10),text="A Simple Python Password Generator").place(x=5,y=0)
    a=StringVar(aboutwin)
    a.set("Github: Github.com/Vahab-Programmer")
    b=StringVar(aboutwin)
    b.set("Email: Vahab.Goudarzi.1390@Gmail.com")
    Entry(aboutwin,width=31,textvariable=a,font=("Tahoma",9),state="readonly").place(x=5,y=28)
    Entry(aboutwin,width=31,textvariable=b,font=("Tahoma",9),state="readonly").place(x=5,y=56)
    aboutwin.mainloop()
def PasswdGen(chars:str)->None:output.set("".join(choices(chars,k=length.get())))
def Generate()->None:
    output.set("")
    up = upp.get()
    lo = low.get()
    sm = smy.get()
    nu = num.get()
    if length.get() >= 8 and length.get() <=128:
        if custom.get():
            if custom_char.get() !="":PasswdGen(custom_char.get());return None
            else:showerror("Error","You Need To Write You'r Characters in custom char field")
        if not up and not lo and not sm and not nu:showerror("Error","You Need to Select A Option!");return None
        char=""
        if up:char += ascii_uppercase
        if lo:char += ascii_lowercase
        if sm:char += punctuation
        if nu:char += digits
        PasswdGen(char)
    elif length.get() >= 129:showerror("Error","Lenght Cannot Be Upper Than 128");length.set(128)
    else:showerror("Error","Lenght Cannot Be Lower Than 8");length.set(8)
def custom_config()->None:
    d={"state":"disable"}
    e={"state":"normal"}
    if custom.get():
        custom_e.config(e)
        up_c.config(d)
        low_c.config(d)
        sym_c.config(d)
        num_c.config(d)
    else:
        custom_e.config(d)
        up_c.config(e)
        low_c.config(e)
        sym_c.config(e)
        num_c.config(e)
Root = Tk()
Root.title("PasswdGen V3")
Root.geometry("250x300+500+150")
Root.resizable(False,False)
menubar = Menu(Root)
menubar.add_command(label="About",command=About)
menubar.add_command(label="Exit",command=exit)
Root.config(menu=menubar)
output = StringVar()
custom_char = StringVar()
upp = IntVar()
low = IntVar()
smy = IntVar()
num = IntVar()
custom = IntVar()
length = IntVar()
Entry(Root,textvariable=output,width=25,bd=10,background="blue",foreground="white").place(x=40,y=25)
custom_e=Entry(Root,textvariable=custom_char,width=30,bd=3,state="disabled")
custom_e.place(x=32,y=185)
Label(Root,text="Options",font=("Tahoma",11)).place(x=100,y=75)
Label(Root,text="Lenght",font=("Tahoma",12)).place(x=55,y=215)
up_c=Checkbutton(Root,text="Upper Case",font=("Tahoma",10),variable=upp,onvalue=1,offvalue=0)
up_c.place(x=35,y=100)
low_c=Checkbutton(Root,text="Lower Case",font=("Tahoma",10),variable=low,onvalue=1,offvalue=0)
low_c.place(x=135,y=100)
sym_c=Checkbutton(Root,text="Symbols",font=("Tahoma",10),variable=smy,onvalue=1,offvalue=0)
sym_c.place(x=35,y=125)
num_c=Checkbutton(Root,text="Numbers",font=("Tahoma",10),variable=num,onvalue=1,offvalue=0)
num_c.place(x=135,y=125)
Checkbutton(Root,text="Custom Char",font=("Tahoma",10),variable=custom,onvalue=1,offvalue=0,command=custom_config).place(x=70,y=150)
Spinbox(Root,textvariable=length,from_=8,to=128,width=12).place(x=130,y=220)
Button(Root,text="Generate",width=18,font=("Tahoma",13),command=Generate).place(x=40,y=250)
Root.mainloop()
