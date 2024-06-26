from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
win=Tk()
win.geometry("568x500+300+60")
win.title("HSMS")
win.resizable(0,0)
win.config(background="lightblue")
win.iconbitmap("c:\\users\\RISHI\\Desktop\\clogo.ico")
photof=Image.open("c:\\users\\RISHI\\Desktop\\logo1.png")
photor=photof.resize((300,280))
photoff=ImageTk.PhotoImage(photor)
image=Label(win,image=photoff)
image.place(x=20,y=100)
lab1=Label(win,text="Welcome To The Hubnet Managment System",font=("monotype corsiva",25,"bold"),bg="black",fg="white")
lab1.place(x=2,y=2)
lab2=Label(win,text="Website : www.hubnettech.net  Ph :  7091499201",font=("monotype corsiva",22,"bold"),bg="black",fg="white")
lab2.place(x=1,y=455)
def SignUp():
    signupwin=Tk()
    import mysql.connector as sql
    mycon=sql.connect(host="localhost",user="root",password="Rishi@123",database="tkinter")
    mycur=mycon.cursor()
    signupwin.geometry("590x500+300+60")
    signupwin.title("HSMS")
    signupwin.resizable(0,0)
    name=StringVar()
    userid=StringVar()
    password=StringVar()
    def save():
        na=ent.get()
        ui=ent1.get()
        ps=ent2.get()
        q="insert into user values ('{}','{}','{}')".format(na,ui,ps)
        mycur.execute(q)
        mycon.commit()
        messagebox.showinfo("signup","SignUp Successful")
    def reset():
        ent.delete(0,END)
        ent1.delete(0,END)
        ent2.delete(0,END)
    signupwin.config(background="lightblue")
    signupwin.iconbitmap("c:\\users\\RISHI\\Desktop\\clogo.ico")
    lab1=Label(signupwin,text="HUBNET USER SIGNUP FORM",font=("algerian",33,"bold"),bg="black",fg="white")
    lab1.place(x=2,y=2)
    label1=Label(signupwin,text="name",font=("algerian",22,"bold"),bg="lightblue",fg="black")
    label1.place(x=40,y=100)
    ent=Entry(signupwin,font=("algerian",20,"bold"),bg="white",fg="black",bd=4,textvariable=name)
    ent.place(x=220,y=100)
    label2=Label(signupwin,text="User Id",font=("algerian",22,"bold"),bg="lightblue",fg="black")
    label2.place(x=40,y=170)
    ent1=Entry(signupwin,font=("algerian",20,"bold"),bg="white",fg="black",bd=4,textvariable=userid)
    ent1.place(x=220,y=170)
    label3=Label(signupwin,text="Password",font=("algerian",22,"bold"),bg="lightblue",fg="black")
    label3.place(x=40,y=240)
    ent2=Entry(signupwin,font=("algerian",20,"bold"),bg="white",fg="black",bd=4,textvariable=password)
    ent2.place(x=220,y=240)
    btn1=Button(signupwin,text="Submit",bg="green",fg="white",bd=5,font=("monotype corsiva",20,"bold"),width=5,command=save)
    btn1.place(x=150,y=350)
    btn2=Button(signupwin,text="Reset",bg="red",fg="white",bd=5,font=("monotype corsiva",20,"bold"),width=5,command=reset)
    btn2.place(x=380,y=350)
    lab2=Label(signupwin,text="Website  :  www.hubnettech.net  Ph :  7091499201 ",font=("monotype corsiva",22,"bold"),bg="black",fg="white")
    lab2.place(x=1,y=455)
