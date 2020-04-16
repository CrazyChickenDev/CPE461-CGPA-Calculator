from tkinter import*
from tkinter import messagebox
from math import *
#create root window
root=Tk()
#set window title
root.title('CGPA CALCULATER')
#create canvas as a child to root window

f=Frame(root,height=400,width=600,bg='darkgray')


h=Label(bg='black',fg='white',text='CGPA CALCULATER')
h.place(x=1,y=1)
c = Canvas(f, bg='darkgray',height=450, width=600)
#create a line in the canvas
id=c.create_line(0,30,600,30,width=1, fill='black')
c.pack()
 
etgpa=IntVar()
etgpa1=IntVar()


l=Label(f,text='Sem 1',fg='black',bg='darkgray')
l.place(x=20,y=35)
l1=Label(f,text='Subject 1',fg='black',bg='darkgray')
l1.place(x=20,y=70)
l2=Label(f,text='Subject 2',fg='black',bg='darkgray')
l2.place(x=20,y=90)
l3=Label(f,text='Subject 3',fg='black',bg='darkgray')
l3.place(x=20,y=110)
l4=Label(f,text='Subject 4',fg='black',bg='darkgray')
l4.place(x=20,y=130)
l5=Label(f,text='Subject 5',fg='black',bg='darkgray')
l5.place(x=20,y=150)
l6=Label(f,text='Subject 6',fg='black',bg='darkgray')
l6.place(x=20,y=170)
l7=Label(f,text='Grade',fg='black',bg='white',borderwidth=1,relief='solid')
l7.place(x=150,y=50,width=35)
l7=Label(f,text='Credit',fg='black',bg='white',borderwidth=1,relief='solid')
l7.place(x=185,y=50,width=35)
#entry of grades and credits
g2=IntVar()
g1 = Entry(f,bg='white',fg='black',borderwidth=1,relief='solid')
g1.place(x=150,y=70,width=35)
g2 = Entry(f,bg='white',fg='black',borderwidth=1,relief='solid')
g2.place(x=185,y=70,width=35)
g3 = Entry(f,bg='white',fg='black',borderwidth=1,relief='solid')
g3.place(x=150,y=90,width=35)
g4 = Entry(f,bg='white',fg='black',borderwidth=1,relief='solid')
g4.place(x=185,y=90,width=35)
g5 = Entry(f,bg='white',fg='black',borderwidth=1,relief='solid')
g5.place(x=150,y=110,width=35)
g6 = Entry(f,bg='white',fg='black',borderwidth=1,relief='solid')
g6.place(x=185,y=110,width=35)
g7 = Entry(f,bg='white',fg='black',borderwidth=1,relief='solid')
g7.place(x=150,y=130,width=35)
g8 = Entry(f,bg='white',fg='black',borderwidth=1,relief='solid')
g8.place(x=185,y=130,width=35)
g9 = Entry(f,bg='white',fg='black',borderwidth=1,relief='solid')
g9.place(x=150,y=150,width=35)
g10 = Entry(f,bg='white',fg='black',borderwidth=1,relief='solid')
g10.place(x=185,y=150,width=35)
g11 = Entry(f,bg='white',fg='black',borderwidth=1,relief='solid')
g11.place(x=150,y=170,width=35)
g12 = Entry(f,bg='white',fg='black',borderwidth=1,relief='solid')
g12.place(x=185,y=170,width=35)




# sem2
id = c.create_line(0, 210, 600, 210, width=1, fill='black')
c.pack()



