from graphics import *


def main():
    win = GraphWin("CSE 342", 500, 500)
    win.setBackground(color_rgb(180, 220, 120))

    pt1 = Point(200, 200)
    cir = Circle(pt1, 80)
    cir.setWidth(5)
    cir.setOutline(color_rgb(100, 140, 250))
    cir.setFill(color_rgb(180, 125, 240))
    cir.draw(win)
    # line 1
    ln1 = Line(Point(120, 200), Point(280, 200))
    ln1.setFill(color_rgb(140, 190, 150))
    ln1.setWidth(5)
    ln1.draw(win)

    # line 2
    ln2 = Line(Point(200, 120), Point(200, 280))
    ln2.setFill(color_rgb(140, 190, 150))
    ln2.setWidth(5)
    ln2.draw(win)

    # Ploygon
    tri = Polygon(Point(25, 25), Point(100, 100), Point(25, 100))
    tri.setFill(color_rgb(180, 180, 200))
    tri.draw(win)
    # image
    img = Image(Point(350, 350), "dora2.png")
    img.draw(win)

    win.getMouse()
    win.close()


main()