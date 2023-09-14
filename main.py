import mysql.connector
import smtplib

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="corona_db"
)
mycursor=mydb.cursor()
#**************************

def insert_data():
    #data insert concept

    sql="insert into appointment_details (name,age,gender,date,vaccine,reason,email) values (%s,%s,%s,%s,%s,%s,%s)"
    print("******CORONA DATABASE MANAGEMENT*****")
    name=input("enter a firstname:")
    age=int(input("enter a age:"))
    gender=input("enter a gender:")
    date=input("enter a date:")
    vaccine=input("enter a vaccine:")
    reason=input("enter a reason:")
    email=input("enter a email:")
    val=(name,age,gender,date,vaccine,reason,email)
    mycursor.execute(sql,val)
    mydb.commit()
    print(f"hi {name} your appointment successfully!..")
    print("****data saved successfully***")

    #************mail code***********

    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("mohamedthoufeek83@gmail.com", "lipfcigwfelicurw")
        message= f"hi {name} your booking has successfully reciecved....."
        s.sendmail("mohamedthoufeek83@gmail.com", email, message)
        print("****mail sent successfully***")
    except:
        print("****sorry mail not sent****")

    var=input("do you want to continue press yes:")
    if var=="yes":
        main_function()
    else:
        print("thanks for visiting our website")

def admin():
    mycursor.execute("select * from appointment_details")
    myresult=mycursor.fetchall()
    for i in myresult:
        print(i)
    var=input("do you want to continue press yes:")
    if var=="yes":
        main_function()
    else:
        print("thanks for visiting")

def update_data():
    
    sql="update appointment_details set email='safin123@gmail.com' where id=7"
    mycursor.execute(sql)
    mydb.commit()
    print("data updated successfully..")
    var=input("do you want to continue press yes:")
    if var=="yes":
        main_function()
    else:
        print("thanks for visiting")
def delete_data():

    sql="delete from appointment_details where id=9 "
    mycursor.execute(sql)
    mydb.commit()
    print("delete successfully")


def main_function():
        print("****CRUD****")
        print("1->insert data")
        print("2->admin")
        print("3->update data")
        print("4->delete data")

        user=int(input("enter your number:"))
        try:
            if user==1:
                insert_data()
            elif user==2:
                admin()
            elif user==3:
                update_data()
            elif user==4:
                delete_data()
            else:
                print("pls type 1 2 3 4 only")
        except:
            print("pls type number only")

main_function()
