from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM')

        #criminal variables start
        self.var_com_criminal_search = StringVar()
        self.var_criminal_search = StringVar()

        self.var_criminal_id=IntVar()
        self.var_first_name=StringVar()
        self.var_last_name=StringVar()
        self.var_date_of_birth=StringVar()
        self.var_gender=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_criminal_status=StringVar()
        self.var_prison_id=StringVar()
        #criminal variables end

        #crime variables start
        self.var_com_crime_search = StringVar()
        self.var_crime_search = StringVar()

        self.var_crime_id=IntVar()
        self.var_crime_name=StringVar()
        self.var_crime_description=StringVar()
        self.var_severity_level=StringVar()
        self.var_date_committed=StringVar()
        self.var_crime_location=StringVar()
        self.var_incharge_officer=IntVar()
        #crime variables end

        #case variables start
        self.var_com_case_search = StringVar()
        self.var_case_search = StringVar()

        self.var_case_id=StringVar()
        self.var_start_date=StringVar()
        self.var_end_date=StringVar()
        self.var_judge=StringVar()
        self.var_verdict=StringVar()
        # self.var_criminal_id=StringVar()
        # self.var_crime_id=StringVar()
        #case variables end

        #prison variables start
        self.var_com_prison_search = StringVar()
        self.var_prison_search = StringVar()
        #prison variables end

        #officer variables start
        self.var_com_officer_search = StringVar()
        self.var_officer_search = StringVar()
        #officer variables end
    #    
        lbl_title=Label(self.root,text='CRIMINAL MANAGEMENT SYSTEM SOFTWARE',font=('times new roman',35,'bold'),bg='black',fg='gold')
        lbl_title.place(x=0,y=0,width=1530,height=70)

        #ncr_logo
        img_logo=Image.open('images/ncr_logo.jpeg')
        img_logo=img_logo.resize((60, 60),Image.BILINEAR)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=80,y=5,width=60,height=60)

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=100)
        self.notebook.pack(fill=BOTH, expand=YES)

        self.create_criminal_tab()
        self.create_case_tab()
        self.create_crimes_tab()
        self.create_prisons_tab()
        self.create_officers_tab()


    def create_criminal_tab(self):
        criminal_tab = ttk.Frame(self.notebook)
        self.notebook.add(criminal_tab, text="Criminals")

        ttk.Label(criminal_tab, text="").pack()

        # Upper_frame (Criminal Information)
        upper_frame = LabelFrame(criminal_tab, bd=2, relief=RIDGE, text='Criminal Information', font=('palatino', 11, 'bold'), fg='red', bg='white')
        upper_frame.place(x=10, y=10, width=1500, height=560)

        firstname=Label(upper_frame,text='First_Name:',font=('palatino',11,'bold'),bg='white')
        firstname.grid(row=0,column=0,padx=2,sticky=W)

        caseentry=ttk.Entry(upper_frame, textvariable=self.var_first_name, width=22,font=('palatino',11,'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)

        lastName=Label(upper_frame,font=('palatino',12,'bold'),text="Last_Name:",bg='white')
        lastName.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_lastName=ttk.Entry(upper_frame,textvariable=self.var_last_name,width=22,font=('palatino',11,'bold'))
        txt_lastName.grid(row=0,column=3,sticky=W,padx=2,pady=7)

        #DOB
        lbl_dob=Label(upper_frame,font=('palatino',12,'bold'),text="DOB:",bg='white')
        lbl_dob.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_dob=ttk.Entry(upper_frame,textvariable=self.var_date_of_birth,width=22,font=('palatino',11,'bold'))
        txt_dob.grid(row=0,column=5,sticky=W,padx=2,pady=7)

        #Gender
        lbl_gender=Label(upper_frame,font=('palatino',12,'bold'),text="Gender:",bg='white')
        lbl_gender.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_gender=ttk.Entry(upper_frame,textvariable=self.var_gender,width=22,font=('palatino',11,'bold'))
        txt_gender.grid(row=1,column=5,sticky=W,padx=2,pady=7)

        # Nationality
        nationality=Label(upper_frame,font=('palatino',12,'bold'),text="Nationality:",bg='white')
        nationality.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_nationality=ttk.Entry(upper_frame,textvariable=self.var_nationality,width=22,font=('palatino',11,'bold'))
        txt_nationality.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        #Address
        lbl_address=Label(upper_frame,font=('palatino',12,'bold'),text="Address:",bg='white')
        lbl_address.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=('palatino',11,'bold'))
        txt_address.grid(row=1,column=3,sticky=W,padx=2,pady=7)

        lbl_criminalID=Label(upper_frame,font=('palatino',12,'bold'),text="Criminal_ID:",bg='white')
        lbl_criminalID.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_criminalID=ttk.Entry(upper_frame,textvariable=self.var_criminal_id,width=22,font=('palatino',11,'bold'))
        txt_criminalID.grid(row=2,column=1,sticky=W,padx=2,pady=7)

        #Prison-id
        lbl_prison_id=Label(upper_frame,font=('palatino',12,'bold'),text="Prison_ID:",bg='white')
        lbl_prison_id.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        txt_prison_id=ttk.Entry(upper_frame, textvariable=self.var_prison_id,width=22,font=('palatino',11,'bold'))
        txt_prison_id.grid(row=2,column=3,sticky=W,padx=2,pady=7)

        #Status
        lbl_status=Label(upper_frame,font=('palatino',12,'bold'),text="Criminal Status:",bg='white')
        lbl_status.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_status=ttk.Entry(upper_frame,textvariable=self.var_criminal_status,width=22,font=('palatino',11,'bold'))
        txt_status.grid(row=3,column=1,sticky=W,padx=2,pady=7)


        # Buttons for Criminal Information
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=5, y=200, width=620, height=45)
        btn_add = Button(button_frame,command=self.add_criminal_data, text='Save', font=('palatino', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_add.grid(row=0, column=0, padx=3, pady=5)
        
        btn_update=Button(button_frame,command=self.update_criminal_data,text='Update',font=('palatino',13,'bold'),width=14,bg='blue',fg='white')
        btn_update.grid(row=0,column=1,padx=3,pady=5)

        #Delete Button
        btn_delete=Button(button_frame,text='Delete',font=('times new roman',13,'bold'),width=14,bg='blue',fg='white')
        btn_delete.grid(row=0,column=2,padx=3,pady=5)

        #Clear Button
        btn_clear=Button(button_frame,command=self.clear_criminal_data,text='Clear',font=('palatino',13,'bold'),width=14,bg='blue',fg='white')
        btn_clear.grid(row=0,column=3,padx=3,pady=5)

         #Main_frame
        Main_frame = Frame(criminal_tab, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=10, y=280, width=1500, height=560)
        
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Criminal Information Table',font=('palatino',11,'bold'),fg='red',bg='white')
        down_frame.place(x=10,y=10,width=1480,height=270)

        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='Search Criminal Record',font=('palatino',11,'bold'),fg='red',bg='white')
        search_frame.place(x=0,y=0,width=1470,height=60)

        search_by=Label(search_frame,font=("palatino",11,"bold"),text="Search By:",bg="red",fg="white")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        # self.var_com_search=StringVar()
        combo_search_box=ttk.Combobox(search_frame,textvariable=self.var_com_criminal_search,font=("palatino",11,"bold"),width=18,state='readonly')
        combo_search_box['value']=('Select Option','prison_id','criminal_id')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky=W,padx=5)

        # self.var_search=StringVar()
        search_txt=ttk.Entry(search_frame,textvariable=self.var_criminal_search,width=18,font=("palatino",11,"bold"))
        search_txt.grid(row=0,column=2,sticky=W,padx=5)

        #search button
        btn_search=Button(search_frame,command=self.search_criminal_data,text='Search',font=("palatino",13,"bold"),width=14,bg='blue',fg='white')
        btn_search.grid(row=0,column=3,padx=3,pady=5)

        #all button
        btn_all=Button(search_frame,command = self.fetch_criminal_data,text='Show All',font=("palatino",13,"bold"),width=14,bg='blue',fg='white')
        btn_all.grid(row=0,column=4,padx=3,pady=5)

        crimeagency=Label(search_frame,font=("palatino",27,"bold"),text="NATIONAL CRIME AGENCY",bg='white',fg='crimson')
        crimeagency.grid(row=0,column=5,sticky=W,padx=70,pady=0)

        # Table Frame
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        # Scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7","8","9"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading("1",text="criminal_id")
        self.criminal_table.heading("2",text="first_name")
        self.criminal_table.heading("3",text="last_name")
        self.criminal_table.heading("4",text="date_of_birth")
        self.criminal_table.heading("5",text="gender")
        self.criminal_table.heading("6",text="nationality")
        self.criminal_table.heading("7",text="address")
        self.criminal_table.heading("8",text="criminal_status")
        self.criminal_table.heading("9",text="prison_id")

        self.criminal_table['show']='headings'

        self.criminal_table.column("1",width=100)
        self.criminal_table.column("2",width=100)
        self.criminal_table.column("3",width=100)
        self.criminal_table.column("4",width=100)
        self.criminal_table.column("5",width=100)
        self.criminal_table.column("6",width=100)
        self.criminal_table.column("7",width=100)
        self.criminal_table.column("8",width=100)
        self.criminal_table.column("9",width=100)

        self.criminal_table.pack(fill=BOTH,expand=1)
        self.criminal_table.bind("<ButtonRelease>", self.get_criminal_cursor) #
        self.fetch_criminal_data()

    def fetch_criminal_data(self):
        conn=mysql.connector.connect(host='localhost', username='root',password='password', database='crime_project')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from criminals')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('',END,values=i)
            conn.commit()
        conn.close()

    def add_criminal_data(self):
        if self.var_criminal_id.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='root',password='password', database='crime_project')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into criminals values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                    self.var_criminal_id.get(),
                    self.var_first_name.get(),
                    self.var_last_name.get(),
                    self.var_date_of_birth.get(),
                    self.var_gender.get(),
                    self.var_nationality.get(),
                    self.var_address.get(),
                    self.var_criminal_status.get(),
                    self.var_prison_id.get()))
                conn.commit()
                self.fetch_criminal_data()
                self.clear_criminal_data()
                conn.close()
                messagebox.showinfo('successful', 'Criminal record has been added')
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}')

    def clear_criminal_data(self):
        self.var_criminal_id.set("")
        self.var_first_name.set("")
        self.var_last_name.set("")
        self.var_date_of_birth.set("")
        self.var_gender.set("")
        self.var_nationality.set("")
        self.var_address.set("")
        self.var_criminal_status.set("")
        self.var_prison_id.set("")

    def get_criminal_cursor(self,event=""):
        cursor_row=self.criminal_table.focus()
        content=self.criminal_table.item(cursor_row)
        data=content['values']

        self.var_criminal_id.set(data[0])
        self.var_first_name.set(data[1])
        self.var_last_name.set(data[2])
        self.var_date_of_birth.set(data[3])
        self.var_gender.set(data[4])
        self.var_nationality.set(data[5])
        self.var_address.set(data[6])
        self.var_criminal_status.set(data[7])
        self.var_prison_id.set(data[8])

    def update_criminal_data(self):
        if self.var_criminal_id.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='root',password='password', database='crime_project')
                my_cursor=conn.cursor()
                my_cursor.execute('update criminals set first_name=%s, last_name=%s, date_of_birth=%s, gender=%s, nationality=%s, address=%s, criminal_status=%s, prison_id=%s where criminal_id=%s',(
                    self.var_first_name.get(),
                    self.var_last_name.get(),
                    self.var_date_of_birth.get(),
                    self.var_gender.get(),
                    self.var_nationality.get(),
                    self.var_address.get(),
                    self.var_criminal_status.get(),
                    self.var_prison_id.get(),
                    self.var_criminal_id.get()))
                conn.commit()
                self.fetch_criminal_data()
                self.clear_criminal_data()
                conn.close()
                messagebox.showinfo('successful', 'Criminal record has been added')
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}')

    def search_criminal_data(self): 
        if self.var_com_criminal_search.get()=="":
            messagebox.showerror('Error','All fields are required') 
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='root',password='password', database='crime_project')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from criminals where '+str(self.var_com_criminal_search.get())+" LIKE'%"+str(self.var_criminal_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in rows:
                        self.criminal_table.insert('',END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}')


    def create_case_tab(self):
        case_tab = ttk.Frame(self.notebook)
        self.notebook.add(case_tab, text="Cases")

        ttk.Label(case_tab, text="").pack()

        # Upper_frame (Criminal Information)
        upper_frame = LabelFrame(case_tab, bd=2, relief=RIDGE, text='Case Related Information', font=('palatino', 11, 'bold'), fg='red', bg='white')
        upper_frame.place(x=10, y=10, width=1500, height=560)

        caseid=Label(upper_frame,text='Case_ID:',font=('palatino',11,'bold'),bg='white')
        caseid.grid(row=0,column=0,padx=2,sticky=W)

        caseentry=ttk.Entry(upper_frame,textvariable=self.var_case_id,width=22,font=('palatino',11,'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)

        startDate=Label(upper_frame,font=('palatino',12,'bold'),text="Start_date:",bg='white')
        startDate.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_sDate=ttk.Entry(upper_frame,textvariable = self.var_start_date,width=22,font=('palatino',11,'bold'))
        txt_sDate.grid(row=0,column=3,sticky=W,padx=2,pady=7)

        #End date
        endDate=Label(upper_frame,font=('palatino',12,'bold'),text="End_date:",bg='white')
        endDate.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_eDate=ttk.Entry(upper_frame,textvariable=self.var_end_date,width=22,font=('palatino',11,'bold'))
        txt_eDate.grid(row=0,column=5,sticky=W,padx=2,pady=7)

        #Judge
        judge=Label(upper_frame,font=('palatino',12,'bold'),text="Judge:",bg='white')
        judge.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_judge=ttk.Entry(upper_frame,textvariable=self.var_judge,width=22,font=('palatino',11,'bold'))
        txt_judge.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        # Verdict
        verdict=Label(upper_frame,font=('palatino',12,'bold'),text="Verdict:",bg='white')
        verdict.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_verdict=ttk.Entry(upper_frame,textvariable=self.var_verdict,width=22,font=('palatino',11,'bold'))
        txt_verdict.grid(row=1,column=3,sticky=W,padx=2,pady=7)

        #criminal id
        lbl_criminalID=Label(upper_frame,font=('palatino',12,'bold'),text="Criminal_ID:",bg='white')
        lbl_criminalID.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_criminalID=ttk.Entry(upper_frame,textvariable=self.var_criminal_id,width=22,font=('palatino',11,'bold'))
        txt_criminalID.grid(row=1,column=5,sticky=W,padx=2,pady=7)

        #crime-id
        crimeid=Label(upper_frame,font=('palatino',12,'bold'),text="Crime_ID:",bg='white')
        crimeid.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_crimeid=ttk.Entry(upper_frame,textvariable=self.var_crime_id, width=22,font=('palatino',11,'bold'))
        txt_crimeid.grid(row=2,column=1,sticky=W,padx=2,pady=7)

        # Buttons for Information
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=5, y=200, width=620, height=45)
        btn_add = Button(button_frame,command=self.add_case_data, text='Save', font=('palatino', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_add.grid(row=0, column=0, padx=3, pady=5)
        
        btn_update=Button(button_frame,command=self.update_case_data,text='Update',font=('palatino',13,'bold'),width=14,bg='blue',fg='white')
        btn_update.grid(row=0,column=1,padx=3,pady=5)

        #Delete Button
        btn_delete=Button(button_frame,text='Delete',font=('times new roman',13,'bold'),width=14,bg='blue',fg='white')
        btn_delete.grid(row=0,column=2,padx=3,pady=5)

        #Clear Button
        btn_clear=Button(button_frame,command=self.clear_case_data,text='Clear',font=('palatino',13,'bold'),width=14,bg='blue',fg='white')
        btn_clear.grid(row=0,column=3,padx=3,pady=5)

         #Main_frame
        Main_frame = Frame(case_tab, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=10, y=280, width=1500, height=560)
        
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Case Information Table',font=('palatino',11,'bold'),fg='red',bg='white')
        down_frame.place(x=10,y=10,width=1480,height=270)

        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='Search Case Record',font=('palatino',11,'bold'),fg='red',bg='white')
        search_frame.place(x=0,y=0,width=1470,height=60)

        search_by=Label(search_frame,font=("palatino",11,"bold"),text="Search By:",bg="red",fg="white")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        # self.var_com_search=StringVar()
        combo_search_box=ttk.Combobox(search_frame,textvariable=self.var_com_case_search,font=("palatino",11,"bold"),width=18,state='readonly')
        combo_search_box['value']=('Select Option','case_id','criminal_id','crime_id','judge')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky=W,padx=5)

        # self.var_search=StringVar()
        search_txt=ttk.Entry(search_frame,textvariable=self.var_case_search,width=18,font=("palatino",11,"bold"))
        search_txt.grid(row=0,column=2,sticky=W,padx=5)

        # search button
        btn_search=Button(search_frame,command=self.search_case_data,text='Search',font=("palatino",13,"bold"),width=14,bg='blue',fg='white')
        btn_search.grid(row=0,column=3,padx=3,pady=5)

        #all button
        btn_all=Button(search_frame,command=self.fetch_case_data,text='Show All',font=("palatino",13,"bold"),width=14,bg='blue',fg='white')
        btn_all.grid(row=0,column=4,padx=3,pady=5)

        crimeagency=Label(search_frame,font=("palatino",27,"bold"),text="NATIONAL CRIME AGENCY",bg='white',fg='crimson')
        crimeagency.grid(row=0,column=5,sticky=W,padx=70,pady=0)

        # Table Frame
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        # Scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.case_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.case_table.xview)
        scroll_y.config(command=self.case_table.yview)

        self.case_table.heading("1",text="case_id")
        self.case_table.heading("2",text="start_date")
        self.case_table.heading("3",text="end_date")
        self.case_table.heading("4",text="judge")
        self.case_table.heading("5",text="verdict")
        self.case_table.heading("6",text="criminal_id")
        self.case_table.heading("7",text="crime_id")

        self.case_table['show']='headings'

        self.case_table.column("1",width=100)
        self.case_table.column("2",width=100)
        self.case_table.column("3",width=100)
        self.case_table.column("4",width=100)
        self.case_table.column("5",width=100)
        self.case_table.column("6",width=100)
        self.case_table.column("7",width=100)

        self.case_table.pack(fill=BOTH,expand=1)
        self.case_table.bind("<ButtonRelease>", self.get_case_cursor) #
        self.fetch_case_data()

    def fetch_case_data(self):
        conn=mysql.connector.connect(host='localhost', username='root',password='password', database='crime_project')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from cases')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.case_table.delete(*self.case_table.get_children())
            for i in data:
                self.case_table.insert('',END,values=i)
            conn.commit()
        conn.close()

    def add_case_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='root',password='password', database='crime_project')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into cases values(%s,%s,%s,%s,%s,%s,%s)',(
                    self.var_case_id.get(),
                    self.var_start_date.get(),
                    self.var_end_date.get(),
                    self.var_judge.get(),
                    self.var_verdict.get(),
                    self.var_criminal_id.get(),
                    self.var_crime_id.get()))
                conn.commit()
                self.fetch_case_data()
                self.clear_case_data()
                conn.close()
                messagebox.showinfo('successful', 'Criminal record has been added')
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}')

    def clear_case_data(self):
        self.var_case_id.set("")
        self.var_start_date.set("")
        self.var_end_date.set("")
        self.var_judge.set("")
        self.var_verdict.set("")
        self.var_criminal_id.set("")
        self.var_crime_id.set("")

    def get_case_cursor(self,event=""):
        cursor_row=self.case_table.focus()
        content=self.case_table.item(cursor_row)
        data=content['values']

        self.var_case_id.set(data[0])
        self.var_start_date.set(data[1])
        self.var_end_date.set(data[2])
        self.var_judge.set(data[3])
        self.var_verdict.set(data[4])
        self.var_criminal_id.set(data[5])
        self.var_crime_id.set(data[6])

    def update_case_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='root',password='password', database='crime_project')
                my_cursor=conn.cursor()
                my_cursor.execute('update cases set start_date=%s, end_date=%s, judge=%s, verdict=%s, criminal_id=%s, crime_id=%s where case_id=%s',(
                    self.var_start_date.get(),
                    self.var_end_date.get(),
                    self.var_judge.get(),
                    self.var_verdict.get(),
                    self.var_criminal_id.get(),
                    self.var_crime_id.get(),
                    self.var_case_id.get()))
                conn.commit()
                self.fetch_case_data()
                self.clear_case_data()
                conn.close()
                messagebox.showinfo('successful', 'Case record has been added')
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}')

    def search_case_data(self): 
        if self.var_com_case_search.get()=="":
            messagebox.showerror('Error','All fields are required') 
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='root',password='password', database='crime_project')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from cases where '+str(self.var_com_case_search.get())+" LIKE'%"+str(self.var_case_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.case_table.delete(*self.case_table.get_children())
                    for i in rows:
                        self.case_table.insert('',END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}')


    
    def create_crimes_tab(self):
        crimes_tab = ttk.Frame(self.notebook)
        self.notebook.add(crimes_tab, text="Crimes")

        ttk.Label(crimes_tab, text="").pack()

        # Upper_frame (Criminal Information)
        upper_frame = LabelFrame(crimes_tab, bd=2, relief=RIDGE, text='Crime Details', font=('palatino', 11, 'bold'), fg='red', bg='white')
        upper_frame.place(x=10, y=10, width=1500, height=560)
        
        crimeid=Label(upper_frame,text='Crime_ID:',font=('palatino',11,'bold'),bg='white')
        crimeid.grid(row=0,column=0,padx=2,sticky=W)

        caseentry=ttk.Entry(upper_frame,textvariable=self.var_crime_id,width=22,font=('palatino',11,'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)

        crimeName=Label(upper_frame,font=('palatino',12,'bold'),text="Crime_Name:",bg='white')
        crimeName.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_cname=ttk.Entry(upper_frame,textvariable=self.var_crime_name,width=22,font=('palatino',11,'bold'))
        txt_cname.grid(row=0,column=3,sticky=W,padx=2,pady=7)

        #Crime Desc
        crimeDesc=Label(upper_frame,font=('palatino',12,'bold'),text="Crime_Description:",bg='white')
        crimeDesc.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_cdesc=ttk.Entry(upper_frame,textvariable=self.var_crime_description,width=22,font=('palatino',11,'bold'))
        txt_cdesc.grid(row=0,column=5,sticky=W,padx=2,pady=7)

        #severity level
        severity=Label(upper_frame,font=('palatino',12,'bold'),text="Severity_Level:",bg='white')
        severity.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_severity=ttk.Entry(upper_frame,textvariable=self.var_severity_level,width=22,font=('palatino',11,'bold'))
        txt_severity.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        # date committed
        datecom=Label(upper_frame,font=('palatino',12,'bold'),text="Date_Committed:",bg='white')
        datecom.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_datecom=ttk.Entry(upper_frame,textvariable=self.var_date_committed,width=22,font=('palatino',11,'bold'))
        txt_datecom.grid(row=1,column=3,sticky=W,padx=2,pady=7)

        #Location
        location=Label(upper_frame,font=('palatino',12,'bold'),text="Location:",bg='white')
        location.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_location=ttk.Entry(upper_frame,textvariable=self.var_crime_location,width=22,font=('palatino',11,'bold'))
        txt_location.grid(row=1,column=5,sticky=W,padx=2,pady=7)

        #criminal_Id
        lbl_criminalID=Label(upper_frame,font=('palatino',12,'bold'),text="Criminal_ID:",bg='white')
        lbl_criminalID.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_criminalID=ttk.Entry(upper_frame,textvariable=self.var_criminal_id, width=22,font=('palatino',11,'bold')) #might cause erros. watchlist
        txt_criminalID.grid(row=2,column=1,sticky=W,padx=2,pady=7)

        #Incharge Officer
        lbl_incharge=Label(upper_frame,font=('palatino',12,'bold'),text="Incharge Officer:",bg='white')
        lbl_incharge.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        txt_incharge=ttk.Entry(upper_frame,textvariable=self.var_incharge_officer,width=22,font=('palatino',11,'bold'))
        txt_incharge.grid(row=2,column=3,sticky=W,padx=2,pady=7)

        # Buttons for Information
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=5, y=200, width=620, height=45)
        btn_add = Button(button_frame,command=self.add_crime_data, text='Save', font=('palatino', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_add.grid(row=0, column=0, padx=3, pady=5)
        
        btn_update=Button(button_frame,command=self.update_crime_data,text='Update',font=('palatino',13,'bold'),width=14,bg='blue',fg='white')
        btn_update.grid(row=0,column=1,padx=3,pady=5)

        #Delete Button
        btn_delete=Button(button_frame,text='Delete',font=('times new roman',13,'bold'),width=14,bg='blue',fg='white')
        btn_delete.grid(row=0,column=2,padx=3,pady=5)

        #Clear Button
        btn_clear=Button(button_frame,command=self.clear_crime_data,text='Clear',font=('palatino',13,'bold'),width=14,bg='blue',fg='white')
        btn_clear.grid(row=0,column=3,padx=3,pady=5)

        #Main_frame
        Main_frame = Frame(crimes_tab, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=10, y=280, width=1500, height=560)
        
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Crime Information Table',font=('palatino',11,'bold'),fg='red',bg='white')
        down_frame.place(x=10,y=10,width=1480,height=270)

        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='Search Crime Record',font=('palatino',11,'bold'),fg='red',bg='white')
        search_frame.place(x=0,y=0,width=1470,height=60)

        search_by=Label(search_frame,font=("palatino",11,"bold"),text="Search By:",bg="red",fg="white")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        # self.var_com_search=StringVar()
        combo_search_box=ttk.Combobox(search_frame,textvariable=self.var_com_crime_search,font=("palatino",11,"bold"),width=18,state='readonly')
        combo_search_box['value']=('Select Option','crime_id','criminal_id','Severity_Level','crime_name','incharge_officer')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky=W,padx=5)

        # self.var_search=StringVar()
        search_txt=ttk.Entry(search_frame,textvariable=self.var_crime_search,width=18,font=("palatino",11,"bold"))
        search_txt.grid(row=0,column=2,sticky=W,padx=5)

        #search button
        btn_search=Button(search_frame,command=self.search_crime_data,text='Search',font=("palatino",13,"bold"),width=14,bg='blue',fg='white', fg='white')
        btn_search.grid(row=0,column=3,padx=3,pady=5)
        
        #all button
        btn_all=Button(search_frame,command=self.fetch_crime_data,text='Show All',font=("palatino",13,"bold"),width=14,bg='blue',fg='white', fg='white')
        btn_all.grid(row=0,column=4,padx=3,pady=5)

        crimeagency=Label(search_frame,font=("palatino",27,"bold"),text="NATIONAL CRIME AGENCY",bg='white',fg='crimson')
        crimeagency.grid(row=0,column=5,sticky=W,padx=70,pady=0)

        # Table Frame
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        # Scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.crime_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7","8"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.crime_table.xview)
        scroll_y.config(command=self.crime_table.yview)

        self.crime_table.heading("1",text="crime_id")
        self.crime_table.heading("2",text="crime_Name")
        self.crime_table.heading("3",text="crime_description")
        self.crime_table.heading("4",text="Severity_Level")
        self.crime_table.heading("5",text="Date_Committed")
        self.crime_table.heading("6",text="location")
        self.crime_table.heading("7",text="criminal_id")
        self.crime_table.heading("8",text="incharge_officer")

        self.crime_table['show']='headings'

        self.crime_table.column("1",width=100)
        self.crime_table.column("2",width=100)
        self.crime_table.column("3",width=120)
        self.crime_table.column("4",width=100)
        self.crime_table.column("5",width=100)
        self.crime_table.column("6",width=100)
        self.crime_table.column("7",width=100)
        self.crime_table.column("8",width=100)

        self.crime_table.pack(fill=BOTH,expand=1)
        self.crime_table.bind("<ButtonRelease>", self.get_crime_cursor) #
        self.fetch_crime_data()

    def add_crime_data(self):
        if self.var_crime_id.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='root',password='password', database='crime_project')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into crimes values(%s,%s,%s,%s,%s,%s,%s,%s)',(
                    self.var_crime_id.get(),
                    self.var_crime_name.get(),
                    self.var_crime_description.get(),
                    self.var_severity_level.get(),
                    self.var_date_committed.get(),
                    self.var_crime_location.get(),
                    self.var_criminal_id.get(),
		            self.var_incharge_officer.get()))
                conn.commit()
                self.fetch_crime_data()
                self.clear_crime_data()
                conn.close()
                messagebox.showinfo('successful', 'Crime has been added')
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}')

    def fetch_crime_data(self):
        conn=mysql.connector.connect(host='localhost', username='root',password='password', database='crime_project')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from crimes')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.crime_table.delete(*self.crime_table.get_children())
            for i in data:
                self.crime_table.insert('',END,values=i)
            conn.commit()
        conn.close()

    def search_crime_data(self): 
        if self.var_com_crime_search.get()=="":
            messagebox.showerror('Error','All fields are required') 
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='root',password='password', database='crime_project')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from crimes where '+str(self.var_com_crime_search.get())+" LIKE'%"+str(self.var_crime_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.crime_table.delete(*self.crime_table.get_children())
                    for i in rows:
                        self.crime_table.insert('',END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}')

    def clear_crime_data(self):
        self.var_crime_id.set(""),
        self.var_crime_name.set(""),
        self.var_crime_description.set(""),
        self.var_severity_level.set(""),
        self.var_date_committed.set(""),
        self.var_crime_location.set(""),
        self.var_criminal_id.set(""),
        self.var_incharge_officer.set("")

    def get_crime_cursor(self,event=""):
        cursor_row=self.crime_table.focus()
        content=self.crime_table.item(cursor_row)
        data=content['values']

        self.var_crime_id.set(data[0]),
        self.var_crime_name.set(data[1]),
        self.var_crime_description.set(data[2]),
        self.var_severity_level.set(data[3]),
        self.var_date_committed.set(data[4]),
        self.var_crime_location.set(data[5]),
        self.var_criminal_id.set(data[6]),
        self.var_incharge_officer.set(data[7])

    def update_crime_data(self):
        if self.var_crime_id.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='root',password='password', database='crime_project')
                my_cursor=conn.cursor()
                my_cursor.execute('update crimes set crime_name=%s, crime_description=%s, Severity_Level=%s, Date_Committed=%s, location=%s, criminal_id=%s, incharge_officer=%s where crime_id=%s',(
                    self.var_crime_name.get(),
                    self.var_crime_description.get(),
                    self.var_severity_level.get(),
                    self.var_date_committed.get(),
                    self.var_crime_location.get(),
                    self.var_criminal_id.get(),
		            self.var_incharge_officer.get(),
                    self.var_crime_id.get()))
                conn.commit()
                self.fetch_crime_data()
                self.clear_crime_data()
                conn.close()
                messagebox.showinfo('successful', 'Crime record has been added')
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}')


    
    def create_prisons_tab(self):
        prisons_tab = ttk.Frame(self.notebook)
        self.notebook.add(prisons_tab, text="Prisons")

        ttk.Label(prisons_tab, text="").pack()
        #Main_frame
        Main_frame = Frame(prisons_tab, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=10, y=20, width=1500, height=560)
        
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Prison Information Table',font=('palatino',11,'bold'),fg='red',bg='white')
        down_frame.place(x=10,y=10,width=1480,height=270)

        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='Search Prison',font=('palatino',11,'bold'),fg='red',bg='white')
        search_frame.place(x=0,y=0,width=1470,height=60)

        search_by=Label(search_frame,font=("palatino",11,"bold"),text="Search By:",bg="red",fg="white")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        # self.var_com_search=StringVar()
        combo_search_box=ttk.Combobox(search_frame,textvariable=self.var_com_prison_search,font=("palatino",11,"bold"),width=18,state='readonly')
        combo_search_box['value']=('Select Option','prison_id')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky=W,padx=5)

        # self.var_search=StringVar()
        search_txt=ttk.Entry(search_frame,textvariable=self.var_prison_search,width=18,font=("palatino",11,"bold"))
        search_txt.grid(row=0,column=2,sticky=W,padx=5)

        #search button
        btn_search=Button(search_frame,command=self.search_prison_data,text='Search',font=("palatino",13,"bold"),width=14,bg='blue',fg='white')
        btn_search.grid(row=0,column=3,padx=3,pady=5)

        #all button
        btn_all=Button(search_frame,command=self.fetch_prison_data,text='Show All',font=("palatino",13,"bold"),width=14,bg='blue',fg='white')
        btn_all.grid(row=0,column=4,padx=3,pady=5)

        crimeagency=Label(search_frame,font=("palatino",27,"bold"),text="NATIONAL CRIME AGENCY",bg='white',fg='crimson')
        crimeagency.grid(row=0,column=5,sticky=W,padx=70,pady=0)

        # Table Frame
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        # Scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.prison_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.prison_table.xview)
        scroll_y.config(command=self.prison_table.yview)

        self.prison_table.heading("1",text="prison_id")
        self.prison_table.heading("2",text="prison_name")
        self.prison_table.heading("3",text="location")
        self.prison_table.heading("4",text="capacity")
        self.prison_table.heading("5",text="warden")
        self.prison_table.heading("6",text="number_of_inmates")

        self.prison_table['show']='headings'

        self.prison_table.column("1",width=100)
        self.prison_table.column("2",width=100)
        self.prison_table.column("3",width=100)
        self.prison_table.column("4",width=100)
        self.prison_table.column("5",width=100)
        self.prison_table.column("6",width=150)

        self.prison_table.pack(fill=BOTH,expand=1)
        self.fetch_prison_data()

    def search_prison_data(self): 
        if self.var_com_prison_search.get()=="":
            messagebox.showerror('Error','All fields are required') 
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='root',password='password', database='crime_project')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from prisons where '+str(self.var_com_prison_search.get())+" LIKE'%"+str(self.var_prison_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.prison_table.delete(*self.prison_table.get_children())
                    for i in rows:
                        self.prison_table.insert('',END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}') 

    def fetch_prison_data(self):
        conn=mysql.connector.connect(host='localhost', username='root',password='password', database='crime_project')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from prisons')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.prison_table.delete(*self.prison_table.get_children())
            for i in data:
                self.prison_table.insert('',END,values=i)
            conn.commit()
        conn.close()


    def create_officers_tab(self):
        officers_tab = ttk.Frame(self.notebook)
        self.notebook.add(officers_tab, text="Officers")

        ttk.Label(officers_tab, text="").pack()
        
        #Main_frame
        Main_frame = Frame(officers_tab, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=10, y=20, width=1500, height=560)
        
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Officer Information Table',font=('palatino',11,'bold'),fg='red',bg='white')
        down_frame.place(x=10,y=10,width=1480,height=270)

        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='Search Officer',font=('palatino',11,'bold'),fg='red',bg='white')
        search_frame.place(x=0,y=0,width=1470,height=60)

        search_by=Label(search_frame,font=("palatino",11,"bold"),text="Search By:",bg="red",fg="white")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        # self.var_com_search=StringVar()
        combo_search_box=ttk.Combobox(search_frame,textvariable=self.var_com_officer_search,font=("palatino",11,"bold"),width=18,state='readonly')
        combo_search_box['value']=('Select Option','officer_id')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky=W,padx=5)

        # self.var_search=StringVar()
        search_txt=ttk.Entry(search_frame,width=18,font=("palatino",11,"bold"))
        search_txt.grid(row=0,column=2,sticky=W,padx=5)

        # search button
        btn_search=Button(search_frame,text='Search',font=("palatino",13,"bold"),width=14,bg='blue',fg='white')
        btn_search.grid(row=0,column=3,padx=3,pady=5)

        #all button
        btn_all=Button(search_frame,text='Show All',font=("palatino",13,"bold"),width=14,bg='blue',fg='white')
        btn_all.grid(row=0,column=4,padx=3,pady=5)

        crimeagency=Label(search_frame,font=("palatino",27,"bold"),text="NATIONAL CRIME AGENCY",bg='white',fg='crimson')
        crimeagency.grid(row=0,column=5,sticky=W,padx=70,pady=0)

        # Table Frame
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=70,width=1470,height=170)

        # Scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.officer_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.officer_table.xview)
        scroll_y.config(command=self.officer_table.yview)

        self.officer_table.heading("1",text="officer_id")
        self.officer_table.heading("2",text="first_name")
        self.officer_table.heading("3",text="last_name")
        self.officer_table.heading("4",text="badge_number")
        self.officer_table.heading("5",text="rank_level")
        self.officer_table.heading("6",text="department")
        self.officer_table.heading("7",text="contact_info")

        self.officer_table['show']='headings'

        self.officer_table.column("1",width=100)
        self.officer_table.column("2",width=100)
        self.officer_table.column("3",width=100)
        self.officer_table.column("4",width=100)
        self.officer_table.column("5",width=100)
        self.officer_table.column("6",width=100)
        self.officer_table.column("7",width=100)

        self.officer_table.pack(fill=BOTH,expand=1)
        self.fetch_officer_data()

    def fetch_officer_data(self):
        conn=mysql.connector.connect(host='localhost', username='root',password='password', database='crime_project')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from policeofficers')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.officer_table.delete(*self.officer_table.get_children())
            for i in data:
                self.officer_table.insert('',END,values=i)
            conn.commit()
        conn.close()

    def search_officer_data(self): 
        if self.var_com_officer_search.get()=="":
            messagebox.showerror('Error','All fields are required') 
        else:
            try:
                conn=mysql.connector.connect(host='localhost', username='root',password='password', database='crime_project')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from policeofficers where '+str(self.var_com_officer_search.get())+" LIKE'%"+str(self.var_officer_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.officer_table.delete(*self.officer_table.get_children())
                    for i in rows:
                        self.officer_table.insert('',END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('error',f'Due to{str(es)}')


if __name__=="__main__":
    root=Tk()
    obj=Criminal(root)
    root.mainloop()


