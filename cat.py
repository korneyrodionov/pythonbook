#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import turtle as t

t.shape('turtle')
t.bgcolor('black')
t.speed('slowest')
t.pensize(3)
t.pencolor('blue')

t.penup()
t.goto(100,240)
t.pendown()

t.goto(100, 180)
t.goto(140, 100)
t.goto(140, 20)
t.goto(60, 20)
t.goto(80, 40)
t.goto(80, 80)
t.goto(40, 140)
t.goto(60, 160)
t.goto(40, 180)
t.goto(40, 240)
t.goto(60, 220)
t.goto(80, 220)
t.goto(100, 240)

t.penup()
t.goto(140, 20)
t.pendown()

t.goto(180, 60)
t.goto(260, 60)
t.goto(220, 20)
t.goto(140, 20)

t.hideturtle()

t.done()