from tkinter import *
from PIL import Image
from graphviz import Digraph
import third_sem.teor_ver.nastya.functions as f


def random_gen():
    """Випадково генерується матриця а.
    Поля для вводу елементів матриці заповнюються згенерованими значеннями."""
    a = f.random_a()
    for i in range(len(list_ent)):
        for j in range(len(list_ent[i])):
            list_ent[i][j].delete(0, END)
            list_ent[i][j].insert(END, round(a[i][j], 3))


def apply_styles(graph, styles):
    """Форматування графу"""
    graph.graph_attr.update(
        ('graph' in styles and styles['graph']) or {}
    )
    graph.node_attr.update(
        ('nodes' in styles and styles['nodes']) or {}
    )
    graph.edge_attr.update(
        ('edges' in styles and styles['edges']) or {}
    )
    return graph


def show_graph():
    """Відображає граф, заданий матрицею а"""

    gr = Digraph(format='png')
    for i in range(4):
        gr.node(str(i + 1))
    for i in range(4):
        for j in range(4):
            if a[i][j] != 0:
                gr.edge(str(i + 1), str(j + 1), label=str(a[i][j]))
    styles = {
        'graph': {
            'fontsize': '16',
            'fontcolor': 'white',
            'bgcolor': '#333333',
            'rankdir': 'BT',
        },
        'nodes': {
            'fontname': 'Helvetica',
            'shape': 'circle',
            'fontcolor': 'white',
            'color': 'white',
            'style': 'filled',
            'fillcolor': '#006699',
        },
        'edges': {
            'color': 'white',
            'arrowhead': 'open',
            'fontname': 'Courier',
            'fontsize': '10',
            'fontcolor': 'white',
        }
    }

    gr = apply_styles(gr, styles)
    gr.render('img/graph')

    Image.open("img/graph.png").show()


def show_counts():
    """Відображає систему рівнянь і порівнює теоретчні та експериментальні значення імовірностей"""
    slave = Toplevel(root)
    slave.title('Обчислення')
    cm = f.coef_matrix(a)
    Label(slave, text='Система рівнянь', font='Calibri 14 bold') \
        .grid(row=0, column=0, columnspan=3)
    Label(slave, text='P1 + P2 + P3 + P4 = 1\n'
                      '({})*P1+({})*P2+({})*P3+({})*P4 = 0\n'
                      '({})*P1+({})*P2+({})*P3+({})*P4 = 0\n'
                      '({})*P1+({})*P2+({})*P3+({})*P4 = 0\n'.format(cm[1][0], cm[1][1], cm[1][2], cm[1][3],
                                                                     cm[2][0], cm[2][1], cm[2][2], cm[2][3],
                                                                     cm[3][0], cm[3][1], cm[3][2], cm[3][3]),
          font='Calibri 14', justify=LEFT).grid(row=1, column=0, columnspan=3, sticky=W)

    p1, p2, p3, p4 = f.count_probabilities(cm)
    Label(slave, text='Теоретичні значення імовірностей', font='Calibri 14 bold') \
        .grid(row=2, column=0, columnspan=3)
    Label(slave, text='P1 = {}\n'
                      'P2 = {}\n'
                      'P3 = {}\n'
                      'P4 = {}\n'.format(p1, p2, p3, p4), font='Calibri 13', justify=LEFT)\
        .grid(row=3, column=0, columnspan=3, sticky=W)
    pe1, pe2, pe3, pe4 = f.experiment(f.model_sys(a))
    Label(slave, text='Практичні значення імовірностей', font='Calibri 14 bold') \
        .grid(row=4, column=0, columnspan=3)
    Label(slave, text='P1 = {}\n'
                      'P2 = {}\n'
                      'P3 = {}\n'
                      'P4 = {}'. format(pe1, pe2, pe3, pe4), font='Calibri 13', justify=LEFT)\
        .grid(row=5, column=0, columnspan=3, sticky=W)


def but_Ok():
    """При натисканні кнопки ОК всі поля стають неактивними для вводу.
    Створюється змінна з матрицею а, з якою надалі будемо працювати."""
    for i in range(len(list_ent)):
        for j in range(len(list_ent[i])):
            list_ent[i][j]['state'] = DISABLED
    global a
    a = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(len(list_ent)):
        for j in range(len(list_ent[i])):
            a[i][j] = float(list_ent[i][j].get())

    Button(root, text='Показати обчислення', font='Calibri 12 bold', bg='yellow', command=show_counts)\
        .grid(column=0, columnspan=3, row=6, pady=10)

    Button(root, text='Показати граф', font='Calibri 12 bold', bg='yellow', command=show_graph)\
        .grid(column=3, columnspan=3, row=6, pady=10)

    but1.grid_forget()
    but2.grid_forget()


if __name__ == '__main__':
    root = Tk()
    root['bg'] = 'slategrey'
    root.title('Головне вікно')

    Label(root, text='Матриця імовірностей переходів', font='Calibri 18 bold', bg='slategrey')\
        .grid(row=0, column=0, columnspan=5, pady=10, padx=10)

    list_ent = []
    for i in range(4):
        list_ent.append([])
        for j in range(4):
            list_ent[i].append(Entry(root, font='Calibri 14', width=6, bg='lavender'))
            list_ent[i][j].grid(row=i + 1, column=j + 1, sticky=W)
            list_ent[i][j].insert(END, '0')

    but1 = Button(root, text='Згенерувати випадково', font='Calibri 12 bold', bg='lightseagreen', command=random_gen)
    but1.grid(column=0, columnspan=3, row=5, pady=10)

    but2 = Button(root, text='OK', font='Calibri 12 bold', bg='lime', width=5, command=but_Ok)
    but2.grid(column=3, row=5, pady=10)

    root.mainloop()
