#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import turtle as t

def draw_star(points, size, col, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180 - (180 / points)
    t.color(col)
    t.begin_fill()
    for i in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()
    
def draw_click(x,y):
    draw_star(5, 50, 'yellow', x, y)

#Основной код
#t.onScreenClick()
t.hideturtle()
t.Screen().bgcolor('dark blue')
draw_star(5, 50, 'yellow', 0, 0)

def main():
    t.onscreenclick(draw_click)
    t.mainloop()
main()