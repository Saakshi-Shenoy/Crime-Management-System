from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
from subprocess import call


class Login_Window:
    def __init__(self,root):
        # self.root=root
        # self.root.title("Login")
        # self.root.geometry("1550x800+0+0")

        # #self.bg=ImageTk.PhotoImage(file=r"C:\Users\Sharwari\Desktop\DBMS MINI PROJECT\images\2.jpeg")
        # #lbl_bg=Label(self.root,image=self.bg)
        # #lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        # frame=Frame(self.root,bg="black",)
        # # frame.place(x=610,y=170,width=340,height=450)
        # frame.place(x=610, y=170, width=500,height=500)

        # get_str=Label(frame,text="ADMIN LOGIN",font=("verdana",20),fg="white",bg="black")
        # get_str.place(x=80,y=100)

        # # Labels
        # username_lbl=Label(frame,text="Username",font=("verdana",15,"bold"),fg="white",bg="black")
        # username.place(x=50,y=155)

        # self.txtuser=ttk.Entry(frame,font=("verdana",15,"bold"))
        # self.txtuser.place(x=40,y=180,width=270)

        # password_lbl=Label(frame,text="Password",font=("verdana",15,"bold"),fg="white",bg="black")
        # password.place(x=50,y=220)

        # self.txtpass=ttk.Entry(frame,font=("verdana",15,"bold"), show = "*")
        # self.txtpass.place(x=40,y=250,width=270)

        # loginbtn=Button(frame,text="Login",command=self.login, font=("verdana",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        # loginbtn.place(x=110,y=300,width=120)

        ####################################

        self.root = root
        self.root.title("Login")
        self.root.geometry("400x300")

        # Centering the window
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (400 / 2)
        y_coordinate = (screen_height / 2) - (300 / 2)
        self.root.geometry("+%d+%d" % (x_coordinate, y_coordinate))

        self.frame = Frame(self.root, bg="white")
        self.frame.pack(expand=True, fill=BOTH)

        get_str = Label(self.frame, text="Admin Login", font=("Verdana", 20), fg="black", bg="white")
        get_str.pack(pady=20)

        username_lbl = Label(self.frame, text="Username", font=("Verdana", 12, "bold"), fg="black", bg="white")
        username_lbl.pack()
        self.txtuser = ttk.Entry(self.frame, font=("Verdana", 12))
        self.txtuser.pack(pady=5)

        password_lbl = Label(self.frame, text="Password", font=("Verdana", 12, "bold"), fg="black", bg="white")
        password_lbl.pack()
        self.txtpass = ttk.Entry(self.frame, font=("Verdana", 12), show="*")
        self.txtpass.pack(pady=5)

        login_btn = Button(self.frame, text="Login", command=self.login, font=("Verdana", 12, "bold"), bd=0, relief=FLAT, fg="white", bg="green")
        login_btn.pack(pady=20)

        #############################
        # self.root = root
        # self.root.title("Login")
        # self.root.geometry("400x300")

        # # Centering the window
        # screen_width = root.winfo_screenwidth()
        # screen_height = root.winfo_screenheight()
        # x_coordinate = (screen_width / 2) - (400 / 2)
        # y_coordinate = (screen_height / 2) - (300 / 2)
        # self.root.geometry("+%d+%d" % (x_coordinate, y_coordinate))

        # self.frame = Frame(self.root, bg="#121212")  # Dark background
        # self.frame.pack(expand=True, fill=BOTH)

        # get_str = Label(self.frame, text="ADMIN LOGIN", font=("Verdana", 20), fg="white", bg="#121212")  # White text
        # get_str.pack(pady=20)

        # username_lbl = Label(self.frame, text="Username", font=("Verdana", 12), fg="white", bg="#121212")  # White text
        # username_lbl.pack()
        # self.txtuser = ttk.Entry(self.frame, font=("Verdana", 12))
        # self.txtuser.pack(pady=5)

        # password_lbl = Label(self.frame, text="Password", font=("Verdana", 12), fg="white", bg="#121212")  # White text
        # password_lbl.pack()
        # self.txtpass = ttk.Entry(self.frame, font=("Verdana", 12), show="*")
        # self.txtpass.pack(pady=5)

        # # Smoother, rounded button with no shadow
        # login_btn = Button(self.frame, text="Login", command=self.login, font=("Verdana", 12), fg="white", bg="#4CAF50", bd=0, relief=FLAT)
        # login_btn.config(width=10)
        # login_btn.pack(pady=20)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                con=mysql.connector.connect(host='localhost', username='root',password='password', database='crime_project')
                cur=con.cursor() 
                cur.execute("select * from users where userid=%s and password=%s", (self.txtuser.get(), self.txtpass.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid User ID or Password")
                else:
                    messagebox.showinfo("successful", "Welcome") 
                    self.root.destroy()
                    call(['python','criminal.py'])                  
                con.close()  
            except Exception as er:
                messagebox.showerror('error',f'Due to {str(er)}')   
        

if __name__=="__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()



    

                      