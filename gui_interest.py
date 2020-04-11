from tkinter import *
from tkinter import messagebox

x = Tk()
x.title("interest calculator")
li=Label(x,text="WHAT WOULD YOU LIKE TO CALCULATE??",padx=102,pady=30,fg="maroon",bg="yellow",font="Times")
li.grid(row=0,column=0,columnspan=2)

def present_value_to_future_value(present_value,duration,interest):
    interest=interest/100.0
    temp=1.0000000+interest
    temp=round(temp,6)
    temp=pow(temp,duration)
    return (present_value*temp)

def future_value_to_present_value(future_value,duration,interest):
    interest=interest/100
    temp=1.0000000+interest
    temp=1.0000000+interest
    temp=round(temp,6)
    temp=pow(temp,duration)
    return(future_value/temp)

def present_value_to_annual_value(present_value,duration,interest):
    interest=interest/100
    temp=1.0000000+interest
    temp=1.0000000+interest
    temp=round(temp,6)
    temp=pow(temp,duration)
    return(present_value*((interest*temp)/(temp-1)))

def annual_value_to_present_value(annual_value,duration,interest):
    interest=interest/100
    temp=1.0000000+interest
    temp=1.0000000+interest
    temp=round(temp,6)
    temp=pow(temp,duration)
    temp=1.0/temp
    temp=1-temp
    temp=temp/interest
    return(temp*annual_value)

def future_value_to_annual_value(future_value,duration,interest):
    interest=interest/100
    temp=1.0000000+interest
    temp=1.0000000+interest
    temp=round(temp,6)
    temp=pow(temp,duration)
    temp=temp-1
    temp=interest/temp
    return future_value*temp
def annual_value_to_future_value(annual_value,duration,interest):
    interest=interest/100
    temp=1.0000000+interest
    temp=1.0000000+interest
    temp=round(temp,6)
    temp=pow(temp,duration)
    temp=temp-1
    temp=temp/interest
    return annual_value*temp

def duration_interest():
    global duration,duration_entry,interest,interest_entry
    duration=Label(x,text="enter duration:-")
    duration.grid(row=5,column=0)
    duration_entry = Entry(x,width="49",bg="yellow",fg="blue",borderwidth="3")
    duration_entry.grid(row=5,column=1)
    interest=Label(x,text="enter interest in %:-")
    interest.grid(row=6,column=0)
    interest_entry = Entry(x,width="49",bg="yellow",fg="blue",borderwidth="3")
    interest_entry.grid(row=6,column=1)
def pvtfv():
    global work,e1,l1
    work=1
    l1=Label(x,text="enter present value:-")
    l1.grid(row=4,column=0)
    e1 = Entry(x,width="49",bg="yellow",fg="blue",borderwidth="3")
    e1.grid(row=4,column=1)
    duration_interest()
    cb = Button(x,text="CALCULATE",padx=50,pady=15,command=calculate,fg="maroon",bg="yellow")
    cb.grid(row=7,column=0,columnspan=2)
    #b1.grid_forget() or pack_forget() removes the label.

def fvtpv():
    global work,e1,l1
    work=2
    l1=Label(x,text="enter future value:-")
    l1.grid(row=4,column=0)
    e1 = Entry(x,width="49",bg="yellow",fg="blue",borderwidth="3")
    e1.grid(row=4,column=1)
    duration_interest()
    cb = Button(x,text="CALCULATE",padx=50,pady=15,command=calculate,fg="maroon",bg="yellow")
    cb.grid(row=7,column=0,columnspan=2)

def pvtav():
    global work,e1,l1
    work=3
    l1=Label(x,text="enter present value:-")
    l1.grid(row=4,column=0)
    e1 = Entry(x,width="49",bg="yellow",fg="blue",borderwidth="3")
    e1.grid(row=4,column=1)
    duration_interest()
    cb = Button(x,text="CALCULATE",padx=50,pady=15,command=calculate,fg="maroon",bg="yellow")
    cb.grid(row=7,column=0,columnspan=2)

