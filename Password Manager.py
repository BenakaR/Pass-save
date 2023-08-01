import os
import time as tm
import random
import pickle as pk
import tkinter as tk
import tkinter.messagebox
from tkinter import scrolledtext

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
LogP=""
pass_len=int(0)

if (os.path.isfile("./data.svf")):
    f=open("data.svf",'rb')
    temp_dat=pk.load(f)
    f.close()
    t=temp_dat["__1"]
    LogP=LogP+t[0]
    pass_len=int(t[1])
else:
    chk=tk.Tk(screenName="new", baseName="Hello", className="iPass")
    chk.geometry('300x250+600+200')
    def check(event=None):
        if e1.get() == e2.get() and not e1.get()=="":
            f=open("data.svf",'wb')
            global LogP,pass_len
            LogP=e1.get()
            pass_len=16
            temp_dat={"__1":[LogP,pass_len]}
            pk.dump(temp_dat,f)
            f.close()            
            chk.destroy()
        else:
            tkinter.messagebox.showinfo("ERROR", "Password does not match.")
            e2.delete( 0 , 'end' )
    l=tk.Label( chk , height=1, text="Enter New Password:", borderwidth=1, font=("Tahoma" , 12), foreground="black", relief="flat")
    l.pack(fill='both')
    e1=tk.Entry(chk,font=("Tahoma",13,'bold'),show="•")
    e1.pack(fill='both', padx=20 , pady=20)
    l=tk.Label( chk , height=1, text="Confirm Password:" , borderwidth=1, font=("Tahoma", 12), foreground="black", relief="flat")
    l.pack(fill='both')
    e2=tk.Entry( chk , font=("Tahoma", 13))
    e2.pack(fill='both', padx=20 , pady=20)
    b=tk.Button( chk , text='SAVE', command=check, width=25, font=("Trebuchet MS", 13 , 'bold'), background="#0066ff", foreground="white", activeforeground="white", activebackground="#3311ff", relief="flat")
    b.pack(fill='both',padx=5)
    chk.bind( "<Return>" , check )
    chk.mainloop()

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Flag=False
log=tk.Tk(screenName="iLogin", baseName="Hello", className="iPass")
log.geometry('300x170+600+200')

def check(event=None):
    temp=e.get()
    if temp==LogP and not LogP=="":
        global Flag
        Flag=True
        log.destroy()

l=tk.Label( log , height=2 , text="Enter Password To Login:", borderwidth=1, font=("Tahoma", 12), foreground="black", relief="flat")
l.pack(fill='both')
e=tk.Entry( log , font=("Tahoma",16,'bold'), show="•")
e.pack(fill='both', padx=20, pady=20)
b=tk.Button( log , text='LOGIN', command=check , width=25, font=("Trebuchet MS", 14), background="#0066ff", foreground="white", activeforeground="white", activebackground="#3311ff", relief="flat")
b.pack(fill='both' , padx=10)
log.bind( "<Return>" , check )

log.mainloop()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

if Flag==False:
    exit()

scr=tk.Tk(screenName="iPass", baseName="Hello", className="iPass")
scr.geometry('600x600+500+100')

data={}
dd={}

def sure():
    win=tk.Toplevel()
    win.geometry('250x150+700+300')

    def inserts():
        t1=text1.get()
        t2=text2.get()
        t3=text3.get()
        global data
        temp_dat={t1:{t2:t3}}
        data.update(temp_dat)
        write_data()
        display()
        clear_text()
        win.destroy()
    def cls():
        text1.delete(0,'end')
        win.destroy()
    
    l=tk.Label( win , height=2, text="Are You Sure You \n Want To Rewrite?", borderwidth=1, font=("Tahoma", 12), background="white", foreground="black", relief="flat")
    l.place( relheight=0.5, relwidth=1, rely=0, relx=0)

    b1=tk.Button( win , text='Yes', command=inserts , font=("Trebuchet MS", 13, 'bold'), background="#0066ff", foreground="white", activeforeground="white", activebackground="#3311ff", relief="flat")
    b1.place( relheight=0.3, relwidth=0.4, rely=0.5, relx=0.07)
    b2=tk.Button( win , text='No', command=cls , font=("Trebuchet MS", 13, 'bold'), background="#0066ff", foreground="white", activeforeground="white", activebackground="#3311ff", relief="flat")
    b2.place( relheight=0.3, relwidth=0.4, rely=0.5, relx=0.53)

