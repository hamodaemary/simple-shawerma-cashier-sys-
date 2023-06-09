import customtkinter
import os
import tempfile
from tkinter import messagebox
c = customtkinter.CTk()
c.geometry('900x500')
c.resizable(False,False)
c.title('shop')
#THE FUNCTIONS:
#Boxes:
en0 = customtkinter.CTkComboBox(c,values=['Small','Meduim','large'])
en0.place(x=1,y=1)
lbl = customtkinter.CTkLabel(c,text='fries roll')
lbl.place(x=150,y=1)
box = customtkinter.CTkOptionMenu(c,values=['1','2','3','4','5'])
box.place(x=205,y=5)
en1 = customtkinter.CTkComboBox(c,values=['Small','Meduim','large'])
en1.place(x=1,y=50)
lbl1 = customtkinter.CTkLabel(c,text='fries crip')
lbl1.place(x=150,y=50)
box1 = customtkinter.CTkOptionMenu(c,values=['1','2','3','4','5'])
box1.place(x=205,y=55)
en2 = customtkinter.CTkComboBox(c,values=['Small','Meduim','large'])
en2.place(x=1,y=100)
lbl2 = customtkinter.CTkLabel(c,text='shawerma roll')
lbl2.place(x=150,y=100)
en3 = customtkinter.CTkComboBox(c,values=['Small','Meduim','large'])
en3.place(x=1,y=150)
box2 = customtkinter.CTkOptionMenu(c,values=['1','2','3','4','5'])
box2.place(x=235,y=100)
lbl3 = customtkinter.CTkLabel(c,text='shawerma Crip')
lbl3.place(x=150,y=150)
box3 = customtkinter.CTkOptionMenu(c,values=['1','2','3','4','5'])
box3.place(x=240,y=150)
en4 = customtkinter.CTkComboBox(c,values=['Small','Meduim','large'])
en4.place(x=1,y=200)
lbl4 = customtkinter.CTkLabel(c,text='Falafel roll')
lbl4.place(x=150,y=200)
box4 = customtkinter.CTkOptionMenu(c,values=['1','2','3','4','5'])
box4.place(x=235,y=200)
en5 = customtkinter.CTkComboBox(c,values=['Small','Meduim','large'])
en5.place(x=1,y=250)
lbl5 = customtkinter.CTkLabel(c,text='Falafel crip')
lbl5.place(x=150,y=250)
box5 = customtkinter.CTkOptionMenu(c,values=['1','2','3','4','5'])
box5.place(x=235,y=250)
en6 = customtkinter.CTkComboBox(c,values=['Small','Meduim','large'])
en6.place(x=1,y=300)
lbl6 = customtkinter.CTkLabel(c,text='Garlic sauce')
lbl6.place(x=150,y=300)
box6 = customtkinter.CTkOptionMenu(c,values=['1','2','3','4','5'])
box6.place(x=235,y=300)

