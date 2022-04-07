import tkinter as tk
import time
import sys
wd=tk.Tk()
wd.geometry('100x80')
n=0
l=tk.Label(wd,text=n)
l.pack()
t=1
def cnp():
    global n
    global l
    global ask
    global w
    global t
    w=tk.Tk()
    w.geometry('200x150')
    ask=tk.Entry(w)
    def get():
        global ask
        global t
        global w
        global n
        global l
        t=int(ask.get())
        n+=t
        l.pack_forget()
        l=tk.Label(wd,text=n)
        l.pack()
        w.destroy()
    go=tk.Button(w,command=get,text='done')
    ask.pack()
    go.pack()
    w.mainloop()
def cnm():
    global n
    global l
    global ask
    global w
    global t
    w=tk.Tk()
    w.geometry('200x150')
    ask=tk.Entry(w)
    def get():
        global ask
        global t
        global w
        global n
        global l
        t=int(ask.get())
        n-=t
        l.pack_forget()
        l=tk.Label(wd,text=n)
        l.pack()
        w.destroy()
    go=tk.Button(w,command=get,text='done')
    ask.pack()
    go.pack()
    w.mainloop()
def cnt():
    global n
    global l
    global ask
    global w
    global t
    w=tk.Tk()
    w.geometry('200x150')
    ask=tk.Entry(w)
    def get():
        global ask
        global t
        global w
        global n
        global l
        t=int(ask.get())
        n=n*t
        l.pack_forget()
        l=tk.Label(wd,text=n)
        l.pack()
        w.destroy()
    go=tk.Button(w,command=get,text='done')
    ask.pack()
    go.pack()
    w.mainloop()
def cnd():
    global n
    global l
    global ask
    global w
    global t
    w=tk.Tk()
    w.geometry('200x150')
    ask=tk.Entry(w)
    def get():
        global ask
        global t
        global w
        global n
        global l
        t=int(ask.get())
        try:
            n=n/t
        except ZeroDivisionError as r:
            el=tk.Label(w,text='don\'t devide numbeer as 0!!!')
            el.pack()
            time.sleep(1)
        l.pack_forget()
        l=tk.Label(wd,text=n)
        l.pack()
        w.destroy()
    go=tk.Button(w,command=get,text='done')
    ask.pack()
    go.pack()
    w.mainloop()
def bz():
    global n
    global l
    n=0
    l.pack_forget()
    l=tk.Label(wd,text=n)
    l.pack()
def ex():
    sys.exit(1)
p=tk.Button(command=cnp,text='+')
m=tk.Button(command=cnm,text='-')
mu=tk.Button(command=cnt,text='x')
de=tk.Button(command=cnd,text='÷')
b0=tk.Button(command=bz,text='ac')
q=tk.Button(command=ex,text='exit')
p.place(x=60,y=40,anchor='se',width=60,height=20)
m.place(x=60,y=40,anchor='sw',width=60,height=20)
mu.place(x=60,y=40,anchor='ne',width=60,height=20)
de.place(x=60,y=40,anchor='nw',width=60,height=20)
b0.place(x=60,y=60,anchor='ne',width=60,height=20)
q.place(x=60,y=60,anchor='nw',width=60,height=20)
l.pack_forget()
l.pack()
wd.mainloop()