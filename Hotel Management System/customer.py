from tkinter import *;
from PIL import Image, ImageTk;    #pip install pillow
from tkinter import ttk;
import mysql.connector
import random
from tkinter import messagebox

class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")



        #    """""""""""""""""""""""Variables""""""""""""""""""""""""
        self.var_ref = StringVar()
        x = random.randint(1000,9999)
        self.var_ref.set(str(x))


        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()



        #    """""""""""""""""""""""Title""""""""""""""""""""""""

        lbl_title = Label(self.root,text="CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)


        #    """""""""""""""""""""""Logo""""""""""""""""""""""""

        img2 = Image.open(r"D:\Python MiniProject\images\hoteldeluxelogo.jpg")
        img2 = img2.resize((100,40))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)


        #    """""""""""""""""""""""labelFrame""""""""""""""""""""""""

        labelframeleft = LabelFrame(self.root,bd=2,bg="#093375",fg="white",relief=RIDGE,text="Customer Details: ",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)


        #    """""""""""""""""""""""labels and entries""""""""""""""""""""""""

        # cust_ref
        lbl_cust_ref = Label(labelframeleft,bg="#093375",fg="white",text="Customer Ref",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref = ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("times new roman",13,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)


        # cust name
        lbl_cust_name = Label(labelframeleft,text="Customer Name",bg="#093375",fg="white",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_name.grid(row=1,column=0,sticky=W)

        entry_ref = ttk.Entry(labelframeleft,textvariable=self.var_cust_name,width=29,font=("times new roman",13,"bold"))
        entry_ref.grid(row=1,column=1)


        # cust Mothername
        lbl_Mother_name = Label(labelframeleft,text="Mother Name",bg="#093375",fg="white",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_Mother_name.grid(row=2,column=0,sticky=W)

        entry_mother_name = ttk.Entry(labelframeleft,textvariable=self.var_mother,width=29,font=("times new roman",13,"bold"))
        entry_mother_name.grid(row=2,column=1)


        # gender combobox
        lbl_gender = Label(labelframeleft,text="Gender",bg="#093375",fg="white",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_gender.grid(row=3,column=0,sticky=W)

        combo_gender = ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=30,state="readonly")
        combo_gender["value"] = ("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)


        # postcode 
        lblpostcode = Label(labelframeleft,text="PostCode",bg="#093375",fg="white",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblpostcode.grid(row=4,column=0,sticky=W)

        entry_postcode = ttk.Entry(labelframeleft,textvariable=self.var_post,width=29,font=("times new roman",13,"bold"))
        entry_postcode.grid(row=4,column=1)


        # mobilenumber
        lblmobilenumber = Label(labelframeleft,text="Mobile Number",bg="#093375",fg="white",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblmobilenumber.grid(row=5,column=0,sticky=W)

        entry_mobilenumber = ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=29,font=("times new roman",13,"bold"))
        entry_mobilenumber.grid(row=5,column=1)


        # email 
        lblemail = Label(labelframeleft,text="Email",bg="#093375",fg="white",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblemail.grid(row=6,column=0,sticky=W)

        entry_email = ttk.Entry(labelframeleft,textvariable=self.var_email,width=29,font=("times new roman",13,"bold"))
        entry_email.grid(row=6,column=1)


        # nationality
        lblnationality = Label(labelframeleft,text="Nationality",bg="#093375",fg="white",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblnationality.grid(row=7,column=0,sticky=W)

        combo_nationality = ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("times new roman",12,"bold"),width=30,state="readonly")
        combo_nationality["value"] = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Anguilla', 'Antigua And Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia And Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Virgin Islands', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Cook Islands', 'Costa Rica', 'Croatia', 'Curacao', 'Cyprus', 'Czech Republic', 'Democratic Republic Of The Congo', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Estonia', 'Ethiopia', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle Of Man', 'Israel', 'Italy', 'Ivory Coast', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Libyan Arab Jamahiriya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macau', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Martinique', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nepal', 'Netherlands', 'Netherlands Antilles', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Reunion', 'Romania', 'Russia', 'Russian Federation', 'Rwanda', 'Saint Kitts And Nevis', 'Saint Lucia', 'Saint Martin', 'Saint Pierre And Miquelon', 'Saint Vincent And The Grenadines', 'Samoa', 'San Marino', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Taiwan', 'Tajikistan', 'Tanzania', 'Tanzania, United Republic Of', 'Thailand', 'Togo', 'Tonga', 'Trinidad And Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks And Caicos Islands', 'U.S. Virgin Islands', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Wallis And Futuna', 'Yemen', 'Zambia', 'Zimbabwe']
        combo_nationality.current(0)
        combo_nationality.grid(row=7,column=1)


        # idproof type combobox
        lblIdProof = Label(labelframeleft,text="Id Proof Type",bg="#093375",fg="white",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblIdProof.grid(row=8,column=0,sticky=W)

        combo_IdProof = ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("times new roman",12,"bold"),width=30,state="readonly")
        combo_IdProof["value"] = ("Aadhar Card","Pan Card","Driving Liscense","Passport")
        combo_IdProof.current(0)
        combo_IdProof.grid(row=8,column=1)


        # IdNumber 
        lblIdNumber = Label(labelframeleft,text="Id Number",bg="#093375",fg="white",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)

        entry_IdNumber = ttk.Entry(labelframeleft,textvariable=self.var_id_number,width=29,font=("times new roman",13,"bold"))
        entry_IdNumber.grid(row=9,column=1)


        # Address 
        lblAddress = Label(labelframeleft,text="Address",bg="#093375",fg="white",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)

        entry_Address = ttk.Entry(labelframeleft,textvariable=self.var_address,width=29,font=("times new roman",13,"bold"))
        entry_Address.grid(row=10,column=1)


        #    """""""""""""""""""""""Button Frame""""""""""""""""""""""""

        btn_frame = Frame(labelframeleft,bg="#093375",bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)


        #    """""""""""""""""""""""Buttons""""""""""""""""""""""""

        buttonAdd = Button(btn_frame,text="Add",command=self.add_data,font=("times new roman",11,"bold"),bg="#22ff00",fg="black",width=10,cursor="hand2")
        buttonAdd.grid(row=0,column=0,padx=1)

        buttonUpdate = Button(btn_frame,text="Update",command=self.update,font=("times new roman",11,"bold"),bg="#05c3fc",fg="black",width=10,cursor="hand2")
        buttonUpdate.grid(row=0,column=1,padx=1)

        buttonDelete = Button(btn_frame,text="Delete",command=self.delete,font=("times new roman",11,"bold"),bg="#ff3300",fg="black",width=10,cursor="hand2")
        buttonDelete.grid(row=0,column=2,padx=1)

        buttonReset = Button(btn_frame,text="Reset",command=self.reset,font=("times new roman",11,"bold"),bg="#fff700",fg="black",width=10,cursor="hand2")
        buttonReset.grid(row=0,column=3,padx=1)



        #    """""""""""""""""""""""Table Frame Search System""""""""""""""""""""""""  

        Table_Frame = LabelFrame(self.root,bd=2,bg="#093375",fg="white",relief=RIDGE,text="View Details and Search System: ",font=("times new roman",12,"bold"),padx=2)
        Table_Frame.place(x=435,y=50,width=860,height=490)


        lblSearchBy = Label(Table_Frame,text="Search By",font=("times new roman",12,"bold"),bg="Red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var = StringVar()

        combo_Search = ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("times new roman",12,"bold"),width=24,state="readonly")
        combo_Search["value"] = ("Ref","Mobile")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search = StringVar()

        entry_Search = ttk.Entry(Table_Frame,textvariable=self.txt_search,width=24,font=("times new roman",13,"bold"))
        entry_Search.grid(row=0,column=2,padx=2)


        buttonSearch = Button(Table_Frame,text="Search",command=self.search,font=("times new roman",11,"bold"),bg="#07f52f",fg="black",width=10,cursor="hand2")
        buttonSearch.grid(row=0,column=3,padx=1)

        buttonShowAll = Button(Table_Frame,text="Show All",command=self.fetch_data,font=("times new roman",11,"bold"),bg="#07f52f",fg="black",width=10,cursor="hand2")
        buttonShowAll.grid(row=0,column=4,padx=1)



        #    """""""""""""""""""""""Show Table Data""""""""""""""""""""""""

        details_table = Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=400)

        scroll_x = ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table,column=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)


        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="PostCode")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id Proof")
        self.Cust_Details_Table.heading("idnumber",text="Id Number")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"] = "headings"

        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)
        
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    #    """""""""""""""""""""""Adding Customer Details to the Database""""""""""""""""""""""""

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                        self.var_ref.get(),
                                                        self.var_cust_name.get(),
                                                        self.var_mother.get(),
                                                        self.var_gender.get(),
                                                        self.var_post.get(),
                                                        self.var_mobile.get(),
                                                        self.var_email.get(),
                                                        self.var_nationality.get(),
                                                        self.var_id_proof.get(),
                                                        self.var_id_number.get(),
                                                        self.var_address.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something Went Wrong:{str(es)}",parent=self.root)



    #    """""""""""""""""""""""Show MySQL data in the Window""""""""""""""""""""""""

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #    """""""""""""""""""""""Automatic Data Fill After Click""""""""""""""""""""""""

    def get_cursor(self,event=""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])


    #    """""""""""""""""""""""Updating Customer Details in the Database""""""""""""""""""""""""

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Enter the Mobile Number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("update customer set Name = %s, Mother = %s, Gender = %s, PostCode = %s, Mobile = %s, Email = %s, Nationality = %s, Idproof = %s, Idnumber = %s, Address = %s where Ref = %s",( 
                                                        self.var_cust_name.get(),
                                                        self.var_mother.get(),
                                                        self.var_gender.get(),
                                                        self.var_post.get(),
                                                        self.var_mobile.get(),
                                                        self.var_email.get(),
                                                        self.var_nationality.get(),
                                                        self.var_id_proof.get(),
                                                        self.var_id_number.get(),
                                                        self.var_address.get(),
                                                        self.var_ref.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer Details has been Updated Successfully",parent=self.root)


    #    """""""""""""""""""""""Deleting the Customer from the Database""""""""""""""""""""""""

    def delete(self):
        delete = messagebox.askyesno("Hotel Management System","Do you want to delete this customer?",parent=self.root)
        if delete > 0:
            conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
            my_cursor = conn.cursor()
            query = "delete from customer where Ref = %s"
            value = (self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return

        conn.commit()
        self.fetch_data()
        conn.close()


    #    """""""""""""""""""""""Resetting the Customer Details""""""""""""""""""""""""

    def reset(self):
        #self.var_ref.set("")
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")

        x = random.randint(1000,9999)
        self.var_ref.set(str(x))


    #    """""""""""""""""""""""Search the Customer Details""""""""""""""""""""""""
    
    def search(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" like "+str(self.txt_search.get()))
        rows = my_cursor.fetchall()

        if len (rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()



if __name__ == '__main__':
    root=Tk()
    object=Cust_Win(root)
    root.mainloop()