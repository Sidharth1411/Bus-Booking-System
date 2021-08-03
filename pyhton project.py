from tkinter import *
import sqlite3
#import title_project

con=sqlite3.Connection('busbookingsystemdb')
cur=con.cursor()

root=Tk()
root.geometry('800x600')
Label(root,text="Bus Booking System",font="Bold 25",fg="black",bg="red" ).grid(row=0,column=5)

#a=PhotoImage(file='download(1).gif')
#Label(root,image=a).grid(row=8,column=5)

def add():
    root=Tk()
    root.geometry('800x600')
    Label(root,text="Bus Booking System",font="Bold 15",fg="red",bg="yellow" ).grid(row=0,column=3)
    Label(root,text="Bus Operator Details Filling ",font="Bold 15",fg="white",bg="black" ).grid(row=1,column=3)
    Label(root,text='Full Name:',font='bold 10').grid(row=40,column=2)
    e1=Entry(root)
    e1.grid(row=40,column=2)
    Label(root,text='Contact Number:',font="bold 10").grid(row=41,column=1)
    e2=Entry(root)
    e2.grid(row=41,column=2)
    Label(root,text='Address:',font="bold 10").grid(row=42,column=1)
    e3=Entry(root)
    e3.grid(row=42,column=2)
    def detail():
        Label(root,text='Opeator:',font="bold 10").grid(row=44,column=1)
        e3=Entry(root)
        e3.grid(row=44,column=2)
        Label(root,text='Bus Type:',font="bold 10").grid(row=45,column=1)
        e3=Entry(root)
        e3.grid(row=45,column=2)
        Label(root,text='From:',font="bold 10").grid(row=46,column=1)
        e3=Entry(root)
        e3.grid(row=46,column=2)
        Label(root,text='To:',font="bold 10").grid(row=47,column=1)
        e3=Entry(root)
        e3.grid(row=47,column=2)
        Label(root,text='Date:',font="bold 10").grid(row=48,column=1)
        e3=Entry(root)
        e3.grid(row=48,column=2)
        Label(root,text='Dep Time:',font="bold 10").grid(row=49,column=1)
        e3=Entry(root)
        e3.grid(row=49,column=2)
        Label(root,text='Arr Time:',font="bold 10").grid(row=50,column=1)
        e3=Entry(root)
        e3.grid(row=50,column=2)
        Label(root,text='Fare:',font="bold 10").grid(row=51,column=1)
        e3=Entry(root)
        e3.grid(row=51,column=2)
        Label(root,text='seats:',font="bold 10").grid(row=52,column=1)
        e3=Entry(root)
        e3.grid(row=52,column=2)
        Button(root,text='Save',command=root ,font="bold 13 " ).grid(row=53,column=3)
        
    Button(root,text='Add Details',command=detail,font="bold 13").grid(row=43,column=4)
         
def search():
    root=Tk()
    root.geometry('350x350')
    Label(root,text="Bus Booking System",font="Bold 15",fg="blue",bg="grey" ).grid(row=0,column=2)
    Label(root,text="Listing Buses ",font="Bold 15",fg="blue",bg="grey" ).grid(row=1,column=2)
    Label(root,text='Bus Type:',font="bold 10").grid(row=49,column=1)
    v=StringVar(root)
    choice=['bus type','AC','NON-AC','AC-SLEEPER','NON-AC-SLEEPER','ALL TYPE']
    v.set(choice[0])
    OptionMenu(root,v,*choice).grid(row=49,column=2)
    
    Label(root,text='From:',font="bold 10").grid(row=50,column=1)
    e3=Entry(root)
    e3.grid(row=50,column=2)
    Label(root,text='To:',font="bold 10").grid(row=51,column=1)
    e3=Entry(root)
    e3.grid(row=51,column=2)
    Label(root,text='Date:',font="bold 10").grid(row=52,column=1)
    e3=Entry(root)
    e3.grid(row=52,column=2)
    Button(root,text='Search',command=root ,font="bold 13 " ).grid(row=55,column=2)
    Button(root,text='Home',command=root ,font="bold 13 " ).grid(row=55,column=3)





Button(root,text='Add Bus',command=add ,font="bold 10").grid(row=10,column=2)
Button(root,text='Search Bus',command=search , font="bold 10").grid(row=10,column=6)



root.mainloop()
