from tkinter import *
from tkinter import ttk
import enum

class Grade(enum.Enum):
    S=10
    A=9
    B=8
    C=7
    D=6
    E=5
    U=0
    I=0
    W=0
    AB=0

    # List all keys of enum(grade)
    def list():
        l=[k for k,v in Grade.__members__.items()]
        return l

i=1
pos=0
def add():
    global i
    i+=1
    global pos
    global subjects
    pos+=100

    # subject name/title
    subjects["sub"+ str(i) +"lbl1"] = Label(window, text="Subject "+str(i) + ":", font=("Arial Bold", 10))
    subjects["sub"+ str(i) +"lbl1"].place(x=0, y=0+pos)

    # credit label
    subjects["sub"+ str(i) +"lbl2"] = Label(window, text="Enter Credit")
    subjects["sub"+ str(i) +"lbl2"].place(x=50, y=25+pos)

    # grade label
    subjects["sub"+ str(i) +"lbl3"] = Label(window, text="Choose Grade")
    subjects["sub"+ str(i) +"lbl3"].place(x=50, y=50+pos)

    # credit input
    subjects["sub" + str(i) + "txt"]=Entry(window,width=10)
    subjects["sub" + str(i) + "txt"].insert(0, 0)
    subjects["sub" + str(i) + "txt"].place(x=150,y=25+pos)

    # grade input
    subjects["sub" + str(i) + "combo"]=ttk.Combobox(window)
    subjects["sub" + str(i) + "combo"]["values"] = ("S", "A", "B", "C", "D", "E", "U", "I", "W", "AB")
    subjects["sub" + str(i) + "combo"].current(0)
    subjects["sub" + str(i) + "combo"].place(x=150, y=50+pos)

    btn1.place(x=100,y=100+pos)
    btn2.place(x=125, y=100 + pos)
    submit.place(x=100, y=150+pos)
    g.place(x=100, y=200 + pos)

def delete():
    global i
    global pos
    if i>1:
        subjects["sub"+ str(i) +"lbl1"].destroy()
        subjects["sub"+ str(i) +"lbl2"].destroy()
        subjects["sub"+ str(i) +"lbl3"].destroy()
        subjects["sub" + str(i) + "txt"].destroy()
        subjects["sub" + str(i) + "combo"].destroy()
        i-=1
        btn1.place(x=100, y=pos)
        btn2.place(x=125, y=pos)
        submit.place(x=100,y=pos+50)
        g.place(x=100, y=100 + pos)
        pos-=100

def gpa():
    total_credit=0
    total = 0
    try:
        for j in range(1,i+1):
            try:
                credit = float(subjects["sub" + str(j) + "txt"].get())
            except ValueError:
                print("Input validation error")
                g.configure(text="Invalid Input for subject " + str(j), fg="red")
                return
            grade_val = Grade[subjects["sub" + str(j) + "combo"].get()].value
            total_credit+=credit
            total+=(credit*grade_val)
        # sum of product credit and grade point divided by total credits
        gpa=total/total_credit
        g.configure(text = "YOUR GPA: {:.3f}".format(gpa), fg="green")
    except:
        print("error,please try again")
        g.configure(text = "Invalid Input", fg="red")

window=Tk()
window.title("GPA Calculator")
window.geometry('4000x3000')

subjects = {}

# Subject Name / title
subjects["sub1lbl1"]=Label(window,text="Subject 1:", font=("Arial Bold", 10))
subjects["sub1lbl1"].place(x=0,y=0)

# Credit label
subjects["sub1lbl2"]=Label(window,text="Enter Credit")
subjects["sub1lbl2"].place(x=50,y=25)

# Grade label
subjects["sub1lbl3"]=Label(window,text="Choose Grade")
subjects["sub1lbl3"].place(x=50,y=50)

# Credit input
subjects["sub1txt"]=Entry(window,width=5)
subjects["sub1txt"].place(x=150,y=25)
subjects["sub1txt"].insert(0, 0)

# Grade input
subjects["sub1combo"]=ttk.Combobox(window, width=2)
subjects["sub1combo"]["values"]=Grade.list()
subjects["sub1combo"].current(0)
subjects["sub1combo"].place(x=150,y=50)

# Add Subject Button
btn1=Button(window,text="+",command=add,bg="green",fg="white")
btn1.place(x=100,y=100)
#Delete Subject Button
btn2=Button(window,text="-",command=delete,bg="orange",fg="white")
btn2.place(x=125,y=100)

#Calculate Button
submit=Button(window,text="CALCULATE",command=gpa,bg="blue",fg="white")
submit.place(x=100,y=150)

#GPA Ouput / Error Label
g = Label(window, text="")
g.place(x=100, y=200)

window.mainloop()
