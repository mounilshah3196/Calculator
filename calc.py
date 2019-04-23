from tkinter import*

def btnClicks(numbers):
    global operator
    operator = operator+str(numbers)
    text_Input.set(operator)

def btnFinal():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)

def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")

cal = Tk()
cal.title("Calculator")
operator = ""
text_Input = StringVar()
textDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                    bg="powder blue", justify="right").grid(columnspan=4)

btn7 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="7", bg="powder blue",
              command=lambda :btnClicks(7)).grid(row=1, column=0)
btn8 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="8", bg="powder blue",
              command=lambda :btnClicks(8)).grid(row=1, column=1)
btn9 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="9", bg="powder blue",
              command=lambda :btnClicks(9)).grid(row=1, column=2)
btnAdd = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="+", bg="powder blue",
                command=lambda :btnClicks(" + ")).grid(row=1, column=3)

btn4 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="4", bg="powder blue",
              command=lambda :btnClicks(4)).grid(row=2,column=0)
btn5 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="5", bg="powder blue",
              command=lambda :btnClicks(5)).grid(row=2, column=1)
btn6 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="6", bg="powder blue",
              command=lambda :btnClicks(6)).grid(row=2, column=2)
btnSub = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="-", bg="powder blue",
                command=lambda :btnClicks(" - ")).grid(row=2, column=3)

btn1 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="1", bg="powder blue",
              command=lambda :btnClicks(1)).grid(row=3, column=0)
btn2 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="2", bg="powder blue",
              command=lambda :btnClicks(2)).grid(row=3, column=1)
btn3 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="3", bg="powder blue",
              command=lambda :btnClicks(3)).grid(row=3, column=2)
btnMul = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="*", bg="powder blue",
                command=lambda :btnClicks(" * ")).grid(row=3, column=3)

btnC = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="C", bg="powder blue",
              command=lambda :btnClearDisplay()).grid(row=4, column=0)
btn0 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="0", bg="powder blue",
              command=lambda :btnClicks(0)).grid(row=4, column=1)
btnDiv = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="/", bg="powder blue",
                command=lambda :btnClicks(" / ")).grid(row=4, column=2)
btnEquals = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="=", bg="powder blue",
                   command=lambda :btnFinal()).grid(row=4, column=3)
cal.mainloop()