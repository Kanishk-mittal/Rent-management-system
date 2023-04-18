import SQL_connection as sq
import GUI as g
import createpdf as pdf
import datetime

#initialising database for our program 
sq.start_connection()
sq.initialise()

#requesting password and checking it 
if g.ask_log_in():
    #here the user is authorised and we can perform our tasks
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
    else:
        print(room_data.loc[g.get_function_value(),"occupied_by"])
        tenant_data=sq.get_tenant_details(room_data.loc[g.get_function_value(),"occupied_by"])
        g.show_room_details(str(tenant_data.loc[1,"Name"]),str(tenant_data.loc[1,'last_balance']),str(tenant_data.loc[1,'rent_paid_till']))
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
sq.close_connection()