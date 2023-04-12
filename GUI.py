# importing required libraries
from tkinter import *
from PIL import ImageTk,Image
import tkinter.messagebox as tmsg

#function to display error code 
def show_error_code(code):
    error="Sorry some error occured please contant admin error code ("+str(code)+")"
    tmsg.showerror("Error",error)

#error_code 101
def ask_log_in():
    global verification 
    try:
        #creating window
        log_in_window=Tk()
        log_in_window.title("log in")
        log_in_window.geometry("550x600")
        #creating requitred tkinter variable
        entered_password=StringVar(log_in_window)
        #adding image to make window attractive
        namaste_image=Image.open("namaste_image.jpg")
        namaste_image=namaste_image.resize((300,300))
        namaste_file=ImageTk.PhotoImage(namaste_image)
        namaste_label=Label(log_in_window,image=namaste_file).pack(pady=20)
        #greeting and asking pin
        Label(log_in_window,text="Welcome to our Rent management system",font=('Arial black',15,'bold')).pack(pady=5)
        Label(log_in_window,text="Please enter your password to continue").pack(pady=20)
        Entry(log_in_window,textvariable=entered_password,font=('Arial black',15,'bold'),borderwidth=3,show="*").pack(pady=5)
        Button(log_in_window,text="submit",font=('Arial black',15,'bold'),command=lambda: check_password(entered_password)).pack(pady=5)
        log_in_window.mainloop()
        return verification
    except:
        show_error_code(101)
        
#error code 102
def check_password(entered_password):
    global verification 
    try:
        password=entered_password.get()
        if password=="1234":  # replace it by tenant
            verification= True
        else:
            verification= False
            entered_password.set("")
            tmsg.showerror("wrong password","You have enterd wrong password")
    except:
        show_error_code(102)
from tkinter import *
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

ask_tenant_details()
print(get_value())
