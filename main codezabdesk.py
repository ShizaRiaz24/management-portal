from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("1250x700+0+0")
root.title("UMS")
root.configure(bg='white')
root.state('zoomed')

# Contains the frame/page after buttons are clicked
mainframe = Frame(root) #highlightbackground='#3A5FCD')
mainframe.pack(side=LEFT)
mainframe.pack_propagate(False)
mainframe.configure(width=1250, height=700)

# Option label
optionframe = Frame(root, bg='#8A360F')
optionframe.place(x=10, y=115, width=300, height=490)


# Home page
def homepage():
    deletepages()
    homeframe = Frame(mainframe)
    homeframe.pack()
    
    btn_logout.place(x=1100, y=10, height=30, width=100)
    
    btn_home.place(x=40, y=30, width=200, height=50)
    
    fop = Button(mainframe, text='FOP', font=("Times New Roman", 20), bg='#8A360F', fg="white",
                 cursor="hand2", command=foppage)
    fop.place(x=450, y=150, width=220, height=170)
    
    coal = Button(mainframe, text='COAL', font=("Times New Roman", 20), bg='#8A360F', fg="white",
                  cursor="hand2", command=coalpage)
    coal.place(x=750, y=150, width=220, height=170)
    
    oop = Button(mainframe, text='OOP', font=("Times New Roman", 20), bg='#8A360F', fg="white",
                 cursor="hand2", command=ooppage)
    oop.place(x=450, y=350, width=220, height=170)
    
    datastr = Button(mainframe, text='DSA', font=("Times New Roman", 20), bg='#8A360F', fg="white", cursor="hand2", command=dspage)
    datastr.place(x=750, y=350, width=220, height=170)
    
    # Back button
    btn_back = Button(mainframe, text="BACK", font=("Times New Roman", 20), bg='#8A360F', 
                      fg="white", cursor="hand2", command=backpage)
    btn_back.place(x=1100, y=690, height=50, width=100)
    
    homeframe.pack(pady=20)

# Information page
def infopage():
    deletepages()
    infoframe = Frame(mainframe)
    infoframe.pack()
    
    lb = Label(infoframe, text='Attendence', font=('bold', 30))
    lb.pack()
    lbl = Label(infoframe, text="Founded in 1992", font=('plain', 20))
    lbl.pack()

# Activity page
def activitypage():
    deletepages()
    activityframe = Frame(mainframe)
    activityframe.pack()
   
    clp = Button(mainframe, text='Current Lecture progress', font=("Times New Roman", 18),
                 bg='#8A360F', fg="white",cursor="hand2", command=foppage)
    clp.place(x=450, y=250, width=270, height=230)
    
    nlp = Button(mainframe, text='Next Lecture progress', font=("Times New Roman", 18), bg='#8A360F', fg="white",
                  cursor="hand2", command=coalpage)
    nlp.place(x=750, y=250, width=270, height=230)
    
    # Back button
    btn_back = Button(mainframe, text="BACK", font=("Times New Roman", 20), bg='#8A360F',
                      fg="white", cursor="hand2", command=backpage)
    btn_back.place(x=1100, y=690, height=50, width=100)

# About Us page
def aboutuspage():
    deletepages()
    aboutusframe = Frame(mainframe)
    aboutusframe.pack()
    
    lb = Label(aboutusframe, text='About Us', font=('bold', 30))
    lb.pack()
    lbl = Label(aboutusframe, text="Contact: +92......", font=('plain', 20))
    lbl.pack()
    lbe1 = Label(aboutusframe, text="Location: Hyderabad", font=('plain', 20))
    lbe1.pack()

# Subject pages
def foppage():
    deletepages()
    fopframe = Frame(mainframe)
    fopframe.pack()
    
    lb = Label(fopframe, text='Fundamentals of Programming', font=('bold', 30))
    lb.pack()
    lbl = Label(fopframe, text="C++", font=('plain', 20))
    lbl.pack()
    
    # Back button
    btn_back = Button(fopframe, text="BACK", font=("Times New Roman", 20), bg='#8A360F',
                      fg="white", cursor="hand2", command=homepage)
    btn_back.place(x=1100, y=630, height=50, width=100)
    btn_back.pack(pady=20)

