from turtle import *

tracer(0)

koef = 20

size = 4

for i in range(6):
    forward(size * koef)
    right(90)
    forward(7 * koef)

up()

for x in range(-koef, koef):
    for y in range(-koef, koef):
        goto(x * koef, y * koef)
        dot(3)

exitonclick()

for size in range(1, 100):
    if (7 + size + 1)**2 > 900:
        print(size)

        break