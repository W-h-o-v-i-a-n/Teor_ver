import random
import third_sem.teor_ver.lab1.startstopnyy_gen_functions as func
from tkinter import *


def show_sequence():
    slave = Toplevel(root)
    slave.focus_set()
    slave.title('Згенерована бінарна послідовність')
    slave['bg'] = 'mint cream'
    t = Text(slave, font='Corbel 12', bg='mint cream')
    t.pack(side=LEFT, fill=BOTH, padx=10)

    t.insert(INSERT, sequence)

    s = Scrollbar(slave)
    s.pack(side=RIGHT, fill=Y)
    s.config(command=t.yview)
    t.config(yscrollcommand=s.set)


def but_bind():
    root.maxsize(430, 450)
    root.minsize(430, 450)

    if len(ent_extra.get()) == len(ent_basic.get()) == 12:
        global basic_num, extra_num, sequence
        ent_basic['state'] = DISABLED
        ent_extra['state'] = DISABLED
        quantity['state'] = DISABLED
        basic_num = ent_basic.get()
        extra_num = ent_extra.get()
        sequence = func.startstop_generator(ent_basic.get(), ent_extra.get(), int(quantity.get()))

        Label(root, text='__________________________________', font='Arial 16', bg='mint cream')\
            .grid(row=9, column=1, columnspan=2, padx=10)
        Button(root, text='Послідовність', font='Arial 12 bold', bg='green yellow', command=show_sequence) \
            .grid(row=10, column=1, columnspan=2, pady=10, sticky=W, padx=30)
        Button(root, text='Результати тестування', font='Arial 12 bold', bg='green yellow', command=window_tests)\
            .grid(row=10, column=1, columnspan=2, pady=10, sticky=E, padx=30)
    else:
        Label(root, text='Неправильно введені дані.', fg='red', font='Arial 12', bg='mint cream')\
            .grid(row=9, column=1, sticky=W)


def random_sequence(length):
    l = ''
    for i in range(length):
        l = l + str(random.choice([1, 0]))
    return l


def but_random_basic():
    ent_basic.delete(0, END)
    ent_basic.insert(END, random_sequence(12))


def but_random_extra():
    ent_extra.delete(0, END)
    ent_extra.insert(END, random_sequence(12))


def window_tests():
    slave = Toplevel(root)
    slave.focus_set()
    slave.title('Результати тестування')
    slave['bg'] = 'mint cream'
    t = Text(slave, font='Corbel 12', bg='mint cream')
    t.pack(side=LEFT, fill=BOTH, padx=10)
    t.insert(INSERT, 'Результат частотного тесту:\n{t1}\n\n'
                     'Результат диференційного частотного тесту: {t2}\n\n'
                     'Результат віконного тесту:\n{t3}\n\n'
                     'Результат нелінійного тесту на складність:\n\n{t4}\n\n'
             .format(t1=func.frequency_test(sequence), t2=func.differential_frequency_test(sequence),
                     t3=func.window_test(sequence), t4=func.complexity_test_nonlinear(sequence)))
    t.tag_add('tag1', '1.0', '1.50')
    t.tag_add('tag2', '5.0', '5.42')
    t.tag_add('tag3', '7.0', '7.50')
    t.tag_add('tag4', '42.0', '42.50')
    t.tag_config('tag1', font='Corbel 14 bold')
    t.tag_config('tag2', font='Corbel 14 bold')
    t.tag_config('tag3', font='Corbel 14 bold')
    t.tag_config('tag4', font='Corbel 14 bold')
    s = Scrollbar(slave)
    s.pack(side=RIGHT, fill=Y)
    s.config(command=t.yview)
    t.config(yscrollcommand=s.set)


if __name__ == '__main__':
    root = Tk()
    root.title('Параметри')
    root['bg'] = 'mint cream'
    root.maxsize(430, 340)
    root.minsize(430, 340)
    Label(root, text='Основна послідовність з 12 чисел', font='Arial 14', bg='mint cream')\
        .grid(row=1, column=1, columnspan=2, pady=10, padx=10)
    Label(root, text='Додаткова послідовність з 12 чисел', font='Arial 14', bg='mint cream')\
        .grid(row=3, column=1, columnspan=2, pady=10, padx=10)
    Label(root, text='Довжина генерованої послідовності', font='Arial 14', bg='mint cream')\
        .grid(row=5, column=1, columnspan=2, pady=10, padx=10)

    ent_basic = Entry(root, width=30, bd=3, bg='light cyan', font='Arial 13')
    ent_basic.grid(row=2, column=1, sticky=W, padx=10)
    ent_extra = Entry(root, width=30, bd=3, bg='light cyan', font='Arial 13')
    ent_extra.grid(row=4, column=1, sticky=W, padx=10)
    quantity = Entry(root, width=30, bd=3, bg='light cyan', font='Arial 13')
    quantity.grid(row=6, column=1, sticky=W, padx=10)

    quantity.insert(END, '10000')

    Button(root, text='Випадково', font='Arial 12 bold', command=but_random_basic, bg='pale green')\
        .grid(row=2, column=2,  sticky=W, pady=10, padx=10)
    Button(root, text='Випадково', font='Arial 12 bold', command=but_random_extra, bg='pale green')\
        .grid(row=4, column=2,  sticky=W, pady=10, padx=10)

    Button(root, text='OK', font='Arial 14 bold', command=but_bind, bg='pale green').grid(row=8, columnspan=2, column=1, pady=15)

    root.mainloop()
