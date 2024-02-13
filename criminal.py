
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox


class Criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM')
        
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
        # self.create_officers_tab()


    def create_criminal_tab(self):
        criminal_tab = ttk.Frame(self.notebook)
        self.notebook.add(criminal_tab, text="Criminals")

        ttk.Label(criminal_tab, text="").pack()

        # Upper_frame (Criminal Information)
        upper_frame = LabelFrame(criminal_tab, bd=2, relief=RIDGE, text='Criminal Information', font=('times new roman', 11, 'bold'), fg='red', bg='white')
        upper_frame.place(x=10, y=10, width=1500, height=560)

        firstname=Label(upper_frame,text='First_Name:',font=('arial',11,'bold'),bg='white')
        firstname.grid(row=0,column=0,padx=2,sticky=W)

        caseentry=ttk.Entry(upper_frame, width=22,font=('arial',11,'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)

        lastName=Label(upper_frame,font=('arial',12,'bold'),text="Last_Name:",bg='white')
        lastName.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_lastName=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_lastName.grid(row=0,column=3,sticky=W,padx=2,pady=7)

        #DOB
        lbl_dob=Label(upper_frame,font=('arial',12,'bold'),text="DOB:",bg='white')
        lbl_dob.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_dob=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_dob.grid(row=0,column=5,sticky=W,padx=2,pady=7)

        #Gender
        lbl_gender=Label(upper_frame,font=('arial',12,'bold'),text="Gender:",bg='white')
        lbl_gender.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_gender=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_gender.grid(row=1,column=5,sticky=W,padx=2,pady=7)

        # Nationality
        nationality=Label(upper_frame,font=('arial',12,'bold'),text="Nationality:",bg='white')
        nationality.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_nationality=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_nationality.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        #Address
        lbl_address=Label(upper_frame,font=('arial',12,'bold'),text="Address:",bg='white')
        lbl_address.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_address=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_address.grid(row=1,column=3,sticky=W,padx=2,pady=7)

        lbl_criminalID=Label(upper_frame,font=('arial',12,'bold'),text="Criminal_ID:",bg='white')
        lbl_criminalID.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_criminalID=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_criminalID.grid(row=2,column=1,sticky=W,padx=2,pady=7)

        #Prison-id
        lbl_dateofCrime=Label(upper_frame,font=('arial',12,'bold'),text="Prison_ID:",bg='white')
        lbl_dateofCrime.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        txt_dateofCrime=ttk.Entry(upper_frame, width=22,font=('arial',11,'bold'))
        txt_dateofCrime.grid(row=2,column=3,sticky=W,padx=2,pady=7)

        #Status
        lbl_status=Label(upper_frame,font=('arial',12,'bold'),text="Criminal Status:",bg='white')
        lbl_status.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_status=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_status.grid(row=3,column=1,sticky=W,padx=2,pady=7)


        # Buttons for Criminal Information
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=5, y=200, width=620, height=45)
        btn_add = Button(button_frame, text='Save', font=('arial', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_add.grid(row=0, column=0, padx=3, pady=5)
        
        btn_update=Button(button_frame,text='Update',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_update.grid(row=0,column=1,padx=3,pady=5)

        #Delete Button
        btn_delete=Button(button_frame,text='Delete',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_delete.grid(row=0,column=2,padx=3,pady=5)

        #Clear Button
        btn_clear=Button(button_frame,text='Clear',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_clear.grid(row=0,column=3,padx=3,pady=5)

         #Main_frame
        Main_frame = Frame(criminal_tab, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=10, y=280, width=1500, height=560)
        
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Criminal Information Table',font=('times new roman',11,'bold'),fg='red',bg='white')
        down_frame.place(x=10,y=10,width=1480,height=270)

        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='Search Criminal Record',font=('times new roman',11,'bold'),fg='red',bg='white')
        search_frame.place(x=0,y=0,width=1470,height=60)

        search_by=Label(search_frame,font=("arial",11,"bold"),text="Search By:",bg="red",fg="white")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        # self.var_com_search=StringVar()
        combo_search_box=ttk.Combobox(search_frame,font=("arial",11,"bold"),width=18,state='readonly')
        combo_search_box['value']=('Select Option','Case_id','Criminal_no')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky=W,padx=5)

        # self.var_search=StringVar()
        search_txt=ttk.Entry(search_frame,width=18,font=("arial",11,"bold"))
        search_txt.grid(row=0,column=2,sticky=W,padx=5)

        #search button
        btn_search=Button(search_frame,text='Search',font=("arial",13,"bold"),width=14,bg='blue')
        btn_search.grid(row=0,column=3,padx=3,pady=5)

        #all button
        btn_all=Button(search_frame,text='Show All',font=("arial",13,"bold"),width=14,bg='blue')
        btn_all.grid(row=0,column=4,padx=3,pady=5)

        crimeagency=Label(search_frame,font=("arial",30,"bold"),text="NATIONAL CRIME AGENCY",bg='white',fg='crimson')
        crimeagency.grid(row=0,column=5,sticky=W,padx=50,pady=0)

        # Table Frame
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        # Scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7","8","9","10","11","12","13","14"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

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

    def create_case_tab(self):
        case_tab = ttk.Frame(self.notebook)
        self.notebook.add(case_tab, text="Cases")

        ttk.Label(case_tab, text="").pack()

        # Upper_frame (Criminal Information)
        upper_frame = LabelFrame(case_tab, bd=2, relief=RIDGE, text='Case Related Information', font=('times new roman', 11, 'bold'), fg='red', bg='white')
        upper_frame.place(x=10, y=10, width=1500, height=560)

        caseid=Label(upper_frame,text='Case_ID:',font=('arial',11,'bold'),bg='white')
        caseid.grid(row=0,column=0,padx=2,sticky=W)

        caseentry=ttk.Entry(upper_frame, width=22,font=('arial',11,'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)

        startDate=Label(upper_frame,font=('arial',12,'bold'),text="Start_date:",bg='white')
        startDate.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_sDate=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_sDate.grid(row=0,column=3,sticky=W,padx=2,pady=7)

        #End date
        endDate=Label(upper_frame,font=('arial',12,'bold'),text="End_date:",bg='white')
        endDate.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_eDate=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_eDate.grid(row=0,column=5,sticky=W,padx=2,pady=7)

        #Judge
        judge=Label(upper_frame,font=('arial',12,'bold'),text="Judge:",bg='white')
        judge.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_judge=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_judge.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        # Verdict
        verdict=Label(upper_frame,font=('arial',12,'bold'),text="Verdict:",bg='white')
        verdict.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_verdict=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_verdict.grid(row=1,column=3,sticky=W,padx=2,pady=7)

        #criminal id
        lbl_criminalID=Label(upper_frame,font=('arial',12,'bold'),text="Criminal_ID:",bg='white')
        lbl_criminalID.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_criminalID=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_criminalID.grid(row=1,column=5,sticky=W,padx=2,pady=7)

        #crime-id
        crimeid=Label(upper_frame,font=('arial',12,'bold'),text="Crime_ID:",bg='white')
        crimeid.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_crimeid=ttk.Entry(upper_frame, width=22,font=('arial',11,'bold'))
        txt_crimeid.grid(row=2,column=1,sticky=W,padx=2,pady=7)

        # Buttons for Information
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=5, y=200, width=620, height=45)
        btn_add = Button(button_frame, text='Save', font=('arial', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_add.grid(row=0, column=0, padx=3, pady=5)
        
        btn_update=Button(button_frame,text='Update',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_update.grid(row=0,column=1,padx=3,pady=5)

        #Delete Button
        btn_delete=Button(button_frame,text='Delete',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_delete.grid(row=0,column=2,padx=3,pady=5)

        #Clear Button
        btn_clear=Button(button_frame,text='Clear',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_clear.grid(row=0,column=3,padx=3,pady=5)

         #Main_frame
        Main_frame = Frame(case_tab, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=10, y=280, width=1500, height=560)
        
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Case Information Table',font=('times new roman',11,'bold'),fg='red',bg='white')
        down_frame.place(x=10,y=10,width=1480,height=270)

        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='Search Case Record',font=('times new roman',11,'bold'),fg='red',bg='white')
        search_frame.place(x=0,y=0,width=1470,height=60)

        search_by=Label(search_frame,font=("arial",11,"bold"),text="Search By:",bg="red",fg="white")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        # self.var_com_search=StringVar()
        combo_search_box=ttk.Combobox(search_frame,font=("arial",11,"bold"),width=18,state='readonly')
        combo_search_box['value']=('Select Option','Case_id','Criminal_no')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky=W,padx=5)

        # self.var_search=StringVar()
        search_txt=ttk.Entry(search_frame,width=18,font=("arial",11,"bold"))
        search_txt.grid(row=0,column=2,sticky=W,padx=5)

        #search button
        btn_search=Button(search_frame,text='Search',font=("arial",13,"bold"),width=14,bg='blue')
        btn_search.grid(row=0,column=3,padx=3,pady=5)

        #all button
        btn_all=Button(search_frame,text='Show All',font=("arial",13,"bold"),width=14,bg='blue')
        btn_all.grid(row=0,column=4,padx=3,pady=5)

        crimeagency=Label(search_frame,font=("arial",30,"bold"),text="NATIONAL CRIME AGENCY",bg='white',fg='crimson')
        crimeagency.grid(row=0,column=5,sticky=W,padx=50,pady=0)

        # Table Frame
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        # Scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7","8","9","10","11","12","13","14"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading("1",text="case_id")
        self.criminal_table.heading("2",text="start_date")
        self.criminal_table.heading("3",text="end_date")
        self.criminal_table.heading("4",text="judge")
        self.criminal_table.heading("5",text="verdict")
        self.criminal_table.heading("6",text="criminal_id")
        self.criminal_table.heading("7",text="crime_id")

        self.criminal_table['show']='headings'

        self.criminal_table.column("1",width=100)
        self.criminal_table.column("2",width=100)
        self.criminal_table.column("3",width=100)
        self.criminal_table.column("4",width=100)
        self.criminal_table.column("5",width=100)
        self.criminal_table.column("6",width=100)
        self.criminal_table.column("7",width=100)

        self.criminal_table.pack(fill=BOTH,expand=1)

    
    def create_crimes_tab(self):
        crimes_tab = ttk.Frame(self.notebook)
        self.notebook.add(crimes_tab, text="Crimes")

        ttk.Label(crimes_tab, text="").pack()

        # Upper_frame (Criminal Information)
        upper_frame = LabelFrame(crimes_tab, bd=2, relief=RIDGE, text='Crime Details', font=('times new roman', 11, 'bold'), fg='red', bg='white')
        upper_frame.place(x=10, y=10, width=1500, height=560)

        crimeid=Label(upper_frame,text='Crime_ID:',font=('arial',11,'bold'),bg='white')
        crimeid.grid(row=0,column=0,padx=2,sticky=W)

        caseentry=ttk.Entry(upper_frame, width=22,font=('arial',11,'bold'))
        caseentry.grid(row=0,column=1,padx=2,sticky=W)

        crimeName=Label(upper_frame,font=('arial',12,'bold'),text="Crime_Name:",bg='white')
        crimeName.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_cname=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_cname.grid(row=0,column=3,sticky=W,padx=2,pady=7)

        #Crime Desc
        crimeDesc=Label(upper_frame,font=('arial',12,'bold'),text="Crime_Description:",bg='white')
        crimeDesc.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_cdesc=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_cdesc.grid(row=0,column=5,sticky=W,padx=2,pady=7)

        #severity level
        severity=Label(upper_frame,font=('arial',12,'bold'),text="Severity_Level:",bg='white')
        severity.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_severity=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_severity.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        # date committed
        datecom=Label(upper_frame,font=('arial',12,'bold'),text="Date_Committed:",bg='white')
        datecom.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_datecom=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_datecom.grid(row=1,column=3,sticky=W,padx=2,pady=7)

        #Location
        location=Label(upper_frame,font=('arial',12,'bold'),text="Location:",bg='white')
        location.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_location=ttk.Entry(upper_frame,width=22,font=('arial',11,'bold'))
        txt_location.grid(row=1,column=5,sticky=W,padx=2,pady=7)

        #criminal_Id
        lbl_criminalID=Label(upper_frame,font=('arial',12,'bold'),text="Criminal_ID:",bg='white')
        lbl_criminalID.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_criminalID=ttk.Entry(upper_frame, width=22,font=('arial',11,'bold'))
        txt_criminalID.grid(row=2,column=1,sticky=W,padx=2,pady=7)

        #Incharge Officer
        lbl_incharge=Label(upper_frame,font=('arial',12,'bold'),text="Incharge Officer:",bg='white')
        lbl_incharge.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        txt_incharge=ttk.Entry(upper_frame, width=22,font=('arial',11,'bold'))
        txt_incharge.grid(row=2,column=3,sticky=W,padx=2,pady=7)

        # Buttons for Information
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=5, y=200, width=620, height=45)
        btn_add = Button(button_frame, text='Save', font=('arial', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_add.grid(row=0, column=0, padx=3, pady=5)
        
        btn_update=Button(button_frame,text='Update',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_update.grid(row=0,column=1,padx=3,pady=5)

        #Delete Button
        btn_delete=Button(button_frame,text='Delete',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_delete.grid(row=0,column=2,padx=3,pady=5)

        #Clear Button
        btn_clear=Button(button_frame,text='Clear',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_clear.grid(row=0,column=3,padx=3,pady=5)

        #Main_frame
        Main_frame = Frame(crimes_tab, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=10, y=280, width=1500, height=560)
        
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Crime Information Table',font=('times new roman',11,'bold'),fg='red',bg='white')
        down_frame.place(x=10,y=10,width=1480,height=270)

        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='Search Crime Record',font=('times new roman',11,'bold'),fg='red',bg='white')
        search_frame.place(x=0,y=0,width=1470,height=60)

        search_by=Label(search_frame,font=("arial",11,"bold"),text="Search By:",bg="red",fg="white")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        # self.var_com_search=StringVar()
        combo_search_box=ttk.Combobox(search_frame,font=("arial",11,"bold"),width=18,state='readonly')
        combo_search_box['value']=('Select Option','Case_id','Criminal_no')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky=W,padx=5)

        # self.var_search=StringVar()
        search_txt=ttk.Entry(search_frame,width=18,font=("arial",11,"bold"))
        search_txt.grid(row=0,column=2,sticky=W,padx=5)

        #search button
        btn_search=Button(search_frame,text='Search',font=("arial",13,"bold"),width=14,bg='blue')
        btn_search.grid(row=0,column=3,padx=3,pady=5)

        #all button
        btn_all=Button(search_frame,text='Show All',font=("arial",13,"bold"),width=14,bg='blue')
        btn_all.grid(row=0,column=4,padx=3,pady=5)

        crimeagency=Label(search_frame,font=("arial",30,"bold"),text="NATIONAL CRIME AGENCY",bg='white',fg='crimson')
        crimeagency.grid(row=0,column=5,sticky=W,padx=50,pady=0)

        # Table Frame
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        # Scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7","8","9","10","11","12","13","14"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading("1",text="crime_id")
        self.criminal_table.heading("2",text="crime_Name")
        self.criminal_table.heading("3",text="crime_description")
        self.criminal_table.heading("4",text="Severity_Level")
        self.criminal_table.heading("5",text="Date_Committed")
        self.criminal_table.heading("6",text="location")
        self.criminal_table.heading("7",text="criminal_id")
        self.criminal_table.heading("8",text="incharge_officer")

        self.criminal_table['show']='headings'

        self.criminal_table.column("1",width=100)
        self.criminal_table.column("2",width=100)
        self.criminal_table.column("3",width=120)
        self.criminal_table.column("4",width=100)
        self.criminal_table.column("5",width=100)
        self.criminal_table.column("6",width=100)
        self.criminal_table.column("7",width=100)
        self.criminal_table.column("8",width=100)

        self.criminal_table.pack(fill=BOTH,expand=1)

    def create_prisons_tab(self):
        prisons_tab = ttk.Frame(self.notebook)
        self.notebook.add(prisons_tab, text="Prisons")

        ttk.Label(prisons_tab, text="").pack()
        #Main_frame
        Main_frame = Frame(prisons_tab, bd=2, relief=RIDGE, bg='white')
        Main_frame.place(x=10, y=20, width=1500, height=560)
        
        down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,text='Prison Information Table',font=('times new roman',11,'bold'),fg='red',bg='white')
        down_frame.place(x=10,y=10,width=1480,height=270)

        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,text='Search Prison',font=('times new roman',11,'bold'),fg='red',bg='white')
        search_frame.place(x=0,y=0,width=1470,height=60)

        search_by=Label(search_frame,font=("arial",11,"bold"),text="Search By:",bg="red",fg="white")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        # self.var_com_search=StringVar()
        combo_search_box=ttk.Combobox(search_frame,font=("arial",11,"bold"),width=18,state='readonly')
        combo_search_box['value']=('Select Option','Case_id','Criminal_no')
        combo_search_box.current(0)
        combo_search_box.grid(row=0,column=1,sticky=W,padx=5)

        # self.var_search=StringVar()
        search_txt=ttk.Entry(search_frame,width=18,font=("arial",11,"bold"))
        search_txt.grid(row=0,column=2,sticky=W,padx=5)

        #search button
        btn_search=Button(search_frame,text='Search',font=("arial",13,"bold"),width=14,bg='blue')
        btn_search.grid(row=0,column=3,padx=3,pady=5)

        #all button
        btn_all=Button(search_frame,text='Show All',font=("arial",13,"bold"),width=14,bg='blue')
        btn_all.grid(row=0,column=4,padx=3,pady=5)

        crimeagency=Label(search_frame,font=("arial",30,"bold"),text="NATIONAL CRIME AGENCY",bg='white',fg='crimson')
        crimeagency.grid(row=0,column=5,sticky=W,padx=50,pady=0)

        # Table Frame
        table_frame=Frame(down_frame,bd=2,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        # Scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7","8","9","10","11","12","13","14"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading("1",text="prison_id")
        self.criminal_table.heading("2",text="prison_name")
        self.criminal_table.heading("3",text="location")
        self.criminal_table.heading("4",text="capacity")
        self.criminal_table.heading("5",text="warden")
        self.criminal_table.heading("6",text="number_of_inmates")

        self.criminal_table['show']='headings'

        self.criminal_table.column("1",width=100)
        self.criminal_table.column("2",width=100)
        self.criminal_table.column("3",width=100)
        self.criminal_table.column("4",width=100)
        self.criminal_table.column("5",width=100)
        self.criminal_table.column("6",width=150)

        self.criminal_table.pack(fill=BOTH,expand=1)



if __name__=="__main__":
    root=Tk()
    obj=Criminal(root)
    root.mainloop()

