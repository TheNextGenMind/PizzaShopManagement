from tkMessageBox import *
from Tkinter import *
root=Tk()

root.title('HOT PIZZA ACE Login')
root.configure(background='light grey')
a=PhotoImage(file="e.gif")
Label(root,image=a).grid(row=0,column=0,columnspan=8)


def check():   
    ''' Check Button for Login Window '''
    global un, pwd, root
    
    
    u=un.get()
    p=pwd.get()
    if 'sanidhya'==u and 'san123'==p:
        
        root.destroy()
        import pro
        
       
       
    else:
        showerror('ERROR','Wrong ID or Password :Please try again')
        root.mainloop()



        # login.close()







    
Label(root,text='HOT PIZZA ACE',font=('arial',20,'bold'),bd=7,fg='red',bg='light grey').grid(row=1,column=0,columnspan=8)
Label(root,text="ME1,Subji Mandi Road,near Barra World Bank,Barra 2,Kanpur",font=('arial',20,'bold'),bg='light grey').grid(row=2,column=0,columnspan=5)
Label(root,text='---------------------------------------------------------------------',bg='light grey').grid(row=3,column=0,columnspan=5)
Label(root, text='Username',font=('arial',10,'bold'),bg='light grey').grid(row=4, column=1)
un=Entry(root,bd=2,width=10)
un.grid(row=4, column=2)
Label(root, text='Password',font=('arial',10,'bold'),bg='light grey').grid(row=5, column=1)
pwd=Entry(root,width=10,bd=2, show="*")
pwd.grid(row=5, column=2)
Label(root,text='').grid(row=6,column=0,columnspan=5)
Button(root,width=6,text='Login',font=('arial',10,'bold'),bd=4,bg='dark grey',command=check).grid(row=7, column=1)
Button(root,width=6,text='Close',font=('arial',10,'bold'),bd=4,bg='dark grey',command=root.destroy).grid(row=7, column=2)


root.title("HOT PIZZA ACE")



root.mainloop()
