from tkinter import *
import third_sem.teor_ver.lab4.functions as f


def create_list_from_ent_get(s: str):
    s.replace(',', ' ')
    return [int(i) for i in s.strip().split(' ')]


def but_show():
    but1['state'] = DISABLED
    slave = Toplevel(root)
    slave.title('Розрахунки')
    Label(slave, text='Задані множини:', font='Calibri 14 bold')\
        .grid(row=0, column=0, padx=10, pady=10)
    Label(slave, text='X1 = {}\n'
                      'X2 = {}\n'
                      'Y = {}\n'.format(X1, X2, Y), font='Calibri 14', justify=LEFT) \
        .grid(row=1, column=0, padx=10, pady=10)

    L, L1, L2 = f.create_L(X1, X2, Y)
    Label(slave, text='Матриця коваріацій', font='Calibri 14 bold')\
        .grid(row=2, column=0, padx=10, pady=10)
    Label(slave, text='{a}\t{b}\n'
                      '{c}\t{d}\n'.format(a=round(L[0][0], 3), b=round(L[0][1], 3), c=round(L[1][0], 3), d=round(L[1][1], 3)), font='Calibri 14') \
        .grid(row=3, column=0, padx=10, pady=10)

    a, b1, b2 = f.count_coefs(L, L1, L2, X1, X2, Y)
    Label(slave, text='Отримана регресія', font='Calibri 14 bold') \
        .grid(row=4, column=0, padx=10, pady=10)
    Label(slave, text='Y =({}) + ({})*X1 + ({})*X2'.format(round(a, 4), round(b1, 4), round(b2, 4)), font='Calibri 14') \
        .grid(row=5, column=0, padx=10, pady=10)


def but_Ok():
    global X1, X2, Y
    X1 = create_list_from_ent_get(ent_X1.get())
    X2 = create_list_from_ent_get(ent_X2.get())
    Y = create_list_from_ent_get(ent_Y.get())

    label1 = Label(root, text='', font='Calibri 14 bold', fg='red')
    label1.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    if len(X1) != len(X2) or len(X2) != len(Y) or len(X1) != len(Y):
        label1['text'] = 'Усі вбірки повинні мати однакову довжину!'
    else:
        ent_X1['state'] = DISABLED
        ent_X2['state'] = DISABLED
        ent_Y['state'] = DISABLED

        but.grid_forget()

        global but1
        but1 = Button(root, text='Показати результат', font='Calibri 14 bold', bg='lime', command=but_show)
        but1.grid(row=4, column=0, columnspan=2, pady=10, padx=10)


if __name__ == '__main__':
    root = Tk()
    root.title('Головне вікно')

    Label(root, text='Введіть множини Х1, Х2, Y', font='Calibri 18 bold')\
        .grid(row=0, column=0, columnspan=2, pady=10, padx=10)
    Label(root, text='Х1', font='Calibri 14 bold') \
        .grid(row=1, column=0, pady=10, padx=10)
    Label(root, text='Х2', font='Calibri 14 bold') \
        .grid(row=2, column=0, pady=10, padx=10)
    Label(root, text='Y', font='Calibri 14 bold') \
        .grid(row=3, column=0, pady=10, padx=10)

    ent_X1 = Entry(root, font='Calibri 14', width=20, bg='lavender')
    ent_X1.grid(row=1, column=1, pady=10, padx=10)
    ent_X2 = Entry(root, font='Calibri 14', width=20, bg='lavender')
    ent_X2.grid(row=2, column=1, pady=10, padx=10)
    ent_Y = Entry(root, font='Calibri 14', width=20, bg='lavender')
    ent_Y.grid(row=3, column=1, pady=10, padx=10)

    but = Button(root, text='OK', font='Calibri 14 bold', bg='lime', command=but_Ok)
    but.grid(row=4, column=0, columnspan=2, pady=10, padx=10)
    root.mainloop()
