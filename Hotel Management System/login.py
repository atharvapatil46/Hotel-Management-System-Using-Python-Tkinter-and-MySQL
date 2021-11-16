from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
from customer import Cust_Win;
from room import Roombooking;
from details import RoomDetails;
import time
from time import strftime
from datetime import datetime
from hotel import HotelManagementSystem


def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")



        #    """""""""""""""""""""""Image1""""""""""""""""""""""""

        img1 = Image.open(r"D:\Python MiniProject\images\loginbg.jpg")
        img1 = img1.resize((1550,800),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=800)

        #    """""""""""""""""""""""Frame""""""""""""""""""""""""

        main_frame = Frame(self.root,bg="black")
        main_frame.place(x=610,y=170,width=340,height=450)

        #    """""""""""""""""""""""Image2""""""""""""""""""""""""

        img2 = Image.open(r"D:\Python MiniProject\images\authentication.png")
        img2 = img2.resize((100,100),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg2.place(x=730,y=175,width=100,height=100)

        #    """""""""""""""""""""""Label and Entry""""""""""""""""""""""""

        lbl_title = Label(main_frame,text="Get Started",font=("times new roman",20,"bold"),bg="#000",fg="white",bd=0,relief=RIDGE)
        lbl_title.place(x=95,y=100)

        lbl_Username = Label(main_frame,text="Username",font=("times new roman",15,"bold"),bg="#000",fg="white",bd=0,relief=RIDGE)
        lbl_Username.place(x=70,y=155)

        self.entry_username = ttk.Entry(main_frame,font=("times new roman",15,"bold"))
        self.entry_username.place(x=40,y=180,width=270)

        lbl_password = Label(main_frame,text="Password",font=("times new roman",15,"bold"),bg="#000",fg="white",bd=0,relief=RIDGE)
        lbl_password.place(x=70,y=225)

        self.entry_password = ttk.Entry(main_frame,font=("times new roman",15,"bold"),show= '*')
        self.entry_password.place(x=40,y=250,width=270)


        #    """""""""""""""""""""""Icon Image""""""""""""""""""""""""

        img3 = Image.open(r"D:\Python MiniProject\images\usernamenew.png")
        img3 = img3.resize((25,25),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimgicon1 = Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimgicon1.place(x=650,y=323,width=25,height=25)


        img4 = Image.open(r"D:\Python MiniProject\images\passwordicon.png")
        img4 = img4.resize((25,25),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimgicon4 = Label(self.root,image=self.photoimg4,bd=0,relief=RIDGE)
        lblimgicon4.place(x=650,y=395,width=25,height=25)

        #    """""""""""""""""""""""Button""""""""""""""""""""""""

        buttonLogin = Button(main_frame,text="Login",command=self.Login,font=("times new roman",15,"bold"),bg="#2e73f2",fg="white",width=10,cursor="hand2",activeforeground="white",activebackground="#2e73f2")
        buttonLogin.place(x=110,y=300,width=120,height=35)

        #    """""""""""""""""""""""Button""""""""""""""""""""""""

        buttonRegister = Button(main_frame,text="New User Register",command=self.register_window,font=("times new roman",12,"bold"),borderwidth=0,bg="black",fg="white",width=10,cursor="hand2",activeforeground="white",activebackground="black")
        buttonRegister.place(x=13,y=350,width=160)

        forgotPasswordButton = Button(main_frame,text="Forgot Password?",command=self.forgotPasswordWindow,font=("times new roman",12,"bold"),borderwidth=0,bg="black",fg="white",width=10,cursor="hand2",activeforeground="white",activebackground="black")
        forgotPasswordButton.place(x=10,y=370,width=160)


    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register_Window(self.new_window)


    def Login(self):
        if self.entry_username.get()=="" or self.entry_password.get()=="":
            messagebox.showerror("Error","Please Fill the Details!")
        elif self.entry_username.get()=="yash" and self.entry_password.get()=="paddalwar":
            messagebox.showinfo("Success","Welcome to Hotel Deluxe!!!!")
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                            self.entry_username.get(),
                                                            self.entry_password.get()
            ))
            row = my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!")
            else:
                open_main = messagebox.askyesno("YesNo","Access Only Admin")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()


    #    """""""""""""""""""""""Reset Password Function""""""""""""""""""""""""

    def ResetPassword(self):
        if self.combo_SecurityQuestion.get() == "Select":
            messagebox.showerror("Error","Please Select a Question!")
        elif self.entry_SecurityAnswer.get() == "":
            messagebox.showerror("Error","Please Enter the Security Answer!")
        elif self.entry_NewPassword.get() == "":
            messagebox.showerror("Error","Please Enter the New Password!")
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s and securityQ=%s and securityA=%s")
            value = (self.entry_username.get(),self.combo_SecurityQuestion.get(),self.entry_SecurityAnswer.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter Correct Answer!")
            else:
                query = ("update register set password=%s where email=%s")
                value = (self.entry_NewPassword.get(),self.entry_username.get())
                my_cursor.execute(query,value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Password has been Reset, You can Login with New Password!")




    #    """""""""""""""""""""""Forgot Password Function""""""""""""""""""""""""

    def forgotPasswordWindow(self):
        if self.entry_username.get()=="":
            messagebox.showerror("Error","Please Enter the Username!")
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.entry_username.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            # print(row)
            if row == None:
                messagebox.showerror("Error","User not Registered!")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")
                
                
                l = Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),bg="#000",fg="white")
                l.place(x=0,y=10,relwidth=1)

                lbl_SecurityQuestion = Label(self.root2,text="Security Question",font=("times new roman",15,"bold"),fg="#3b0e80",bd=0,relief=RIDGE)
                lbl_SecurityQuestion.place(x=50,y=80)

                self.combo_SecurityQuestion = ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_SecurityQuestion["value"] = ("Select","Your Birth Place","Your Pet Name","Your Favourite Thing")
                self.combo_SecurityQuestion.current(0)
                self.combo_SecurityQuestion.place(x=50,y=110,width=250)

                lbl_SecurityAnswer = Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),fg="#3b0e80",bd=0,relief=RIDGE)
                lbl_SecurityAnswer.place(x=50,y=150)

                self.entry_SecurityAnswer = ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.entry_SecurityAnswer.place(x=50,y=180,width=250)

                lbl_NewPassword = Label(self.root2,text="New Password",font=("times new roman",15,"bold"),fg="#3b0e80",bd=0,relief=RIDGE)
                lbl_NewPassword.place(x=50,y=220)

                self.entry_NewPassword = ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.entry_NewPassword.place(x=50,y=250,width=250)

                buttonResetPassword = Button(self.root2,text="Reset Password",command=self.ResetPassword,font=("times new roman",12,"bold"),bg="#3b0e80",fg="white",width=10,cursor="hand2",activeforeground="white",activebackground="#3b0e80")
                buttonResetPassword.place(x=110,y=290,width=120)




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

        self.entry_Password = ttk.Entry(main_frame,textvariable=self.var_password,font=("times new roman",15,"bold"),show= '*')
        self.entry_Password.place(x=50,y=340,width=250)

        lbl_ConfirmPassword = Label(main_frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="#000",fg="#d640ff",bd=0,relief=RIDGE)
        lbl_ConfirmPassword.place(x=370,y=310)

        self.entry_ConfirmPassword = ttk.Entry(main_frame,textvariable=self.var_confirmPassword,font=("times new roman",15,"bold"),show='*')
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

        buttonlogin = Button(main_frame,command=self.ReturnToLogin,text="Login Now",font=("times new roman",12,"bold"),borderwidth=0,bg="#9417c2",fg="white",width=10,cursor="hand2",activebackground="#a927d9",activeforeground="white")
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

    def ReturnToLogin(self):
        self.root.destroy()


