import matplotlib.pyplot as plt

def draw_circle(center_x, center_y, radius):
    # Initialize variables
    x = radius - 1
    y = 0
    dx = 1
    dy = 1
    err = dx - (radius << 1)

    # Plot initial points
    plt.plot(center_x + x, center_y + y, 'bo')
    plt.plot(center_x - x, center_y + y, 'bo')
    plt.plot(center_x + x, center_y - y, 'bo')
    plt.plot(center_x - x, center_y - y, 'bo')

    # Plot remaining points using the midpoint circle algorithm
    while x >= y:
        y += 1
        if err < 0:
            err += dy
            dy += 2
        else:
            x -= 1
            dx += 2
            err += dx - (radius << 1)
        plt.plot(center_x + x, center_y + y, 'bo')
        plt.plot(center_x - x, center_y + y, 'bo')
        plt.plot(center_x + x, center_y - y, 'bo')
        plt.plot(center_x - x, center_y - y, 'bo')
        if x != y:
            plt.plot(center_x + y, center_y + x, 'bo')
            plt.plot(center_x - y, center_y + x, 'bo')
            plt.plot(center_x + y, center_y - x, 'bo')
            plt.plot(center_x - y, center_y - x, 'bo')

    # Show plot
    plt.show()

# Get input from user
center_x = int(input("Enter the center x-coordinate: "))
center_y = int(input("Enter the center y-coordinate: "))
radius = int(input("Enter the radius: "))

# Call function to draw circle
draw_circle(center_x, center_y, radius)