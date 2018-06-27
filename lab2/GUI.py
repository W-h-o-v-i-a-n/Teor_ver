from tkinter import *
import third_sem.teor_ver.lab2.functions as f


def show_row():
    slave = Toplevel(root)
    slave.focus_set()
    slave.title('Згенеровані числа')
    slave['bg'] = 'mint cream'
    t = Text(slave, font='Corbel 12', bg='mint cream')
    t.pack(side=LEFT, fill=BOTH, padx=10)

    for i in row:
        t.insert(END, str(i)+'\n')

    s = Scrollbar(slave)
    s.pack(side=RIGHT, fill=Y)
    s.config(command=t.yview)
    t.config(yscrollcommand=s.set)


def but_bind():
    root.maxsize(600, 450)
    root.minsize(600, 450)

    if ent_sigma.get().isdigit() & ent_m.get().isdigit() & ent_range.get().isdigit():
        global m, sigma, row
        m = int(ent_m.get())
        sigma = int(ent_sigma.get())
        row = [f.gen_random_number(m, sigma) for i in range(int(ent_range.get()))]

        Label(root, text='________________________________________', font='Arial 16', bg='mint cream', justify=LEFT)\
            .grid(row=9, column=1, columnspan=4, padx=10)
        Label(root, text='\nМатематичне очікування --> {}'
                         '\nСередньоквадратичне відхилення --> {}\n'.format(f.count_m(row), f.count_sigma(row, m)),
              font='Arial 16', bg='mint cream', justify=LEFT)\
            .grid(row=10, column=1, columnspan=4, padx=10, sticky=W)
        Button(root, text='Згенерований ряд', font='Arial 12 bold', bg='green yellow', command=show_row) \
            .grid(row=12, column=1, columnspan=4, pady=10, padx=30)
    else:
        Label(root, text='Неправильно введені дані.', fg='red', font='Arial 12', bg='mint cream')\
            .grid(row=9, column=1, sticky=W)


root = Tk()
root.title('Параметри')
root['bg'] = 'mint cream'
root.maxsize(480, 400)
root.minsize(480, 400)
Label(root, text='Введіть параметри', font='Arial 16 bold', bg='mint cream')\
    .grid(row=1, column=1, columnspan=2, pady=10, padx=10)
Label(root, text='Математичне очікування:\n\n'
                 'Середньоквадратичне відхилення:\n\n'
                 'Кількість:', font='Arial 14', bg='mint cream', justify=LEFT)\
    .grid(row=2, column=1, rowspan=3, pady=10, padx=10)

ent_m = Entry(root, width=10, bd=3, bg='light cyan', font='Arial 13')
ent_m.grid(row=2, column=2, sticky=W, padx=10)
ent_sigma = Entry(root, width=10, bd=3, bg='light cyan', font='Arial 13')
ent_sigma.grid(row=3, column=2, sticky=W, padx=10)
ent_range = Entry(root, width=10, bd=3, bg='light cyan', font='Arial 13')
ent_range.grid(row=4, column=2, sticky=W, padx=10)
ent_range.insert(END, '5000')

Button(root, text='OK', font='Arial 14 bold', command=but_bind, bg='pale green').grid(row=8, columnspan=4, column=1, pady=15)

root.mainloop()
