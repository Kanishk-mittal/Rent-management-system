import mysql.connector as msc
def initialise():
    con=msc.connect(host="localhost",user="root",password="1234")
    cur=con.cursor()
    try:
        cur.execute("Use Rent_details;")
    except:
        cur.execute("Create Database Rent_details;")
        cur.execute("Use Rent_details;")
        cur.execute("Create table Tenant_Details(Tenant_ID int(5),Name varchar(25),address varchar(50),room_alloted varchar(10),last_balance int(10),extra_charge int(10),extra_charge_comment varchar(50),rent_paid_till date,left_room_on date);")
        cur.execute("Create table Room_Details(room_ID int(5),rent int(6),currently_occupied varchar(3),internet_provided varchar(3),last_electricity_unit int(5),agreement_ID varchar(20),agreement_Date date);")
        cur.execute("Create table Payment_Details(payment_ID int(10),amount int(10),paid_by int(5));")
    con.commit()
    cur.close()
initialise()