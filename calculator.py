from tkinter import*

def btnClick (numbers):
	global operator
	operator = operator + str(numbers)
	text_Input.set(operator)

def btnClearDisplay():
	global operator
	operator = ""
	text_Input.set("")

def btnEqualsInput():
	global operator
	sumup = str(eval(operator))
	text_Input.set(sumup)
	operator=""

cal = Tk()
cal.title("calculator")
operator=""
text_Input= StringVar()
txtDisplay = Entry(cal,font = ('arial', 20, 'bold'),textvariable=text_Input, bd=30, insertwidth = 4,bg = "powder blue", justify ='right').grid(columnspan=4)
btn7=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20, 'bold'),text="7",bg="powder blue", command = lambda:btnClick(7)).grid(row=1,column=0)
btn8=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20, 'bold'),text="8",bg="powder blue", command = lambda:btnClick(8)).grid(row=1,column=1)