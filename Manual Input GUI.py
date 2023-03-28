import tkinter as tk
import csv
import time
import datetime
from tkinter import simpledialog

def ask_user():
    # Use the simpledialog module to create a modal dialog for user input
    root = tk.Tk()
    root.withdraw() # hide the main window
    
    result = simpledialog.askstring("Task Input", "What are you doing?", parent=root)
    
    # Save the user input and current time to a CSV file
    with open('activity_log.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Convert the timestamp to a more readable format
        timestamp = time.time()
        dt_object = datetime.datetime.fromtimestamp(timestamp)
        dt_string = dt_object.strftime("%Y-%m-%d %H:%M:%S")
        
        # Write the timestamp and user input to the CSV file
        writer.writerow([dt_string, result])

def create_gui():
    # Create a new Tkinter window
    window = tk.Tk()
    window.title("Activity Logger")
    
    # Add a button that prompts the user for input when clicked
    button = tk.Button(window, text="Log Activity", command=ask_user)
    button.pack()
    
    # Run the Tkinter event loop
    window.mainloop()

# Call the create_gui() function to create the GUI interface
create_gui()
