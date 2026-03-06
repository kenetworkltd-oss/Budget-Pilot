from database import database_connector #from database file, we import database-connector(): def func
from datetime import datetime


#def func for user input about their exepenses and INSERT into Database 
def entry_exepenses():
    while True: #MASTER LOOP cos we have lot of line for input to interate over
        print("\n Welcome, Enter your daily expenses ") #print this welcome for user  
        
        while True:
            amount = input("Enter Amount: ").strip() #strip off empty space  to collect  value  data
            if not amount: #if there is no any value number
                print("Error: Amount cannot be empty, :")
                continue #go back and ask again for value number
            
            try: #then come and try this
                full_amount = float(amount)
                if full_amount <= 0:  #if full amount less than or equal to zero
                    print("Error Enter a positive number") #show this
                    continue # go back to the next above and request for number greater than 0
                break # if so or obey,  loop can now stop & break here
                
            except ValueError: #if try doesn't work, dont crash, print this instead of crashing (ValueError)
                print("Error: Please enter a valid number (e.g, 5000).")
                    
        while True:
            category = input("Enter Category: ").strip().capitalize() #remove whitespace and start initial with capital letter
            if len(category) < 2 or not any(char.isalnum() for char in category):# check if the lenght of the category input & character is more than 2 or is it true alphanumeric, itetrate each char in the input to confirm
                print("Error: Please enter a real category name.")
                continue #ask for category input again
            break # Exit category loop if name is correct, and jump next to below code
        
        while True:
            description = input("Enter Description: ").strip().capitalize()
            if len(description) < 2 or not any(char.isalnum() for char in description):  #confirm lenght of the data, no short char, or is it truly alphanumeric, itetrate each char in the input to confirm
                print("Error: Please enter a descriptive note (at least 2 characters).")
                continue #ask for description input again
            break  # Exit description loop if name is correct, and jump next to below code
        
        while True:
             payment_method = input("Enter Payment Method: ").strip().capitalize() 
             if len(payment_method) < 2 or not any(char.isalnum() for char in payment_method): #confirm lenght of the data, no short char, or is it truly alphanumeric, itetrate each char in the input to confirm
                print("Error: Please enter a descriptive note (at least 2 characters).") 
                continue #ask for payment_method input again
             break  # Exit payment_method loop if name is correct, and jump next to below code
        
        date = datetime.now().strftime('%Y-%m-%d') #get todays date automatically, using datetime.now modules we imported

        #REVIEW & CONFIRMATION
        print(f"\n Review Your Expenses Entry ")
        print(f"Date: {date} | Total: {full_amount} Naira")
        print(f"Category: {category} | Method: {payment_method}")
        print(f"Note: {description if description else 'N/A'}")
        
        #INSERT into Database & Table
        confirm = input("Save this to database? (y/n): ").lower() #ask user to save after review carefully
        
        if confirm == 'y': #if  user enter y which indicate yes
            #Try this first
            try:
                conbe = database_connector()  #bringout our sql connector using conbe
                cursor = conbe.cursor()    #wrap conbe inside cursor for sql command
                insert_query = "INSERT INTO expenses (date, category, amount, description, payment_method) VALUES (%s, %s, %s, %s, %s)" #put the input collected into database according to the way table was created & thier tittle
                cursor.execute(insert_query, (date, category, full_amount, description, payment_method))  #merging the table tittle and input values
                conbe.commit() #to save the insertion made to the database
                conbe.close() #to close the connection to the database
                
                print("your expenses entry has been saved successfully !!")
                break #Exit the MASTER LOOP and return to main menu
                
            except Exception as e:
                print(f" Database Error: {e}") #if error occur, show why by using the variable of (e) print it value
                break #Exit loop if database fails
                
        elif confirm == 'n':
            print("Restarting Entry... starting from Amount.")
            continue #go back to the top of the MASTER LOOP and ask for amount again
                
        else:
            print("Entry Discarded. Returning to main menu.") #back to our if statement, anything else loop exit 
            break # Exit loop for any other input