class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")


        #    """"""""""""""""""""1st Image""""""""""""""""""""

        img1 = Image.open(r"D:\Python MiniProject\images\Hotel1.jpg")
        img1 = img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)


        #    """""""""""""""""""""""Logo""""""""""""""""""""""""

        img2 = Image.open(r"D:\Python MiniProject\images\hoteldeluxelogo.jpg")
        img2 = img2.resize((230,140))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)


        #    """""""""""""""""""""""Title""""""""""""""""""""""""

        lbl_title = Label(self.root,text="HOTEL DELUXE",font=("times new roman",40,"bold"),bg="#000",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        def time():
            string = strftime('%H:%M:%S %p')
            lblx.config(text = string)
            lblx.after(1000,time)

        lblx = Label(lbl_title,font=("times new roman",20,"bold"),bg="#000",fg="white")
        lblx.place(x=50,y=0,width=150,height=40)
        time()


        #    """""""""""""""""""""""Main Frame""""""""""""""""""""""""

        main_frame = Label(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)


        #    """""""""""""""""""""""Menu""""""""""""""""""""""""

        lbl_menu = Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="white",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)


        #    """""""""""""""""""""""Button Frame""""""""""""""""""""""""

        btn_frame = Label(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        cust_btn = Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="white",bd=0,relief=RIDGE,cursor="hand2")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn = Button(btn_frame,text="ROOM",command=self.Roombooking,width=22,font=("times new roman",14,"bold"),bg="black",fg="white",bd=0,relief=RIDGE,cursor="hand2")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn = Button(btn_frame,text="DETAILS",width=22,command=self.RoomDetails,font=("times new roman",14,"bold"),bg="black",fg="white",bd=0,relief=RIDGE,cursor="hand2")
        details_btn.grid(row=2,column=0,pady=1)

        report_btn = Button(btn_frame,text="REPORT",width=22,font=("times new roman",14,"bold"),bg="black",fg="white",bd=0,relief=RIDGE,cursor="hand2")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn = Button(btn_frame,text="LOGOUT",command=self.LogOut,width=22,font=("times new roman",14,"bold"),bg="black",fg="white",bd=0,relief=RIDGE,cursor="hand2")
        logout_btn.grid(row=4,column=0,pady=1)


        #    """""""""""""""""""""""MainFrame Image""""""""""""""""""""""""

        img3 = Image.open(r"D:\Python MiniProject\images\rightFrameImg.jpg")
        img3 = img3.resize((1310,590))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=590)


        #    """""""""""""""""""""""Left Bottom Image""""""""""""""""""""""""

        img4 = Image.open(r"D:\Python MiniProject\images\BedroomImg.jpg")
        img4 = img4.resize((230,210))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg1 = Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=225,width=230,height=210)


        img5 = Image.open(r"D:\Python MiniProject\images\BathtubImg1.jpg")
        img5 = img5.resize((230,190))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg1 = Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=420,width=230,height=190)


    def cust_details(self):                           # Function to open customer details window
        self.new_window = Toplevel(self.root)         # Toplevel: To Open any window
        self.app = Cust_Win(self.new_window)

    
    def Roombooking(self):                           # Function to open Room-booking details window
        self.new_window = Toplevel(self.root)         # Toplevel: To Open any window
        self.app = Roombooking(self.new_window)

    def RoomDetails(self):                           # Function to open Details Room window
        self.new_window = Toplevel(self.root)         # Toplevel: To Open any window
        self.app = RoomDetails(self.new_window)

    def LogOut(self):                           # Function to open Details Room window
        self.root.destroy()



if __name__ == '__main__':
    main()


