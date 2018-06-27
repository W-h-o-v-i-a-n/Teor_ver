from tkinter import *
from PIL import ImageTk, Image
import math
import third_sem.teor_ver.lab3.f_real as f_real


def counts():
    X, Y = f_real.gen_xy(n)
    l = 'Мат очікування X = {Mx}\n'\
        'Мат очікування Y = {My}\n'\
        'Дисперсія X = {Dx}\n'\
        'Дисперсія Y = {Dy}\n'\
        'Середньоквадр. відхилення X = {Sx}\n'\
        'Середньоквадр. відхилення Y = {Sy}\n'\
        'Коваріація = {cov}\n'\
        'Коеф кореляції = {corel}\n'.format(Mx=f_real.mean(X), My=f_real.mean(Y),
                                            Dx=math.pow(f_real.deviation(X), 2), Dy=math.pow(f_real.deviation(Y), 2),
                                            Sx=f_real.deviation(X), Sy=f_real.deviation(Y),
                                            cov=f_real.cov(X, Y), corel=f_real.corel(X, Y))
    return l


def but_bind():
    if ent_n.get().isalnum():
        global n
        n = int(ent_n.get())
        ent_n['state'] = DISABLED

        l['text'] = counts()
        l['fg'] = 'black'
        l['font'] = 'Arial 14'
    else:
        l['text'] = '*Перевірте введену довжину вибірки на зайві символи'
        l['fg'] = 'red'
        l['font'] = 'Arial 14 bold'


if __name__ == '__main__':
    root = Tk()

    Label(root, text='Функція щільності\n(куб зі стороною 1)', font='Arial 16 bold').grid(row=0, column=0)

    canvas = Canvas(root,width=400, height=300)
    canvas.grid(row=1, column=0)
    pilImage = Image.open("photo.jpg")
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(200, 150, image=image)

    Label(root, text='Введіть довжину вибірки', font='Arial 14 bold').grid(row=2, column=0)

    ent_n = Entry(root, width=10, bd=3, bg='light cyan', font='Arial 13')
    ent_n.insert(END, '5000')
    ent_n.grid(row=3, column=0, pady=10)

    Button(root, text='OK',font='Arial 14 bold', bg='pale green', command=but_bind).grid(row=4, column=0)

    l = Label(root, text='', justify=LEFT)
    l.grid(row=5, column=0)

    root.mainloop()
