from matplotlib import pyplot as plt
def DDA(x0,y0,x1,y1):
    dx=abs(x1-x0)
    dy=abs(y1-y0)
    m=dy/dx
    steps=max(dx,dy)
    xlist=[]
    ylist=[]
    print(steps)
    for i in range(steps):
        if m<1:
            x0=x0+1
            y0=y0+m
        elif m==1:
            x0=x0+1
            y0=y0+1
        elif m>1:
            x0=x0+1/m
            y0=y0+1

        x0=round(x0,2)
        y0=round(y0,2)
        print("x=",x0, end=", ")
        print("y=",y0, end="\n")

        xlist.append(x0)
        ylist.append(y0)
    plt.plot(xlist,ylist,linestyle="--",marker="+")
    plt.show()

#main()
print("Insert Starting Coordinate")
x0=int(input())
y0=int(input())
print("Insert n Coordinate")
x1=int(input())
y1=int(input())
DDA(x0,y0,x1,y1)
