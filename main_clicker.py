import tkinter as tk
import os
import time

root = tk.Tk()
root.title('Clicker')

info = tk.Label(text='Нажми <ПРОБЕЛ>, чтобы кликнуть')
info.pack()
info = tk.Label(text='Каждый апгрейд стоит 100 очков и добавляет +1 к очкам за клик')
btn = tk.Button(text='Click Me for upgrade!', width=15, height=7)

info.pack()

n = 0
a = 1
start = time.time()
tt = 0


def nplus(event):
    global start
    global tt
    tt = time.time() - start
    global n
    global a
    start = time.time()
    # print(tt)
    if tt > 0.06:
        n = n + a
        label['text'] = str(n)
    else:
        pass

    return start


def aplus(event):
    global n
    global a
    if n >= 100:
        n -= 100
        a += 1
    label['text'] = str(n)


btn.bind('<Button-1>', aplus)
root.bind("<space>", nplus)

label = tk.Label(root, text=str(n))
label.pack()

btn.pack()

tk.mainloop()

