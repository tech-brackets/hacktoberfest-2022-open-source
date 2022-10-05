# Use this command if you want build into .exe file
# pyinstaller --onefile -w calculator.py
# ./dist/calculator

import tkinter as tk

root = tk.Tk()
root.geometry("300x300")
root.title("Calculator")

calc_input = tk.Text(root, height=1, width=19, font=("Helvetica", 20))
calc_input.grid(columnspan=3)
result=""

def calc():
    result=eval(retrieve_input())#"1+2" -> 1+2
    calc_input.delete(1.0, "end")
    calc_input.insert(1.0, str(result))

def retrieve_input():
    input = calc_input.get("1.0", tk.END)
    return input

def input(number):
    calc_input.insert("end", str(number))

def clear():
    calc_input.delete(1.0, "end")


__button1__ = tk.Button(root, text="1", command=lambda:input(1), height=1, width=5, font=("Helvetica", 18))
__button1__.grid(row=1, column=0)

__button2__ = tk.Button(root, text="2", command=lambda:input(2), height=1, width=5, font=("Helvetica", 18))
__button2__.grid(row=1, column=1)

__button3__ = tk.Button(root, text="3", command=lambda:input(3), height=1, width=5, font=("Helvetica", 18))
__button3__.grid(row=1, column=2)

__button4__ = tk.Button(root, text="4", command=lambda:input(4), height=1, width=5, font=("Helvetica", 18))
__button4__.grid(row=2, column=0)

__button5__ = tk.Button(root, text="5", command=lambda:input(5), height=1, width=5, font=("Helvetica", 18))
__button5__.grid(row=2, column=1)

__button6__ = tk.Button(root, text="6", command=lambda:input(6), height=1, width=5, font=("Helvetica", 18))
__button6__.grid(row=2, column=2)

__button7__ = tk.Button(root, text="7", command=lambda:input(7), height=1, width=5, font=("Helvetica", 18))
__button7__.grid(row=3, column=0)

__button8__ = tk.Button(root, text="8", command=lambda:input(8), height=1, width=5, font=("Helvetica", 18))
__button8__.grid(row=3, column=1)

__button9__ = tk.Button(root, text="9", command=lambda:input(9), height=1, width=5, font=("Helvetica", 18))
__button9__.grid(row=3, column=2)

__button0__ = tk.Button(root, text="0", command=lambda:input(0), height=1, width=5, font=("Helvetica", 18))
__button0__.grid(row=4, column=0)


__plusBtn__ = tk.Button(root, text="+", command=lambda:input("+"), height=1, width=5, font=("Helvetica", 18))
__plusBtn__.grid(row=4, column=1)

__minusBtn__ = tk.Button(root, text="-", command=lambda:input("-"), height=1, width=5, font=("Helvetica", 18))
__minusBtn__.grid(row=4, column=2)

__resultBtn__ = tk.Button(root, text="=", command=lambda:calc(), height=1, width=5, font=("Helvetica", 18))
__resultBtn__.grid(row=5, column=0)

__devideBtn__ = tk.Button(root, text="/", command=lambda:input("/"), height=1, width=5, font=("Helvetica", 18))
__devideBtn__.grid(row=5, column=1)

__multiplyBtn__ = tk.Button(root, text="*", command=lambda:input("*"), height=1, width=5, font=("Helvetica", 18))
__multiplyBtn__.grid(row=5, column=2)

__resultBtn__ = tk.Button(root, text='clear', command=lambda:clear(), height=1, width=5, font=("Helvetica", 18), bg='#b42506', fg='white')
__resultBtn__.grid(row=6, column=1)

root.mainloop()