def avtpv():
    global work,e1,l1
    work=4
    l1=Label(x,text="enter annual value:-")
    l1.grid(row=4,column=0)
    e1 = Entry(x,width="49",bg="yellow",fg="blue",borderwidth="3")
    e1.grid(row=4,column=1)
    duration_interest()
    cb = Button(x,text="CALCULATE",padx=50,pady=15,command=calculate,fg="maroon",bg="yellow")
    cb.grid(row=7,column=0,columnspan=2)

def fvtav():
    global work,e1,l1
    work=5
    l1=Label(x,text="enter future value:-")
    l1.grid(row=4,column=0)
    e1 = Entry(x,width="49",bg="yellow",fg="blue",borderwidth="3")
    e1.grid(row=4,column=1)
    duration_interest()
    cb = Button(x,text="CALCULATE",padx=50,pady=15,command=calculate,fg="maroon",bg="yellow")
    cb.grid(row=7,column=0,columnspan=2)

def avtfv():
    global work,e1,l1
    work=6
    l1=Label(x,text="enter annual value:-")
    l1.grid(row=4,column=0)
    e1 = Entry(x,width="49",bg="yellow",fg="blue",borderwidth="3")
    e1.grid(row=4,column=1)
    duration_interest()
    cb = Button(x,text="CALCULATE",padx=50,pady=15,command=calculate,fg="maroon",bg="yellow")
    cb.grid(row=7,column=0,columnspan=2)
    
def calculate():
    global res
    if interest_entry.get()=="" or duration_entry.get()=="":
       messagebox.showinfo("missing value","kindly check")
       return
    i=float(interest_entry.get())
    n=int(duration_entry.get())
    if work==1:
        if e1.get()=="":
            messagebox.showinfo("missing present value","kindly check")
            return
        result=present_value_to_future_value(float(e1.get()),n,i)
        res=Label(x,text="Future value is :-"+str(result))
    if work==2:
        if e1.get()=="":
            messagebox.showinfo("missing future value","kindly check")
            return
        result=future_value_to_present_value(float(e1.get()),n,i)
        res=Label(x,text="present value is :-"+str(result))
    if work==3:
        if e1.get()=="":
            messagebox.showinfo("missing present value","kindly check")
            return
        result=present_value_to_annual_value(float(e1.get()),n,i)
        res=Label(x,text="annual value is :-"+str(result))
    if work==4:
        if e1.get()=="":
            messagebox.showinfo("missing annual value","kindly check")
            return
        result=annual_value_to_present_value(float(e1.get()),n,i)
        res=Label(x,text="present value is :-"+str(result))
    if work==5:
        if e1.get()=="":
            messagebox.showinfo("missing future value","kindly check")
            return
        result=future_value_to_annual_value(float(e1.get()),n,i)
        res=Label(x,text="annual value is :-"+str(result))
    if work==6:
        if e1.get()=="":
            messagebox.showinfo("missing annual value","kindly check")
            return
        result=annual_value_to_future_value(float(e1.get()),n,i)
        res=Label(x,text="future value is :-"+str(result))
    res.grid(row=8,column=0,columnspan=2)
    
    

b1 = Button(x,text="PRESENT VALUE TO FUTURE VALUE",padx=53,pady=35,command=pvtfv,fg="green",bg="pink")
b1.grid(row=1,column=0)
b2 = Button(x,text="FUTURE VALUE TO PRESENT VALUE",padx=53,pady=35,command=fvtpv,fg="green",bg="pink")
b2.grid(row=1,column=1)
b3 = Button(x,text="PRESENT VALUE TO ANNUAL VALUE",padx=50,pady=35,command=pvtav,fg="green",bg="pink")
b3.grid(row=2,column=0)
b4 = Button(x,text="ANNUAL VALUE TO PRESENT VALUE",padx=50,pady=35,command=avtpv,fg="green",bg="pink")
b4.grid(row=2,column=1)
b5 = Button(x,text="FUTURE VALUE TO ANNUAL VALUE",padx=53,pady=35,command=fvtav,fg="green",bg="pink")
b5.grid(row=3,column=0)
b6 = Button(x,text="ANNUAL VALUE TO FUTURE VALUE",padx=53,pady=35,command=avtfv,fg="green",bg="pink")
b6.grid(row=3,column=1)


x.mainloop()
