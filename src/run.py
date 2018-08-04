from main import Main
import tkinter
from tkinter import *
from tkinter import messagebox


def submit():
    yyyyMM = e_yyyyMM.get()
    dd = e_dd.get()
    try:
        numYYYYMM = int(yyyyMM.strip())
    except:
        messagebox.askokcancel('消息框', '请输入六位数年月，如：201808')
        return
    if numYYYYMM<100000 or numYYYYMM > 999999:
        messagebox.askokcancel('消息框', '请输入六位数年月，如：201808')
        return
    try:
        numDD = int(dd.strip())
    except:
        messagebox.askokcancel('消息框', '请输入二位数日期，如：08')
        return
    if numDD<0 or numDD > 31:
        messagebox.askokcancel('消息框', '请输入二位数日期，如：08')
        return

    msg = Main(yyyyMM, dd).main()
    messagebox.askokcancel('消息框', msg)


def center_window(w=500, h=350):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))


root = tkinter.Tk(className='成交持仓排名')
center_window(200, 100)
l_yyyyMM = Label(root, text='年月：')
l_yyyyMM.grid(row=0, sticky=W)
e_yyyyMM = Entry(root)
e_yyyyMM.grid(row=0, column=1, sticky=E)
l_dd = Label(root, text='日期：')
l_dd.grid(row=1, sticky=W)
e_dd = Entry(root)
e_dd.grid(row=1, column=1, sticky=E)
b_submit = Button(root, text='抓取', command=submit)
b_submit.grid(row=2, column=1, sticky=E)
root.mainloop()