#TExtbox:
txt = customtkinter.CTkTextbox(c,height=800)
txt.place(x=700,y=1)
txt.insert('end','\t WELCOME')
txt.insert('end','\n\n --------------------------------------------')
def g():

    if en0.get()== 'Small':
        txt.delete('0.0', 'end')
        txt.insert('end', '\t WELCOME')
        txt.insert('end', '\n\n --------------------------------------------')
        txt.insert('end', '\n\n Fries Roll')
        txt.insert('end','\t\t Small')
        txt.insert('end','\n\n Number:'+'\t\t'+box.get())
        if box.get()=='1':
            txt.insert('end','\n\n Price: \t\t 15')
        if box.get()=='2':
            txt.insert('end','\n\n Price: \t\t 30')
        if box.get()=='3':
            txt.insert('end','\n\n Price: \t\t 45')
        if box.get()=='4':
            txt.insert('end','\n\n Price: \t\t 60')
        if box.get() == '5':
            txt.insert('end','\n\n Price: \t\t 75')


    if en0.get() == "Meduim":
        txt.delete('0.0', 'end')
        txt.insert('end', '\t WELCOME')
        txt.insert('end', '\n\n --------------------------------------------')
        txt.insert('end', '\n\n Fries Roll')
        txt.insert('end', '\t\t Medium')

        if box.get() == '1':
            txt.insert('end', '\n\n Price: \t\t 25')
        if box.get() == '2':
            txt.insert('end', '\n\n Price: \t\t 50')
        if box.get() == '3':
            txt.insert('end', '\n\n Price: \t\t 75')
        if box.get() == '4':
            txt.insert('end', '\n\n Price: \t\t 100')
        if box.get() == '5':
            txt.insert('end', '\n\n Price: \t\t 125')
    if en0.get() == 'large':
        txt.delete('0.0', 'end')
        txt.insert('end', '\t WELCOME')
        txt.insert('end', '\n\n -------------------')
        txt.insert('end', '\n\n Fries Roll')
        txt.insert('end', '\t\t Large')

        if box.get() == '1':
            txt.insert('end', '\n\n Price: \t\t 40')
        if box.get() == '2':
            txt.insert('end', '\n\n Price: \t\t 80')
        if box.get() == '3':
            txt.insert('end', '\n\n Price: \t\t 120')
        if box.get() == '4':
            txt.insert('end', '\n\n Price: \t\t 160')
        if box.get() == '5':
            txt.insert('end', '\n\n Price: \t\t 200')
    #fries cripe


def fricrip():
    if en1.get() == 'Small':

        txt.insert('end', '\n\n Fries crip')
        txt.insert('end', 'size: \t\t Small')
        txt.insert('end', '\n\n Number:' + '\t\t' + box1.get())
        if box1.get() == '1':
            txt.insert('end', '\n\n Price: \t\t 20')
        if box1.get() == '2':
            txt.insert('end', '\n\n Price: \t\t 40')
        if box1.get() == '3':
            txt.insert('end', '\n\n Price: \t\t 60')
        if box1.get() == '4':
            txt.insert('end', '\n\n Price: \t\t 80')
        if box1.get() == '5':
            txt.insert('end', '\n\n Price: \t\t 100')

    if en1.get() == "Meduim":


        txt.insert('end', '\n\n Number:' + '\t\t' + box1.get())
        txt.insert('end', '\n\n Fries crip')
        txt.insert('end', 'size: \t\t Medium')

        if box1.get() == '1':
            txt.insert('end', '\n\n Price: \t\t 25')
        if box1.get() == '2':
            txt.insert('end', '\n\n Price: \t\t 50')
        if box1.get() == '3':
            txt.insert('end', '\n\n Price: \t\t 75')
        if box1.get() == '4':
            txt.insert('end', '\n\n Price: \t\t 100')
        if box1.get() == '5':
            txt.insert('end', '\n\n Price: \t\t 125')
    if en1.get() == 'large':
        txt.insert('end', '\n\n Fries crip')
        txt.insert('end', '\n\n Number:' + '\t\t' + box1.get())
        txt.insert('end', 'size : \t\t Large')

        if box1.get() == '1':
            txt.insert('end', '\n\n Price: \t\t 40')
        if box1.get() == '2':
            txt.insert('end', '\n\n Price: \t\t 80')
        if box1.get() == '3':
            txt.insert('end', '\n\n Price: \t\t 120')
        if box1.get() == '4':
            txt.insert('end', '\n\n Price: \t\t 160')
        if box1.get() == '5':
            txt.insert('end', '\n\n Price: \t\t 200')

