from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector

class Register_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1600x900+0+0")

        #    """""""""""""""""""""""Variables""""""""""""""""""""""""
        
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contactno = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_password = StringVar()
        self.var_confirmPassword = StringVar()


        #    """""""""""""""""""""""Image1""""""""""""""""""""""""

        img1 = Image.open(r"D:\Python MiniProject\images\villaregister.jpg")
        img1 = img1.resize((1550,800),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root,image=self.photoimg1,bd=0,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=800)


        #    """""""""""""""""""""""Left Image""""""""""""""""""""""""

        img2 = Image.open(r"D:\Python MiniProject\images\leftvillaregister.jpg")
        img2 = img2.resize((470,550),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg2.place(x=50,y=100,width=470,height=550)

        #    """""""""""""""""""""""Frame""""""""""""""""""""""""

        main_frame = Frame(self.root,bg="black")
        main_frame.place(x=520,y=100,width=800,height=550)

        #    """""""""""""""""""""""Labels and Entry""""""""""""""""""""""""

        lbl_title = Label(main_frame,text="Register Here",font=("times new roman",20,"bold"),bg="black",fg="#c90ffc",bd=0,relief=RIDGE)
        lbl_title.place(x=20,y=20)

        lbl_fname = Label(main_frame,text="First Name",font=("times new roman",15,"bold"),bg="#000",fg="#d640ff",bd=0,relief=RIDGE)
        lbl_fname.place(x=50,y=100)

        self.entry_fname = ttk.Entry(main_frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.entry_fname.place(x=50,y=130,width=250)

        lbl_lname = Label(main_frame,text="Last Name",font=("times new roman",15,"bold"),bg="#000",fg="#d640ff",bd=0,relief=RIDGE)
        lbl_lname.place(x=370,y=100)

        self.entry_lname = ttk.Entry(main_frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.entry_lname.place(x=370,y=130,width=250)

        lbl_contactno = Label(main_frame,text="Contact No",font=("times new roman",15,"bold"),bg="#000",fg="#d640ff",bd=0,relief=RIDGE)
        lbl_contactno.place(x=50,y=170)

        self.entry_contactno = ttk.Entry(main_frame,textvariable=self.var_contactno,font=("times new roman",15,"bold"))
        self.entry_contactno.place(x=50,y=200,width=250)

        lbl_Email = Label(main_frame,text="Email",font=("times new roman",15,"bold"),bg="#000",fg="#d640ff",bd=0,relief=RIDGE)
        lbl_Email.place(x=370,y=170)

        self.entry_Email = ttk.Entry(main_frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.entry_Email.place(x=370,y=200,width=250)

        lbl_SecurityQuestion = Label(main_frame,text="Security Question",font=("times new roman",15,"bold"),bg="#000",fg="#d640ff",bd=0,relief=RIDGE)
        lbl_SecurityQuestion.place(x=50,y=240)

        combo_SecurityQuestion = ttk.Combobox(main_frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        combo_SecurityQuestion["value"] = ("Select","Your Birth Place","Your Pet Name","Your Favourite Thing")
        combo_SecurityQuestion.current(0)
        combo_SecurityQuestion.place(x=50,y=270,width=250)

        lbl_SecurityAnswer = Label(main_frame,text="Security Answer",font=("times new roman",15,"bold"),bg="#000",fg="#d640ff",bd=0,relief=RIDGE)
        lbl_SecurityAnswer.place(x=370,y=240)

        self.entry_SecurityAnswer = ttk.Entry(main_frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.entry_SecurityAnswer.place(x=370,y=270,width=250)

        lbl_Password = Label(main_frame,text="Password",font=("times new roman",15,"bold"),bg="#000",fg="#d640ff",bd=0,relief=RIDGE)
        lbl_Password.place(x=50,y=310)

        self.entry_Password = ttk.Entry(main_frame,textvariable=self.var_password,font=("times new roman",15,"bold"),show="*")
        self.entry_Password.place(x=50,y=340,width=250)

        lbl_ConfirmPassword = Label(main_frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="#000",fg="#d640ff",bd=0,relief=RIDGE)
        lbl_ConfirmPassword.place(x=370,y=310)

        self.entry_ConfirmPassword = ttk.Entry(main_frame,textvariable=self.var_confirmPassword,font=("times new roman",15,"bold"),show="*")
        self.entry_ConfirmPassword.place(x=370,y=340,width=250)

        #    """""""""""""""""""""""Labels and Entry""""""""""""""""""""""""

        self.var_checkbtn = IntVar()
        checkBtn = Checkbutton(main_frame,text="I Agree to all Terms and Conditions!",variable=self.var_checkbtn,font=("times new roman",12,"bold"),bg="#000",fg="#d640ff",activeforeground="#d640ff",activebackground="#000",onvalue=1,offvalue=0)
        checkBtn.place(x=45,y=380)

        #    """""""""""""""""""""""ButtonImages""""""""""""""""""""""""

        buttonRegister = Button(main_frame,text="Register Now",command=self.Register_data,font=("times new roman",12,"bold"),borderwidth=0,bg="#9417c2",fg="white",width=10,cursor="hand2",activebackground="#a927d9",activeforeground="white")
        buttonRegister.place(x=50,y=420,width=200)

        lbl_ConfirmPassword = Label(main_frame,text="Already Have An Account?",font=("times new roman",12,"bold"),bg="#000",fg="#d640ff",bd=0,relief=RIDGE)
        lbl_ConfirmPassword.place(x=370,y=380)

        buttonlogin = Button(main_frame,text="Login Now",font=("times new roman",12,"bold"),borderwidth=0,bg="#9417c2",fg="white",width=10,cursor="hand2",activebackground="#a927d9",activeforeground="white")
        buttonlogin.place(x=370,y=420,width=200)


    #    """""""""""""""""""""""Function Declaration""""""""""""""""""""""""
    
    def Register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select" or self.var_securityA.get()=="":
            messagebox.showerror("Error","All Credentials are required!",parent=self.root)
        elif self.var_password.get()!=self.var_confirmPassword.get():
            messagebox.showerror("Error","Password and Confirm Password must be same!",parent=self.root)
        elif self.var_checkbtn.get()==0:
            messagebox.showerror("Error","Please Agree our Terms and Conditions!",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Already Exists!")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                            self.var_fname.get(),
                                                            self.var_lname.get(),
                                                            self.var_contactno.get(),
                                                            self.var_email.get(),
                                                            self.var_securityQ.get(),
                                                            self.var_securityA.get(),
                                                            self.var_password.get()
                                                            
                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Successfully Registered!!!!")






if __name__ == '__main__':
    root=Tk()
    object = Register_Window(root)
    root.mainloop()