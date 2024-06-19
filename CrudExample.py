import mysql.connector as sql
mycon=sql.connect(host="localhost",user='root',password="Rishi@123",database="hubnetdb")
mycur=mycon.cursor()
print("\t\t------------------------------------------------------------------------------")
print("\t\t\t\t\tWelcome To Hubnet Managment System")
print("\t\t------------------------------------------------------------------------------")
ch=int(input("\t\t\tPress 1 For LogIn and Press 2 For SignUp : "))
if ch==1:
    print("\n\t\t\tUser Login")
    uid=input("\n\t\t\tEnter UserId : ")
    pas=input("\t\t\tEnter password : ")
    q="select userid,password from users where userid='{}' and password='{}'".format(uid,pas)
    mycur.execute(q)
    data=mycur.fetchall()
    if data==[]:
        print("Login Faild Bcz Invalid userid or password ...!!!!!!")
    else:
        print("\t\t------------------------------------------------------------------------------")
        print("\t\t\t\t\tWelcome To Hubnet Managment System")
        print("\t\t------------------------------------------------------------------------------")
        print("\t\t\t1. Press 1 For New Entry of Student   : ")
        print("\t\t\t2. Press 2 For Student Verification   : ")
        print("\t\t\t3. Press 3 For Update Student Details : ")
        print("\t\t\t4. Press 4 For Delete Student Records : ")
        print("\t\t\t5. Press 5 For Close The Application  : ")
        chh=int(input("\t\t\tEnter Your Choice : "))
        if chh==1:
            sid=input("\t\t\tEnter Student Id : ")
            sname=input("\t\t\tEnter Student Name : ")
            dob=input("\t\t\tEnter Student Date Of Birth : ")
            phone=input("\t\t\tEnter Student Phone No : ")
            doa=input("\t\t\tEnter Student Date of Admision : ")
            cid=input("\t\t\tEnter Student Course Name : ")
            q="insert into student values ('{}','{}','{}','{}','{}','{}')".format(sid,sname,dob,phone,doa,cid)
            mycur.execute(q)
            mycon.commit()
            print("Record Update Successfully...!!!!!!")           
        elif chh==2:
            sid=input("\t\t\tEnter Student Id : ")
            q="select sid from student where sid='{}'".format(sid)
            mycur.execute(q)
            data=mycur.fetchall()
            if data==[]:
                print("Record Not Found !!!!")
            else:
                print("Record Found!!!!",data)
        elif chh==3:
            pass
        elif chh==4:
            pass
        elif chh==5:
            pass
elif ch==2:
    print("\n\t\t\tUser SignUP")
    uid=input("\n\t\t\tEnter UserId : ")
    pas=input("\t\t\tEnter password : ")
    q="insert into users values ('{}','{}')".format(uid,pas)
    mycur.execute(q)
    mycon.commit()
    print("User SignUp Successfully!!!!!!!")
    
        
