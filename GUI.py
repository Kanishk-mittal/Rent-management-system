# importing required libraries
from tkinter import *
from PIL import ImageTk,Image
import tkinter.messagebox as tmsg
copy=None
#function to display error code 
def show_error_code(code):
    error="Sorry some error occured please contant admin error code ("+str(code)+")"
    tmsg.showerror("Error",error)

#error_code 101
def ask_log_in():
    global verification 
    global log_in_window
    #try:
        #creating window
    log_in_window=Tk()
    log_in_window.title("log in")
    log_in_window.geometry("550x550")
    #creating requitred tkinter variable
    entered_password=StringVar(log_in_window)
    Label(log_in_window,text="Welcome to our Rent management system",font=('Arial black',15,'bold')).pack(pady=5)
    Label(log_in_window,text="Please enter your password to continue").pack(pady=20)
    Entry(log_in_window,textvariable=entered_password,font=('Arial black',15,'bold'),borderwidth=3,show="*").pack(pady=5)
    Button(log_in_window,text="submit",font=('Arial black',15,'bold'),command=lambda: check_password(entered_password)).pack(pady=5)
    log_in_window.mainloop()
    return verification
#    except:
#        show_error_code(101)
        
#error code 102
def check_password(entered_password):
    global verification
    global log_in_window 
    try:
        password=entered_password.get()
        if password=="1234":  # replace it by tenant
            verification= True
            log_in_window.destroy()
        else:
            verification= False
            entered_password.set("")
            tmsg.showerror("wrong password","You have enterd wrong password")
    except:
        show_error_code(102)

def get_value():
    global temp
    for i in range(len(temp)):
        temp[i]=temp[i].get()
    return temp

def create_data_copy():
    global Details_list1
    global temp
    global tenant_details
    #print(Details_list1)
    temp=list(Details_list1)
    tenant_details.destroy()

def ask_tenant_details():
    #Name,address,room_alloted,last_balance,extra_charge,extra_charge_comment,rent_paid_till,left_room_on,agreement_ID
    global Details_list1
    global tenant_details
    tenant_details=Tk()
    Name=StringVar(tenant_details)
    address=StringVar(tenant_details)
    room_alloted=StringVar(tenant_details)
    last_balance=StringVar(tenant_details)
    extra_charge=StringVar(tenant_details)
    extra_charge_comment=StringVar(tenant_details)
    rent_paid_till=StringVar(tenant_details)
    left_room_on=StringVar(tenant_details)
    left_room_on.set("NULL")
    agreement_ID=StringVar(tenant_details)
    Details_list1=[Name,address,room_alloted,last_balance,extra_charge,extra_charge_comment,rent_paid_till,left_room_on,agreement_ID]
    Details_list2=[Name,address,room_alloted,last_balance,extra_charge,extra_charge_comment,rent_paid_till,agreement_ID]
    details=['Name','Address','Room alloted','Last balance','Extra charge','Extra charge comment','Rent paid till','Agreement ID']
    Label(tenant_details,text="Enter details ",font=('Arial black',15,'bold'),bg="black",fg="white").grid(row=1,column=1)
    for i in range(len(details)):
        Label(tenant_details,text=details[i],font=('Arial black',15,)).grid(row=i+2,column=1,pady=10)
        Entry(tenant_details,textvariable=Details_list2[i],font=('Arial black',15,)).grid(row=i+2,column=2)
    Button(tenant_details,text="Submit",font=('Arial black',15,),command=create_data_copy).grid(row=11,column=2)
    tenant_details.mainloop()

def create_copy(value):
    global main_window
    global copy
    copy=value
    main_window.destroy()
    
def get_function_value():
    global copy
    return copy

def showrooms(room_detail_dataframe):
    global main_window
    main_window=Tk()
    main_window.title("Rent management system")
    main_window.geometry("1920x1080")
    Label(main_window,text="Room \t\t\t currently occupied \t\t\t occupied by",font=("Segor print",25,"italic"),bg="cyan",fg="Black").pack(fill=X)
    for i in range(1,len(room_detail_dataframe)+1):
        Button(main_window,text=f"{room_detail_dataframe.loc[i,'Room_name']}\t\t\t\t{room_detail_dataframe.loc[i,'currently_occupied']}\t\t\t\t{room_detail_dataframe.loc[i,'occupied_by']}",font=("Segor print",15,"italic"),justify=LEFT,command=lambda value=i:create_copy(value),pady=20,borderwidth=5).pack(fill=X,pady=15,padx=10)
    main_window.mainloop()

def show_room_details(name,last_balance,rent_paid_till):
    room_detail=Tk()
    room_detail.geometry("1920x1018")

    namevar=StringVar(room_detail)
    balancevar=StringVar(room_detail)
    rentvar=StringVar(room_detail)

    namevar.set(name)
    balancevar.set(last_balance)
    rentvar.set(rent_paid_till)

    Left_frame=Frame(room_detail,bg='cyan',padx=15,pady=20,bd=3,relief="solid")
    Left_frame.pack(side=LEFT, fill=Y, expand=True,anchor=W)

    Label(Left_frame,text="Tenanat details",font=("cosmic sans MS",25,"bold"),bd=2, relief="solid",bg="cyan",fg="black").pack(side=TOP,padx=5,pady=15)

    Label(Left_frame,text="Name",font=("cosmic sans MS",25,"bold"),bg="cyan",fg="black").pack(padx=5,pady=15,anchor=W)
    Label(Left_frame,textvariable=namevar,font=("cosmic sans MS",25,"bold"),bd=2, relief="solid",bg="cyan",fg="black").pack(padx=5,pady=15,anchor=W)

    Label(Left_frame,text="Last Balance",font=("cosmic sans MS",25,"bold"),bg="cyan",fg="black").pack(padx=5,pady=15,anchor=W)
    Label(Left_frame,textvariable=balancevar,font=("cosmic sans MS",25,"bold"),bd=2, relief="solid",bg="cyan",fg="black").pack(padx=5,pady=15,anchor=W)

    Label(Left_frame,text="Rent Paid Till",font=("cosmic sans MS",25,"bold"),bg="cyan",fg="black").pack(padx=5,pady=15,anchor=W)
    Label(Left_frame,textvariable=rentvar,font=("cosmic sans MS",25,"bold"),bd=2, relief="solid",bg="cyan",fg="black").pack(padx=5,pady=15,anchor=W)

    Button(room_detail,text="Generate Bill",font=("cosmic sans MS",25,"bold"),borderwidth=10,command=lambda:create_copy("Generate_Bill")).pack(pady=20,padx=250)
    Button(room_detail,text="Generate Recipt",font=("cosmic sans MS",25,"bold"),borderwidth=10,command=lambda:create_copy("Generate_recipt")).pack(pady=20,padx=250)
    Button(room_detail,text="Replace tenant",font=("cosmic sans MS",25,"bold"),borderwidth=10,command=lambda:create_copy("Replac_tenant")).pack(pady=20,padx=250)
    Button(room_detail,text="Edit property details",font=("cosmic sans MS",25,"bold"),borderwidth=10,command=lambda:create_copy("Edit_property_Details")).pack(pady=20,padx=250)
    Button(room_detail,text="Mark as Empyt",font=("cosmic sans MS",25,"bold"),borderwidth=10,command=lambda:create_copy("Mark_as_empty")).pack(pady=20,padx=250)
    room_detail.mainloop()