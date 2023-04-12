import SQL_connection as sq
import GUI as g

#initialising database for our program 
sq.initialise()

#requesting password and checking it 
if g.ask_log_in():
    #here the user is authorised and we can perform our tasks
    pass
