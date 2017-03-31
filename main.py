# symulacja

from Tkinter import *
import numpy as np
import math
import random

n = 10
tablica = np.arange(n*n)
tablica = tablica.reshape((n,n))
tablica = np.ones_like(tablica)
scale = 10

window = Tk()
canvas = Canvas(window, width=100, height=120)
canvas.pack()
 
def main():
    init_tablica()
    register_window()
 
def init_tablica():
        for i in xrange(0, 9):
          for j in xrange(0, 9):
            canvas.create_rectangle(i * scale, j * scale, (i + 1) * scale, (j + 1) * scale, fill="yellow")
 
def register_window():
    canvas.bind('<Double-1>', my_on_click)
 
    button_start = Button(window, text="START", command=start)
    button_start.configure(width=10, activebackground="red", relief=FLAT)
    button_start.window = canvas.create_window(10, 10, anchor=S, window=button_start)
    button_start.place(x=50, y=110)
    
    window.mainloop()
 
def my_on_click(event):

    x = event.x/scale
    y = event.y/scale
 
    tablica[x, y] = tablica[x, y] * (-1)
    refresh()
 
 
def refresh():
    for j in xrange(0,9):
       x = i
       y = j
         if tablica[x, y] is 1:
             color = "red"
         elif tablica[x, y] is -1:
             color = "blue"
         else:
             color = "white"
           
        canvas.create_rectangle(x*scale, y*scale, (x+1)*scale, (y+1)*scale, fill=color)
 
def start():
     for i in xrange(0, 9):
        for j in xrange(0, 9):
            x = i * scale
            y = j * scale

            if 0 < y < (n - 1) * scale and 0 < x < (n - 1) * scale:
                algorytm(tablica[i - 1, j], tablica[i + 1, j], tablica[i, j - 1], tablica[i, j + 1], i, j)

            elif x == 0 and y == 0:
                algorytm(tablica[i, j + 1], tablica[i + 1, j], 0, 0, i, j)

            elif x == (n - 1) * scale and y == 0:
                algorytm(tablica[i, j + 1], tablica[i - 1, j], 0, 0, i, j)

            elif x == 0 and y == (n - 1) * scale:
                algorytm(tablica[i, j - 1], tablica[i + 1, j], 0, 0, i, j)

            elif x == (n - 1) * scale and y == (n - 1) * scale:
                algorytm(tablica[i, j - 1], tablica[i - 1, j], 0, 0, i, j)

            elif y == 0:
                algorytm(tablica[i, j + 1], tablica[i + 1, j], tablica[i - 1, j], 0, i, j)

            elif y == (n - 1) * scale:
                algorytm(tablica[i, j - 1], tablica[x + 1, j], tablica[i - 1, j], 0, i, j)

            elif x == 0:
                algorytm(tablica[i, j + 1], tablica[i + 1, j], tablica[i, j - 1], 0, i, j)

            elif x == (n - 1) * scale:
                algorytm(tablica[i, j + 1], tablica[i, j - 1], tablica[i - 1, j], 0, i, j)

def algorytm (one, two, three, four, x, y):
    h = one + two + three + four
    b = 0.5
    p = math.exp(b * h)
    r = random.uniform(0, 1)

    if r > p:
        tablica[x, y] = 1
    else:
        tablica[x, y] = -1

    refresh()
        
 
if __name__ == '__main__':
    main()

