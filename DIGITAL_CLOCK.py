from tkinter import *
import datetime

# print(datetime.datetime.now())
def date_time():
    time=datetime.datetime.now()
    hr=time.strftime('%I')
    mi=time.strftime('%M')
    se=time.strftime('%S')
    am=time.strftime('%p')
    date=time.strftime('%d')
    month=time.strftime('%m')
    year=time.strftime('%y')
    day=time.strftime('%a')

    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=se)
    lab_am.config(text=am)
    lab_date.config(text=date)
    lab_mo.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)

    lab_hr.after(200,date_time)
    
clock=Tk()

clock.title("DIGITAL CLOCK")
clock.geometry('1000x500')
clock.config(bg='black')

lab_hr=Label(clock,text="00",font=('Time New Roman',40,"bold"),bg='black',fg='gray')
lab_hr.place(x=120,y=50,height=110,width=100)

lab_hr_txt=Label(clock,text="Hours",font=('Time New Roman',20,"bold"),bg='black',fg='gray')
lab_hr_txt.place(x=120,y=190,height=40,width=100)

lab_min=Label(clock,text="00",font=('Time New Roman',40,"bold"),bg='black',fg='gray')
lab_min.place(x=340,y=50,height=110,width=100)

lab_min_txt=Label(clock,text="Min.",font=('Time New Roman',20,"bold"),bg='black',fg='gray')
lab_min_txt.place(x=340,y=190,height=40,width=100)

lab_sec=Label(clock,text="00",font=('Time New Roman',40,"bold"),bg='black',fg='gray')
lab_sec.place(x=560,y=50,height=110,width=100)

lab_sec_txt=Label(clock,text="Sec.",font=('Time New Roman',20,"bold"),bg='black',fg='gray')
lab_sec_txt.place(x=560,y=190,height=40,width=100)

lab_am=Label(clock,text="00",font=('Time New Roman',40,"bold"),bg='black',fg='gray')
lab_am.place(x=780,y=50,height=110,width=100)

lab_am_txt=Label(clock,text="AM/PM",font=('Time New Roman',20,"bold"),bg='black',fg='gray')
lab_am_txt.place(x=780,y=190,height=40,width=100)

lab_date=Label(clock,text="00",font=('Time New Roman',40,"bold"),bg='black',fg='gray')
lab_date.place(x=120,y=270,height=110,width=100)

lab_date_txt=Label(clock,text="Hours",font=('Time New Roman',20,"bold"),bg='black',fg='gray')
lab_date_txt.place(x=120,y=410,height=40,width=100)

lab_mo=Label(clock,text="00",font=('Time New Roman',40,"bold"),bg='black',fg='gray')
lab_mo.place(x=340,y=270,height=110,width=100)

lab_mo_txt=Label(clock,text="Months",font=('Time New Roman',20,"bold"),bg='black',fg='gray')
lab_mo_txt.place(x=340,y=410,height=40,width=100)

lab_year=Label(clock,text="00",font=('Time New Roman',40,"bold"),bg='black',fg='gray')
lab_year.place(x=560,y=270,height=110,width=100)

lab_year_txt=Label(clock,text="Year",font=('Time New Roman',20,"bold"),bg='black',fg='gray')
lab_year_txt.place(x=560,y=410,height=40,width=100)

lab_day=Label(clock,text="00",font=('Time New Roman',40,"bold"),bg='black',fg='gray')
lab_day.place(x=780,y=270,height=110,width=100)

lab_day_txt=Label(clock,text="Day",font=('Time New Roman',20,"bold"),bg='black',fg='gray')
lab_day_txt.place(x=780,y=410,height=40,width=100)


date_time()

clock.mainloop()