def Rand_Password():
    text3.delete(0,'end')
    rand_pass=""
    while(True):
        t=tm.time()
        tt=(((t*100)%1)*10000)//1
        random.seed(tt)
        rand_pass=""
        a=b=c=d=False
        upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower="abcdefghijklmnopqrstuvwxyz"
        num="0123456789"
        char="!#$&*,-./:;?@_"
        universal="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$&*,-./:;?@_"
        for i in range(pass_len):
            ch=random.choice(universal)
            rand_pass = rand_pass + ch
        for i in rand_pass:
            if i in upper:
                a=True
            if i in lower:
                b=True
            if i in num:
                c=True
            if i in char:
                d=True
        if a and b and c and d:
            break
    text3.insert(0,rand_pass)

def insert_entry():
    t1=text1.get()
    t2=text2.get()
    t3=text3.get()
    global data
    if t1=="__1":
        return
    if (not t1) or (not t2) or (not t3) == True:
        return
    if t1 in data:
        sure()
        return
    td={t1:{t2:t3}}
    data.update(td)
    write_data()
    display()
    clear_text()

def delete_entry():
    t1=text1.get()
    t2=text2.get()
    t3=text3.get()
    td={t2:t3}
    global data
    if t1=="__1":
        clear_text()
        return
    if t1 in data:
        if data[t1]==td:
            data.pop(t1)
    write_data()
    display()
    clear_text()

def clear_text():
    text1.delete(0,'end')
    text2.delete(0,'end')
    text3.delete(0,'end')

def write_data():
    f=open("data.svf",'wb')
    global data
    pk.dump(data,f)
    f.close()

def read_data():
    f=open("data.svf",'rb')
    global data
    data=pk.load(f)
    f.close()

def display():
    global data
    string=''
    for key in data:
        if key=="__1":
            continue
        temp=data[key]
        for k_key in temp:
            string = string + "\nWebsite : " + key + "\n     Username : " + k_key + ' , Password : ' + temp[k_key]
    l = scrolledtext.ScrolledText( scr , font=("Tahoma", 12))
    l.insert(1.0,string)
    l.configure( state = "disabled" )
    l.place ( height= -130 , relheight=1 , border="outside" , relx=0.005 , relwidth=0.99 , y=130)

def PassL(key):
    global pass_len,LogP,data
    pass_len=key
    f=open("data.svf",'wb')
    temp_dat={"__1":[LogP,pass_len]}
    data.update(temp_dat)
    pk.dump(data,f)
    f.close()

def Change():
    chk=tk.Toplevel(master=scr)
    chk.geometry('300x350+600+200')
    def chck():
        if entry2.get() == entry3.get() and not entry2.get()=="":
            f=open("data.svf",'wb')
            global LogP,data,pass_len
            LogP=entry2.get()
            temp_dat={"__1":[LogP,pass_len]}
            data.update(temp_dat)
            pk.dump(data,f)
            f.close()
            tkinter.messagebox.showinfo("SUCCESS", "Password changed Successfully!")
            chk.destroy()
        else:
            tkinter.messagebox.showinfo("ERROR", "Passwords does not match or empty password.")
            entry3.delete(0,'end')
    def check(event=None):
        global data
        tmp=data["__1"]
        if entry1.get()==tmp[0]:
            chck()
        else:
            tkinter.messagebox.showinfo("ERROR", "Previous Password is incorrect.")
            entry1.delete( 0 , 'end' )
    l=tk.Label( chk, height=1, text="Enter Previous Password:", borderwidth=1, font=("Tahoma", 12), foreground="black", relief="flat")
    l.pack(fill='both')
    entry1=tk.Entry(chk,font=("Tahoma",13,'bold'),show="•")
    entry1.pack(fill='both',padx=20,pady=20)
    l=tk.Label( chk , height=1 , text="Enter New Password:" , borderwidth=1, font=("Tahoma", 12), foreground="black", relief="flat")
    l.pack( fill='both' )
    entry2=tk.Entry( chk , font=("Tahoma", 13, 'bold') , show="•")
    entry2.pack( fill='both', padx=20, pady=20)
    l=tk.Label( chk , height=1, text="Confirm Password:" , borderwidth=1 , font=("Tahoma", 12), foreground="black", relief="flat")
    l.pack( fill='both' )
    entry3=tk.Entry(chk,font=("Tahoma",13))
    entry3.pack( fill='both', padx=20, pady=20 )
    b=tk.Button( chk , text='SAVE', command=check, width=25, font=("Trebuchet MS", 13, 'bold'), background="#0066ff", foreground="white", activeforeground="white", activebackground="#3311ff", relief="flat")
    b.pack( fill='both', padx=10)
    chk.bind( "<Return>" , check )

    # Causes the second window to be centered in the parent window amongst other things like: if the parent window gets minimized, the second window will get minimized too.
    chk.transient(scr)
    # In some cases, updating idle tasks is required before doing a grab_set(). Without it, it may show an exception when attempting to use grab_set()
    chk.update_idletasks()
    # Causes the second window to be on top of the parent window, and it won't allow any interaction with the parent window.
    chk.grab_set()
    # Waits for Toplevel to close
    chk.wait_window(chk)

    chk.mainloop()