lsem2=Label(f,text='Sem 2',fg='black',bg='darkgray')
lsem2.place(x=20,y=215)
l8=Label(f,text='Subject 1',fg='black',bg='darkgray')
l8.place(x=20,y=240)
l9=Label(f,text='Subject 2',fg='black',bg='darkgray')
l9.place(x=20,y=260)
l10=Label(f,text='Subject 3',fg='black',bg='darkgray')
l10.place(x=20,y=280)
l11=Label(f,text='Subject 4',fg='black',bg='darkgray')
l11.place(x=20,y=300)
l12=Label(f,text='Subject 5',fg='black',bg='darkgray')
l12.place(x=20,y=320)
l13=Label(f,text='Subject 6',fg='black',bg='darkgray')
l13.place(x=20,y=340)
l14=Label(f,text='Grade',fg='black',bg='white',borderwidth=1,relief='solid')
l14.place(x=150,y=220,width=35)
l15=Label(f,text='Credit',fg='black',bg='white',borderwidth=1,relief='solid')
l15.place(x=185,y=220,width=35)
g13 = Entry(f,bg='white',fg='black',borderwidth=1,relief='solid')
g13.place(x=150,y=240,width=35)
g14 = Entry(f,bg='white',fg='black',borderwidth=1,relief='solid')
g14.place(x=185,y=240,width=35)
g15 = Entry(f,bg='white',fg='black',borderwidth=1,relief='solid')
g15.place(x=150,y=260,width=35)
g16 = Entry(f,bg='white',fg='black',borderwidth=1,relief='solid')
g16.place(x=185,y=260,width=35)
g17= Entry(f,bg='white',fg='black',borderwidth=1,relief='solid')
g17.place(x=150,y=280,width=35)
g18 = Entry(f,bg='white',fg='black',borderwidth=1,relief='solid')
g18.place(x=185,y=280,width=35)
g19 = Entry(f,bg='white',fg='black',borderwidth=1,relief='solid')
g19.place(x=150,y=300,width=35)
g20 = Entry(f,bg='white',fg='black',borderwidth=1,relief='solid')
g20.place(x=185,y=300,width=35)
g21 = Entry(f,bg='white',fg='black',borderwidth=1,relief='solid')
g21.place(x=150,y=320,width=35)
g22 = Entry(f,bg='white',fg='black',borderwidth=1,relief='solid')
g22.place(x=185,y=320,width=35)
g23 = Entry(f,bg='white',fg='black',borderwidth=1,relief='solid')
g23.place(x=150,y=340,width=35)
g24 = Entry(f,bg='white',fg='black',borderwidth=1,relief='solid')
g24.place(x=185,y=340,width=35)





#final cgpa




#backend

# storing all the grades of sem1 in array




tgpa1 = 0.00

def calculatetgpa1():
    global tgpa1
    # storing all the grades of sem1 in array
    global grades,credits
    grades = []
    grades.append(g1.get())
    grades.append(g3.get())
    grades.append(g5.get())
    grades.append(g7.get())
    grades.append(g9.get())
    grades.append(g11.get())

    # storing all the credits of sem1 in array
    credits = []

    credits.append(int(eval(g2.get())))
    credits.append(int(eval(g4.get())))
    credits.append(int(eval(g6.get())))
    credits.append(int(eval(g8.get())))
    credits.append(int(eval(g10.get())))
    credits.append(int(eval(g12.get())))


    tsum = 0
    sum_credits = 0
    for i in range(0,6):
        if(grades[i]=='O'):
            tsum=tsum+10*credits[i]
        elif(grades[i]=='A+'):
            tsum=tsum+9*credits[i]
        elif(grades[i]=='A'):
            tsum=tsum+8*credits[i]
        elif(grades[i]=='B+'):
            tsum=tsum+7*credits[i]
        elif(grades[i]=='B'):
            tsum=tsum+6*credits[i]
        elif(grades[i]=='C'):
            tsum=tsum+5*credits[i]
        elif(grades[i]=='E'):
            tsum = tsum + 0*credits[i]
        elif (grades[i] == ''):
            messagebox.showinfo('Empty grade',"please enter grade")
            goto(41)
        else:
            messagebox.showinfo('Invalid grade', "please enter a valid grade")
            goto(41)
    for j in range(0,6):
        sum_credits = sum_credits + credits[j]


    tgpa1=float(tsum/sum_credits)
    etgpa=Label(bg='white', fg='black', borderwidth=1,width=20, relief='solid',text=tgpa1)
    etgpa.place(x=335, y=120)


