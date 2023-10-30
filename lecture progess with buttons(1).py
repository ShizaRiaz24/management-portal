#NEXT LECTURE PROGRESS
from tkinter import *
import tkinter as tk
from tkinter import ttk

class Table:

    def __init__(self, root, data):
    
        total_rows = len(data) // 2  # Divide by 2 since there are 2 columns
        total_columns = 2

        # Create the table
        self.entries = []  # To keep track of Entry widgets
        for i in range(total_rows):
            for j in range(total_columns):
                if j == 0:  # Check if it's the first column
                    self.e = Entry(root, width=40, fg='white', bg='#8A360F', font=('Arial', 20, 'bold'))
                else:
                    self.e = Entry(root, width=40, fg='black', font=('Arial', 20, 'bold'))
                self.e.grid(row=i+1, column=j)  # +1 to leave space for F5 at the top
                self.e.insert(END, data[i * 2 + j])
                self.entries.append(self.e)


labels_data = [
    "Lecture No.", "5",
    "Date", "9/15/2023",
    "Class Start Time", "Hours",
    "Class End Time", "Hours",
    "Topics Covered", "Data Movement, Arithmetic and Logic"]  

root = Tk()

# Add F5 LabelFrame and sem_lbl label at the top
F5 = ttk.LabelFrame(root)
F5.grid(row=0, column=0, columnspan=2, padx=0, pady=10)

sem_lbl = tk.Label(F5, text="Next Lecture Progress", fg="white",bg="#8A360F" ,font=("times new roman", 30, "bold"))
sem_lbl.grid(row=0, column=0, columnspan=2, padx=150, pady=10, sticky="nsew")

class_status_label = tk.Label(root, width= 35, text="Class Status", fg="white", bg="#8A360F", font=("Arial", 20, "bold"))
class_status_label.grid(row=6, column=0, padx=0, pady=0,)

            
F9 = ttk.LabelFrame(root)
F9.place(x=500, y=350, relwidth=1)
change_password_btn = Button(F9, text=" Submit ", bg="#8A360F", fg="white", font=("Arial", 20))
change_password_btn.grid(row=0, column=0, pady=10, padx=10)
Reset_btn = Button(F9, text="Reset", font=("arial ", 20))
Reset_btn.grid(row=0, column=1, pady=0, padx=0)

t = Table(root, labels_data)
# Create a Combobox for "Class Status"
class_status_var = tk.StringVar(root)
class_status_combo = ttk.Combobox(root, textvariable=class_status_var, values=["Held", "Cancelled", "Rescheduled"])
class_status_combo.grid(row=6, column=1, padx=5, pady=0, sticky="ew")  # Place the ComboBox in the 2nd column of the 6th row

# Create Combobox for hours and minutes
hours_var = tk.StringVar(root)
minutes_var = tk.StringVar(root)
hours_var1 = tk.StringVar(root)

hours_combo = ttk.Combobox(root, textvariable=hours_var, values=[str(i).zfill(2) for i in range(24)])
hours_combo1 = ttk.Combobox(root,  textvariable=hours_var1, values=[str(i).zfill(2) for i in range(24)])
minutes_combo = ttk.Combobox(root, textvariable=minutes_var, values=[str(i).zfill(2) for i in range(60)])
minutes_combo2 = ttk.Combobox(root, textvariable=minutes_var, values=[str(i).zfill(2) for i in range(60)])


hours_combo.grid(row=3, column=1, padx=100, pady=0, sticky="w")
hours_combo1.grid(row=4, column=1, padx=100, pady=0, sticky="w")
# minutes_combo.grid(row=3, column=1, padx=0, pady=0, sticky="w")
# minutes_combo.grid(row=4, column=1, padx=0, pady=0, sticky="w")
           
root.geometry("1920x1080+0+10")
root.mainloop()