def ooppage():
    deletepages()
    oopframe = Frame(mainframe)
    oopframe.pack()
    
    lb = Label(oopframe, text='Object Oriented Programming', font=('bold', 30))
    lb.pack()
    lbl = Label(oopframe, text="Java", font=('plain', 20))
    lbl.pack()
    
    # Back button
    btn_back = Button(oopframe, text="BACK", font=("Times New Roman", 20), bg='#8A360F', 
                      fg="white", cursor="hand2", command=homepage)
    btn_back.place(x=1100, y=630, height=50, width=100)
    btn_back.pack(pady=20)

def coalpage():
    deletepages()
    coalframe = Frame(mainframe)
    coalframe.pack()
    
    lb = Label(coalframe, text='Assembly language', font=('bold', 30))
    lb.pack()
    lbl = Label(coalframe, text="0,1", font=('plain', 20))
    lbl.pack()
    
    # Back button
    btn_back = Button(coalframe, text="BACK", font=("Times New Roman", 20), bg='#8A360F', 
                      fg="white", cursor="hand2", command=homepage)
    btn_back.place(x=1100, y=690, height=50, width=100)
    btn_back.pack(pady=20)

def dspage():
    deletepages()
    dsframe = Frame(mainframe)
    dsframe.pack()
   
    lb = Label(dsframe, text='Algorithm', font=('bold', 30))
    lb.pack()
    lbl = Label(dsframe, text="Python", font=('plain', 20))
    lbl.pack()
    
    # Back button
    btn_back = Button(dsframe, text="BACK", font=("Times New Roman", 20), bg='#8A360F', 
                      fg="white", cursor="hand2", command=homepage)
    btn_back.place(x=1100, y=690, height=50, width=100)
    btn_back.pack(pady=20)

