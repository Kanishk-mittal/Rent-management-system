import mysql.connector as msc
import pandas as pd
con=msc.connect(host="localhost",user="root",password="1234")
cur=con.cursor()

def add_room(room_name,rent,currently_occupied,internet_provided,last_electricity_unit,agreement_ID,agreement_Date,occupied_by):
    cur.execute(f"insert into Room_Details(Room_name,rent,currently_occupied,internet_provided,last_electricity_unit,agreement_ID,agreement_Date,occupied_by) values('{room_name}',{rent},'{currently_occupied}','{internet_provided}',{last_electricity_unit},'{agreement_ID}','{agreement_Date}',{occupied_by})")

def initialise():
    try:
        cur.execute("Use Rent_details;")
    except:
        cur.execute("Create Database Rent_details;")
        cur.execute("Use Rent_details;")

        cur.execute("Create table Tenant_Details(Tenant_ID int(5) AUTO_INCREMENT primary key,Name varchar(25),address varchar(50),room_alloted varchar(10),last_balance int(10),extra_charge int(10),extra_charge_comment varchar(50),rent_paid_till date,left_room_on date,agreement_ID varchar(20));")

        cur.execute("Create table Room_Details(room_ID int(5) AUTO_INCREMENT primary key,Room_name varchar(25),rent int(6),currently_occupied varchar(3),internet_provided varchar(3),last_electricity_unit int(5),agreement_ID varchar(20),agreement_Date date,occupied_by varchar(25));")

        cur.execute("Create table Payment_Details(payment_ID int(10) AUTO_INCREMENT primary key,amount int(10),paid_by int(5));")

        add_room("first floor",5500,"YES","YES",1234,"alkdufdhlnadij","2023-03-01","NULL")
        add_room("second floor room 1",3200,"YES","NO",1234,"alkdufdhlnadij","2023-03-01","NULL")
        add_room("second floor room 2",3000,"NO","NO",1234,"alkdufdhlnadij","2023-03-01","NULL")
        add_room("Shop no 5",5500,"YES","NO",1234,"alkdufdhlnadij","2023-03-01","NULL")
        add_room("Shop no 6",5500,"YES","NO",1234,"alkdufdhlnadij","2023-03-01","NULL")
initialise()
def add_tenant(Name,address,room_alloted,last_balance,extra_charge,extra_charge_comment,rent_paid_till,left_room_on,agreement_ID):
    cur.execute(f"insert into Tenant_Details(Name,address,room_alloted,last_balance,extra_charge,extra_charge_comment,rent_paid_till,left_room_on,agreement_ID) values('{Name}','{address}','{room_alloted}',{last_balance},{extra_charge},'{extra_charge_comment}',{rent_paid_till},'{left_room_on}','{agreement_ID}')")
def get_room_data():
    # Read the table into a Pandas DataFrame
    df = pd.read_sql_query("SELECT * FROM  room_details", con,index_col="room_ID")
    return df
    
con.commit()
con.close()
