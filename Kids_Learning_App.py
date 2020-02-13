from functools import *
from tkinter import *
from tkinter import messagebox
import random
import sqlite3


mW=Tk()
mW.title('Mnimi : Kids Learnig Program')
mW.geometry('1200x650')
mW.configure(bg="#a6a6a6")
frame_option=Frame(mW)
frame_option.pack()

def imageguess():
    frame_option.destroy()
    framea=Frame(mW, bg="red")
    framea.pack(side=TOP, fill=X)
    frameb=Frame(mW, bg="skyblue")
    frameb.pack(side=TOP, fill=X)

    def superhero():
        frameb.destroy()

        def clr():
            frameb.destroy()
            ani.destroy()
            butt.destroy()
            superhero()

        ani=Frame(mW, bg="#a6a6a6")
        ani.pack(side=TOP, fill=X)
        butt=Frame(mW, bg="#a6a6a6")
        butt.pack(side=TOP, fill=X)
        flo=Frame(mW, bg="yellow")
        flo.pack(side=TOP)
        g=["Captain America","Thor Odinson","Superman","The Arrow","The Flash","Ironman"]


        def check(inp):

            if name==inp:
                messagebox.showinfo("Message","Correct Answer!")
                clr()

            else:
                messagebox.showinfo("Message","Incorrect Answer!")




        name=random.choice(g)

        lab=Label(ani,width=700,height=350)
        img_loc="D:\\H\\Notes\\Python\\project\\hsr\\resources\\"+name+".png"
        lab.img=PhotoImage(file=img_loc)
        lab["image"]=lab.img
        lab.pack()

        p="Captain America"
        but=Button(butt,text=p,font="calibri 18 bold italic",bg="red",fg="white",bd=5,width=15,command=partial(check,p))
        q="The Flash"
        but2=Button(butt,text=q,font="calibri 18 bold italic",bg="red",fg="white",bd=5,width=10,command=partial(check,q))
        r="The Arrow"
        but3=Button(butt,text=r,font="calibri 18 bold italic",bg="red",fg="white",bd=5,width=10,command=partial(check,r))
        s="Ironman"
        but6=Button(butt,text=s,font="calibri 18 bold italic",bg="red",fg="white",bd=5,width=10,command=partial(check,s))
        t="Thor Odinson"
        but4=Button(butt,text=t,font="calibri 18 bold italic",bg="red",fg="white",bd=5,width=10,command=partial(check,t))
        u="Superman"
        but5=Button(butt,text=u,font="calibri 18 bold italic",bg="red",fg="white",bd=5,width=10,command=partial(check,u))
        but.pack(side=LEFT,padx=9)
        but2.pack(side=LEFT,padx=9)
        but3.pack(side=LEFT,padx=9)
        but4.pack(side=LEFT,padx=9)
        but5.pack(side=LEFT,padx=9)
        but6.pack(side=LEFT,padx=9)

    checkbox=Checkbutton(frameb,text="Super Heroes Quiz",bg="grey",font="calibri 40 bold italic",width=20,bd=6,fg="black",relief=RIDGE,command=superhero)
    checkbox.pack(side=TOP)


def start_the_game():
    frame_option.destroy()
    def cmr():
        fr.destroy()
        framea1.destroy()
        mainer.destroy()
    def check1(valt):
        a=valt
        b=str(val[pos])
        print('a is ',a,type(a))
        print('b is ',b,type(b))
        if(a==b):
            messagebox.showinfo("Message","Correct Answer!")
            buf.destroy()
            fr.destroy()
            clr1()
            start_the_game()
        else:
            messagebox.showinfo("Message","Incorrect Answer!")
    def clr1():
        frame.destroy()
        frame1.destroy()
        frame4.destroy()
    clr1()
    li=["Five","Six","Seven","One","Two","Three","Four","Eight","Nine"]
    val=[5,6,7,1,2,3,4,8,9]
    copy_of_val=val[:]
    m=random.choice(li)
    pos=li.index(m)
    print(pos,li[pos],val[pos])
    fr=Frame(mW,bg='black')
    fr.pack()
    la=Label(fr,text=m,bg="black",fg="#80d9ff",width=6,font=("calibri",80,"bold"),bd=3,relief=RAISED)
    la.pack(pady=30)
    mainer=Frame(mW)
    mainer.pack()
    framea1=Frame(mainer)
    framea1.pack(fill=X)
    finlist=[]
    for i in range(7):
        b=random.choice(copy_of_val)
        finlist.append(b)
        copy_of_val.remove(b)
    #print(finlist)
    #print(copy_of_val)
    if (val[pos] in finlist):
        finlist.remove(val[pos])
    finlist.append(val[pos])
    bu=[]
    buf=Frame(mW)
    buf.pack()
    for i in range(len(finlist)):
        for j in range(len(finlist)):
            p1=random.choice(finlist)
            finlist.remove(p1)
            bu.append(Button(buf,text=str(p1),font=('calibri',30,'bold'),bd=5,relief=RAISED,bg='white',command=partial(check1,str(p1))))
            bu[-1].pack(side=LEFT,padx=20,pady=20)


