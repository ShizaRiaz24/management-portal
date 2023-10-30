#CHANGE PASSWORD
from tkinter import*
from tkinter import ttk


class Zabdest:

    def  __init__(self,root):
            self.root=root
            self.root.geometry("1366x768")
            self.root.title("Zabdesk")
            
            title=Label(self.root,text="Change Password or Update Secret Question",bg='#8A360F',fg="white",font=("time new roman",30,"bold"),pady=2).pack(fill=X)
            
            F1=LabelFrame(self.root,)
            F1.place(x=0,y=70,relwidth=1)
            name_lbl=Label(F1,width= 30, text="Name",bg="#8A360F",fg="white",font=("time new roman",20,"bold")).grid(row=0,column=0,pady=0,padx=0)
            cname_txt=Label(F1 ,width=50,text="Mr Humair Bughio",font="arial 15",).grid(row=0,column=1,pady=0,padx=10,)
           
            F2=LabelFrame(self.root,)
            F2.place(x=0,y=110, relwidth=1)
            sem_lbl=Label(F2,width= 30, text="Semester",bg="#8A360F",fg="white",font=("time new roman",20,"bold")).grid(row=0,column=0,pady=0,padx=0)
            sem_txt=Label(F2 ,width=50,text="Fall-2023",font="arial 15",).grid(row=0,column=1,pady=0,padx=0)
            
            F3=LabelFrame(self.root,)
            F3.place(y=160,relwidth=1)
            sem_lbl=Label(F3, width=120,text="Change Password ",bg="#8A360F",fg="White",font=("time new roman",30,"bold"))
            sem_lbl.pack(pady=0, padx=0, anchor="center")
            
            F4=LabelFrame(self.root,)
            F4.place(x=0,y=220,relwidth=1)
            Program_lbl=Label(F4,width= 30,height=2, text="Old Password:",bg="#8A360F",fg="white",font=("time new roman",20,"bold")).grid(row=0,column=0,pady=0,padx=0)
            Program_txt=Entry(F4 ,width=80, bd=20,   font="arial 20",).grid(row=0,column=1,pady=0,padx=10)
            
            F5=LabelFrame(self.root,)
            F5.place(x=0,y=280,relwidth=1)
            New_Password_lbl=Label(F5,width= 30,height=2, text="New Password:",bg="#8A360F",fg="white",font=("time new roman",20,"bold")).grid(row=0,column=0,pady=0,padx=0)
            New_Password_txt=Entry(F5 ,width=80, bd=20,   font="arial 20",).grid(row=0,column=1,pady=0,padx=10)
            
            F6=LabelFrame(self.root,)
            F6.place(x=0,y=350,relwidth=1)
            Retype_password_lbl=Label(F6,width= 30,height=2, text="Retype new Password ",bg="#8A360F",fg="white",font=("time new roman",20,"bold")).grid(row=0,column=0,pady=0,padx=0)
            Retype_password_txt=Entry(F6 ,width=80, bd=20,   font="arial 20",).grid(row=0,column=1,pady=0,padx=10)
            
            F7 = LabelFrame(self.root)
            F7.place(x=0, y=420, relwidth=1)
            Secrect_Question_lbl = Label(F7, width=30, height=2, text="Secret Question ", bg="#8A360F", fg="white",font=("time new roman", 20, "bold"))
            Secrect_Question_lbl.grid(row=0, column=0, pady=0, padx=0)
            choices = ["Mother Birth Place", "Favorite Color", "Favorite Teacher", "Birth Place", "Favorite Place"]
            selected_choices = StringVar()
            Secrect_Question_combo = ttk.Combobox(F7, textvariable=selected_choices,values=choices, state="readonly", height=150, width=100, font=("Arial", 15))
            Secrect_Question_combo.set("Select choices...")
            Secrect_Question_combo.grid(row=0, column=1, pady=0, padx=10) 
            
            
            F8=LabelFrame(self.root,)
            F8.place(x=0,y=480,relwidth=1)
            answer_lbl=Label(F8,width= 30,height=2, text="Answer ",bg="#8A360F",fg="white",font=("time new roman",20,"bold")).grid(row=0,column=0,pady=0,padx=0)
            answer_password_txt=Entry(F8 ,width=80, bd=20,   font="arial 20",).grid(row=0,column=1,pady=0,padx=10)
            
            F9=LabelFrame(self.root)
            F9.place(x=500,y=580,relwidth=1)
            change_password_btn =Button(F9, text="Change Password", bg="#8A360F", fg="white", font=("Arial", 20))
            change_password_btn.grid(row=0, column=0, pady=10, padx=10)
            Reset_btn=Button(F9 ,text="Reset",font=("arial ",20)).grid(row=0,column=1,pady=0,padx=0)
        
            
            
 
            
root=Tk()
obj = Zabdest(root)

root.mainloop()