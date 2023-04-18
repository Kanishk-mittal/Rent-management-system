import mysql.connector as msc
import pandas as pd


def start_connection():
    global con,cur
    con=msc.connect(host="localhost",user="root",password="1234")
    cur=con.cursor()

def add_room(room_name,rent,currently_occupied,internet_provided,last_electricity_unit,occupied_by):
    global cur
    global con
    print("room added")
    cur.execute(f"insert into Room_Details(Room_name,rent,currently_occupied,internet_provided,last_electricity_unit,occupied_by) values('{room_name}',{rent},'{currently_occupied}','{internet_provided}',{last_electricity_unit},{occupied_by})")
    con.commit()

def initialise():
    global cur
    try:
        cur.execute("Use Rent_details;")
    except:
        print("intialising database")
        cur.execute("Create Database Rent_details;")
        cur.execute("Use Rent_details;")

        cur.execute("Create table Tenant_Details(Tenant_ID int(5) AUTO_INCREMENT primary key,Name varchar(25),address varchar(50),room_alloted varchar(10),last_balance int(10),rent_paid_till date,left_room_on date);")

        cur.execute("Create table Room_Details(room_ID int(5) AUTO_INCREMENT primary key,Room_name varchar(25),rent int(6),currently_occupied varchar(3),internet_provided varchar(3),last_electricity_unit int(5),occupied_by varchar(25));")

        #cur.execute("Create table Payment_Details(payment_ID int(10) AUTO_INCREMENT primary key,amount int(10),paid_by int(5));")

        add_room("first floor",5500,"NO","YES",1234,"NULL")
        add_room("second floor room 1",3200,"NO","NO",1234,"NULL")
        add_room("second floor room 2",3000,"NO","NO",1234,"NULL")
        add_room("Shop no 5",5500,"NO","NO",1234,"NULL")
        add_room("Shop no 6",5500,"NO","NO",1234,"NULL")
        con.commit()

def add_tenant(lst,room_ID):
    global cur
    cur.execute(f"insert into Tenant_Details(Name,address,room_alloted,last_balance,rent_paid_till) values('{lst[0]}','{lst[1]}','{lst[2]}',{lst[3]},{lst[4]})")
    con.commit()

def get_room_data():
    global con
    # Read the table into a Pandas DataFrame
    df = pd.read_sql_query("SELECT * FROM  room_details", con,index_col="room_ID")
    return df

def close_connection():
    con.commit()
    con.close()

def get_tenant_details(name):
    df = pd.read_sql_query(f"SELECT * FROM  tenant_details where name='{name}'", con,index_col="Tenant_ID")
    return df

def change_rent_paid_till(date,roomID):
    global con 
    global cur
    cur.execute(f"update tenant_details set rent_paid_till = '{date}' where room_alloted={roomID}")
    con.commit()

def set_current_active(roomID,name):
    global cur
    cur.execute(f"update room_details set occupied_by = '{name}' where room_ID = {roomID}")
    con.commit()

def update_room_detail(list):
    global cur
    global con
    cur.execute(f"update room_details set rent={list[0]},internet_provided={list[1]}")
    con.commit()

def add_payment(room_ID,name,date,current_units,balance):
    global cur
    global con 
    cur.execute(f"update room_details set last_electricity_unit={current_units} where room_ID = {room_ID}")
    cur.execute(f"update tenant_details set rent_paid_till='{date}',last_balance={balance} where Name = {name}")
    con.commit()

def set_empty(room,tenant,date):
    global cur
    global con
    cur.execute(f"update room_details set currently_occupied ='NO',occupied_by=NULL where room_ID={room}")
    cur.execute(f"update tennant_details set room_alloted=NULL , left_room_on = {date} where name = {tenant}")
    con.commit()