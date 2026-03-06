from database import database_connector #from database file, we import database-connector(): def func
from datetime import datetime

monthly_limit = 250000  #set up a global variable for monthly use


def entry_budget(): #all budget analyzer recipe under this def func
    
    conbe = database_connector()  #bringout our sql connector using conbe
    cursor = conbe.cursor()  #wrap conbe inside cursor for sql command
    month = datetime.now().month #real time now of month into a month variable
    year = datetime.now().year #real time now of year into a year variable
    
    
    #SELECT command from sql to fetch or retrieve amount from exepenses table with month in date  & year in date
    cursor.execute("SELECT SUM(amount) FROM expenses WHERE MONTH(date) = %s AND YEAR(date) = %s", (month, year))
    
    monthly_expense = cursor.fetchone()[0] or 0 #fetch the query we made above,if there is no amount yet, the 0 should be the fallback, wrap it inside monthly_expense variable
    cursor.close() #close the SQL execution
    conbe.close() #close the SQL database
    
    print(f"\n Total amount spent this month is : {monthly_expense}")  #show total amount spent in a month
    
    if monthly_expense > monthly_limit:
       print("Warning !! you have exceeded your monthly budget ")  # show warning if monthly expense exceed limit
       
    elif monthly_expense > (monthly_limit * 0.8):  #show caution if it already 80% of the limit amount spent
       print("Caution !! you have reached 80% of your budget limit")
       
       
    return monthly_expense #to be able to use it or pass the variable later
