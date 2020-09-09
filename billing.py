from Tkinter import *
import random
import time;
from tkMessageBox import *
import math
from sqlite3 import *
import tkMessageBox
root=Tk()
root.geometry("1600x800+0+0")
Tops=Frame(root,width=1600,height=50,bg="BLACK",relief=SUNKEN)
Tops.pack(side='top')

f1=Frame(root,width=800,height=700,relief=SUNKEN)
f1.pack(side='left')

f2=Frame(root,width=300,height=700,relief='raised')
f2.pack(side='right')


localtime=time.asctime(time.localtime(time.time()))
root.title('Hot PIzza Ace BillIng')

lblInfo=Label(Tops,font=('IMPACT',50),text="HOT PIZZA ACE BILLING SYSTEM",fg="BLACK",bd=15,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('TIMES',20,'bold'),text=localtime,fg="BLACK",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)


text_Input=StringVar()
operator=""

def click(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)

def clear():
    global operator
    operator=""
    text_Input.set("")

def EqualTo():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""



def Ref():
    x=random.randint(10908,500876)
    randomRef=str(x)
    rand.set(randomRef)


    COP=float(PIZZA.get())
    CoMILKSHAKE=float(MILKSHAKE.get())
    CoICECRM=float(ICECRM.get())
    CoSDRINKS=float(SDRINKS.get())
    CoPASTA=float(PASTA.get())
    CoBRGSDW=float(BRGSDW.get())
    CoGARBRD=float(GARBRD.get())

    CostofPIZZA=COP*400
    CostofMILKSHAKE=CoMILKSHAKE*70
    CostofICECRM=CoICECRM*80
    CostofSDRINKS= CoSDRINKS*45
    CostofPASTA= CoPASTA*90
    CostofBRGSDW=CoBRGSDW*60
    CostofGARBRD=CoGARBRD*75

    Costofitems="Rs",str('%.2f' % (  CostofPIZZA+CostofMILKSHAKE+CostofICECRM+ CostofSDRINKS+CostofPASTA+CostofBRGSDW+ CostofGARBRD))
    PayTax=(( CostofPIZZA+CostofMILKSHAKE+ CostofICECRM+ CostofSDRINKS+ CostofPASTA+ CostofBRGSDW+ CostofGARBRD)*0.08)
    TotalCost=( CostofPIZZA+ CostofMILKSHAKE+CostofICECRM+CostofSDRINKS+CostofPASTA+ CostofBRGSDW+CostofGARBRD)
    Ser_Charge=(( CostofPIZZA+ CostofMILKSHAKE+CostofICECRM+CostofSDRINKS+CostofPASTA+ CostofBRGSDW+CostofGARBRD)/99)
    Service='Rs',str('%.2f'%Ser_Charge)
    PaidTax="Rs",str('%.2f'%PayTax)

    Service_Charge.set(Ser_Charge)
    COST.set(TotalCost)
    STATETAX.set(PayTax)
    
    
    TOTAL=CostofPIZZA+CostofMILKSHAKE+CostofICECRM+ CostofSDRINKS+CostofPASTA+CostofBRGSDW+CostofGARBRD
    if TOTAL > 5000:
        tkMessageBox.showinfo('DISCOUNT','YOU HAVE GOT THE DISCOUNT OF 10%')
        TOTALDISCOUNT.set((CostofPIZZA+CostofMILKSHAKE+CostofICECRM+ CostofSDRINKS+CostofPASTA+CostofBRGSDW+
                        CostofGARBRD)/10.0)
        SUBTOTAL.set(math.floor((CostofPIZZA+CostofMILKSHAKE+CostofICECRM+ CostofSDRINKS+CostofPASTA+CostofBRGSDW+
                        CostofGARBRD)/1.1111))
        TOTALCOST.set((PayTax+math.floor((CostofPIZZA+CostofMILKSHAKE+CostofICECRM+ CostofSDRINKS+CostofPASTA+CostofBRGSDW+
                        CostofGARBRD)/1.1111)+Ser_Charge))
        NET.set(math.floor(PayTax+((CostofPIZZA+CostofMILKSHAKE+CostofICECRM+ CostofSDRINKS+CostofPASTA+CostofBRGSDW+
                        CostofGARBRD)/1.1111)+Ser_Charge))
        
    elif TOTAL > 2000:
        tkMessageBox.showinfo('DISCOUNT','YOU HAVE GOT THE DISCOUNT OF 5%')
        TOTALDISCOUNT.set((CostofPIZZA+CostofMILKSHAKE+CostofICECRM+ CostofSDRINKS+CostofPASTA+CostofBRGSDW+CostofGARBRD)/20.0)
        SUBTOTAL.set(math.floor((CostofPIZZA+CostofMILKSHAKE+CostofICECRM+ CostofSDRINKS+CostofPASTA+CostofBRGSDW+
                        CostofGARBRD)/1.0526))
        TOTALCOST.set((PayTax+math.floor((CostofPIZZA+CostofMILKSHAKE+CostofICECRM+ CostofSDRINKS+CostofPASTA+CostofBRGSDW+
                        CostofGARBRD)/1.0526)+Ser_Charge))
        NET.set(math.floor(PayTax+((CostofPIZZA+CostofMILKSHAKE+CostofICECRM+ CostofSDRINKS+CostofPASTA+CostofBRGSDW+
                        CostofGARBRD)/1.0526)+Ser_Charge))
                      
    else:
        TOTALDISCOUNT.set(0)
        SUBTOTAL.set(CostofPIZZA+CostofMILKSHAKE+CostofICECRM+ CostofSDRINKS+CostofPASTA+CostofBRGSDW+
                        CostofGARBRD)
        TOTALCOST.set((PayTax+(CostofPIZZA+CostofMILKSHAKE+CostofICECRM+ CostofSDRINKS+CostofPASTA+CostofBRGSDW+
                        CostofGARBRD)+Ser_Charge))
        NET.set(PayTax+(CostofPIZZA+CostofMILKSHAKE+CostofICECRM+ CostofSDRINKS+CostofPASTA+CostofBRGSDW+
                        CostofGARBRD)+Ser_Charge)



   


    