def change_password_page():
    deletepages()
    change_password_frame = Frame(mainframe, bg='white')
    change_password_frame.pack()
    
    # Title
    title = Label(mainframe, text="Change Password or Update Secret Question", bg='#8A360F',
                  fg="white", font=("times new roman", 15, "bold"), pady=2)
    title.pack()
                   
    # Frame F1
    F1 = LabelFrame(mainframe, bg='#8A360F')
    F1.place(x=10, y=100, relwidth=0.95)
    
    name_lbl = Label(F1, text="Name", bg="#8A360F", fg="white", font=("times new roman", 10, "bold"))
    name_lbl.pack()
   # name_lbl.grid(row=0, column=0, pady=10, padx=20)
    
    cname_txt = Label(F1, text="Mr Humair Bughio", bg="#8A360F", fg="white", font="arial 15")
    cname_txt.pack()
    # cname_txt.grid(row=0, column=1, pady=10, padx=20)
                   
    # Frame F2
    F2 = LabelFrame(mainframe, bg='#8A360F')
    F2.place(x=90, y=20, relwidth=0.95)
    
    sem_lbl = Label(F2, text="Semester", bg="#8A360F", fg="white", font=("times new roman", 10, "bold"))
    sem_lbl.grid(row=0, column=0, pady=10, padx=20)
    
    sem_txt = Label(F2, text="Fall-2023", bg="#074463", fg="white", font="arial 15")
    sem_txt.grid(row=0, column=1, pady=10, padx=20)
                   
    # Frame F3
    F3 = LabelFrame(mainframe, bg='#074463')
    F3.place(y=260, relwidth=0.95)
    
    sem_lbl = Label(F3, text="Change Password", bg="#074463", fg="White", font=("times new roman", 30, "bold"))
    sem_lbl.pack(pady=10, padx=20, anchor="center")
            
    # Frame F4
    F4 = LabelFrame(mainframe, bg='#074463')
    F4.place(x=10, y=340, relwidth=0.95)
    
    Program_lbl = Label(F4, text="Old Password:", bg="#074463", fg="white", font=("times new roman", 20, "bold"))
    Program_lbl.grid(row=0, column=0, pady=10, padx=20)
    
    Program_txt = Entry(F4, width=45, bd=20, font=("arial", 20), bg="lightgray")  # Change background color
    Program_txt.grid(row=0, column=1, pady=10, padx=20)
    
    # Frame F5
    F5 = LabelFrame(mainframe, bg='#074463')
    F5.place(x=10, y=420, relwidth=0.95)
    
    New_Password_lbl = Label(F5, text="New Password:", bg="#074463", fg="white", font=("times new roman", 20, "bold"))
    New_Password_lbl.grid(row=0, column=0, pady=10, padx=20)
    
    New_Password_txt = Entry(F5, width=45, bd=20, font=("arial", 20), bg="lightgray")  # Change background color
    New_Password_txt.grid(row=0, column=1, pady=10, padx=20)
    
    # Frame F6
    F6 = LabelFrame(mainframe, bg='#074463')
    F6.place(x=10, y=500, relwidth=0.95)
    
    Retype_password_lbl = Label(F6, text="Retype new Password", bg="#074463", fg="white", font=("times new roman", 20, "bold"))
    Retype_password_lbl.grid(row=0, column=0, pady=10, padx=20)
    
    Retype_password_txt = Entry(F6, width=45, bd=20, font=("arial", 20), bg="lightgray")  # Change background color
    Retype_password_txt.grid(row=0, column=1, pady=10, padx=20)
    
    # Frame F7
    F7 = LabelFrame(mainframe, bg='#074463')
    F7.place(x=10, y=580, relwidth=0.95)
    
    Secrect_Question_lbl = Label(F7, text="Secret Question", bg="#074463", fg="white", font=("times new roman", 20, "bold"))
    Secrect_Question_lbl.grid(row=0, column=0, pady=10, padx=20)
    
    choices = ["Mother Birth Place", "Favorite Color", "Favorite Teacher", "Birth Place", "Favorite Place"]
    selected_choices = StringVar()
    
    Secrect_Question_combo = ttk.Combobox(F7, textvariable=selected_choices,values=choices,
                                          state="readonly", font=("Arial", 15))
    Secrect_Question_combo.set("Select a security question...")
    Secrect_Question_combo.grid(row=0, column=1, pady=10, padx=20)
            
    # Frame F8
    F8 = LabelFrame(mainframe, bg='#074463')
    F8.place(x=10, y=660, relwidth=0.95)
    
    answer_lbl = Label(F8, text="Answer", bg="#074463", fg="white", font=("times new roman", 20, "bold"))
    answer_lbl.grid(row=0, column=0, pady=10, padx=20)
    
    answer_password_txt = Entry(F8, width=45, bd=20, font=("arial", 20), bg="lightgray")  # Change background color
    answer_password_txt.grid(row=0, column=1, pady=10, padx=20)
    
    # Frame F9
    F9 = LabelFrame(mainframe, bg='#074463')
    F9.place(x=500, y=750, relwidth=0.4)
    
    change_password_btn = Button(F9, text="Change Password", bg="#1C2833", fg="white", font=("Arial", 20), pady=10)  # Change button color
    change_password_btn.grid(row=0, column=0, pady=10, padx=20)
            
    Reset_btn = Button(F9, text="Reset", font=("arial", 20), pady=10)
    Reset_btn.grid(row=0, column=1, pady=10, padx=20)

    # Back button
    btn_back = Button(change_password_frame, text="BACK", font=("Times New Roman", 20), bg='#3A5FCD', 
                      fg="white", cursor="hand2", command=backpage)
    btn_back.place(x=1100, y=690, height=50, width=100)
    
    
