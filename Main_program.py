import SQL_connection as sq
import GUI as g

#initialising database for our program 
sq.start_connection()
sq.initialise()

#requesting password and checking it 
if g.ask_log_in():
    #here the user is authorised and we can perform our tasks
    room_data=sq.get_room_data()
    print(room_data)
    choise=g.showrooms(room_data[["Room_name","currently_occupied","occupied_by"]])
    if int(g.get_function_value()) ==1:
        if room_data.loc[1,"currently_occupied"]=="NO":
            g.show_room_details("NULL","NULL","NULL")
        else:
            tenant_data=sq.get_tenant_details(room_data.loc[1,"occupied_by"])
            g.show_room_details(str(tenant_data.Name),str(tenant_data.last_balance),str(tenant_data.rent_paid_till))
    elif int(g.get_function_value()) ==2:
        if room_data.loc[2,"currently_occupied"]=="NO":
            g.show_room_details("NULL","NULL","NULL")
        else:
            tenant_data=sq.get_tenant_details(room_data.loc[1,"occupied_by"])
            g.show_room_details(str(tenant_data.Name),str(tenant_data.last_balance),str(tenant_data.rent_paid_till))
    elif int(g.get_function_value()) ==3:
        if room_data.loc[3,"currently_occupied"]=="NO":
            g.show_room_details("NULL","NULL","NULL")
        else:
            tenant_data=sq.get_tenant_details(room_data.loc[1,"occupied_by"])
            g.show_room_details(str(tenant_data.Name),str(tenant_data.last_balance),str(tenant_data.rent_paid_till))
    elif int(g.get_function_value()) ==4:
        if room_data.loc[4,"currently_occupied"]=="NO":
            g.show_room_details("NULL","NULL","NULL")
        else:
            tenant_data=sq.get_tenant_details(room_data.loc[1,"occupied_by"])
            g.show_room_details(str(tenant_data.Name),str(tenant_data.last_balance),str(tenant_data.rent_paid_till))
    elif int(g.get_function_value()) ==5:
        if room_data.loc[3,"currently_occupied"]=="NO":
            g.show_room_details("NULL","NULL","NULL")
        else:
            tenant_data=sq.get_tenant_details(room_data.loc[1,"occupied_by"])
            g.show_room_details(str(tenant_data.Name),str(tenant_data.last_balance),str(tenant_data.rent_paid_till))
            

sq.close_connection()