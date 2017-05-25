from Tkinter import *
import numpy as np
import math
import random
import json

n = 40
tablica = np.arange(n * n)
tablica = tablica.reshape((n, n))
tablica = np.ones_like(tablica)
scale = 10

wyniki = {}
licznik = 0
it = 0

window = Tk()
canvas = Canvas(window, width=10*n, height=10*n + 40)
canvas.pack()


def main():
    init_tablica()
    #print tablica[0, 0]
    #print tablica[n-1, n-1]
    register_window()


def init_tablica():

    for i in xrange(0, n):
        for j in xrange(0, n):
            k = random.randrange(0, 2)
            if k == 0:
                col = "blue"
                tablica[i, j] = -1
            else:
                col = "red"
                tablica[i, j] = 1

            canvas.create_rectangle(i * scale, j * scale, (i + 1) * scale, (j + 1) * scale, fill=col)

def init_tablica2():
    for i in xrange(0, n):
        for j in xrange(0, n):
            col = "red"
            tablica[i, j] = 1
            canvas.create_rectangle(i * scale, j * scale, (i + 1) * scale, (j + 1) * scale, fill=col)

def register_window():
    canvas.bind('<Button-1>', my_on_click)

    button_start = Button(window, text="START", command=start)
    button_start.configure(width=10, activebackground="green", relief=FLAT)
    button_start.window = canvas.create_window(10, 10, anchor=S, window=button_start)
    button_start.place(x=5*n, y=10*n + 20)

    window.mainloop()


def my_on_click(event):
    x = event.x / scale            #canvas.canvasx() etc.
    y = event.y / scale

    tablica[x, y] = tablica[x, y] * (-1)
    refresh()


def refresh():

    for i in xrange(0, n):
        for j in xrange(0, n):
            x = i
            y = j
            if tablica[x, y] == 1:
                color = "red"
            elif tablica[x, y] == -1:
                color = "blue"
            else:
                color = "white"

            canvas.create_rectangle(x * scale, y * scale, (x + 1) * scale, (y + 1) * scale, fill=color)
            window.update_idletasks()
            window.update()

def refresh2(x, y):
    if tablica[x, y] == 1:
        color = "red"
    elif tablica[x, y] == -1:
        color = "blue"
    else:
        color = "white"

    canvas.create_rectangle(x * scale, y * scale, (x + 1) * scale, (y + 1) * scale, fill=color)
    window.update_idletasks()
    window.update()

def start():

    while True:

        i = random.randint(0, n-1)
        j = random.randint(0, n-1)
        #print tablica[n-1, n-1]

        if 0 < j < (n - 1) and 0 < i < (n - 1):
            algorytm(tablica[i - 1, j], tablica[i + 1, j], tablica[i, j - 1], tablica[i, j + 1], i, j)

        elif i == 0 and j == 0:
            algorytm(tablica[i, j + 1], tablica[i + 1, j], tablica[n-1, j], tablica[i, n-1], i, j)

        elif i == (n - 1) and j == 0:
            algorytm(tablica[i, j + 1], tablica[i - 1, j], tablica[n-1, n - 1], tablica[0, 0], i, j)

        elif i == 0 and j == (n - 1):
            algorytm(tablica[i, j - 1], tablica[i + 1, j], tablica[n-1, n-1], tablica[0, 0], i, j)

        elif i == (n - 1) and j == (n - 1):
            algorytm(tablica[i, j - 1], tablica[i - 1, j], tablica[0, n-1], tablica[n-1, 0], i, j)

        elif j == 0:
            algorytm(tablica[i, j + 1], tablica[i + 1, j], tablica[i - 1, j], tablica[i, n-1], i, j)

        elif j == (n - 1):
            algorytm(tablica[i, j - 1], tablica[i + 1, j], tablica[i - 1, j], tablica[i, 0], i, j)

        elif i == 0:
            algorytm(tablica[i, j + 1], tablica[i + 1, j], tablica[i, j - 1], tablica[n-1, j], i, j)

        elif i == (n - 1):
            algorytm(tablica[i, j + 1], tablica[i, j - 1], tablica[i - 1, j], tablica[0, j], i, j)



def algorytm(one, two, three, four, x, y):
    h = 2*tablica[x, y]*(one + two + three + four)
    b = 0.440687
    p = 1.0/(1.0 + math.exp(b * h))
    r = random.uniform(0, 1)
    global it

    if r < p:
        tablica[x, y] = tablica[x, y] *(-1)
    #else:
     #   tablica[x, y] = tablica[x, y]

    it += 1
    if it == n*n:
        korel()

    #refresh2(x, y)

def korel():
    global it
    global wyniki
    global licznik
    licznik += 1
    M = 0.0
    it = 0

    for i in xrange(0, n):
        for j in xrange(0, n):
            M = M + tablica[i, j]

    M = M/(n*n)

    wyniki[licznik] = M

    if licznik == 1:
        zapisz()
        licznik = 0
        wyniki = {}

def zapisz():
    with open("wyniki.csv", 'a') as f:
        f.write(str(wyniki[1]) + "/")
        print "k"
        #f.write(str(wyniki[2]) + "/")
        #f.write(str(wyniki[3]) + "/")
        #f.write(str(wyniki[4]) + "/")
        #f.write(str(wyniki[5]) + "/")
        #f.write(str(wyniki[6]) + "/")
        #f.write(str(wyniki[7]) + "/")
        #f.write(str(wyniki[8]) + "/")
        #f.write(str(wyniki[9]) + "/")
        #f.write(str(wyniki[10]) + "/")

if __name__ == '__main__':
    main()