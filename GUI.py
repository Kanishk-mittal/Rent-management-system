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
        greet_label=Label(log_in_window,text="Welcome to our Rent management system",font=('Arial black',15,'bold')).pack(pady=5)
        greet_label2=Label(log_in_window,text="Please enter your password to continue").pack(pady=20)
        password_box=Entry(log_in_window,textvariable=entered_password,font=('Arial black',15,'bold'),borderwidth=3,show="*").pack(pady=5)
        Submit_button=Button(log_in_window,text="submit",font=('Arial black',15,'bold'),command=lambda: check_password(entered_password)).pack(pady=5)
        log_in_window.mainloop()
        return verification
    except:
        show_error_code(101)
        
def check_password(entered_password):
    global verification 
    password=entered_password.get()
    if password=="1234":  # replace it by tenant
        verification= True
    else:
        verification= False
        entered_password.set("")
        tmsg.showerror("wrong password","You have enterd wrong password")
a=ask_log_in()