def clp_page():
    deletepages()
    clp_frame = Frame(mainframe, bg='white')
    clp_frame.pack()
    
    btn_back = Button(mainframe, text="BACK", font=("Times New Roman", 20), bg='#3A5FCD', 
                      fg="white", cursor="hand2", command=activitypage)
    btn_back.place(x=1100, y=690, height=50, width=100)
    
    # Title
    title = tk.Label(mainframe, text="Lecture Progress", bg='blue', fg="white",
                     font=("times new roman", 30, "bold"), pady=2)
    title.pack(fill=tk.X)

    # Frame F1
    F1 = ttk.LabelFrame(mainframe)
    F1.place(x=0, y=100, relwidth=1)

    name_lbl = tk.Label(F1, width=30, text="Name", bg="blue", fg="white",
                        font=("times new roman", 20, "bold"))
    name_lbl.grid(row=0, column=0, pady=0, padx=0)

    cname_txt = tk.Label(F1, width=50, text="Mr Humair Bughio", font="arial 15")
    cname_txt.grid(row=0, column=1, pady=5, padx=10)

    # Frame F2
    F2 = ttk.LabelFrame(mainframe)
    F2.place(x=0, y=140, relwidth=1)

    sem_lbl = tk.Label(F2, width=30, text="Semester", bg="blue", fg="white",
                       font=("times new roman", 20, "bold"))
    sem_lbl.grid(row=0, column=0, pady=0, padx=0)

    sem_txt = tk.Label(F2, width=50, text="Fall-2023", font="arial 15")
    sem_txt.grid(row=0, column=1, pady=0, padx=0)

    # Frame F3
    F3 = ttk.LabelFrame(mainframe)
    F3.place(x=0, y=220, relwidth=1)

    Program_lbl = tk.Label(F3, width=30, text="Program :", bg="blue", fg="white",
                           font=("times new roman", 20, "bold"))
    Program_lbl.grid(row=0, column=0, pady=0, padx=0)

    Program_txt = tk.Label(F3, width=20, text="BSC/BS-3", font="arial 15")
    Program_txt.grid(row=0, column=1, pady=0, padx=0)

    Section_lbl = tk.Label(F3, width=20, text="Section", bg="blue", fg="white",
                           font=("times new roman", 20, "bold"))
    Section_lbl.grid(row=0, column=2, padx=20, pady=0)

    Section_txt = tk.Label(F3, width=15, text="A", font="arial 15")
    Section_txt.grid(row=0, column=5, pady=5, padx=10)

    # Frame F4
    F4 = ttk.LabelFrame(mainframe)
    F4.place(x=0, y=260, relwidth=1)

    Course_lbl = tk.Label(F4, width=30, text="Course:", bg="blue", fg="white",
                          font=("times new roman", 20, "bold"))
    Course_lbl.grid(row=0, column=0, pady=0, padx=0)

    Course_txt = tk.Label(F4, width=50,
                          text="Computer Organization and Assembly Language", font="arial 15")
    Course_txt.grid(row=0, column=1, pady=0, padx=0)

    # Frame F5
    F5 = ttk.LabelFrame(mainframe)
    F5.place(y=350, relwidth=1)

    sem_lbl = tk.Label(F5, width=100, text="Previous Lecture Progress", fg="black",
                       font=("times new roman", 20, "bold"))
    sem_lbl.grid(pady=0, padx=0)

    # Frame F6
    F6 = ttk.LabelFrame(mainframe)
    F6.place(y=400, relwidth=1)

    data = [(1, 'Aug 21 2023', '08:15', '11:15', 'Held', 3.0)]
    col_names = ["Lecture NO.", "Date", "Class Start Time", "Class Finish Time", 
                 "Held/Cancelled/Rescheduled","Accumulated Hour"]
    total_rows = len(data)
    total_columns = len(data[0])

    for i in range(total_rows):
        for j in range(total_columns):
            label = tk.Label(F6, text=col_names[j], font=("arial", 14, "bold"))
            label.grid(row=0, column=j, padx=5, pady=5)

            label = tk.Label(F6, text=data[i][j], font=("arial", 14))
            label.grid(row=i + 1, column=j, padx=5, pady=5)
            
