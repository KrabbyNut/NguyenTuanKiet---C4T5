from turtle import *

shape("turtle")
colors = ['red', 'blue', 'brown', 'yellow', 'grey']

n_angle = 3
# left_radius = 360 / n_angle


color(colors[0])

for i in range(n_angle):
    forward(100)
    left(360/n_angle)

color(colors[1])

for i in range(4):
    forward(100)
    left(360/4)

color(colors[2])

for i in range(5):
    forward(100)
    left(360/5)

color(colors[3])

for i in range(6):
    forward(100)
    left(360/6)

color(colors[4])

for i in range(7):
    forward(100)
    left(360/7)


mainloop()