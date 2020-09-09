from Tkinter import *
import subprocess
def splash():
    root.destroy()
    fun()
def fun():
    subprocess.call('python begin.py')




    
root=Tk()
root.geometry('1300x900')
root.title('welcome')
a=PhotoImage(file='splashh.gif')
Label(root,image=a).pack()

root.after(4000,splash)
root.mainloop()