def DEL_ALL():
    w=tk.Toplevel()
    w.geometry('250x150+700+300')

    def yes():
        os.remove("./data.svf")
        scr.destroy()
    def no():
        w.destroy()
    
    l=tk.Label( w , height = 2, text = "Are you sure you want to\ndelete all data from program?", borderwidth = 1 , font=("Tahoma", 12), background="white", foreground="black", relief="flat")
    l.place( relheight=0.5, relwidth=1, rely=0, relx=0)

    b1=tk.Button( w , text='Yes' , command = yes , font = ("Trebuchet MS", 13, 'bold'), background="#0066ff", foreground="white", activeforeground="white", activebackground="#3311ff", relief="flat")
    b1.place( relheight=0.3,relwidth=0.4,rely=0.5,relx=0.07)
    b2=tk.Button( w , text='No' , command = no , font = ("Trebuchet MS", 13, 'bold'), background="#0066ff", foreground="white", activeforeground="white", activebackground="#3311ff", relief="flat")
    b2.place( relheight=0.3, relwidth=0.4, rely=0.5, relx=0.53)
    

l=tk.Label( scr, text="Website :", width=25, borderwidth=1, anchor='w', justify='left', font=("Tahoma", 12), background="white", foreground="black", relief="flat")
l.place( height=30, relwidth=0.5, relx=0, y=0 )
l=tk.Label( scr, text="Username :", width=25, borderwidth=1, anchor='w', justify='left', font=("Tahoma", 12), background="white", foreground="black", relief="flat")
l.place( height=30, relwidth=0.5, relx=0, y=30 )
l=tk.Label( scr, text="Password :", width=25, borderwidth=1, anchor='w', justify='left', font=("Tahoma", 12), background="white", foreground="black", relief="flat")
l.place( height=30, relwidth=0.5, relx=0, y=60 )

text1=tk.Entry( scr , font=("Tahoma", 12))
text1.place( height=30, relwidth=0.5, relx=0.5, y=0 )
text2=tk.Entry( scr , font=("Tahoma", 12))
text2.place( height=30, relwidth=0.5, relx=0.5, y=30 )
text3=tk.Entry( scr , font=("Tahoma", 12))
text3.place( height=30, relwidth=0.5, relx=0.5, y=60 )

b=tk.Button(scr, text ="Add", command=insert_entry, width=25, font=("Trebuchet MS", 13, 'bold'), background="#0066ff", foreground="white", activeforeground="white", activebackground="#3311ff", relief="flat")
b.place(height=40, relwidth=0.245, relx=0.005, y=90 )
b=tk.Button(scr, text ="Randomize Password", command=Rand_Password, width=25, font=("Trebuchet MS", 13, 'bold'), background="#0066ff", foreground="white", activeforeground="white", activebackground="#3311ff", relief="flat")
b.place(height=40, relwidth=0.49, relx=0.2525, y=90 )
b=tk.Button(scr, text ="Remove", command=delete_entry, width=25, font=("Trebuchet MS", 13, 'bold'), background="#0066ff", foreground="white", activeforeground="white", activebackground="#3311ff", relief="flat")
b.place(height=40, relwidth=0.245, relx=0.745, y=90 )

menubar = tk.Menu(scr)
file = tk.Menu(menubar, tearoff = 0)
edit = tk.Menu(menubar, tearoff = 0)
PassLen = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
menubar.add_cascade(label ='Edit', menu = edit)
edit.add_command(label ='Change Login Password', command = Change)
edit.add_separator()
edit.add_command(label ='Delete All Passwords', command = DEL_ALL)
edit.add_separator()
edit.add_cascade(label = 'Random Password Length', menu=PassLen )
PassLen.add_command(label=' 8',command=lambda:PassL(8))
PassLen.add_command(label='10',command=lambda:PassL(10))
PassLen.add_command(label='12',command=lambda:PassL(12))
PassLen.add_command(label='14',command=lambda:PassL(14))
PassLen.add_command(label='16',command=lambda:PassL(16))
PassLen.add_command(label='24',command=lambda:PassL(24))
PassLen.add_command(label='32',command=lambda:PassL(32))
PassLen.add_command(label='64',command=lambda:PassL(64))
file.add_command(label ='Exit', command = scr.destroy)
scr.config(menu = menubar)

read_data()
display()
scr.mainloop()