def shaeroll():
    if en2.get() == 'Small':

        txt.insert('end', '\n\n name:\t\tshwrma roll')
        txt.insert('end', '\n\n size: \t\t Small')
        txt.insert('end', '\n\n Number:' + '\t\t' + box2.get())
        if box2.get() == '1':
            txt.insert('end', '\n\n Price: \t\t 20')
        if box2.get() == '2':
            txt.insert('end', '\n\n Price: \t\t 40')
        if box2.get() == '3':
            txt.insert('end', '\n\n Price: \t\t 60')
        if box2.get() == '4':
            txt.insert('end', '\n\n Price: \t\t 80')
        if box2.get() == '5':
            txt.insert('end', '\n\n Price: \t\t 100')

    if en2.get() == "Meduim":
        txt.insert('end','\n\n name: \t\t shwrmaroll')
        txt.insert('end', '\n\n Number:' + '\t\t' + box2.get())
        txt.insert('end', '\n\n size: \t\t Medium')

        if box2.get() == '1':
            txt.insert('end', '\n\n Price: \t\t 25')
        if box2.get() == '2':
            txt.insert('end', '\n\n Price: \t\t 50')
        if box2.get() == '3':
            txt.insert('end', '\n\n Price: \t\t 75')
        if box2.get() == '4':
            txt.insert('end', '\n\n Price: \t\t 100')
        if box2.get() == '5':
            txt.insert('end', '\n\n Price: \t\t 125')
    if en2.get() == 'large':
        txt.insert('end', '\n\n name: \t\t shawerma roll ')
        txt.insert('end', '\n\n Number:' + '\t\t' + box2.get())
        txt.insert('end', '\n\n size : \t\t Large')

        if box2.get() == '1':
            txt.insert('end', '\n\n Price: \t\t 40')
        if box2.get() == '2':
            txt.insert('end', '\n\n Price: \t\t 80')
        if box2.get() == '3':
            txt.insert('end', '\n\n Price: \t\t 120')
        if box2.get() == '4':
            txt.insert('end', '\n\n Price: \t\t 160')
        if box2.get() == '5':
            txt.insert('end', '\n\n Price: \t\t 200')
def shcr():
    if en3.get() == 'Small':

        txt.insert('end', '\n\n name:\t\tshwrma crip')
        txt.insert('end', '\n\n size: \t\t Small')
        txt.insert('end', '\n\n Number:' + '\t\t' + box3.get())
        if box3.get() == '1':
            txt.insert('end', '\n\n Price: \t\t 25')
        if box3.get() == '2':
            txt.insert('end', '\n\n Price: \t\t 50')
        if box3.get() == '3':
            txt.insert('end', '\n\n Price: \t\t 75')
        if box3.get() == '4':
            txt.insert('end', '\n\n Price: \t\t 100')
        if box3.get() == '5':
            txt.insert('end', '\n\n Price: \t\t 125')

    if en3.get() == "Meduim":
        txt.insert('end', '\n\n name: \t\t shwrmacrip')
        txt.insert('end', '\n\n Number:' + '\t\t' + box3.get())
        txt.insert('end', '\n\n size: \t\t Medium')

        if box3.get() == '1':
            txt.insert('end', '\n\n Price: \t\t 30')
        if box3.get() == '2':
            txt.insert('end', '\n\n Price: \t\t 60')
        if box3.get() == '3':
            txt.insert('end', '\n\n Price: \t\t 90')
        if box3.get() == '4':
            txt.insert('end', '\n\n Price: \t\t 120')
        if box3.get() == '5':
            txt.insert('end', '\n\n Price: \t\t 150')
    if en3.get() == 'large':
        txt.insert('end', '\n\n name: \t\t shwrmacrip ')
        txt.insert('end', '\n\n Number:' + '\t\t' + box3.get())
        txt.insert('end', '\n\n size : \t\t Large')

        if box3.get() == '1':
            txt.insert('end', '\n\n Price: \t\t 40')
        if box3.get() == '2':
            txt.insert('end', '\n\n Price: \t\t 80')
        if box3.get() == '3':
            txt.insert('end', '\n\n Price: \t\t 120')
        if box3.get() == '4':
            txt.insert('end', '\n\n Price: \t\t 160')
        if box3.get() == '5':
            txt.insert('end', '\n\n Price: \t\t 200')