def SignIn():
    signinwin=Tk()
    import mysql.connector as sql
    mycon=sql.connect(host="localhost",user="root",password="Rishi@123",database="tkinter")
    mycur=mycon.cursor()
    signinwin.config(background="lightblue")
    signinwin.iconbitmap("c:\\users\\RISHI\\Desktop\\clogo.ico")
    signinwin.geometry("590x500+300+60")
    signinwin.title("HSMS")
    signinwin.resizable(0,0)
    name=StringVar()
    userid=StringVar()
    password=StringVar()
    def login():
        import mysql.connector as sql
        mycon=sql.connect(host="localhost",user="root",password="Rishi@123",database="tkinter")
        mycur=mycon.cursor()
        uid=ent.get()
        pas=ent1.get()
        q="select * from user where userid='{}' and password='{}'".format(uid,pas)
        mycur.execute(q)
        rec=mycur.fetchall()
        if rec!=[]:
            crud=Tk()
            crud.config(background="lightblue")
            crud.iconbitmap("c:\\users\\RISHI\\Desktop\\clogo.ico")
            crud.geometry("590x500+300+60")
            crud.title("HSMS")
            crud.resizable(0,0)
            name=StringVar()
            ssid=StringVar()
            phne=StringVar()
            cur=StringVar()
            doa=StringVar()
            fee=StringVar()
            def addnew():
                s=sn.get()
                i=sid.get()
                p=ph.get()
                c=crs.get()
                d=ad.get()
                f=fe.get()
                q="insert into student values ('{}','{}','{}','{}','{}','{}')".format(s,i,p,c,d,f)
                mycur.execute(q)
                mycon.commit()
                messagebox.showinfo("Add New","Record Add Successfully")
            def delete():
                s=sn.get()
                i=sid.get()
                p=ph.get()
                c=crs.get()
                d=ad.get()
                f=fe.get()
                q="delete from student where sid='{}'".format(i)
                mycur.execute(q)
                mycon.commit()
                messagebox.showinfo("Delete","Record Delete Successfully")
            def find():
                s=sn.get()
                i=sid.get()
                p=ph.get()
                c=crs.get()
                d=ad.get()
                f=fe.get()
                q="select * from student where sid='{}'".format(i)
                mycur.execute(q)
                rec=mycur.fetchall()
                print(rec)
                messagebox.showinfo("REC","Here Your Data")
            lab1=Label(crud,text="Hubnet_Student _Detail_Form",font=("algerian",27,"bold"),bg="black",fg="white")
            lab1.place(x=1,y=2)
            labh=Label(crud,text="Student Crud Operation",fg="white",bg="green",bd=5,font=("algerian",20),width=20)
            labh.place(x=110,y=50)
            label1=Label(crud,text="Name : ",font=("algerian",18,"bold"),bg="lightblue",fg="black")
            label1.place(x=30,y=100)
            sn=Entry(crud,font=("algerian",18,"bold"),bg="white",fg="black",bd=4,textvariable=name)
            sn.place(x=150,y=100)
            label2=Label(crud,text="ID : ",font=("algerian",18,"bold"),bg="lightblue",fg="black")
            label2.place(x=30,y=150)
            sid=Entry(crud,font=("algerian",18,"bold"),bg="white",fg="black",bd=4,textvariable=ssid)
            sid.place(x=150,y=150)
            label3=Label(crud,text="Phone : ",font=("algerian",18,"bold"),bg="lightblue",fg="black")
            label3.place(x=30,y=200)
            ph=Entry(crud,font=("algerian",18,"bold"),bg="white",fg="black",bd=4,textvariable=phne)
            ph.place(x=150,y=200)
            label4=Label(crud,text="Course : ",font=("algerian",18,"bold"),bg="lightblue",fg="black")
            label4.place(x=30,y=250)
            crs=Entry(crud,font=("algerian",18,"bold"),bg="white",fg="black",bd=4,textvariable=cur)
            crs.place(x=150,y=250)
            label5=Label(crud,text="D.O.A : ",font=("algerian",18,"bold"),bg="lightblue",fg="black")
            label5.place(x=30,y=300)
            ad=Entry(crud,font=("algerian",18,"bold"),bg="white",fg="black",bd=4,textvariable=doa)
            ad.place(x=150,y=300)
            label6=Label(crud,text="Fee : ",font=("algerian",18,"bold"),bg="lightblue",fg="black")
            label6.place(x=30,y=350)
            fe=Entry(crud,font=("algerian",18,"bold"),bg="white",fg="black",bd=4,textvariable=fee)
            fe.place(x=150,y=350)
            btn1=Button(crud,text="Add New",bg="white",fg="black",bd=3,font=("monotype corsiva",16,"bold"),command=addnew)
            btn1.place(x=40,y=400)
            btn2=Button(crud,text="Update",bg="white",fg="black",bd=3,font=("monotype corsiva",16,"bold"))
            btn2.place(x=200,y=400)
            btn3=Button(crud,text="Delete",bg="white",fg="black",bd=3,font=("monotype corsiva",16,"bold"),command=delete)
            btn3.place(x=360,y=400)
            btn4=Button(crud,text="Find",bg="white",fg="black",bd=3,font=("monotype corsiva",16,"bold"),command=find)
            btn4.place(x=500,y=400)
            lab2=Label(crud,text="Website  :  www.hubnettech.net  Ph :  7091499201 ",font=("monotype corsiva",22,"bold"),bg="black",fg="white")
            lab2.place(x=1,y=455)
        else:
            print("faild")
            
    def reset():
        uid=ent.delete(0,END)
        pas=ent1.delete(0,END)        
    lab1=Label(signinwin,text="Hubnet_User _SignIn_Form",font=("algerian",31,"bold"),bg="black",fg="white")
    lab1.place(x=1,y=2)
    lab2=Label(signinwin,text="Website  :  www.hubnettech.net  Ph :  7091499201 ",font=("monotype corsiva",22,"bold"),bg="black",fg="white")
    lab2.place(x=1,y=455)
    labh=Label(signinwin,text="LOGIN FORM",fg="white",bg="green",bd=5,font=("algerian",24),width=10)
    labh.place(x=200,y=80)
    labid=Label(signinwin,text="UserId : ",font=("algerian",18,"bold"),bg="black",fg="white")
    labid.place(x=80,y=200)
    ent=Entry(signinwin,font=("algerian",18,"bold"),bg="white",fg="black",bd=4,textvariable=userid)
    ent.place(x=240,y=200)
    bt1=Button(signinwin,text="Login",font=("monotype corsiva",22,"bold"),bg="white",fg="red",bd=5,width=5,command=login)
    bt1.place(x=130,y=370)
    labpas=Label(signinwin,text=("Password : "),font=("algerian",18,"bold"),bg="black",fg="white")
    labpas.place(x=80,y=300)
    bt2=Button(signinwin,text="Reset",font=("monotype corsiva",22,"bold"),bg="red",fg="white",bd=5,width=5,command=reset)
    bt2.place(x=400,y=370)
    ent1=Entry(signinwin,font=("algerian",18,"bold"),bg="white",fg="black",bd=4,textvariable=password,show="*")
    ent1.place(x=240,y=300)
btn1=Button(win,text="SignUp",bg="white",fg="red",bd=10,font=("monotype corsiva",22,"bold"),width=7,command=SignUp)
btn1.place(x=400,y=100)
btn2=Button(win,text="SignIn",bg="white",fg="red",bd=10,font=("monotype corsiva",23,"bold"),width=7,command=SignIn)
btn2.place(x=400,y=200)
btn3=Button(win,text="Exit",bg="white",fg="red",bd=10,font=("monotype corsiva",23,"bold"),width=7)
btn3.place(x=400,y=300)
win.mainloop()
