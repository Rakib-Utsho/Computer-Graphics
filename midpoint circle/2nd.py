from matplotlib import pyplot as plt


def midPointCircle(x0, y0, r):
    if(x0<0):
        x0 = x0*(-1)
    if(y0<0):
        y0 = y0*(-1)
    x = 0
    y = r
    xlist = [0]
    ylist = [y]
    Oct1x = [x+x0]
    Oct1y = [y+y0]
    Oct2x = [y + y0]
    Oct2y = [x + x0]
    Oct3x = [y + y0]
    Oct3y = [-(x + x0)]
    Oct4x = [x + x0]
    Oct4y = [-(y + y0)]
    Oct5x = [-(x + x0)]
    Oct5y = [-(y + y0)]
    Oct6x = [-(y + y0)]
    Oct6y = [-(x + x0)]
    Oct7x = [-(y + y0)]
    Oct7y = [x + x0]
    Oct8x = [-(x + x0)]
    Oct8y = [y + y0]
    d = 1-r
    #print("d0",d)
    print("X= ", x+x0, end=" ")
    print("y= ", y+y0, end="\n")

    while (x < y):
        if (d < 0):
           # print("E")
            d = d+2*x+3
            x = x + 1
        else:
            #print("SE")
            d = d+(2*x)+5-(2*y)
            y = y - 1
            x = x + 1
        xlist.append(x)
        ylist.append(y)
        Oct1x.append(x+x0)
        Oct1y.append(y+y0)
        Oct2x.insert(0,y+y0)
        Oct2y.insert(0,x+x0)
        Oct3x.insert(0,y+y0)
        Oct3y.insert(0,-(x+x0))
        #matha amar noshto
        Oct4x.append(x+x0)
        Oct4y.append(-(y+y0))
        Oct5x.append(-(x+x0))
        Oct5y.append(-(y+y0))
        Oct6x.insert(0,-(y+y0))
        Oct6y.insert(0,-(x+x0))
        Oct7x.insert(0,-(y+y0))
        Oct7y.insert(0,x+x0)
        Oct8x.append(-(x+x0))
        Oct8y.append(y+y0)

        #print("d0=",d)
        print("X= ", x+x0, end=" ")
        print("y= ", y+y0, end="\n")

    print("Octant1-x",Oct3x)
    print("Octant1-y", Oct3y)
    #plt.plot(xlist, ylist, linestyle="--", marker="+", color="blue")
    plt.plot(Oct1x, Oct1y, linestyle="--", marker="+", color="blue")
    plt.plot(Oct2x, Oct2y, linestyle="--", marker="+", color="black")
    plt.plot(Oct3x, Oct3y, linestyle="--", marker="+", color="yellow")
    plt.plot(Oct4x, Oct4y, linestyle="--", marker="+", color="orange")
    plt.plot(Oct5x, Oct5y, linestyle="--", marker="+", color="olive")
    plt.plot(Oct6x, Oct6y, linestyle="--", marker="+", color="green")
    plt.plot(Oct7x, Oct7y, linestyle="--", marker="+", color="navy")
    plt.plot(Oct8x, Oct8y, linestyle="--", marker="+", color="red")
    plt.show()
# main
print("Enter circle center point:")
x0 = int(input())
y0 = int(input())
print("Enter radius of circle:")
r = int(input())


midPointCircle(x0, y0, r)