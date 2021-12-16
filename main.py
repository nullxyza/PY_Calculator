import tkinter as tk
win = tk.Tk()
win.resizable(0, 0)
win.title("PY Calculator")
win.geometry("380x597")
win.config(bg='#A7C7E7')
label = tk.Label(win, text="PY Calculator", bg="#A7C7E7", fg='white')
label.config(font=('Verdana 14 bold'))
label.pack()
frame2 = tk.Frame(win,height=100).pack(side='top',fill='both')
input_text = tk.StringVar()
entry = tk.Entry(frame2,justify='right', font=('Verdana', 30, 'bold'), textvariable=input_text, width=15,bg="#eee", bd=0,fg = '#4682B4')
entry.place(x=10, y=50)
entry.pack()
def bt_clear():
    global expr
    expr = ""
    input_text.set("")
def btn_click(item):
    global expr
    expr = expr + str(item)
    input_text.set(expr)
expr = ""
def bt_equal():
    try:
        global expr
        result = str(eval(expr))
        input_text.set(result)
        expr = ""
    except:
        input_text.set(" error ")
        expr = ""

btns_frame = tk.Frame(win, width=402, height=400, bg="#4682B4")
btns_frame.place(x=50, y=100)
btns_frame.pack()
clear = tk.Button(btns_frame, text="C", fg="#191970", width=35, height=5, bd=0, bg="#ADD8E6", cursor="hand2",
                  command=lambda: bt_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1, sticky='news')
divide = tk.Button(btns_frame, text="/", fg="#191970", width=17, height=5, bd=0, bg="#eee", cursor="hand2",
                   command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1, stick='news')
seven = tk.Button(btns_frame, text="7", fg="black", width=11, height=5, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1, stick='news')
eight = tk.Button(btns_frame, text="8", fg="black", width=11, height=5, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1, stick='news')
nine = tk.Button(btns_frame, text="9", fg="black", width=11, height=5, bd=0, bg="#fff", cursor="hand2",
                 command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1, stick='news')
multiply = tk.Button(btns_frame, text="*", fg="#191970", width=11, height=5, bd=0, bg="#eee", cursor="hand2",
                     command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1, stick='news')
four = tk.Button(btns_frame, text="4", fg="black", width=10, height=5, bd=0, bg="#fff", cursor="hand2",
                 command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1, stick='news')
five = tk.Button(btns_frame, text="5", fg="black", width=10, height=5, bd=0, bg="#fff", cursor="hand2",
                 command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1, stick='news')
six = tk.Button(btns_frame, text="6", fg="black", width=10, height=5, bd=0, bg="#fff", cursor="hand2",
                command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1, stick='news')
minus = tk.Button(btns_frame, text="-", fg="#191970", width=10, height=5, bd=0, bg="#eee", cursor="hand2",
                  command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1, stick='news')
one = tk.Button(btns_frame, text="1", fg="black", width=10, height=5, bd=0, bg="#fff", cursor="hand2",
                command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1, stick='news')
two = tk.Button(btns_frame, text="2", fg="black", width=10, height=5, bd=0, bg="#fff", cursor="hand2",
                command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1, stick='news')
three = tk.Button(btns_frame, text="3", fg="black", width=10, height=5, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1, stick='news')
plus = tk.Button(btns_frame, text="+", fg="#191970", width=10, height=5, bd=0, bg="#eee", cursor="hand2",
                 command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1, stick='news')
zero = tk.Button(btns_frame, text="0", fg="black", width=21, height=5, bd=0, bg="#fff", cursor="hand2",
                 command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1, stick='news')
point = tk.Button(btns_frame, text=".", fg="black", width=10, height=5, bd=0, bg="#eee", cursor="hand2",
                  command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1, stick='news')
equals = tk.Button(btns_frame, text="=", fg="#191970", width=10, height=5, bd=0, bg="#4682B4", cursor="hand2",
                   command=lambda: bt_equal()).grid(row=4, column=3, padx=1, pady=1, stick='news')

win.mainloop()





