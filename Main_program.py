import SQL_connection as sq
import GUI as g
import createpdf as pdf
import datetime
import tkinter.messagebox as tmsg

#initialising database for our program 
sq.start_connection()
sq.initialise()
run=True
#requesting password and checking it 
if g.ask_log_in():
    #here the user is authorised and we can perform our tasks
    while run:
        room_data=sq.get_room_data()
        choise=g.showrooms(room_data[["Room_name","currently_occupied","occupied_by"]])
        room_ID=int(g.get_function_value())
        if room_data.loc[room_ID,"currently_occupied"]=="NO":
            g.show_room_details("NULL","NULL","NULL")
            if g.get_function_value()=="Add_tenant":
                g.ask_tenant_details()
                lst=g.get_value()
                lst.insert(-1,room_ID)
                lst.append("NULL")
                sq.add_tenant(lst,room_ID)
                if room_data.loc[room_ID,"internet_provided"]=="YES":
                    internet_charges=266
                else:
                    internet_charges=0
                pdf.new_tenant_recipt(lst[0],str(datetime.date.today()),room_data.loc[room_ID,"rent"],internet_charges,500,250)
                current_date = datetime.date.today()
                one_month_later = current_date.replace(month=current_date.month+1)
                sq.change_rent_paid_till(str(one_month_later),room_ID)
                sq.set_current_active(room_ID,lst[0])
            if g.get_function_value()=="Quit":
                run=False
            if g.get_function_value()=="Generate_Bill":
                tmsg.showerror("No tenant","there is currently no tenant in this room please add tenant first")
            if g.get_function_value()=="Generate_recipt":
                tmsg.showerror("No tenant","there is currently no tenant in this room please add tenant first")
            if g.get_function_value()=="Mark_as_empty":
                tmsg.showerror("No tenant","there is currently no tenant in this room please add tenant first")
            if g.get_function_value()=="Edit_property_Details":
                g.ask_room_details()
                lst=g.get_value()
                sq.update_room_detail(lst)
        else:
            tenant_data=sq.get_tenant_details(room_data.loc[room_ID,"currently_occupied"])
            g.show_room_details(str(tenant_data.iloc[0,0]),str(tenant_data.iloc[0,3]),str(tenant_data.iloc[0,4]))
            if g.get_function_value()=="Add_tenant":
                g.ask_tenant_details()
                lst=g.get_value()
                lst.insert(-1,room_ID)
                lst.append("NULL")
                sq.add_tenant(lst,room_ID)
                if room_data.loc[room_ID,"internet_provided"]=="YES":
                    internet_charges=266
                else:
                    internet_charges=0
                pdf.new_tenant_recipt(lst[0],str(datetime.date.today()),room_data.loc[room_ID,"rent"],internet_charges,500,250)
                current_date = datetime.date.today()
                one_month_later = current_date.replace(month=current_date.month+1)
                sq.change_rent_paid_till(str(one_month_later),room_ID)
                sq.set_current_active(room_ID,lst[0])
            if g.get_function_value()=="Quit":
                run=False
            if g.get_function_value()=="Edit_property_Details":
                g.ask_room_details()
                lst=g.get_value()
                sq.update_room_detail(lst)
            if g.get_function_value()=="Generate_Bill":
                if room_data.loc[room_ID,"internet_provided"]=="YES":
                    internet_charges=266
                else:
                    internet_charges=0
                date=datetime.date.today()
                last_date=str(tenant_data.iloc[0,5])
                paid_till=date_obj = datetime.strptime(last_date, '%Y-%m-%d')
                room_data.loc[room_ID,"rent"]
                rent=room_data.loc[room_ID,"rent"]*(date.month-paid_till.month)
                g.ask_current_unit()
                current_unit=g.get_function_value()
                pdf.generate_Bill(room_data.loc[room_ID,"currently_occupied"],str(date),rent,internet_charges,room_data.loc[room_ID,"last_electricity_unit"],current_unit,tenant_data.iloc[0,4])
            if g.get_function_value()=="Generate_recipt":
                if room_data.loc[room_ID,"internet_provided"]=="YES":
                    internet_charges=266
                else:
                    internet_charges=0
                date=datetime.date.today()
                last_date=str(tenant_data.iloc[0,5])
                paid_till=date_obj = datetime.strptime(last_date, '%Y-%m-%d')
                room_data.loc[room_ID,"rent"]
                rent=room_data.loc[room_ID,"rent"]*(date.month-paid_till.month)
                g.ask_current_unit_amount()
                datalist=g.get_function_value()
                current_unit=datalist[0].get()
                amount_paid=datalist[1].get()
                total =tenant_data.iloc[0,4]+ rent + internet_charges + (float(current_unit)-float(room_data.loc[room_ID,"last_electricity_unit"]))*7.5
                balance=total-amount_paid
                pdf.generate_invoice(room_data.loc[room_ID,"currently_occupied"],date,rent,internet_charges,room_data.loc[room_ID,"last_electricity_unit"],current_unit,amount_paid,balance,tenant_data.iloc[0,4])
                sq.add_payment(room_ID,room_data.loc[room_ID,"currently_occupied"],str(date),current_unit,balance)
            if g.get_function_value()=="Mark_as_empty":
                date=datetime.date.today()
                sq.set_empty(room_ID,room_data.loc[room_ID,"currently_occupied"],date)
            if g.get_function_value()=="Edit_property_Details":
                g.ask_room_details()
                lst=g.get_value()
                sq.update_room_detail(lst)
sq.close_connection()