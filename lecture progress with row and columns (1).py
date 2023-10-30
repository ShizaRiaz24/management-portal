#LECTURE PROGRESS
from tkinter import *
from tkinter import ttk

class Zabdest:

    def  __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("UMS")
        bg_color = "#074463"
        
        # Title
        title = Label(self.root, text="Lecture Progress", bg='#8A360F', fg="white", font=("times new roman", 30, "bold"), pady=2)
        title.pack(fill=X)
            
        # Frame F1
        F1 = LabelFrame(self.root)
        F1.place(x=0, y=100, relwidth=1)
        
        name_lbl = Label(F1, width=30, text="Name", bg="#8A360F", fg="white", font=("times new roman", 20, "bold"))
        name_lbl.grid(row=0, column=0, pady=0, padx=0)
        
        cname_txt = Label(F1, width=50, text="Mr Humair Bughio", font="arial 15")
        cname_txt.grid(row=0, column=1, pady=5, padx=10)
           
        # Frame F2
        F2 = LabelFrame(self.root)
        F2.place(x=0, y=140, relwidth=1)
        
        sem_lbl = Label(F2, width=30, text="Semester", bg="#8A360F", fg="white", font=("times new roman", 20, "bold"))
        sem_lbl.grid(row=0, column=0, pady=0, padx=0)
        
        sem_txt = Label(F2, width=50, text="Fall-2023", font="arial 15")
        sem_txt.grid(row=0, column=1, pady=0, padx=0)
        
        # Frame F3
        F3 = LabelFrame(self.root)
        F3.place(x=0, y=220, relwidth=1)
        
        Program_lbl = Label(F3, width=30, text="Program :", bg="#8A360F", fg="white", font=("times new roman", 20, "bold"))
        Program_lbl.grid(row=0, column=0, pady=0, padx=0)
        
        Program_txt = Label(F3, width=20, text="BSC/BS-3", font="arial 15")
        Program_txt.grid(row=0, column=1, pady=0, padx=0)
        
        Section_lbl = Label(F3, width=20, text="Section", bg="#8A360F", fg="white", font=("times new roman", 20, "bold"))
        Section_lbl.grid(row=0, column=2, padx=20, pady=0)
        
        Section_txt = Label(F3, width=15, text="A", font="arial 15")
        Section_txt.grid(row=0, column=5, pady=5, padx=10)
        
        # Frame F4
        F4 = LabelFrame(self.root)
        F4.place(x=0, y=260, relwidth=1)
        
        Course_lbl = Label(F4, width=30, text="Course:", bg="#8A360F", fg="white", font=("times new roman", 20, "bold"))
        Course_lbl.grid(row=0, column=0, pady=0, padx=0)
        
        Course_txt = Label(F4, width=50, text="Computer Organization and Assembly Language", font="arial 15")
        Course_txt.grid(row=0, column=1, pady=0, padx=0)
        
        # Frame F5
        F5 = LabelFrame(self.root)
        F5.place(y=350, relwidth=1)
        
        sem_lbl = Label(F5, width=100, text="Previous Lecture Progress", fg="black", font=("times new roman", 20, "bold"))
        sem_lbl.grid(pady=0, padx=0)
        
        # Frame F6
        F6 = LabelFrame(self.root)
        F6.place(y=400, relwidth=1)
        
        data = [(1, 'Aug 21 2023', '08:15', '11:15', 'Held', 3.0)]
        col_names = ["Lecture NO.", "Date", "Class Start Time", "Class Finish Time", "Held/Cancelled/Rescheduled", "Accumulated Hour"]
        total_rows = len(data)
        total_columns = len(data[0])
        
        for i in range(total_rows):
            for j in range(total_columns):
                label = Label(F6, text=col_names[j], font=("arial", 14, "bold"))
                label.grid(row=0, column=j, padx=5, pady=5)
                
                label = Label(F6, text=data[i][j], font=("arial", 14))
                label.grid(row=i+1, column=j, padx=5, pady=5)


if __name__ == "__main__":
    root = Tk()
    obj = Zabdest(root)
    root.mainloop()
