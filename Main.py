import database  #import (databse.py) file as a modules
import exepenses #import (exepenses.py) file as a modules
import budget   #import (budget.py) file as a modules
import visual   #import (visual.py) file as a modules
from datetime import datetime 


def main_menu(): #def func for budget-expeno menu
    print("WELCOME to Budget Expeno ")
    
    
    while True:
        print("\n Main Menu Select between (1-4)")
        print("1. Log Daily Expenses ")
        print("2. Check Monthly Budget Status")
        print("3. View Chart of your Expenses (bar/pie")
        print("4. Exit")
        
        choice = input("Select an option: ")
 
        if choice == "1":
            exepenses.entry_exepenses()
        
        
        elif choice == "2":
            budget.entry_budget()
            
            
        elif choice == "3":  
            chart_type = input("Enter chart type (bar/pie): ").lower()   
            if chart_type == "bar":
                visual.bar_chart()
            elif chart_type == "pie":
                visual.pie_chart()
            else:
                print("Enter bar or pie)")
                
                
        elif choice == "4":
            break #the loop break here

        else:
            print("Invalid Option, Enter between (1-4) ")
         
                
        
main_menu()  #Call out budget expeno apps