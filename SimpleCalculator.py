from tkinter import *

root = Tk()
root.title("simple Calculator")


display = Entry(root,width=35, borderwidth=2)
display.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

#Button Inside works,
def button_click(number):
    current = display.get()
    display.delete(0,END)  # using clear display
    display.insert(0,str(current) + str(number))

def button_add():
     first_num = display.get()
     global f_num
     global math
     math = "add"
     f_num = int(first_num)
     display.delete(0,END)

def button_mul():
     first_num = display.get()
     global f_num
     global math
     math = "mul"
     f_num = int(first_num)
     display.delete(0,END)


def button_sub():
     first_num = display.get()
     global f_num
     global math
     math = "sub"
     f_num = int(first_num)
     display.delete(0,END)

def button_div():
     first_num = display.get()
     global f_num
     global math
     math = "div"
     f_num = int(first_num)
     display.delete(0,END)


def button_equal():
    last_num = display.get()

    if math == "add":
         calculation = f_num + int(last_num)
         button_clear()
         display.insert(0,calculation)
    elif math == "sub":
         calculation = f_num - int(last_num)
         button_clear()
         display.insert(0,calculation)
    elif math == "mul":
         calculation = f_num * int(last_num)
         button_clear()
         display.insert(0,calculation)
    elif math == "div":
         calculation = f_num / int(last_num)
         button_clear()
         display.insert(0,calculation)
    

def button_clear():
    display.delete(0,END)


#Buttons 
btn1 = Button(root,text="1",padx=40,pady=20, command=lambda: button_click(1))
btn2 = Button(root,text="2",padx=40,pady=20, command=lambda: button_click(2))
btn3 = Button(root,text="3",padx=40,pady=20, command=lambda: button_click(3))
btn4 = Button(root,text="4",padx=40,pady=20, command=lambda: button_click(4))
btn5 = Button(root,text="5",padx=40,pady=20, command=lambda: button_click(5))
btn6 = Button(root,text="6",padx=40,pady=20, command=lambda: button_click(6))
btn7 = Button(root,text="7",padx=40,pady=20, command=lambda: button_click(7))
btn8 = Button(root,text="8",padx=40,pady=20, command=lambda: button_click(8))
btn9 = Button(root,text="9",padx=40,pady=20, command=lambda: button_click(9))
btn0 = Button(root,text="0",padx=40,pady=20, command=lambda: button_click(0))
btn_add = Button(root,text="+",padx=40,pady=20,command=button_add)
btn_mul = Button(root,text="*",padx=40,pady=20, command=button_mul)
btn_sub = Button(root,text="-",padx=40,pady=20,command=button_sub)
btn_div = Button(root,text="/",padx=40,pady=20,command=button_div)
btn_equal = Button(root,text="=",padx=40,pady=50,command=button_equal)
btn_clear = Button(root, text="Clear", padx=77, pady=20,command=button_clear)



#Show On display,
btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1)
btn3.grid(row=3,column=2)

btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)

btn7.grid(row=1,column=0)
btn8.grid(row=1,column=1)
btn9.grid(row=1,column=2)

btn0.grid(row=4,column=0)
btn_sub.grid(row=4,column=1)
btn_mul.grid(row=4,column=2)
btn_div.grid(row=5,column=1)
btn_add.grid(row=5,column=0)
btn_equal.grid(row=5,column=2, rowspan=7)
btn_clear.grid(row=6,column=0, columnspan=2)



root.mainloop()