def falrol():
    if en4.get() == 'Small':

        txt.insert('end', '\n\n name:\t\tfalroll')
        txt.insert('end', '\n\n size: \t\t Small')
        txt.insert('end', '\n\n Number:' + '\t\t' + box4.get())
        if box4.get() == '1':
            txt.insert('end', '\n\n Price: \t\t 25')
        if box4.get() == '2':
            txt.insert('end', '\n\n Price: \t\t 50')
        if box4.get() == '3':
            txt.insert('end', '\n\n Price: \t\t 75')
        if box4.get() == '4':
            txt.insert('end', '\n\n Price: \t\t 100')
        if box4.get() == '5':
            txt.insert('end', '\n\n Price: \t\t 125')

    if en4.get() == "Meduim":
        txt.insert('end', '\n\n name: \t\t falroll')
        txt.insert('end', '\n\n Number:' + '\t\t' + box4.get())
        txt.insert('end', '\n\n size: \t\t Medium')

        if box4.get() == '1':
            txt.insert('end', '\n\n Price: \t\t 30')
        if box4.get() == '2':
            txt.insert('end', '\n\n Price: \t\t 60')
        if box4.get() == '3':
            txt.insert('end', '\n\n Price: \t\t 90')
        if box4.get() == '4':
            txt.insert('end', '\n\n Price: \t\t 120')
        if box4.get() == '5':
            txt.insert('end', '\n\n Price: \t\t 150')
    if en4.get() == 'large':
        txt.insert('end', '\n\n name: \t\t falroll ')
        txt.insert('end', '\n\n Number:' + '\t\t' + box4.get())
        txt.insert('end', '\n\n size : \t\t Large')

        if box4.get() == '1':
            txt.insert('end', '\n\n Price: \t\t 40')
        if box4.get() == '2':
            txt.insert('end', '\n\n Price: \t\t 80')
        if box4.get() == '3':
            txt.insert('end', '\n\n Price: \t\t 120')
        if box4.get() == '4':
            txt.insert('end', '\n\n Price: \t\t 160')
        if box4.get() == '5':
            txt.insert('end', '\n\n Price: \t\t 200')
def falcrip():
    if en5.get() == 'Small':

        txt.insert('end', '\n\n name:\t\tfalcrip')
        txt.insert('end', '\n\n size: \t\t Small')
        txt.insert('end', '\n\n Number:' + '\t\t' + box5.get())
        if box5.get() == '1':
            txt.insert('end', '\n\n Price: \t\t 25')
        if box5.get() == '2':
            txt.insert('end', '\n\n Price: \t\t 50')
        if box5.get() == '3':
            txt.insert('end', '\n\n Price: \t\t 75')
        if box5.get() == '4':
            txt.insert('end', '\n\n Price: \t\t 100')
        if box5.get() == '5':
            txt.insert('end', '\n\n Price: \t\t 125')

    if en5.get() == "Meduim":
        txt.insert('end', '\n\n name: \t\t falcrip')
        txt.insert('end', '\n\n Number:' + '\t\t' + box5.get())
        txt.insert('end', '\n\n size: \t\t Medium')

        if box5.get() == '1':
            txt.insert('end', '\n\n Price: \t\t 30')
        if box5.get() == '2':
            txt.insert('end', '\n\n Price: \t\t 60')
        if box5.get() == '3':
            txt.insert('end', '\n\n Price: \t\t 90')
        if box5.get() == '4':
            txt.insert('end', '\n\n Price: \t\t 120')
        if box5.get() == '5':
            txt.insert('end', '\n\n Price: \t\t 150')
    if en5.get() == 'large':
        txt.insert('end', '\n\n name: \t\t falroll ')
        txt.insert('end', '\n\n Number:' + '\t\t' + box5.get())
        txt.insert('end', '\n\n size : \t\t Large')

        if box5.get() == '1':
            txt.insert('end', '\n\n Price: \t\t 40')
        if box5.get() == '2':
            txt.insert('end', '\n\n Price: \t\t 80')
        if box5.get() == '3':
            txt.insert('end', '\n\n Price: \t\t 120')
        if box5.get() == '4':
            txt.insert('end', '\n\n Price: \t\t 160')
        if box5.get() == '5':
            txt.insert('end', '\n\n Price: \t\t 200')
