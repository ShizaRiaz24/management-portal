
#LECTURE ATTENDENCE
from tkinter import*

class Zabdesk:

    def  __init__(self,root):
            self.root=root
            self.root.geometry("1920x1080+0+0")
            self.root.title("Zabdesk")
            bg_color= "#8A360F"
            title=Label(self.root,text="Lecture Attendence",bg='#8A360F',fg="white",font=("time new roman",30,"bold"),pady=2).pack(fill=X)
            
            F1=LabelFrame(self.root,)
            F1.place(x=0,y=100,relwidth=1)
            name_lbl=Label(F1,width= 20, text="Name",bg="#8A360F",fg="white",font=("time new roman",20,"bold")).grid(row=0,column=0,pady=0,padx=0)
            cname_txt=Label(F1 ,width=40,text="Mr Humair Bughio",font="arial 15",).grid(row=0,column=1,pady=5,padx=10)
           
            F2=LabelFrame(self.root,)
            F2.place(x=0,y=140,relwidth=1)
            sem_lbl=Label(F2,width= 20, text="Semester",bg="#8A360F",fg="white",font=("time new roman",20,"bold")).grid(row=0,column=0,pady=0,padx=0)
            sem_txt=Label(F2 ,width=40,text="Fall-2023",font="arial 15",).grid(row=0,column=1,pady=0,padx=0)
            
            F3=LabelFrame(self.root,)
            F3.place(x=0,y=220,relwidth=1)
            Program_lbl=Label(F3,width= 20, text="Program :",bg="#8A360F",fg="white",font=("time new roman",20,"bold")).grid(row=0,column=0,pady=0,padx=0)
            Program_txt=Label(F3 ,width=40,text="BSC/BS-3",font="arial 15",).grid(row=0,column=1,pady=0,padx=0)
            Section_lbl=Label(F3,width= 10,text="Section",bg="#8A360F",fg="white",font=("time new roman",20,"bold")).grid(row=0,column=2,padx=20,pady=0)
            Section_txt=Label(F3 , width=10,text="A" ,font="arial 15",).grid(row=0,column=5,pady=5,padx=10)
            F4=LabelFrame(self.root,)
            F4.place(x=0,y=260,relwidth=1)
            Course_lbl=Label(F4,width= 20, text="Course:",bg="#8A360F",fg="white",font=("time new roman",20,"bold")).grid(row=0,column=0,pady=0,padx=0)
            Course_txt=Label(F4 ,width=40,text="Computer Organization and Assembly Language",font="arial 15",).grid(row=0,column=1,pady=0,padx=0)
            
            F5=LabelFrame(self.root,)
            F5.place(y=300,relwidth=1)
            instuctore_lbl=Label(F5,width= 20, text="Instructor: ",bg="#8A360F",fg="white",font=("time new roman",20,"bold")).grid(row=0,column=0,pady=0,padx=0)
            instuctore_txt=Label(F5 ,width=40,text="Mr Humair Bughio",font="arial 15",).grid(row=0,column=1,pady=0,padx=0, )
            
            F6 = LabelFrame(self.root)
            F6.place(y=300, relwidth=1)
        
           
            data = [("Edit", 1, '2212101', "Sara Shaikh","Present", "Present", "Present", "Present" )]
            data1 = [("Edit", 2, '2212102', "Hafsa", "Present", "Present", "Present", "Present")]
            data2 = [("Edit", 3, '2212103', "Aqsa", "Present", "Present", "Present", "Present")]
            data3 = [("Edit", 5, '2212104', "Raveena", "Present", "Present", "Present", "Present")]
            data4 = [("Edit", 6, '2212105', "Shiza", "Present", "Present", "Present", "Present")]
            data5 = [("Edit", 7, '2212106', "Umema", "Present", "Present", "Present", "Present")]
            data6 = [("Edit", 8, '2212107', "Iqra Qadir", "Present", "Present", "Present", "Present")]
            data7 = [("Edit", 9, '2212108', "Muskan ", "Present", "Present", "Present", "Present")]
            data8 = [("Edit",10, '2212109', "Areeba Laghari", "Present", "Present", "Present", "Present")]
            
            


            col_names = ["Edit.", "S.#", "Reg.# ", " Name ", "lecture# 1, Aug 21 2023", "lecture# 2, Aug 21 2023", "lecture# 3, Aug 21 2023", "lecture# 4, Aug 21 2023"]
            total_rows = len(data)
            total_columns = len(data[0])
            for i in range(total_rows):


                 for j in range(total_columns):
                    label = Label(F6, text=col_names[j], font=("arial", 14, "bold"),bg="#8A360F", fg="white")
                    label.grid(row=i, column=j, padx=5, pady=5)
                
                    label = Label(F6, text=data[i][j], font=("arial", 14))
                    label.grid(row=i+1, column=j, padx=5, pady=5)
                    
                 

        

        # Adding the second row of data
            for i in range(total_rows):
                for j in range(total_columns):
                    label = Label(F6, text=data1[i][j], font=("arial", 14))
                    label.grid(row=i+2, column=j, padx=5, pady=5)
                    
                    

        # Adding the second row of data
            for h in range(total_rows):
                for j in range(total_columns):
                    label = Label(F6, text=data2[i][j], font=("arial", 14))
                    label.grid(row=i+3, column=j, padx=5, pady=5)
                    
                            # Adding the third row of data
            for i in range(total_rows):
                for j in range(total_columns):
                    label = Label(F6, text=data3[i][j], font=("arial", 14))
                    label.grid(row=i+4, column=j, padx=5, pady=5)

                    
                      # Adding the second row of data
            for i in range(total_rows):
                for j in range(total_columns):
                    label = Label(F6, text=data4[i][j], font=("arial", 14))
                    label.grid(row=i+5, column=j, padx=5, pady=5)
                    
                    
                      # Adding the second row of data
            for i in range(total_rows):
                for j in range(total_columns):
                    label = Label(F6, text=data5[i][j], font=("arial", 14))
                    label.grid(row=i+6, column=j, padx=5, pady=5)
                    
                    
                      # Adding the second row of data
            for i in range(total_rows):
                for j in range(total_columns):
                    label = Label(F6, text=data6[i][j], font=("arial", 14))
                    label.grid(row=i+7, column=j, padx=5, pady=5)
                    
                    
                    
                      # Adding the second row of data
            for i in range(total_rows):
                for j in range(total_columns):
                    label = Label(F6, text=data7[i][j], font=("arial", 14))
                    label.grid(row=i+8, column=j, padx=5, pady=5)
                    
                    
                      # Adding the second row of data
            for i in range(total_rows):
                for j in range(total_columns):
                    label = Label(F6, text=data8[i][j], font=("arial", 14))
                    label.grid(row=i+9, column=j, padx=5, pady=5)
                    
                    
            for i in range(total_rows):
                for j in range(total_columns):
                    label = Label(F6, text=data8[i][j], font=("arial", 14))
                    label.grid(row=i+9, column=j, padx=5, pady=5)
                    
            

                    
                    
                    
                         
                    
           
           
root=Tk()
obj = Zabdesk(root)

root.mainloop()




