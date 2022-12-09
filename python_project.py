import mysql.connector

con=mysql.connector.connect(host='localhost',user="root",passwd='1234',database='ayush')
if con.is_connected():
    print("success")
cursor=con.cursor()

#querry 1-----insert function---------------------------------------

def insert():
    while True:
        admno=int(input("enter admission nomber--"))
        name=input("enter name--")
        
        dob=input("enter date of birth--")

        marks=int(input("enter marks--"))
        fee=int(input("enter fee paif--"))
        emai=input("enter email--")
        qry2="insert into stu_info values({},'{}',{},{},{},'{}')".format(admno,name,dob,marks,fee,emai)

        cursor.execute(qry2)
        con.commit()   

        print("data inserted successfully....")
        x=input("do you want to continue(y/n)--")
        if x=="n":
            break
        else:
            print("ok")


#querry 2-----update functions--------------------------------------

def update_marks():
    adm=int(input("enter admission number--:"))
    mar=int(input("enter marks to be updated--:"))
    a="update stu_info set marks={} where admno='{}'".format(mar,adm)
    cursor.execute(a)
    con.commit()
    print("updated succesfully....")
 
def update_name():
    adm=int(input("enter admission number--:"))
    nam=input("enter new name--:")
    a="update stu_info set name='{}' where admno={}".format(nam,adm)
    cursor.execute(a)
    con.commit()
    print("updated succesfully....")

def update_fee():
    adm=int(input("enter admission number--:"))
    fee=int(input("enter fee to be updated--:"))
    a="update stu_info set fee='{}' where admno={}".format(fee,adm)
    cursor.execute(a)
    con.commit()
    print("updated succesfully....")

def update_email():
    adm=int(input("enter admission number--:"))
    emai=input("enter new email--:")
    a="update stu_info set email='{}' where admno={}".format(emai,adm)
    cursor.execute(a)
    con.commit()
    print("updated succesfully....")

def update():
    while True:
        print("\n")
        choice=int(input('''1---name update\n2---marks update
3---fee update\n4---email update\n5---Exit\nenter choice---:'''))
        if choice==1:
            update_name()
        elif choice==2:
            update_marks()
        elif choice==3:
            update_fee()
        elif choice==4:
            update_email()
        elif choice==5:
            break     
        else:
            print("wrong choice is entered  ENTER AGAIN")
        

#querry 3-----delete function--------------------------------------

def delete_info():
    adm=int(input("enter admission number--:"))
    cursor.execute("SELECT * FROM stu_info where admno="+str(adm))
    result=cursor.fetchall()
    print(result)
    ch=input("do you want to delete these info(y/n)--:")
    a="delete from stu_info where admno={}".format(adm)
    if ch=="y":
        cursor.execute(a)
        con.commit()
        print("updated succesfully....")
    elif ch=="n":
        exit()
    
#querry 4-----display function-------------------------------------

def display():
    cursor.execute("SELECT * FROM stu_info")
    result=cursor.fetchall()
    for i in result:
        print(i)
def show_feedefaulters():
    cursor.execute("SELECT * FROM stu_info where fee=0")
    result=cursor.fetchall()
    for i in result:
        print(i)

def search():
    ad=int(input("Enter admission number:  "))
    cursor.execute("select * from stu_info where admno="+str(ad))
    res=cursor.fetchall()
    print(res)



#querry  5------message sender-------------------------------------   

def sendemail(): 
    import smtplib
    cursor.execute("SELECT email FROM stu_info where fee=0")
    result=cursor.fetchall()
    '''for i in result:
        connection=smtplib.SMTP("smtp.gmail.com",587)        
        connection.starttls()        
        connection.login(user="ayushkumar8418@gmail.com", password="ayushkumarsingh1234@#")
    
        connection.sendmail(from_addr="ayushkumar8418@gmail.com", to_addrs="i", msg="Hello")
        connection.close()'''
    print("Mail is sent to these students",result)


while True:
    print("\n*******************************************")
    print("     FEE MANAGEMENT SYSTEM")
    print("******************************************")

    print("\n1. SHOW STUDENT LIST ")
    print("2. ADD NEW STUDENT")
    print("3. SEARCH STUDENT ")
    print("4. EDIT STUDENT ")
    print("5. DELETE STUDENT ")
    print("6. SEND E-MAIL to FEE DEFAULTERS")
    print("7. show fee defaulters")
    print("0. EXIT")
    ans=int(input("Enter your choice -:"))
    if ans==1:
        display()
    elif ans==2:
        insert()
    elif ans==3:
        search()
    elif ans==4:
        update()    
    elif ans==5:
        delete_info()
    elif ans==6:
        sendemail()
    elif ans==7:
        show_feedefaulters()
    elif ans==0:
        print("\nBye!!")
        break
    else :
        print("ENTER CORRECT CHOICE--")