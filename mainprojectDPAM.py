from tkinter import *

######################################################################################

######################################################################################

def g2():
    f2 = Tk()
    f2.title('WELCOME TO THE CGPA PREDICTION PART OF OUR APPLICATION')
    f2.geometry("550x260+950+100")


    def kuch2(event):
        MM1 = int(EE1.get())

        MM6 = float(EE6.get())

        MM2 = int(EE2.get())

        MM3 = int(EE3.get())

        MM4 = int(EE4.get())

        MM5 = int(EE5.get())

        S=MM1+MM2+MM3+MM4+MM5
        T1=float(MM6*5*9.5)
        T2=(T1-S)

        if(T2>250):
            print("BHAI NAHI HO PAYEGA BETTER LUCK NEXT TIME")
        elif(T2<=0):
            print("BINGO-> ALREADY ACHIEVED ")
        else:
            print("YOU HAVE TO SCORE A MINIMUM TOTAL OF ",T2,"MARKS OUT OF 250 MARKS(MAX MARKS AVAILABLE MARKS)")
            print("YOU HAVE TO SCORE AN AVERAGE OF ", T2/5, "MARKS IN EACH SUBJECT")

    LL7 = Label(f2, text=" ONLY INTEGERS SHOULD BE ENTERED BETWEEN(0-50)")
    LL1 = Label(f2, text="ENTER YOUR MARKS YOU GOT IN FIRST HALF OF ENG->")
    LL2 = Label(f2, text="ENTER YOUR MARKS YOU GOT IN FIRST HALF OF MTH->")
    LL3 = Label(f2, text="ENTER YOUR MARKS YOU GOT IN FIRST HALF OF PHY->")
    LL4 = Label(f2, text="ENTER YOUR MARKS YOU GOT IN FIRST HALF OF CHE->")
    LL5 = Label(f2, text="ENTER YOUR MARKS YOU GOT IN FIRST HALF OF CSE->")
    LL8 = Label(f2, text="SUBJECTS")
    LL9 = Label(f2, text="MARKS")
    LL10 = Label(f2, text="ENTER THE CGPA YOU WANT TO ACHIEVE->")

    EE1 = Entry(f2)
    EE2 = Entry(f2)
    EE3 = Entry(f2)
    EE4 = Entry(f2)
    EE5 = Entry(f2)
    EE6 = Entry(f2)

    LL7.grid(columnspan=30)
    LL1.grid(row=3, column=0)
    LL2.grid(row=4, column=0)
    LL3.grid(row=5, column=0)
    LL4.grid(row=6, column=0)
    LL5.grid(row=7, column=0)
    LL8.grid(row=2, column=0)
    LL9.grid(row=2, column=1)
    LL10.grid(row=1, column=0)

    EE1.grid(row=3, column=1)
    EE2.grid(row=4, column=1)
    EE3.grid(row=5, column=1)
    EE4.grid(row=6, column=1)
    EE5.grid(row=7, column=1)
    EE6.grid(row=1, column=1)

    BB1 = Button(f2, text="CLICK HERE TO SEE THE MAGIC")
    BB1.bind("<Button-1>", kuch2)
    BB1.grid(row=8, column=1)

    LL6 = Label(f2, text="THANKS FOR USING THIS APPLICATION")
    LL6.grid(row=9, column=0)

    f2.mainloop()
#########################################################################################

#########################################################################################

def g1():
    f = Tk()
    f.title('WELCOME TO THE CGPA CALCULATION PART OF OUR APPLICATION')
    f.geometry("550x260+65+100")


    def kuch(event):
        M1 = int(E1.get())
        M11=float(M1/9.5)

        M2 = int(E2.get())
        M12=float(M2 / 9.5)

        M3 = int(E3.get())
        M13=float (M3 / 9.5)

        M4 = int(E4.get())
        M14=float (M4 / 9.5)

        M5 = int(E5.get())
        M15=float(M5 / 9.5)

        d=M11 + M12 + M13 + M14 + M15
        d2=(d/5)

        if(d2>10):
            print(10)
        else:
            print('YOUR CGPA IS->' , '%.2f'%d2)



    L7 = Label(f, text=" ONLY INTEGERS SHOULD BE ENTERED BETWEEN(0-100)")
    L1 = Label(f, text="ENTER YOUR MARKS YOU GOT IN ENG->")
    L2 = Label(f, text="ENTER YOUR MARKS YOU GOT IN MTH->")
    L3 = Label(f, text="ENTER YOUR MARKS YOU GOT IN PHY->")
    L4 = Label(f, text="ENTER YOUR MARKS YOU GOT IN CHE->")
    L5 = Label(f, text="ENTER YOUR MARKS YOU GOT IN CSE->")
    L8 = Label(f, text="SUBJECTS")
    L9 = Label(f, text="MARKS")

    E1 = Entry(f)
    E2 = Entry(f)
    E3 = Entry(f)
    E4 = Entry(f)
    E5 = Entry(f)

    L7.grid(columnspan=30)
    L1.grid(row=2, column=0)
    L2.grid(row=3, column=0)
    L3.grid(row=4, column=0)
    L4.grid(row=5, column=0)
    L5.grid(row=6, column=0)
    L8.grid(row=1, column=0)
    L9.grid(row=1, column=1)


    E1.grid(row=2, column=1)
    E2.grid(row=3, column=1)
    E3.grid(row=4, column=1)
    E4.grid(row=5, column=1)
    E5.grid(row=6, column=1)

    B1 = Button(f, text="CLICK HERE TO SEE THE MAGIC")
    B1.bind("<Button-1>", kuch)
    B1.grid(row=7,column=1)

    L6 = Label(f, text="THANKS FOR USING THIS APPLICATION")
    L6.grid(row=8,column=0)


    f.mainloop()

#######################################################################################

#######################################################################################


p = Tk()
p.title('WELCOME TO THE MAIN WINDOW OF OUR APPLICATION')
p.geometry("550x260+950+510")
fram1 = Canvas(p, width=800, height=600,)
fram1.pack()
photo=PhotoImage(file='C:\\Users\\user\\Desktop\\ece\\PH.png')
fram1.create_image(0,0,image=photo,anchor=NW)

L1=Label(fram1,text="WELCOME TO OUR APPLICATION")
L1.place(relx = 0.49, rely = 0.2, anchor = N)

B1 = Button(p, text="CLICK HERE FOR CALCULATION",command=g1)
B1.place(relx = 0.3, rely = 0.5, anchor=CENTER)
B1.bind("<Button-1>")

B2 = Button(p, text="CLICK HERE FOR PREDICTION",command=g2)
B2.place(relx = 0.7, rely = 0.5, anchor = CENTER)
B2.bind("<Button-1>")
p.mainloop()