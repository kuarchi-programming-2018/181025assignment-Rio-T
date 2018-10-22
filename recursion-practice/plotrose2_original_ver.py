#正７角形を表示したいのですが上手く表示されません。
#どこが間違っているのかも分かりませんTT

from turtle import *
from rose2 import *
import math
hideturtle()
pi=math.pi
cos=math.cos
sin=math.cos
rose_window_recursion(
        [[70*cos(2*pi/7),70*sin(2*pi/7)],
         [70*cos(4*pi/7),70*sin(4*pi/7)],         
         [70*cos(6*pi/7),70*sin(6*pi/7)],
         [70*cos(8*pi/7),70*sin(8*pi/7)],
         [70*cos(10*pi/7),70*sin(10*pi/7)],
         [70*cos(12*pi/7),70*sin(12*pi/7)],
         [70*cos(14*pi/7),70*sin(14*pi/7)]],0.1,50)
done()