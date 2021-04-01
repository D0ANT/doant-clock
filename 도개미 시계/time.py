from tkinter import *
import datetime as dt
import time

def time_lab():
    lab.config(text = "{0}년 {1}월 {2}일 {3}시 {4}분 {5}초".format(dt.datetime.now().year,
                                                         dt.datetime.now().month,
                                                         dt.datetime.now().day,
                                                         dt.datetime.now().hour,
                                                         dt.datetime.now().minute,
                                                         dt.datetime.now().second))
    lab.after(500,time_lab)
    print('1')
    lab.pack()
tk = Tk()
tk.geometry("450x100")
tk.title("도개미 시계")
tk.option_add("*Font","고딕 20")
lab = Label(tk)
time_lab()

button1 = Button(tk, text="Quit", command=tk.destroy).pack()

tk.mainloop()
