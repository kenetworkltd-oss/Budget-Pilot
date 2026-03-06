from database import database_connector #from database file, we import database-connector(): def func
import matplotlib.pyplot as be #matplot lib/mod will help us plot all the chart for users, (be) is the aliasing to draw plot

# BAR CHART def func recipes
def bar_chart(): #all recipes for  bar chart under this def func
    conbe = database_connector()  #opening the database connection by calling out def func we imported as modules
    cursor = conbe.cursor() #put it into the SQL command (Cursor) , the keyword that talk to the sql database opening
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category") ##using SELECT SQL command to get data (amount, category & group each row seprately) for the chart/plot
    database_data = cursor.fetchall() ##fetch it all and put it inside (datbse_data) variable
    cursor.close() #close the SQL execution
    conbe.close() #close the SQL database
    
    #our safety mode for crashing/error
    if not database_data: #means if there is no any data it fetch
        print("No data available for a Bar Chart yet!") #print NO data available
        return #retun back to basic (main.py)
     
    #Comphrension list
    category = [row[0] for row in database_data] #put all the category data you find in database  & put it into variable (category)
    amount =  [row[1] for row in database_data] #put all the amount data you find in database  & put it into variable (amount)
    
    be.figure(figsize=(10, 6)) #Size of the charts
    be.bar(category, amount, color = "blue")  #Calling and styling the bar chart (plt.bar)
    be.title("The Expenses Bar-view") #Title of the bar chart
    be.xlabel("Category") #label for x
    be.ylabel("Amount") #label for  y line 
    be.show( )  #The display or print of the bar chart
    

        
# PIE CHART def func recipes     
def pie_chart():
    conbe = database_connector()  #opening the database connection by calling out def func we imported as modules
    cursor = conbe.cursor() #put it into the SQL command (Cursor) , the keyword that talk to the sql database opening
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category") ##using SELECT SQL command to get data (amount, category & group each row seprately) for the chart/plot
    database_data = cursor.fetchall() ##fetch it all and put it inside (datbse_data) variable
    cursor.close() #close the SQL execution
    conbe.close() #close the SQL database
    
    #our safety mode for crashing/error
    if not database_data: #means if there is no any data it fetch
        print("No data available for Pie Chart yet!") #print NO data available
        return #retun back to basic (main.py)
    
    #Comphrension list
    category = [row[0] for row in database_data] #put all the category data you find in database  & put it into variable (category)
    amount =  [row[1] for row in database_data] #put all the amount data you find in database  & put it into variable (amount)
    
    be.pie(amount, labels=category, autopct='%1.1f%%', startangle=140) #in percent%, starting from 140 degree in circle
    be.title("The Expenses Pie-view") #Title of the pie chart
    be.axis("equal") #making sure the circle shape are in equal size, no part is more bigger than any other
    be.show() #display or print the pie chart
    