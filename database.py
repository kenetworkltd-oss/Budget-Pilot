import mysql.connector 
import os
from dotenv import load_dotenv
load_dotenv("pword.env") # This tells Python to read your specific file

#store config settings info into  dictionary
be_settings = {
    "host" :"localhost",
    "user":"root",
    "password" :os.getenv("BE_PASSWORD"),
    "database" :"budget_expeno"  
}

# return the above into a single func for reuse by unpacking the dict into sql database connector
def database_connector():
    return mysql.connector.connect(**be_settings) 
   
   
# Start Database Creation & Table 
def create_database():
    conbe = mysql.connector.connect(**be_settings) # unpack the dict to sql database connector
    cursor = conbe.cursor()
    
    #CREATE a database Name and use it
    cursor.execute("CREATE DATABASE IF NOT EXISTS budget_expeno")
    cursor.execute( "USE budget_expeno" )
    
    #CREATE a TABLE in the database
    cursor.execute(" CREATE TABLE IF NOT EXISTS expenses ( id INT AUTO_INCREMENT PRIMARY KEY,  date DATE, category VARCHAR(50), amount DECIMAL(12, 2), description TEXT, payment_method VARCHAR (50) )")
    
    conbe.commit() #to save the changes made to the database
    conbe.close() #to close the connection to the database
    
    
