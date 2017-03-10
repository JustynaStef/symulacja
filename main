# symulacja

from Tkinter import *
import numpy
import math
import random

tablica = numpy.matrix(100,100)
 
 
def main():
    init_tablica()
    register_window()
 
 
def register_window():
    window = Tk()
    canvas = Canvas(window)
 
    canvas.on_click = my_on_click
 
    button_start = Button(window)
    button_start.on_click = start
 
 
def my_on_click(e):

    x = e.x
    y = e.y
 
    tablica[x,y] = tablica[x,y] * (-1)
    refresh()
 
 
def refresh():
    for punkt in tablica:
        if punkt == 1:
            color = "red"
        elif punkt == -1:
            color = "blue"
 
        canvas.draw_rectangle(x,y, 10, 10, fill=color)
 
 
def start():
    for punkt in tablica:
        if 0 < y < 90 and 0 < x < 90
            algorytm(tablica[x - 10, y], tablica[x + 10, y], tablica[x, y - 10], tablica[x, y + 10])
            
        elif x == 0 and y == 0
            algorytm(tablica[x, y + 10], tablica[x + 10, y], 0, 0)

        elif x == 90 and y == 0
            algorytm(tablica[x, y + 10], tablica[x - 10, y], 0, 0)

        elif x == 0 && y == 90
            algorytm(tablica[x, y - 10], tablica[x + 10, y], 0, 0)

        elif x == 90 and y == 90
            algorytm(tablica[x, y - 10], tablica[x - 10, y], 0, 0)

        elif y == 0
            algorytm(tablica[x, y + 10], tablica[x + 10, y], tablica[x - 10, y], 0)

        elif y == 90
            algorytm(tablica[x, y - 10], tablica[x + 10, y], tablica[x - 10, y], 0)

        elif x == 0
            algorytm(tablica[x, y + 10], tablica[x + 10, y], tablica[x, y - 10], 0)

        elif x == 90
            algorytm(tablica[x, y + 10], tablica[x, y - 10], tablica[x - 10, y], 0)


def algorytm (one, two, three, four)
    h = one + two + three + four
    b = 0.5
    p = math.exp(b*h)
    r = random.uniform(0, 1)

    if r > p
        tablica[x,y] = 1
    else
        tablica[x,y] = -1

    refresh()
        
 
 
if __name__ == '__main__':
    main()

