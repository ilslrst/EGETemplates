from turtle import *

tracer(0)

koef = 20

size = 0
forward((size + 2) * koef)
for i in range(4):
    forward(size * koef)
    right(90)
    forward((size + 2) * koef)
right(90)
forward((2 * size) * koef)
for n in range(4):
    right(90)
    forward((3 * size - 1) * koef)

up()

for x in range(-koef, koef):
    for y in range(-koef, koef):
        goto(x * koef, y * koef)
        dot(3)

exitonclick()

for size in range (1, 100):
    if (size + size + 2)**2 + (3 * size - 1)**2 - (size + 2)*(2 * size) >= 1500:
        print(size)
        break