def garlic():
    if en6.get() == 'Small':

        txt.insert('end', '\n\n name:\t\tgarlic')
        txt.insert('end', '\n\n size: \t\t Small')
        txt.insert('end', '\n\n Number:' + '\t\t' + box6.get())
        if box6.get() == '1':
            txt.insert('end', '\n\n Price: \t\t 5')
        if box6.get() == '2':
            txt.insert('end', '\n\n Price: \t\t 10')
        if box6.get() == '3':
            txt.insert('end', '\n\n Price: \t\t 15')
        if box6.get() == '4':
            txt.insert('end', '\n\n Price: \t\t 20')
        if box6.get() == '5':
            txt.insert('end', '\n\n Price: \t\t 25')

    if en6.get() == "Meduim":
        txt.insert('end', '\n\n name: \t\t garlic')
        txt.insert('end', '\n\n Number:' + '\t\t' + box6.get())
        txt.insert('end', '\n\n size: \t\t Medium')

        if box6.get() == '1':
            txt.insert('end', '\n\n Price: \t\t 10')
        if box6.get() == '2':
            txt.insert('end', '\n\n Price: \t\t 20')
        if box6.get() == '3':
            txt.insert('end', '\n\n Price: \t\t 30')
        if box6.get() == '4':
            txt.insert('end', '\n\n Price: \t\t 40')
        if box6.get() == '5':
            txt.insert('end', '\n\n Price: \t\t 50')
    if en6.get() == 'large':
        txt.insert('end', '\n\n name: \t\t garlic ')
        txt.insert('end', '\n\n Number:' + '\t\t' + box6.get())
        txt.insert('end', '\n\n size : \t\t Large')

        if box6.get() == '1':
            txt.insert('end', '\n\n Price: \t\t 20')
        if box6.get() == '2':
            txt.insert('end', '\n\n Price: \t\t 40')
        if box6.get() == '3':
            txt.insert('end', '\n\n Price: \t\t 60')
        if box6.get() == '4':
            txt.insert('end', '\n\n Price: \t\t 80')
        if box6.get() == '5':
            txt.insert('end', '\n\n Price: \t\t 100')
#-------------------------BUTTONS of submit:  --------------------------
buttv = customtkinter.CTkButton(c,command=g,text='submit')
buttv.place(x=350,y=5)
crip = customtkinter.CTkButton(c,text='submit',command=fricrip)
crip.place(x=350,y=60)
shaee = customtkinter.CTkButton(c,text='submit',command=shaeroll)
shaee.place(x=385,y=105)
shaeecr = customtkinter.CTkButton(c,text='submit',command=shcr)
shaeecr.place(x=385,y=150)
fal = customtkinter.CTkButton(c,text='submit',command=falrol)
fal.place(x=385,y=207)
falcr = customtkinter.CTkButton(c,text='submit',command=falcrip)
falcr.place(x=385,y=250)
grl = customtkinter.CTkButton(c,text='submit',command=garlic)
grl.place(x=385,y=300)
def gh ():
    d = txt.get('1.0','end-1c')

    filename = tempfile.mktemp('.txt')
    open(filename,'w').write(d)
    os.startfile(filename,'print')
def xd ():
    messagebox.showinfo('welcome','welcome to the program')
xd()
def g():
    txt.delete('0.0', 'end')
clear = customtkinter.CTkButton(c,text='clear',command=g)
clear.place(x=730,y=405)
burs = customtkinter.CTkButton(c,command=gh,text='print')
burs.place(x=730,y=440)


if __name__ == "__main__":
    c.mainloop()
#--------------------------------------WITH LOVE OF THE EMARY------------------------------------