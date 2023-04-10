import mysql.connector as msc
def initialise():
    con=msc.connect(host="localhost",user="root",password="1234")
    cur=con.cursor()
    try:
        cur.execute("Use Rent_details")
    except:
        cur.execute("Create Database Rent_details")
        cur.execute("Create table Tenant_Details")
        cur.execute("Create table Room_Details")
        cur.execute("Create table Payment_Details")
    con.commit()
    cur.close()