def option():
    frame4.destroy()
    frame3.destroy()
    frame1.destroy()
    frame.destroy()

    instruction = Label(frame_option, text='Select the desired category below \n', font=("Times New Roman", 25))
    instruction.pack(side=TOP)

    Frame_empty1=Label(frame_option,height=3,bg='#a6a6a6')
    Frame_empty1.pack(fill=X)
    
    b2=Button(frame_option,text="Pictures",bg="grey",fg="black",bd=5,font=("calibri",30,"bold"),width=20,relief=RAISED,command=imageguess)
    b2.pack()

    Frame_empty1=Label(frame_option,height=3,bg='#a6a6a6')
    Frame_empty1.pack(fill=X)
    
    b3=Button(frame_option,text="Numbers",bg="grey",fg="black",bd=5,relief=RAISED,width=20,font=("calibri",30,"bold"),command=start_the_game)
    b3.pack()
    

def Game():
    e_name=entry_1.get()
    e_pass=entry_2.get()
    found=False
    con=sqlite3.connect('game.db')
    c=con.execute("select * from sign_up")
    for x in c:
        if(e_name==x[0] and e_pass==x[1]):
            found=True
            break
        else:
            found=False
    con.commit()

    if (found==True and (entry_1.get()!="" and entry_2.get()!='')):
        b.destroy()
        option()
    else:
        messagebox.showinfo("Message", "Account doesn't exist")


frame3=Frame(mW,bg="#a6a6a6")
frame3.pack(fill=X)
Frame_label=Label(frame3, text="Mnimi : Kids Learnig Program",bg="#f7f7f7",fg="#ff6600",font=("Auto Mode",35))
Frame_label.pack()

Frame_empty=Label(frame3,height=3,bg='#a6a6a6')
Frame_empty.pack(fill=X)

Frame_n=Label(frame3,text="Detect the Object",bg="#f7f7f7",fg="#662900",font=("Comic Sans MS",34))
Frame_n.pack(fill=X)

Frame_empty1=Label(frame3,height=3,bg='#a6a6a6')
Frame_empty1.pack(fill=X)

frame=Frame(mW,bg='#a6a6a6',height=200)
frame.pack(pady=30)
label_1=Label(frame,text=" Username  ",fg="black",bg="#a6a6a6",font=("calibri",30,"bold"),bd=4)
entry_1=Entry(frame,bg="white",fg="black",font=("calibri",25))
label_1.pack(side=LEFT,fill=X)
entry_1.pack(side=LEFT,padx=16)

frame1=Frame(mW,bg='#a6a6a6')
frame1.pack(pady=30)
label_2=Label(frame1,text="Password   ",fg="black",bg="#a6a6a6",font=("calibri",30,"bold"),bd=4)
entry_2=Entry(frame1,bg="white",fg="black",font=("calibri",25), show='*')
label_2.pack(side=LEFT,fill=X)
entry_2.pack(side=LEFT,padx=14)




frame4=Frame(mW,bg='#a6a6a6')
frame4.pack()
button=Button(frame4,text="Login",bg="#00004d",fg="white",bd=5,font=("calibri",20),relief=RIDGE,command=Game)
button.pack(side=LEFT,pady=10)


def sign_up():
    win=Tk()
    win.title('Sign up')
    win.geometry('550x350')
    win.configure(bg='#3333ff')
    
    def save_data():
        print('Database created')
        password=pass_entry.get()
        name=name_entry.get()
        passwordC=pass_entryC.get()
        
        if(name=='' or password=='' or passwordC==''):
            message=messagebox.showinfo('Message','Entry fields cannot be empty!')
        elif(password==passwordC):
            con=sqlite3.connect('game.db')
            #con.execute("create table sign_up(username varchar(50),password varchar(50));")
            #print('Table created')
            con.execute("insert into sign_up(username,password)values(?,?)",(name,password))
            con.commit()
            win.destroy()
            message=messagebox.showinfo('Message','Account created!')
        else:
            message=messagebox.showinfo("Sign Up unsuccessful ", "Passcodes does not match. \n   Try again.")
            pass_entry.delete(first=0, last=END)
            pass_entryC.delete(first=0, last=END)    
    
    
    name_label=Label(win,text=' Username          ',fg='white',font=('calibri',15,'bold'),bg='#3333ff',padx=10,pady=5)
    name_label.place(x=50,y=50)
    name_entry=Entry(win,font=('calibri',18,'bold'))
    name_entry.place(x=155,y=50)
    
    pass_label=Label(win,text=' Password          ',fg='white',font=('calibri',15,'bold'),bg='#3333ff',padx=10,pady=5)
    pass_label.place(x=50,y=100)
    pass_entry=Entry(win,font=('calibri',18,'bold'),show='*')
    pass_entry.place(x=155,y=100)

    pass_labelC=Label(win,text='Confirm \nPassword ',fg='white',font=('calibri',15,'bold'),bg='#3333ff',padx=10,pady=5)
    pass_labelC.place(x=50,y=150)
    pass_entryC=Entry(win,font=('calibri',18,'bold'),show='*')
    pass_entryC.place(x=155,y=165)
    sign_button=Button(win,text=' Sign Up ',fg='white',font=('calibri',15,'bold'),bg='black',command=save_data)
    sign_button.place(x=200,y=230)
       
    
    win.mainloop()

b=Button(mW,text='Sign up', bg="#00004d", fg="white", command=sign_up)
b.place(x=900,y=600)


mW.mainloop()