def nlp_page():
    deletepages()
    nlp_frame = Frame(mainframe, bg='white')
    nlp_frame.pack()

    total_rows = len(data) // 2  # Divide by 2 since there are 2 columns
    total_columns = 2

    F5 = ttk.LabelFrame(mainframe)
    F5.place(y=350, relwidth=1)

    sem_lbl = tk.Label(F5, width=100, text="Next Lecture Progress", fg="black",
                       font=("times new roman", 20, "bold"))
    sem_lbl.pack(pady=0, padx=0)

    for i in range(total_rows):
        row_frame = Frame(F5, bg='white')
        row_frame.pack(fill='both', expand=True)

        for j in range(total_columns):
            label = tk.Label(row_frame, text=labels_data[i * total_columns + j], font=("arial", 14))
            label.pack(side=LEFT, padx=5, pady=5)

    btn_back = Button(mainframe, text="BACK", font=("Times New Roman", 20), bg='#3A5FCD',
                      fg="white", cursor="hand2", command=backpage)
    btn_back.place(x=1100, y=690, height=50, width=100)




            
# Deleting the widgets in the mainframe while switching to the next page
def deletepages():
    for widget in mainframe.winfo_children():
        widget.destroy()

# Navigation functions
def change_frame(new_frame):
    deletepages()
    new_frame()

def backpage():
    deletepages()
    homepage()
    activitypage()

# Szabist label
title = Label(root, text="TEKNOFEST", font=("Times New Roman", 30, "bold"), bg='white', 
              fg="#8A360F", anchor="w", padx=20, bd=2)
title.place(x=0, y=0, relwidth=1, height=50)

# Header
title = Label(root, text="FACULTY PORTAL", font=("Times New Roman", 20, "bold"), 
              bg='#8A360F', fg="white", anchor="w", padx=20, bd=2, relief="ridge")
title.place(x=0, y=50, relwidth=1, height=50)

# Footer
title = Label(root, text="All Copyright © TEKNOFETS Reserved", font=("Times New Roman", 10, 
                        "bold"), bg='#8A360F', fg="white", bd=2, relief="ridge")
title.place(x=0, y=620, relwidth=1, height=40)

# Home button
btn_home = Button(optionframe, text="Course", font=("Times New Roman", 20), bg='#8A360F', fg="white", cursor="hand2", command=homepage)
btn_home.place(x=40, y=30, width=200, height=50)

# Info button
btn_info = Button(optionframe, text="Information", font=("Times New Roman", 20),
                bg='#8A360F', fg="white", cursor="hand2", command=infopage)
btn_info.place(x=40, y=100, width=200, height=50)

# ACTIVITY BUTTON
btn_act = Button(optionframe, text="Activity", font=("Times New Roman", 20), bg='#8A360F', fg="white", cursor="hand2", command=activitypage)
btn_act.place(x=40, y=170, width=200, height=50)

# Password BUTTON
btn_pass = Button(optionframe, text="Change password", font=("Times New Roman", 20), bg='#8A360F', fg="white", cursor="hand2", command=change_password_page)
btn_pass.place(x=40, y=240, width=200, height=50)

# About BUTTON
btn_about = Button(optionframe, text="About", font=("Times New Roman", 20), bg='#8A360F', fg="white", cursor="hand2", command=aboutuspage)
btn_about.place(x=40, y=310, width=200, height=50)

# Szabist title
title = Label(optionframe, text="Teknofest", font=("Times New Roman", 40, "bold"), bg='#8A360F', fg="WHITE")
title.place(x=10, y=400)

def logout():
    root.destroy()

btn_logout = Button(root, text='Logout', font=("Times New Roman", 10), bg='#8A360F', fg="white", 
                    cursor="hand2", command=logout)
btn_logout.place(x=1100, y=10, height=30, width=100)

root.mainloop()