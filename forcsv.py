import csv
from database import database_connector #
from datetime import datetime

def export_to_csv():
    try:
        conbe = database_connector() #
        cursor = conbe.cursor()
        
        # Fetch all expenses from the database
        cursor.execute("SELECT id, date, category, amount, description, payment_method FROM expenses")
        rows = cursor.fetchall()
        
        # Create a filename with today's date
        filename = f"expenses_backup_{datetime.now().strftime('%Y-%m-%d')}.csv"
        
        # Write to CSV
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Write the header row
            writer.writerow(['ID', 'Date', 'Category', 'Amount', 'Description', 'Payment Method'])
            # Write the data rows
            writer.writerows(rows)
            
        print(f"\nSuccessfully exported {len(rows)} records to {filename}!")
        
        cursor.close()
        conbe.close()
    except Exception as e:
        print(f"Error exporting to CSV: {e}")
        
        
#export_to_csv()
        
        