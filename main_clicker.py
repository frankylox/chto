import tkinter as tk

root = tk.Tk()
root.title('Clicker')

info = tk.Label(text='Нажми <ПРОБЕЛ>, чтобы кликнуть')
info.pack()
info = tk.Label(text='Каждый апгрейд стоит 100 кликов и добавляет +1 к очкам за клик')
btn = tk.Button(text='Click Me for upgrade!', width=15, height=7)

info.pack()

n = 0  # переменная для счетчика
a = 1


def nplus(event):
    global n
    global a
    n = n + a
    label['text'] = str(n)


def aplus(event):
    global n
    global a
    if n >= 100:
        n -= 100
        a += 1
    label['text'] = str(n)


btn.bind('<Button-1>', aplus)
root.bind("<space>", nplus)
label = tk.Label(root, text=str(n), font='Helvetica')
label.pack()

btn.pack()

tk.mainloop()
