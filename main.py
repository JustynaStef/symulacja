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
    for punkt in tablica:
        x, y = np.where(tablica == punkt)
        canvas.create_rectangle(x*scale, y*scale, (x+1)*scale, (y+1)*scale, fill="yellow")
 
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
 
    tablica[[x],[y]] = tablica[[x],[y]] * (-1)
    refresh()
 
 
def refresh():
    for punkt in tablica:
        if punkt == 1:
            color = "red"
        elif punkt == -1:
            color = "blue"
         
        x, y = np.where(tablica == punkt)
        canvas.create_rectangle(x*scale, y*scale, (x+1)*scale, (y+1)*scale, fill=color)
 
def start():
    for punkt in tablica:
        xx, yy = np.where(tablica == punkt)
        x = xx * scale
        y = yy * scale
    
        if 0 < y < (n-1)*scale and 0 < x < (n-1)*scale:
            algorytm(tablica[[x - 10], [y]], tablica[[x + 10], [y]], tablica[[x], [y - 10]], tablica[[x], [y + 10]], x, y)
            
        elif x == 0 and y == 0:
            algorytm(tablica[[x], [y + 10]], tablica[[x + 10], [y]], 0, 0, x, y)

        elif x == (n-1)*scale and y == 0:
            algorytm(tablica[[x], [y + 10]], tablica[[x - 10], [y]], 0, 0, x, y)

        elif x == 0 and y == (n-1)*scale:
            algorytm(tablica[[x], [y - 10]], tablica[[x + 10], [y]], 0, 0, x, y)

        elif x == (n-1)*scale and y == (n-1)*scale:
            algorytm(tablica[[x], [y - 10]], tablica[[x - 10], [y]], 0, 0, x, y)

        elif y == 0:
            algorytm(tablica[[x], [y + 10]], tablica[[x + 10], [y]], tablica[[x - 10], [y]], 0, x, y)

        elif y == (n-1)*scale:
            algorytm(tablica[[x], [y - 10]], tablica[[x + 10], [y]], tablica[[x - 10], [y]], 0, x, y)

        elif x == 0:
            algorytm(tablica[[x], [y + 10]], tablica[[x + 10], [y]], tablica[[x], [y - 10]], 0, x, y)

        elif x == (n-1)*scale:
            algorytm(tablica[[x], [y + 10]], tablica[[x], [y - 10]], tablica[[x - 10], [y]], 0, x, y)


def algorytm (one, two, three, four, x, y):
    h = one + two + three + four
    b = 0.5
    p = math.exp(b*h)
    r = random.uniform(0, 1)

    if r > p:
        tablica[[x],[y]] = 1
    else:
        tablica[[x],[y]] = -1

    refresh()
        
 
if __name__ == '__main__':
    main()

