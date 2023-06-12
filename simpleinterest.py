from tkinter import *

window=Tk()

window.title("Simple Interest App")
window.geometry("400x400")
window.configure(bg="#FFAEBC")

def calculate_interest():
    p = float(principal.get())
    r = float(rate.get())
    t = float(time.get())
    i = (p*r*t)/100
    interest = round(i,2)
    showlabel.destroy()
    message = Label(output,text="Interest on is."+str(p)+" at rate of interest "+str(r)+" for "+str(t)+" years it is."+str(interest),bg="grey",font=("Comic Sans MS",12),width=55)
    message.place(x=20,y=40)
    message.pack()

headingLabel = Label(window,text="Simple Interest App",fg="white",bg="#FFAEBC",font=("Comic Sans MS",18),bd=1)
headingLabel.place(x=50,y=10)

principalLabel = Label(window,text="Enter Your Principal:",fg="white",bg="#FFAEBC",font=("Comic Sans MS",12),bd=1)
principalLabel.place(x=0,y=60)
principal = Entry(window,text="",bd=1,width=30)
principal.place(x=170,y=60)

rateLabel = Label(window,text="Enter Your Rate:",fg="white",bg="#FFAEBC",font=("Comic Sans MS",12),bd=1)
rateLabel.place(x=0,y=90)
rate = Entry(window,text="",bd=1,width=30)
rate.place(x=140,y=90)

timeLabel = Label(window,text="Enter Your Time:",fg="white",bg="#FFAEBC",font=("Comic Sans MS",12),bd=1)
timeLabel.place(x=0,y=120)
time = Entry(window,text="",bd=1,width=30)
time.place(x=140,y=120)

cal = Button(window,text="Calculate",fg="black",bg="white",bd=4,command=calculate_interest)
cal.place(x=20,y=270)

output = LabelFrame(window,text="Result",bg="#FBE7C6",font=("Comic Sans MS",12))
output.pack(padx=20,pady=20)
output.place(x=20,y=300)

showlabel=Label(output,text="Your result will be displayed here",bg="#FBE7C6",font=("Comic Sans MS",12),width=55)
showlabel.place(x=20,y=20)
showlabel.pack()

window.mainloop()