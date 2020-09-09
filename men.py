         
from Tkinter import *
from tkMessageBox import *
import sqlite3
import subprocess
con=sqlite3.Connection('MENU')
cur=con.cursor()
cur.execute('create table if not exists menu1(Sno number(10) primary key,variety varchar2(30),Price number(4))')
def create():
   cur.execute('create table menu1 if not exists(Sno number(10) primary key,variety varchar2(30),Price number(4))')
   cur.fetchall()
def insert():
   root_ins=Tk()
   Label(root_ins,text="Sno").grid()
   e1=Entry(root_ins)
   e1.grid() 
   Label(root_ins,text="ITEM").grid()
   e2=Entry(root_ins)
   e2.grid()
   Label(root_ins,text="Price").grid()
   e3=Entry(root_ins)
   e3.grid()
   def insert_info():
      a=(int(e1.get()),e2.get(),int(e3.get()))
      print a
      cur.execute('insert into menu1 values (?,?,?)',((int(e1.get()),e2.get(),int(e3.get()))))
      cur.fetchall()
      con.commit()
      showinfo("Success","Successfully Inserted")
   Button(root_ins,text="Insert",command=insert_info).grid()
   root_ins.mainloop()
   
def disp():
   rotw=Tk()
   rotw.geometry('600x600')
   rotw.configure(background='light grey')
   rotw.title('MENU CARD')
   #Label(rotw,text='HOT PIZZA ACE MENU CARD').grid()
   
   
   Label(rotw,text='SNO',font=('arial',20,'underline'),bd=7,relief='raised',bg='DARK GREY').grid(row=0,column=0)
   Label(rotw,text='VARIETY',font=('arial',20,'underline'),bd=7,relief='raised',bg='DARK GREY').grid(row=0,column=1)
   Label(rotw,text='PRICE',font=('arial',20,'underline'),bd=7,relief='raised',bg='DARK GREY').grid(row=0,column=2)
   cur.execute('select * from menu1 order by Sno')
   c=cur.fetchall()
   global count
   count=0
   
   for i in c:
      count=count+1
      Label(rotw,text=str(i[0]),font=('constancia',8,'bold','italic'),bg='light GREY').grid(row=0+count,column=0)
      Label(rotw,text=str(i[1]),font=('constancia',8,'italic','bold'),bg='light GREY').grid(column=1,row=0+count)
      Label(rotw,text=str(i[2]),font=('constancia',8,'italic','bold'),bg='light GREY').grid(column=2,row=0+count)
  

   #Label(rotw,text="details"+str(c)).grid()
   rotw.mainloop()
   
#from PIL import ImageTk, Image
def donothing():
   filewin = Toplevel(wel)
   button = Button(filewin, text="DO NOTHING")
   button.pack()
def bill():
   subprocess.call("python billing.py")
   
def delete():
   dele=Tk()
   Label(dele,text="Enter the serial no. you want to delete:").grid()
   e1=Entry(dele)
   e1.grid()
   def dequery():
      cur.execute('delete from menu1 where Sno=(?)',(e1.get(),))
      con.commit()
      showinfo('Successful','Data Deleted Successfully')
   Button(dele,text="Delete",command=dequery).grid()   
   dele.mainloop()
def deleteall():
   dele1=Tk()
   def dequery():
      cur.execute('delete from menu1')
      con.commit()
      showinfo('Successful','Data Deleted Successfully')
   Button(dele1,text="Delete ALL",command=dequery).grid()   
   dele1.mainloop()
   
wel = Tk()
wel.geometry("1350x1350")
wel.title("HOT PIZZA ACE Menu Window")
Label(wel,text="HOT PIZZA ACE WELCOMES YOU ",relief='ridge',font='times 40 bold underline',bd=10,bg='dark grey').pack()

b=PhotoImage(file="counter.gif")
Label(wel,image=b).pack()
menubar = Menu(wel)
stockmenu = Menu(menubar, tearoff=0)
stockmenu.add_command(label="Add Items", command=insert)
stockmenu.add_command(label="Delete Items", command=delete)
stockmenu.add_command(label="Delete ALL Items", command=deleteall)

stockmenu.add_separator()

stockmenu.add_command(label="Exit", command=wel.quit)
menubar.add_cascade(label="Stock MAINTAINENCE", menu=stockmenu)
expirymenu = Menu(menubar, tearoff=0)
expirymenu.add_command(label="MILK ", command=donothing)

expirymenu.add_separator()

expirymenu.add_command(label="soft drinks", command=donothing)
expirymenu.add_command(label="cheese", command=donothing)

menubar.add_cascade(label="Expiry", menu=expirymenu)
billmenu = Menu(menubar, tearoff=0)
billmenu.add_command(label="Billing", command=bill)
billmenu.add_command(label="TOTAL INCOME",command=donothing)
menubar.add_cascade(label="Billing", menu=billmenu)
wel.config(menu=menubar)




    

#Button(wel,text='create',font='times 20 bold italic underline',command=create).pack()
#Button(wel,text='insert',font='times 20 bold italic underline',command=insert).pack()
Button(wel,text='DISPLAY MENU CARD',font='times 30 bold ',bd=7,fg='grey',bg='INDIGO',command=disp).pack()

Button(wel,text='EXIT',font='times 30 bold ',bd=7,bg='INDIGO',fg='grey',command=wel.destroy).pack()

wel.configure(bg='silver')
wel.mainloop()
