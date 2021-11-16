from tkinter import *;
from PIL import Image, ImageTk;    #pip install pillow
from tkinter import ttk;
import mysql.connector
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox


class RoomDetails:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #    """""""""""""""""""""""Img Frame""""""""""""""""""""""""

        Img_frame = Label(self.root,bd=4,relief=RIDGE)
        Img_frame.place(x=5,y=400,width=1295,height=140)

        #    """""""""""""""""""""""ImgFrame Image""""""""""""""""""""""""

        img3 = Image.open(r"D:\Python MiniProject\images\bed1.jpg")
        img3 = img3.resize((431,140))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(Img_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=0,width=431,height=140)

        img4 = Image.open(r"D:\Python MiniProject\images\bed2.jpg")
        img4 = img4.resize((431,140))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg4 = Label(Img_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg4.place(x=432,y=0,width=431,height=140)

        img5 = Image.open(r"D:\Python MiniProject\images\bed3.jpg")
        img5 = img5.resize((427,140))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg5 = Label(Img_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg5.place(x=864,y=0,width=427,height=140)


        #    """""""""""""""""""""""Title""""""""""""""""""""""""

        lbl_title = Label(self.root,text="ROOM-BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)


        #    """""""""""""""""""""""Logo""""""""""""""""""""""""

        img2 = Image.open(r"D:\Python MiniProject\images\hoteldeluxelogo.jpg")
        img2 = img2.resize((100,40))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)


         #    """""""""""""""""""""""labelFrame""""""""""""""""""""""""

        labelframeleft = LabelFrame(self.root,bg="black",bd=2,fg="white",relief=RIDGE,text="Add New Room: ",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=540,height=350)
        

        #    """""""""""""""""""""""labels and entries""""""""""""""""""""""""

        # Floor
        lbl_Floor = Label(labelframeleft,text="Floor",bg="black",fg="white",font=("times new roman",18,"bold"),padx=2,pady=6)
        lbl_Floor.grid(row=0,column=0,sticky=W,padx=20)

        self.var_Floor = StringVar()

        entry_Floor = ttk.Entry(labelframeleft,textvariable=self.var_Floor,width=20,font=("times new roman",18,"bold"))
        entry_Floor.grid(row=0,column=1,sticky=W)

        self.var_RoomNo = StringVar()

        # Room No
        lbl_RoomNo = Label(labelframeleft,text="Room No",bg="black",fg="white",font=("times new roman",18,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W,padx=20)

        entry_RoomNo = ttk.Entry(labelframeleft,textvariable=self.var_RoomNo,width=20,font=("times new roman",18,"bold"))
        entry_RoomNo.grid(row=1,column=1,sticky=W)

        self.var_RoomType = StringVar()

        # Room Type
        lbl_RoomType = Label(labelframeleft,text="Room Type",bg="black",fg="white",font=("times new roman",18,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W,padx=20)

        entry_RoomType = ttk.Entry(labelframeleft,textvariable=self.var_RoomType,width=20,font=("times new roman",18,"bold"))
        entry_RoomType.grid(row=2,column=1,sticky=W)


        #    """""""""""""""""""""""Button Frame""""""""""""""""""""""""

        btn_frame = Frame(labelframeleft,bd=0,bg="black",relief=RIDGE)
        btn_frame.place(x=5,y=200,width=520,height=50)


        #    """""""""""""""""""""""Buttons""""""""""""""""""""""""

        buttonAdd = Button(btn_frame,text="Add",command=self.add_data,font=("times new roman",15,"bold"),bg="#22ff00",fg="black",width=10,cursor="hand2")
        buttonAdd.grid(row=0,column=0,padx=1)

        buttonUpdate = Button(btn_frame,text="Update",command=self.update,font=("times new roman",15,"bold"),bg="#05c3fc",fg="black",width=10,cursor="hand2")
        buttonUpdate.grid(row=0,column=1,padx=1)

        buttonDelete = Button(btn_frame,text="Delete",command=self.delete,font=("times new roman",15,"bold"),bg="#ff3300",fg="black",width=10,cursor="hand2")
        buttonDelete.grid(row=0,column=2,padx=1)

        buttonReset = Button(btn_frame,text="Reset",command=self.reset,font=("times new roman",15,"bold"),bg="#fff700",fg="black",width=10,cursor="hand2")
        buttonReset.grid(row=0,column=3,padx=1)


        #    """""""""""""""""""""""Table Frame Search System""""""""""""""""""""""""

        Table_Frame = LabelFrame(self.root,bd=2,relief=RIDGE,fg="white",bg="black",text="Room Details Display: ",font=("times new roman",12,"bold"),padx=2)
        Table_Frame.place(x=550,y=50,width=745,height=350)



        #    """""""""""""""""""""""Show Table Data""""""""""""""""""""""""

        scroll_x = ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame,orient=VERTICAL)

        self.Room_Table = ttk.Treeview(Table_Frame,column=("floor","roomno","roomType"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Room_Table.xview)
        scroll_y.config(command=self.Room_Table.yview)

        self.Room_Table.heading("floor",text="Floor")
        self.Room_Table.heading("roomno",text="Room No")
        self.Room_Table.heading("roomType",text="Room Type")

        self.Room_Table["show"] = "headings"

        self.Room_Table.column("floor",width=100)
        self.Room_Table.column("roomno",width=100)
        self.Room_Table.column("roomType",width=100)
        
        self.Room_Table.pack(fill=BOTH,expand=1)
        self.Room_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    #    """""""""""""""""""""""Adding Customer Details to the Database""""""""""""""""""""""""

    def add_data(self):
        if self.var_Floor.get()=="" or self.var_RoomType.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                        self.var_Floor.get(),
                                                        self.var_RoomNo.get(),
                                                        self.var_RoomType.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New Room Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something Went Wrong:{str(es)}",parent=self.root)


    #    """""""""""""""""""""""Show MySQL data in the Window""""""""""""""""""""""""

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from details")
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

        self.var_Floor.set(row[0])
        self.var_RoomNo.set(row[1]),
        self.var_RoomType.set(row[2])


    #    """""""""""""""""""""""Updating Room Details in the Database""""""""""""""""""""""""

    def update(self):
        if self.var_Floor.get()=="":
            messagebox.showerror("Error","Enter the Floor Number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("update details set Floor = %s, RoomType = %s where RoomNo = %s",( 
                                                        self.var_Floor.get(),
                                                        self.var_RoomType.get(),
                                                        self.var_RoomNo.get(),
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","New Room Updated Successfully",parent=self.root)


    #    """""""""""""""""""""""Deleting the New Room Details from the Database""""""""""""""""""""""""

    def delete(self):
        delete = messagebox.askyesno("Hotel Management System","Do you want to delete this New Room?",parent=self.root)
        if delete > 0:
            conn = mysql.connector.connect(host="localhost",username="root",password="yash2001",database="management")
            my_cursor = conn.cursor()
            query = "delete from details where RoomNo = %s"
            value = (self.var_RoomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return

        conn.commit()
        self.fetch_data()
        conn.close()


    #    """""""""""""""""""""""Resetting the New Room Details""""""""""""""""""""""""

    def reset(self):
        self.var_Floor.set("")
        self.var_RoomNo.set(""),
        self.var_RoomType.set("")


if __name__ == '__main__':
    root=Tk()
    object=RoomDetails(root)
    root.mainloop()