def qExit():
    root.destroy()


def Reset():
    rand.set("")
    PIZZA.set(0)
    MILKSHAKE.set(0)
    ICECRM.set(0)
    SDRINKS.set(0)
    PASTA.set(0)
    BRGSDW.set(0)
    GARBRD.set(0)
    COST.set(0)
    Service_Charge.set(0)
    STATETAX.set(0)
    SUBTOTAL.set(0)
    TOTALCOST.set(0)
    TOTALDISCOUNT.set(0)
    NET.set(0)

def Memo():
    con=Connection('data')
    cur=con.cursor()
    #cur.execute("drop table cust")
    cur.execute("create table if not exists cust(bno varchar2(5) PRIMARY KEY,cname varchar2(10),amount varchar2(10),cont varchar2(10),d varchar2(10))")

    root1=Tk()
    root1.geometry("1170x300")
    root1.title("Customer Bill Generation")
    
    Label(root1,text="CUSTOMER",font='induction 20 bold',bd=10,bg='dark grey').grid(row=0,column=0,sticky=E+W)
    Label(root1,text=" BILLING",font='induction 20 bold',bd=10,bg='dark grey').grid(row=0,column=1,sticky=E+W)
    Label(root1,text=" RECORD",font='induction 20 bold',bd=10,bg='dark grey').grid(row=0,column=2,sticky=E+W)
    Label(root1,text=" SYSTEM ",font='induction 20 bold',bd=10,bg='dark grey').grid(row=0,column=3,sticky=E+W)






    Label(root1,text="Enter BILL no.",font='calibri 10').grid(row=1,column=0)
    Label(root1,text="Enter Full Name :",font='calibri 10').grid(row=2,column=0)
    Label(root1,text="Enter AMOUNT TO BE PAID(in Rs.) :",font='calibri 10').grid(row=3,column=0)
    Label(root1,text="CONTACT NO :",font='calibri 10').grid(row=4,column=0)
    Label(root1,text="Date of BILLING :",font='calibri 10').grid(row=5,column=0)
    Label(root1,text="BILL TO BE SEARCHED :",font='calibri 10').grid(row=5,column=2)

    global bno,cname,amount,cont,fetchBn,d
    bno=Entry(root1)
    cname=Entry(root1)
    amount=Entry(root1)
    cont=Entry(root1)
    fetchBn=Entry(root1)
    d=Entry(root1)

    bno.grid(row=1,column=1)
    cname.grid(row=2,column=1)
    amount.grid(row=3,column=1)
    cont.grid(row=4,column=1)
    d.grid(row=5,column=1)
    fetchBn.grid(row=5,column=3)


    def insert():
        try:
            cur.execute("insert into cust values(?,?,?,?,?)",(bno.get(),cname.get(),amount.get(),cont.get(),d.get()))
            con.commit()
            showinfo('Success','The record has been inserted successfully')
        except:
            showerror('Error!','An entry with same bill no already exists!')
    

    def show():
        showbn=str(fetchBn.get())
        if showbn=="":
            showerror('Error!','Invalid Entry!')
        else:
            comm=('select bno,cname,amount,cont,d from cust where bno=')+showbn    
            cur.execute(comm)
            x=cur.fetchall()
        
            if x==[]:
                showerror('Error!','Invalid Entry!')
            else:
                win=Tk()
                win.title("BILL Record")
                win.geometry("400x250")
                win.configure(background='powder blue')
                print bno.get()
                Label(win,text="BILL NO.: "+x[0][0],font=('arial',16,'bold'),bg='powder blue').pack()
                Label(win,text="CUSTOMER NAME:"+x[0][1],font=('arial',16,'bold'),bg='powder blue').pack()
                Label(win,text="CONTACT NO.:"+x[0][3],font=('arial',16,'bold'),bg='powder blue').pack()
                Label(win,text="AMOUNT PAID: Rs."+x[0][2],font=('arial',16,'bold'),bg='powder blue').pack()
                Label(win,text="BILLING DATE:"+x[0][4],font=('arial',16,'bold'),bg='powder blue').pack()
                win.mainloop()

    def show_all():
        cur.execute('select bno,cname,amount,cont,d from cust')
        x=cur.fetchall()
        new=Tk()
        new.geometry("1000x1400")
        new.title("All Records")
        new.configure(background='powder blue')
        i=0
        Label(new,text="|SNO.|",font=('arial',16,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=0)
        Label(new,text="|  BILL NO. |",font=('arial',16,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=1)
        Label(new,text="|    CUSTOMER NAME     |",font=('arial',16,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=2)
        Label(new,text="|AMOUNT PAID|",font=('arial',16,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=3)
        Label(new,text="|   CONTACT   |",font=('arial',16,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=4)
        Label(new,text="|   BILLING DATE   |",font=('arial',16,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=5)
        for i in range (0,len(x)):
        
            Label(new,text=i+1,font=('arial',16,'bold'),bg='powder blue').grid(row=i+1,column=0)
            Label(new,text=x[i][0],font=('arial',16,'bold'),bg='powder blue').grid(row=i+1,column=1)
            Label(new,text=x[i][1],font=('arial',16,'bold'),bg='powder blue').grid(row=i+1,column=2)
            Label(new,text="Rs."+x[i][2],font=('arial',16,'bold'),bg='powder blue').grid(row=i+1,column=3)
            Label(new,text=x[i][3],font=('arial',16,'bold'),bg='powder blue').grid(row=i+1,column=4)
            Label(new,text=x[i][4],font=('arial',16,'bold'),bg='powder blue').grid(row=i+1,column=5)
          
        new.mainloop()
        
    def empty():
        new1=Tk()
        r=tkMessageBox.askyesno("Rethink","Are you sure you want to delete all previous data?")
        if r==True:
            cur.execute('delete from cust')
            con.commit()
            showinfo('Successful','All Details Deleted Successfully')
        else:
            new1.destroy()
        print r
            
            
        
        
    
            
    def exitpls():
        root1.destroy()
    

    Button(root1,text='Insert',command=insert,bd=5,bg='dark grey',font=('arial',16,'bold')).grid(row=6,column=0)
    Button(root1,text='Show Bill Details',font=('arial',16,'bold'),bd=5,bg='dark grey',command=show).grid(row=6,column=3)
    Button(root1,text='Exit',font=('arial',16,'bold'),bd=5,bg='dark grey',command=exitpls).grid(row=6,column=1)
    Button(root1,text='Show  All Details',font=('arial',16,'bold'),bd=5,bg='dark grey',command=show_all).grid(row=7,column=3)
    Button(root1,text='Reset Details',font=('arial',14,'bold'),bd=5,bg='dark grey',command=empty).grid(row=9,column=1)
    

    root1.mainloop()






    

####

rand=StringVar()
PIZZA=IntVar()
MILKSHAKE=IntVar()
ICECRM=IntVar()
SDRINKS=IntVar()
PASTA=IntVar()
BRGSDW=IntVar()
GARBRD=IntVar()
COST=IntVar()
Service_Charge=IntVar()
STATETAX=IntVar()
TOTALDISCOUNT=IntVar()
SUBTOTAL=IntVar()
TOTALCOST=IntVar()
NET=IntVar()
                      
###########################################################################################


lblRefrence=Label(f1,font=('arial',16,'bold','italic'),text='Reference',bd=16,anchor='w')
lblRefrence.grid(row=0,column=0)
txtRefrence=Entry(f1,font=('arial',16,'bold'),textvariable =rand,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtRefrence.grid(row=0,column=1)




lblPIZZA=Label(f1,font=('arial',16,'bold','italic'),text='PIZZA',bd=16,anchor='w')
lblPIZZA.grid(row=1,column=0)
txtPIZZA=Entry(f1,font=('arial',16,'bold'),textvariable =PIZZA,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtPIZZA.grid(row=1,column=1)



lblMILKSHAKE=Label(f1,font=('arial',16,'bold','italic'),text='MILKSHAKES',bd=16,anchor='w')
lblMILKSHAKE.grid(row=2,column=0)
txtMILKSHAKE=Entry(f1,font=('arial',16,'bold'),textvariable =MILKSHAKE,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtMILKSHAKE.grid(row=2,column=1)


lblICECRM=Label(f1,font=('arial',16,'bold','italic'),text='ICE CREAMS',bd=16,anchor='w')
lblICECRM.grid(row=3,column=0)
txtICECRM=Entry(f1,font=('arial',16,'bold'),textvariable =ICECRM,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtICECRM.grid(row=3,column=1)



lblSDRINKS=Label(f1,font=('arial',16,'bold','italic'),text='SOFT DRINKS',bd=16,anchor='w')
lblSDRINKS.grid(row=4,column=0)
txtSDRINKS=Entry(f1,font=('arial',16,'bold'),textvariable =SDRINKS,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSDRINKS.grid(row=4,column=1)


lblPASTA=Label(f1,font=('arial',16,'bold'),text='ITALIAN PASTA',bd=16,anchor='w')
lblPASTA.grid(row=4,column=0)
txtPASTA=Entry(f1,font=('arial',16,'bold'),textvariable =PASTA,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtPASTA.grid(row=4,column=1)


lblBRGSDW=Label(f1,font=('arial',16,'bold'),text='BURGERS/SANDWICHES',bd=16,anchor='w')
lblBRGSDW.grid(row=5,column=0)
txtBRGSDW=Entry(f1,font=('arial',16,'bold'),textvariable =BRGSDW,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtBRGSDW.grid(row=5,column=1)





lblGARBRD=Label(f1,font=('arial',16,'bold'),text='GARLIC BREAD',bd=16,anchor='w')
lblGARBRD.grid(row=6,column=0)
txtGARBRD=Entry(f1,font=('arial',16,'bold'),textvariable =GARBRD,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtGARBRD.grid(row=6,column=1)



####################################################################################



lblCOST=Label(f1,font=('arial',16,'bold'),text='COST OF ITEMS(in Rs.)',bd=16,anchor='w')
lblCOST.grid(row=0,column=2)
txtCOST=Entry(f1,font=('arial',16,'bold'),textvariable =COST,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtCOST.grid(row=0,column=3)


lblDISCOUNT=Label(f1,font=('arial',16,'bold'),text='DISCOUNT(in Rs.)',bd=16,anchor='w')
lblDISCOUNT.grid(row=1,column=2)
txtDISCOUNT=Entry(f1,font=('arial',16,'bold'),textvariable =TOTALDISCOUNT,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtDISCOUNT.grid(row=1,column=3)


lblSUBTOTAL=Label(f1,font=('arial',16,'bold'),text='AMOUNT AFTER DISCOUNT(in Rs.)',bd=16,anchor='w')
lblSUBTOTAL.grid(row=2,column=2)
txtSUBTOTAL=Entry(f1,font=('arial',16,'bold'),textvariable =SUBTOTAL,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSUBTOTAL.grid(row=2,column=3)




lblService_Charge=Label(f1,font=('arial',16,'bold'),text='SERVICE CHARGE(in Rs.)',bd=16,anchor='w')
lblService_Charge.grid(row=3,column=2)
txtService_Charge=Entry(f1,font=('arial',16,'bold'),textvariable =Service_Charge,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtService_Charge.grid(row=3,column=3)



lblSTATETAX=Label(f1,font=('arial',16,'bold'),text='GST(in Rs.)',bd=16,anchor='w')
lblSTATETAX.grid(row=4,column=2)
txtSTATETAX=Entry(f1,font=('arial',16,'bold'),textvariable =STATETAX,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtSTATETAX.grid(row=4,column=3)






lblTOTALCOST=Label(f1,font=('arial',16,'bold'),text='NETT AMOUNT(in Rs.)',bd=16,anchor='w')
lblTOTALCOST.grid(row=5,column=2)
txtTOTALCOST=Entry(f1,font=('arial',16,'bold'),textvariable =TOTALCOST,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtTOTALCOST.grid(row=5,column=3)


lblNET=Label(f1,font=('arial',16,'bold'),text='NETT ROUNDED OFF AMOUNT(in Rs.)',bd=16,anchor='w')
lblNET.grid(row=6,column=2)
txtNET=Entry(f1,font=('arial',16,'bold'),textvariable =NET,bd=10,insertwidth=4,bg="powder blue",justify='right')
txtNET.grid(row=6,column=3)


#####

btnTotal=Button(f1,padx=10,pady=8,fg='black',font=('arial',16,'bold'),width=10,text='TOTAL',bd=5,bg="DARK GREY",command=Ref).grid(row=7,column=0)

btnReset=Button(f1,padx=10,pady=8,fg='black',font=('arial',16,'bold'),width=10,text='Reset',bd=5,bg="DARK GREY",command=Reset).grid(row=7,column=1)


btnExit=Button(f1,padx=10,pady=8,fg='black',font=('arial',16,'bold'),width=10,text='Exit',bd=5,bg="DARK GREY",command=qExit).grid(row=7,column=2)


btnMemo=Button(f1,padx=10,pady=8,fg='black',font=('arial',16,'bold'),width=10,text='BILL ENTRY',bd=5,bg="DARK GREY",command=Memo).grid(row=7,column=3)
















root.mainloop()
