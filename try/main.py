from graphics import *
import math
def func(x,y):
    p=[x , y]
    a = (x)
    b = (y+100)
    q =[a,b]
    dis = (math.sqrt( ((p[0]-q[0])**2)+((p[1]-q[1])**2) ))
    print(dis)
    centerX = (x+a)/2
    centerY = (y+b)/2
    win=GraphWin("myWindow", 500, 500)
    win.setBackground(color_rgb(255,255,255))

    pt2=Point(a,b)
    p3=centerX-(dis/2)
    p4=centerX+(dis/2)
    pt3 = Point(centerX-dis,centerY-50)
    pt4 = Point(centerX+dis,centerY-50)
    pt5 = Point(p3,centerY-80)
    pt6 = Point(p4,centerY-80)

    #line
    ln1 = Line(pt4, pt6)
    ln2 = Line(pt4, pt2)
    ln3 = Line(pt2,pt3)
    ln4 = Line(pt3, pt5)
    ln5 = Line(pt5,pt6)
    ln1.setWidth(8)
    ln1.setOutline(color_rgb(0,0,0))
    ln2.setWidth(8)
    ln2.setOutline(color_rgb(150, 0, 0))
    ln3.setWidth(8)
    ln3.setOutline(color_rgb(0, 100, 80))
    ln4.setWidth(8)
    ln4.setOutline(color_rgb(90, 0, 150))
    ln5.setWidth(8)
    ln5.setOutline(color_rgb(255, 255, 0))
    ln1.draw(win)
    ln2.draw(win)
    ln3.draw(win)
    ln4.draw(win)
    ln5.draw(win)
    win.getMouse()
    win.close()

print("Enter coordinates ")
x = int(input())
y = int(input())
func(x,y)