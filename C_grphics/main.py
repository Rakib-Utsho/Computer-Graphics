from graphics import *
def main():
    win = GraphWin("CSE 342", 500, 500)
    win.setBackground(color_rgb(180,220,120))

    pt1= Point(350,100)
    cir = Circle(pt1,80)
    cir.setWidth(5)
    cir.setOutline(color_rgb(100,140,250))
    cir.setFill(color_rgb(180,125,240))
    cir.draw(win)
#line 1
    ln1 = Line(Point(270,100),Point(430,100))
    ln1.setFill(color_rgb(140,190,150))
    ln1.setWidth(5)
    ln1.draw(win)

#line 2
    ln2 = Line(Point(350,20),Point(350,180))
    ln2.setFill(color_rgb(140, 190, 150))
    ln2.setWidth(5)
    ln2.draw(win)

#Ploygon
    tri = Polygon(Point(75, 75),Point(200,200),Point(75,200))
    tri.setFill(color_rgb(180,180,200))
    tri.setWidth(5)
    tri.draw(win)
#image
    img = Image(Point(250,350),"sin.png")
    img.draw(win)

    win.getMouse()
    win.close()
main()