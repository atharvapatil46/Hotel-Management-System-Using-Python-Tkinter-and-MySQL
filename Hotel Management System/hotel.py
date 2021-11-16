from tkinter import *;
from PIL import Image, ImageTk;    #pip install pillow
from customer import Cust_Win;
from room import Roombooking;
from details import RoomDetails;
import time
from time import strftime
from datetime import datetime


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
    root=Tk()
    object = HotelManagementSystem(root)
    root.mainloop()