tgpa2=0.00
def calculatetgpa2():
    global grades1,credits1
    global tgpa2
    grades1 = []
    grades1.append(g13.get())
    grades1.append(g15.get())
    grades1.append(g17.get())
    grades1.append(g19.get())
    grades1.append(g21.get())
    grades1.append(g23.get())

    # storing all the credits of sem1 in array
    credits1 = []
    credits1.append(int(eval(g14.get())))
    credits1.append(int(eval(g16.get())))
    credits1.append(int(eval(g18.get())))
    credits1.append(int(eval(g20.get())))
    credits1.append(int(eval(g22.get())))
    credits1.append(int(eval(g24.get())))
    tsum1 = 0
    sum_credits1 = 0
    for i in range(0,6):
        if(grades1[i]=='O'):
            tsum1=tsum1+10*credits1[i]
        elif(grades1[i]=='A+'):
            tsum1=tsum1+9*credits1[i]
        elif(grades1[i]=='A'):
            tsum1=tsum1+8*credits1[i]
        elif(grades1[i]=='B+'):
            tsum1=tsum1+7*credits1[i]
        elif(grades1[i]=='B'):
            tsum1=tsum1+6*credits1[i]
        elif(grades1[i]=='C'):
            tsum1=tsum1+5*credits1[i]
        elif(grades1[i]=='E'):
            tsum1 = tsum1 + 0*credits1[i]
        elif (grades1[i] == ''):
            messagebox.showinfo('Empty grade', "please enter grade")
            goto(41)
        else:
            messagebox.showinfo('Invalid grade', "please enter a valid grade")
            goto(41)

    for j in range(0,6):
        sum_credits1 = sum_credits1 + credits1[j]

    tgpa2=tsum1/sum_credits1
    etgpa1=Label(bg='white', fg='black', borderwidth=1, relief='solid',width=20,text=tgpa2)
    etgpa1.place(x=335, y=300)




cgpa=0.00
id = c.create_line(0, 390, 600,390, width=1, fill='black')
lcgpa=LabelFrame(bg='white',height=30,width=30)
lcgpa.place(x=150,y=391)
def calculatecgpa():
    global cgpa
    cgpa=(tgpa1+tgpa2)/2
    m1=Label(lcgpa,bg='white',text=cgpa)
    m1.grid(row=1,column=2)

def remarks():
    count=0
    count1=0
    global subno,subno1

    #checking reappear in 1st sem
    for i in range(0,6):
        if grades[i]=='E':
            subno=i
            count=count+1
    # checking reappear in 2nd sem
    for i in range(0,6):
        if grades1[i]=='E':
            subno1=i
            count1=count1+1
    if(count>0 and count1==0):
        m2 = Label(lcgpa, bg='white',text=('Reappear in subject',subno+1,'in semester 1'),borderwidth=1,relief='solid')
        m2.grid(row=2,column=2)
    elif(count==0 and count1>0):
        m2 = Label(lcgpa, bg='white',text=('Reappear in subject',subno1+1,'in semester 2'),borderwidth=1,relief='solid')
        m2.grid(row=2, column=2)
    elif(count>0 and count1>0):
        m2 = Label(lcgpa, bg='white',text='Reappear in both semesters',borderwidth=1,relief='solid')
        m2.grid(row=2, column=2)
    else:
        m2 = Label(lcgpa, bg='white',text=('pass'),borderwidth=1,relief='solid')
        m2.grid(row=2, column=2)




#cgpacalulate
l1cgpa=Button(lcgpa,text='CGPA',borderwidth=1,relief='solid',bg='darkgray',width=7,height=1,command=calculatecgpa)
l1cgpa.grid(row=1,column=1)

#remarks
l2cgpa=Button(lcgpa,text='remarks',borderwidth=1,relief='solid',bg='darkgray',width=7,height=1,command=remarks)
l2cgpa.grid(row=2,column=1)



#calculatetgpa1
ltgpa=Button(text='TGPA',bg='darkgray',fg='black', borderwidth=1,relief='solid',width=20,command=calculatetgpa1)
ltgpa.place(x=300,y=120,width=35)

#calculatetgpa2
ltgpa=Button(text='TGPA',bg='darkgray',fg='black', borderwidth=1,relief='solid',width=20,command=calculatetgpa2)
ltgpa.place(x=300,y=300,width=35)




c.pack()
f.pack()
root.mainloop()
