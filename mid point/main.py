from matplotlib import pyplot as plt


def midPointLine(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    x = x0
    y = y0
    xList = [x]
    yList = [y]
    d = dy - (dx / 2)
    print("x= ", x, end=" ")
    print("y= ", y, end="\n")
    while (x < x1):
        x = x + 1
        if (d < 0):
            d = d + dy
        else:
            d = d + dy - dx
            y = y + 1
        xList.append(x)
        yList.append(y)
        print("x= ", x, end=" ")
        print("y= ", y, end="\n")
    plt.plot(xList, yList, linestyle="--", marker="+", color="blue")
    plt.show()


# main
x0 = int(input("Enter first point of x: "))
y0 = int(input("Enter first point of y: "))
x1 = int(input("Enter end point of x: "))
y1 = int(input("Enter end point of x: "))
midPointLine(x0, y0, x1, y1)