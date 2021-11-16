from tkinter import *;
from PIL import Image, ImageTk;    #pip install pillow
from tkinter import ttk;
import mysql.connector
from bill import GenerateBill;
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox

class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")




        #    """""""""""""""""""""""Variables""""""""""""""""""""""""

        self.var_contact = StringVar()
        self.var_checkindate = StringVar()
        self.var_checkoutdate = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noOfdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()


        #    """""""""""""""""""""""Title""""""""""""""""""""""""

        lbl_title = Label(self.root,text="ROOM-BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)


        #    """""""""""""""""""""""Logo""""""""""""""""""""""""

        img2 = Image.open(r"D:\Python MiniProject\images\hoteldeluxelogo.jpg")
        img2 = img2.resize((110,40))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=110,height=40)


         #    """""""""""""""""""""""labelFrame""""""""""""""""""""""""

        labelframeleft = LabelFrame(self.root,bd=2,relief=RIDGE,bg="#ff455e",fg="white",text="Room-Booking Details: ",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)


        #    """""""""""""""""""""""labels and entries""""""""""""""""""""""""

        # Cust_Contact
        lbl_contact = Label(labelframeleft,text="Customer Contact",bg="#ff455e",fg="white",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_contact.grid(row=0,column=0,sticky=W)

        entry_contact = ttk.Entry(labelframeleft,textvariable=self.var_contact,width=20,font=("times new roman",13,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)

        #    """""""""""""""""""""""Fetch Data Button""""""""""""""""""""""""

        buttonFetchData = Button(labelframeleft,text="Fetch Data",command=self.Fetch_Contact,font=("times new roman",8,"bold"),bg="black",fg="white",width=10,cursor="hand2")
        buttonFetchData.place(x=330,y=4)

        # Check In Date
        check_in_date = Label(labelframeleft,text="Check_In Date",bg="#ff455e",fg="white",font=("times new roman",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)

        txt_check_in_date = ttk.Entry(labelframeleft,textvariable=self.var_checkindate,width=29,font=("times new roman",13,"bold"))
        txt_check_in_date.grid(row=1,column=1)


        # Check Out Date
        check_out_date = Label(labelframeleft,text="Check_Out Date",bg="#ff455e",fg="white",font=("times new roman",12,"bold"),padx=2,pady=6)
        check_out_date.grid(row=2,column=0,sticky=W)

        txt_check_out_date = ttk.Entry(labelframeleft,textvariable=self.var_checkoutdate,width=29,font=("times new roman",13,"bold"))
        txt_check_out_date.grid(row=2,column=1)


        # Room Type
        label_RoomType = Label(labelframeleft,text="Room Type",bg="#ff455e",fg="white",font=("times new roman",12,"bold"),padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)

        conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide = my_cursor.fetchall()

        combo_RoomType = ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("times new roman",12,"bold"),width=30,state="readonly")
        combo_RoomType["value"] = ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)


        # Available Rooms 
        lblRoomAvailable = Label(labelframeleft,text="Available Rooms",bg="#ff455e",fg="white",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)


        conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows = my_cursor.fetchall()


        combo_RoomNo = ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("times new roman",12,"bold"),width=30,state="readonly")
        combo_RoomNo["value"] = rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4,column=1)


        # Meal
        lblMeal = Label(labelframeleft,text="Meal",bg="#ff455e",fg="white",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)

        combo_Meal = ttk.Combobox(labelframeleft,textvariable=self.var_meal,font=("times new roman",12,"bold"),width=30,state="readonly")
        combo_Meal["value"] = ("Room Only","Breakfast Only","Half Board","Full Board")
        combo_Meal.current(0)
        combo_Meal.grid(row=5,column=1)


        # No Of Days 
        lblNoOfDays = Label(labelframeleft,text="No. Of Days",bg="#ff455e",fg="white",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)

        txtNoOfDays = ttk.Entry(labelframeleft,textvariable=self.var_noOfdays,width=29,font=("times new roman",13,"bold"),state="readonly")
        txtNoOfDays.grid(row=6,column=1)


        # Paid Tax
        lblPaidTax = Label(labelframeleft,text="Paid Tax",bg="#ff455e",fg="white",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblPaidTax.grid(row=7,column=0,sticky=W)

        txtPaidTax = ttk.Entry(labelframeleft,textvariable=self.var_paidtax,width=29,font=("times new roman",13,"bold"),state="readonly")
        txtPaidTax.grid(row=7,column=1)


        # Sub Total
        lblSubTotal = Label(labelframeleft,text="Sub Total",bg="#ff455e",fg="white",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblSubTotal.grid(row=8,column=0,sticky=W)

        txtSubTotal = ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,width=29,font=("times new roman",13,"bold"),state="readonly")
        txtSubTotal.grid(row=8,column=1)


        # Total Cost
        lblTotalCost = Label(labelframeleft,text="Total Cost",bg="#ff455e",fg="white",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblTotalCost.grid(row=9,column=0,sticky=W)

        txtTotalCost = ttk.Entry(labelframeleft,textvariable=self.var_total,width=29,font=("times new roman",13,"bold"),state="readonly")
        txtTotalCost.grid(row=9,column=1)


        #    """""""""""""""""""""""Button Frame""""""""""""""""""""""""

        btn_frame = Frame(labelframeleft,bg="#ff455e",bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)


        #    """""""""""""""""""""""Bill Button""""""""""""""""""""""""
        buttonBill = Button(labelframeleft,text="Calculate",command=self.total,font=("times new roman",11,"bold"),bg="black",fg="white",width=10,cursor="hand2")
        buttonBill.grid(row=10,column=0,padx=1,sticky=W)

        #    """""""""""""""""""""""Print Bill Button""""""""""""""""""""""""
        buttonGenerateBill = Button(labelframeleft,text="Generate Bill",command=self.GenerateBill,font=("times new roman",11,"bold"),bg="black",fg="white",width=10,cursor="hand2")
        buttonGenerateBill.grid(row=10,column=1,padx=1,sticky=W)


        #    """""""""""""""""""""""Buttons""""""""""""""""""""""""

        buttonAdd = Button(btn_frame,text="Add",command=self.add_data,font=("times new roman",11,"bold"),bg="#22ff00",fg="black",width=10,cursor="hand2")
        buttonAdd.grid(row=0,column=0,padx=1)

        buttonUpdate = Button(btn_frame,text="Update",command=self.update,font=("times new roman",11,"bold"),bg="#05c3fc",fg="black",width=10,cursor="hand2")
        buttonUpdate.grid(row=0,column=1,padx=1)

        buttonDelete = Button(btn_frame,text="Delete",command=self.delete,font=("times new roman",11,"bold"),bg="#ff3300",fg="black",width=10,cursor="hand2")
        buttonDelete.grid(row=0,column=2,padx=1)

        buttonReset = Button(btn_frame,text="Reset",command=self.reset,font=("times new roman",11,"bold"),bg="#fff700",fg="black",width=10,cursor="hand2")
        buttonReset.grid(row=0,column=3,padx=1)


        #    """""""""""""""""""""""Right Side Image""""""""""""""""""""""""
        
        img3 = Image.open(r"D:\Python MiniProject\images\Bed.jpg")
        img3 = img3.resize((520,300))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=760,y=55,width=520,height=300)


        #    """""""""""""""""""""""Table Frame Search System""""""""""""""""""""""""

        Table_Frame = LabelFrame(self.root,bd=2,relief=RIDGE,bg="#ff455e",fg="white",text="View Details and Search System: ",font=("times new roman",12,"bold"),padx=2)
        Table_Frame.place(x=435,y=280,width=860,height=260)


        lblSearchBy = Label(Table_Frame,text="Search By",font=("times new roman",12,"bold"),bg="dark blue",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var = StringVar()

        combo_Search = ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("times new roman",12,"bold"),width=24,state="readonly")
        combo_Search["value"] = ("Contact","roomavailable")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search = StringVar()

        entry_Search = ttk.Entry(Table_Frame,textvariable=self.txt_search,width=24,font=("times new roman",13,"bold"))
        entry_Search.grid(row=0,column=2,padx=2)


        buttonSearch = Button(Table_Frame,text="Search",command=self.search,font=("times new roman",11,"bold"),bg="black",fg="white",width=10,cursor="hand2")
        buttonSearch.grid(row=0,column=3,padx=1)

        buttonShowAll = Button(Table_Frame,text="Show All",command=self.fetch_data,font=("times new roman",11,"bold"),bg="black",fg="white",width=10,cursor="hand2")
        buttonShowAll.grid(row=0,column=4,padx=1)


        #    """""""""""""""""""""""Show Table Data""""""""""""""""""""""""

        details_table = Frame(Table_Frame,bg="#ff455e",bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)

        scroll_x = ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Room_Table = ttk.Treeview(details_table,column=("contact","checkindate","checkoutdate","roomtype","roomavailable","meal","noOfdays","paidtax","subtotal","total"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Room_Table.xview)
        scroll_y.config(command=self.Room_Table.yview)


        self.Room_Table.heading("contact",text="Contact")
        self.Room_Table.heading("checkindate",text="Check-In")
        self.Room_Table.heading("checkoutdate",text="Check-Out")
        self.Room_Table.heading("roomtype",text="Room Type")
        self.Room_Table.heading("roomavailable",text="Room No")
        self.Room_Table.heading("meal",text="Meal")
        self.Room_Table.heading("noOfdays",text="NoOfDays")
        self.Room_Table.heading("paidtax",text="Paid Tax")
        self.Room_Table.heading("subtotal",text="Sub Total")
        self.Room_Table.heading("total",text="Total")


        self.Room_Table["show"] = "headings"

        self.Room_Table.column("contact",width=100)
        self.Room_Table.column("checkindate",width=100)
        self.Room_Table.column("checkoutdate",width=100)
        self.Room_Table.column("roomtype",width=100)
        self.Room_Table.column("roomavailable",width=100)
        self.Room_Table.column("meal",width=100)
        self.Room_Table.column("noOfdays",width=100)
        self.Room_Table.column("paidtax",width=100)
        self.Room_Table.column("subtotal",width=100)
        self.Room_Table.column("total",width=100)
        
        self.Room_Table.pack(fill=BOTH,expand=1)
        self.Room_Table.bind("<ButtonRelease-1>",self.get_cursor)        # Bind with the Table
        self.fetch_data()


    #    """""""""""""""""""""""Adding Customer Details to the Database""""""""""""""""""""""""

    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkindate.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                        self.var_contact.get(),
                                                        self.var_checkindate.get(),
                                                        self.var_checkoutdate.get(),
                                                        self.var_roomtype.get(),
                                                        self.var_roomavailable.get(),
                                                        self.var_meal.get(),
                                                        self.var_noOfdays.get(),
                                                        self.var_paidtax.get(),
                                                        self.var_actualtotal.get(),
                                                        self.var_total.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room Details Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something Went Wrong:{str(es)}",parent=self.root)


    #    """""""""""""""""""""""Show MySQL data in the Window""""""""""""""""""""""""

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Room_Table.delete(*self.Room_Table.get_children())
            for i in rows:
                self.Room_Table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #    """""""""""""""""""""""Automatic Data Fill After Click""""""""""""""""""""""""

    def get_cursor(self,event=""):
        cursor_row = self.Room_Table.focus()
        content = self.Room_Table.item(cursor_row)
        row = content["values"]

        self.var_contact.set(row[0])
        self.var_checkindate.set(row[1]),
        self.var_checkoutdate.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noOfdays.set(row[6])
        self.var_paidtax.set(row[7]),
        self.var_actualtotal.set(row[8]),
        self.var_total.set(row[9])


    #    """""""""""""""""""""""Updating Room Details in the Database""""""""""""""""""""""""

    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Enter the Contact Number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("update room set Contact = %s, check_in = %s, check_out = %s, roomtype = %s, meal = %s, noOfdays = %s, paidtax = %s, subtotal = %s, total = %s where roomavailable = %s",( 
                                                        self.var_contact.get(),
                                                        self.var_checkindate.get(),
                                                        self.var_checkoutdate.get(),
                                                        self.var_roomtype.get(),
                                                        self.var_meal.get(),
                                                        self.var_noOfdays.get(),
                                                        self.var_paidtax.get(),
                                                        self.var_actualtotal.get(),
                                                        self.var_total.get(),
                                                        self.var_roomavailable.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room Details has been Updated Successfully",parent=self.root)


    #    """""""""""""""""""""""Deleting the Room Details from the Database""""""""""""""""""""""""

    def delete(self):
        delete = messagebox.askyesno("Hotel Management System","Do you want to delete this Room?",parent=self.root)
        if delete > 0:
            conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
            my_cursor = conn.cursor()
            query = "delete from room where Contact = %s"
            value = (self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return

        conn.commit()
        self.fetch_data()
        conn.close()


    #    """""""""""""""""""""""Resetting the Room Details""""""""""""""""""""""""

    def reset(self):
        self.var_contact.set("")
        self.var_checkindate.set(""),
        self.var_checkoutdate.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noOfdays.set(""),
        self.var_paidtax.set(""),
        self.var_actualtotal.set(""),
        self.var_total.set("")


    #    """""""""""""""""""""""Fetching Data from Contact Number""""""""""""""""""""""""

    def Fetch_Contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Fill the Contact Number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
            my_cursor = conn.cursor()
            query = ("select Name from customer where Mobile=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error","The Number is not found!",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showdataframe = Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showdataframe.place(x=450,y=55,width=300,height=180)

                lblName = Label(showdataframe,text="Name:",font=("times new roman",12,"bold"))
                lblName.place(x=0,y=0)

                lbl = Label(showdataframe,text=row,font=("times new roman",12,"bold"))
                lbl.place(x=90,y=0)

                #    """""""""""""""""""""""Gender""""""""""""""""""""""""

                conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
                my_cursor = conn.cursor()
                query = ("select Gender from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lblGender = Label(showdataframe,text="Gender:",font=("times new roman",12,"bold"))
                lblGender.place(x=0,y=30)

                lbl2 = Label(showdataframe,text=row,font=("times new roman",12,"bold"))
                lbl2.place(x=90,y=30)

                #    """""""""""""""""""""""Email""""""""""""""""""""""""

                conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
                my_cursor = conn.cursor()
                query = ("select Email from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lblEmail = Label(showdataframe,text="Email:",font=("times new roman",12,"bold"))
                lblEmail.place(x=0,y=60)

                lbl3 = Label(showdataframe,text=row,font=("times new roman",12,"bold"))
                lbl3.place(x=90,y=60)

                #    """""""""""""""""""""""Nationality""""""""""""""""""""""""

                conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
                my_cursor = conn.cursor()
                query = ("select Nationality from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lblNationality = Label(showdataframe,text="Nationality:",font=("times new roman",12,"bold"))
                lblNationality.place(x=0,y=90)

                lbl4 = Label(showdataframe,text=row,font=("times new roman",12,"bold"))
                lbl4.place(x=90,y=90)

                #    """""""""""""""""""""""Address""""""""""""""""""""""""

                conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
                my_cursor = conn.cursor()
                query = ("select Address from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query,value)
                row = my_cursor.fetchone()

                lblAddress = Label(showdataframe,text="Address:",font=("times new roman",12,"bold"))
                lblAddress.place(x=0,y=120)

                lbl5 = Label(showdataframe,text=row,font=("times new roman",12,"bold"))
                lbl5.place(x=90,y=120)


    #    """""""""""""""""""""""Search the Room Details""""""""""""""""""""""""
    
    def search(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from room where "+str(self.search_var.get())+" like "+str(self.txt_search.get()))
        rows = my_cursor.fetchall()

        if len (rows) != 0:
            self.Room_Table.delete(*self.Room_Table.get_children())
            for i in rows:
                self.Room_Table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def total(self):
        inDate = self.var_checkindate.get()
        outDate = self.var_checkoutdate.get()
        inDate = datetime.strptime(inDate,"%d/%m/%Y")
        outDate = datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noOfdays.set(abs(outDate-inDate).days)

        if (self.var_meal.get()=="Room Only" and self.var_roomtype.get()=="Single"):
            q1 = float(0)
            q2 = float(700)
            q3 = float(self.var_noOfdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f"%((q5*q3)*0.1))
            ST = "Rs." + str("%.2f"%((q5*q3)))
            TT = "Rs." + str("%.2f"%((q5*q3)+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Room Only" and self.var_roomtype.get()=="Double"):
            q1 = float(0)
            q2 = float(900)
            q3 = float(self.var_noOfdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f"%((q5*q3)*0.1))
            ST = "Rs." + str("%.2f"%((q5*q3)))
            TT = "Rs." + str("%.2f"%((q5*q3)+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Room Only" and self.var_roomtype.get()=="Luxury"):
            q1 = float(0)
            q2 = float(1500)
            q3 = float(self.var_noOfdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f"%((q5*q3)*0.1))
            ST = "Rs." + str("%.2f"%((q5*q3)))
            TT = "Rs." + str("%.2f"%((q5*q3)+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Breakfast Only" and self.var_roomtype.get()=="Single"):
            q1 = float(100)
            q2 = float(700)
            q3 = float(self.var_noOfdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f"%((q5*q3)*0.1))
            ST = "Rs." + str("%.2f"%((q5*q3)))
            TT = "Rs." + str("%.2f"%((q5*q3)+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Breakfast Only" and self.var_roomtype.get()=="Double"):
            q1 = float(100)
            q2 = float(900)
            q3 = float(self.var_noOfdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f"%((q5*q3)*0.1))
            ST = "Rs." + str("%.2f"%((q5*q3)))
            TT = "Rs." + str("%.2f"%((q5*q3)+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Breakfast Only" and self.var_roomtype.get()=="Luxury"):
            q1 = float(300)
            q2 = float(1500)
            q3 = float(self.var_noOfdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f"%((q5*q3)*0.1))
            ST = "Rs." + str("%.2f"%((q5*q3)))
            TT = "Rs." + str("%.2f"%((q5*q3)+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Half Board" and self.var_roomtype.get()=="Single"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noOfdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f"%((q5*q3)*0.1))
            ST = "Rs." + str("%.2f"%((q5*q3)))
            TT = "Rs." + str("%.2f"%((q5*q3)+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Half Board" and self.var_roomtype.get()=="Double"):
            q1 = float(300)
            q2 = float(900)
            q3 = float(self.var_noOfdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f"%((q5*q3)*0.1))
            ST = "Rs." + str("%.2f"%((q5*q3)))
            TT = "Rs." + str("%.2f"%((q5*q3)+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Half Board" and self.var_roomtype.get()=="Luxury"):
            q1 = float(500)
            q2 = float(1500)
            q3 = float(self.var_noOfdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f"%((q5*q3)*0.1))
            ST = "Rs." + str("%.2f"%((q5*q3)))
            TT = "Rs." + str("%.2f"%((q5*q3)+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Full Board" and self.var_roomtype.get()=="Single"):
            q1 = float(500)
            q2 = float(700)
            q3 = float(self.var_noOfdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f"%((q5*q3)*0.1))
            ST = "Rs." + str("%.2f"%((q5*q3)))
            TT = "Rs." + str("%.2f"%((q5*q3)+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Full Board" and self.var_roomtype.get()=="Double"):
            q1 = float(500)
            q2 = float(900)
            q3 = float(self.var_noOfdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f"%((q5*q3)*0.1))
            ST = "Rs." + str("%.2f"%((q5*q3)))
            TT = "Rs." + str("%.2f"%((q5*q3)+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Full Board" and self.var_roomtype.get()=="Luxury"):
            q1 = float(600)
            q2 = float(1500)
            q3 = float(self.var_noOfdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "Rs." + str("%.2f"%((q5*q3)*0.1))
            ST = "Rs." + str("%.2f"%((q5*q3)))
            TT = "Rs." + str("%.2f"%((q5*q3)+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

    def GenerateBill(self):                           # Function to open Room-booking details window
        self.new_window = Toplevel(self.root)         # Toplevel: To Open any window
        self.app = GenerateBill(self.new_window)






if __name__ == '__main__':
    root=Tk()
    object=Roombooking(root)
    root.mainloop()