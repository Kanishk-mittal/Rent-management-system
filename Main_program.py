import SQL_connection as sq
import GUI as g

#initialising database for our program 
sq.start_connection()
sq.initialise()

#requesting password and checking it 
if g.ask_log_in():
    #here the user is authorised and we can perform our tasks
    room_data=sq.get_room_data()
    choise=g.showrooms(room_data[["Room_name","currently_occupied","occupied_by"]])
    print(g.get_function_value())
