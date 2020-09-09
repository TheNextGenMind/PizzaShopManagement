from Tkinter import *
import subprocess
root=Tk()

root.title('welcome')
root.geometry("1800x1800")
root.configure(background='light grey')
b=PhotoImage(file="s.gif")
c=PhotoImage(file="T.gif")
d=PhotoImage(file="TT.gif")
n=PhotoImage(file="ff.gif")
def images():
   i=Toplevel()
   i.title('imagehub')
   i.configure(background='grey')
   Label(i,image=b).grid(row=0,column=0)
   Label(i,image=c).grid(row=0,column=1)
   Label(i,image=d).grid(row=1,column=0)
   Label(i,image=n).grid(row=1,column=1)
   i.mainloop()

   
   


      

#for new Window      
def welcome():
   
   
   subprocess.call("python men.py")  
   
  
   
   
def fun():
   owner=Toplevel()
   owner.geometry('1350x1350')
   owner.title('About us')
   owner.configure(background='black')
   c = PhotoImage(file = "a.gif")
   Label(owner , image = c).place(x=700,y=5)

   b = PhotoImage(file = "e.gif")
   Label(owner , image = b).place(x=0,y=5)
   k = PhotoImage(file = "dj.gif")
   Label(owner , image = k).place(x=0,y=250)
   f= PhotoImage(file = "jk.gif")
   Label(owner , image = f).place(x=280,y=85)
   Label(owner,text='FSSAI certified veg restaurant',relief='raised',font='times 30 bold italic ',bd=0,fg='white',bg='black').place(x=125,y=300)
   Label(owner,text='OWNER:-SANIDHYA TRIVEDI',relief='raised',font='times 20 bold italic ').place(x=700,y=520)
   Label(owner,text='* CONTACT NO:7376054990,8896767754',relief='raised',font='times 25 bold italic underline').place(x=10,y=470)
   Label(owner,text='CONTACT NO:7354195331',relief='raised',font='times 15 bold italic ').place(x=700,y=560)
   Label(owner,text='* hotpizza.ace@gmail.com',relief='raised',font='times 25 bold italic underline').place(x=10,y=520)
   Label(owner,text='sanidhya.8.tigerworld@gmail.com',relief='raised',font='times 15 bold italic ').place(x=700,y=590)
   
   owner.mainloop()    
def log():
   root.destroy()
   subprocess.call("python begin.py")
   
a=PhotoImage(file="hot pizza.gif")
Label(root,image=a).pack()
Label(root,text='Welcome to HOT PIZZA ACE',relief='raised',font='times 40 bold italic underline',bd=6,bg='white',fg='red').pack()

Label(root,text='ME1,Subji Mandi Road,near Barra World Bank,Barra 2,Kanpur',relief='raised',font='times 32 bold italic ',bd=0,bg='light grey',fg='black').pack()

Button(root,text='MANAGE SHOP',font='times 30 bold',bd=7,bg='dark grey',command=welcome).pack()


Button(root,text="ABOUT  US ",font='times 30 bold',bd=7,bg='dark grey',command=fun).pack(side='left')
Label(root,text='                              ',relief='raised',font='times 32 bold italic ',bd=0,bg='light grey',fg='black').pack(side='left')
Button(root,text="LOGOUT",font='times 20 bold',bd=7,bg='dark grey',fg='red',command=log).pack(side='left')
Button(root,text='SHOP IMAGES',font='times 30 bold',bd=7,bg='dark grey',command=images).pack(side='right')





root.mainloop()
