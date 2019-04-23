from tkinter import*
cal = Tk()
cal.title("Calculator")
operator = ""
text_Input = StringVar()
textDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                    bg="powder blue", justify="right").grid(columnspan=4)

btn7 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="7", bg="powder blue").grid(row=1,
                                                                                                           column=0)
btn8 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="8", bg="powder blue").grid(row=1,
                                                                                                           column=1)
btn9 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="9", bg="powder blue").grid(row=1,
                                                                                                           column=2)
btnAdd = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="+", bg="powder blue").grid(row=1,
                                                                                                             column=3)

btn4 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="4", bg="powder blue").grid(row=2,
                                                                                                           column=0)
btn5 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="5", bg="powder blue").grid(row=2,
                                                                                                           column=1)
btn6 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="6", bg="powder blue").grid(row=2,
                                                                                                           column=2)
btnSub = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="-", bg="powder blue").grid(row=2,
                                                                                                             column=3)

btn1 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="1", bg="powder blue").grid(row=3,
                                                                                                           column=0)
btn2 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="2", bg="powder blue").grid(row=3,
                                                                                                           column=1)
btn3 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="3", bg="powder blue").grid(row=3,
                                                                                                           column=2)
btnAdd = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="*", bg="powder blue").grid(row=3,
                                                                                                             column=3)

btnC = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="C", bg="powder blue").grid(row=4,
                                                                                                           column=0)
btn0 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="0", bg="powder blue").grid(row=4,
                                                                                                           column=1)
btnDiv = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="/", bg="powder blue").grid(row=4,
                                                                                                           column=2)
btnEquals = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="=", bg="powder blue").grid(row=4,
                                                                                                             column=3)
cal.mainloop()