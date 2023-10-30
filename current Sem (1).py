#CURRENT SEMESTER
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
def create_table(root, data):
    
    custom_font1 = tkfont.Font(family="Arial", size=20)
    
    for i, row_data in enumerate(data):
        for j, text in enumerate(row_data):
            font_size = 12  # Default font size for most cells
            if i >= 1 and i <= 5:
                font_size = 18  # Larger font size for rows 2 to 5
            if j >= 1 and j <= 4:
                font_size = 15  # Larger font size for columns 1 to 4

            custom_font = tk.font.nametofont("TkDefaultFont")
            custom_font.configure(size=font_size)
           
            if i == 0:
                label = tk.Label(root, text=text, bg='#8A360F', fg='white',font= custom_font1 )
            elif (j == 0 and i >= 1 and i <= 6) or (j == 2 and i >= 1 and i <= 6) or (j == 3 and i >= 1 and i <= 6):
                label = tk.Label(root, text=text, fg='black')
                
                        
            else:
                label = tk.Label(root, text=text)
            label.grid(row=i, column=j, padx=0, pady=0, sticky='nsew')

# Create the main window
root = tk.Tk()
root.title("Zabdesk")
#   


# Define table data
table_data = [
    ["Course Name", "Class", "Outline", "Attendence"],
    ["Discrete Mathematical Structure      ", "BCS/ BS 3A", "Outline", "Attendence"],
    ["Multivariate Calculus", "BCS/ BS 3A", "Outline", "Attenendence"],
    ["Data Structure and Algorithms", "BCS/ BS 3A", "Outline", "Attendence"],
    ["Lab Data Structure and Algorithms", "BCS/ BS 3A", "Outline", "Attendence"],
    ["Computer Organization and Assembly Language", "BCS/ BS 3A", "Outline", "Attendence"],
    ["Management Principle", "BCS/ BS 3A", "Outline", "Attendence"],
]

for i in range(len(table_data)):
    root.grid_rowconfigure(i, weight=1)
for j in range(len(table_data[0])):
    root.grid_columnconfigure(j, weight=1)

# Create the table
create_table(root, table_data)

# Add separators between columns
for i in range(0, len(table_data)):
    sep = ttk.Separator(root, orient="vertical")
    sep.place(x=i * 539, rely=0, relheight=2.5)
    
# Add separators between rows
for i in range(1, len(table_data)):
    sep = ttk.Separator(root, orient="horizontal")
    sep.place(x=1, rely=i / len(table_data), relwidth=2)

root.mainloop()
