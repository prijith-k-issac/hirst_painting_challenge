#
# import colorgram
#
# color_list = colorgram.extract('img.jpg', 100)
# color_pallette = []
# for item in color_list:
#     red = item.rgb.r
#     green = item.rgb.g
#     blue = item.rgb.b
#     if red < 240 and green < 240 and blue < 240:
#         color_pallette.append((red, green, blue))

color_collection = [ (166, 155, 146), (40, 76, 181), (82, 234, 200), \
                    (12, 37, 172), (237, 168, 163), (68, 199, 224), (173, 178, 231), (209, 72, 16), \
                    (84, 85, 212), (212, 5, 4), (52, 7, 4), (216, 138, 195), (247, 234, 41), (205, 246, 233), \
                    (65, 232, 241), (238, 227, 5), (237, 155, 216), (246, 212, 235), (18, 150, 22), \
                    (6, 245, 223), (240, 16, 16), (229, 17, 121), (214, 6, 83), (11, 227, 239), (10, 29, 59), \
                    (104, 197, 148), (10, 79, 112), (236, 43, 145), (221, 85, 58), (29, 216, 64), (10, 97, 61), \
                    (1, 67, 31), (16, 54, 243), (247, 9, 42), (73, 9, 31), (228, 153, 20)]
from random import choice
from turtle import Turtle, Screen
t = Turtle()
s = Screen()
po = t.pos()
t.penup()
t.hideturtle()
h = 50
t.setpos(-250, -220)
s.colormode(255)
for y_axis in range(10):

    for x_axis in range(10):
        t.dot(20, choice(color_collection))
        t.forward(50)
    t.setpos(-250, (-220+h))
    h += 50
s.exitonclick()

