# matplotlib_intro.py
"""Python Essentials: Intro to Matplotlib.
Leah Holmes
MTH 420 - Applied Mathematics
05/05/2022
"""
from cmath import sin
import numpy as np
import matplotlib.pyplot as plt

# Problem 1
def var_of_means(n):
    """Construct a random matrix A with values drawn from the standard normal
    distribution. Calculate the mean value of each row, then calculate the
    variance of these means. Return the variance.

    Parameters:
        n (int): The number of rows and columns in the matrix A.

    Returns:
        (float) The variance of the means of each row.
    """
    n = int(n)
    A = np.random.normal(3,2.5, size = (n,n)) 
    A_mean = np.mean(A,axis = 1)
    A_var = np.var(A_mean)
    return A_var

    # raise NotImplementedError("Problem 1 Incomplete")

def prob1():
    """Create an array of the results of var_of_means() with inputs
    n = 100, 200, ..., 1000. Plot and show the resulting array.
    """
    x = np.arange(100,1000,100)
    y = np.array([var_of_means(n) for n in x])
    plt.plot(x,y,'--',color = 'black')
    plt.plot(x,y,'ro')
    plt.xlabel('n')
    plt.ylabel('var(mean(A))')
    plt.show()
    # raise NotImplementedError("Problem 1 Incomplete")

# Problem 2
def prob2():
    """Plot the functions sin(x), cos(x), and arctan(x) on the domain
    [-2pi, 2pi]. Make sure the domain is refined enough to produce a figure
    with good resolution.
    """
    # raise NotImplementedError("Problem 2 Incomplete")
    dx = 0.01
    x = np.arange(-2*np.pi,2*np.pi+dx,dx)
    plt.plot(x,np.sin(x),color = 'blue',label = 'sin(x)')
    plt.plot(x,np.cos(x), color = 'orange',label = 'cos(x)')
    plt.plot(x,np.arctan(x), color = 'lime',label = 'arctan(x)')
    plt.xlabel('x')
    plt.ylabel('F(x)')
    plt.legend()
    plt.show()


# Problem 3
def prob3():
    """Plot the curve f(x) = 1/(x-1) on the domain [-2,6].
        1. Split the domain so that the curve looks discontinuous.
        2. Plot both curves with a thick, dashed magenta line.
        3. Set the range of the x-axis to [-2,6] and the range of the
           y-axis to [-6,6].
    """
    steps =1000
    dx = (8/steps)
    x = np.linspace(-2,6,steps)
    f = 1/(x-1)
    print(x[-1])
    plt.plot(x[(x < 1)],f[(x < 1)],'m--',markersize = 4)
    plt.plot(x[(x > 1)],f[(x > 1)],'m--',markersize = 4)
    plt.ylim([-6,6])
    plt.xlim([-2,6])
    plt.xlabel('x')
    plt.ylabel('1/(x-1)')
    plt.show()
    # raise NotImplementedError("Problem 3 Incomplete")



# Problem 4
def prob4():
    """Plot the functions sin(x), sin(2x), 2sin(x), and 2sin(2x) on the
    domain [0, 2pi].
        1. Arrange the plots in a square grid of four subplots.
        2. Set the limits of each subplot to [0, 2pi]x[-2, 2].
        3. Give each subplot an appropriate title.
        4. Give the overall figure a title.
        5. Use the following line colors and styles.
              sin(x): green solid line.
             sin(2x): red dashed line.
             2sin(x): blue dashed line.
            2sin(2x): magenta dotted line.
    """
    # raise NotImplementedError("Problem 4 Incomplete")
    x = np.arange(0,2*np.pi,0.01)
    fig = plt.figure(figsize=(8,6))
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)
    ax4 = fig.add_subplot(224)
    ax1.plot(x,np.sin(x), color = 'green')
    ax2.plot(x,np.sin(2*x),'--', color = 'red')
    ax3.plot(x,2*np.sin(x),'--', color = 'green')
    ax4.plot(x,2*np.sin(2*x),'.',color = 'magenta')
    ax1.set_xlim([0,2*np.pi])
    ax2.set_xlim([0,2*np.pi])
    ax3.set_xlim([0,2*np.pi])
    ax4.set_xlim([0,2*np.pi])
    ax1.set_ylim([-2,2])
    ax2.set_ylim([-2,2])
    ax3.set_ylim([-2,2])
    ax4.set_ylim([-2,2])
    ax1.set_title('original')
    ax2.set_title('T/2')
    ax3.set_title('2A')
    ax4.set_title('2A and T/2')
    fig.suptitle('sin(x)')
    plt.show()

# Problem 5
def prob5():
    """Visualize the data in FARS.npy. Use np.load() to load the data, then
    create a single figure with two subplots:
        1. A scatter plot of longitudes against latitudes. Because of the
            large number of data points, use black pixel markers (use "k,"
            as the third argument to plt.plot()). Label both axes.
        2. A histogram of the hours of the day, with one bin per hour.
            Label and set the limits of the x-axis.
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def prob6():
    """Plot the function f(x,y) = sin(x)sin(y)/xy on the domain
    [-2pi, 2pi]x[-2pi, 2pi].
        1. Create 2 subplots: one with a heat map of f, and one with a contour
            map of f. Choose an appropriate number of level curves, or specify
            the curves yourself.
        2. Set the limits of each subplot to [-2pi, 2pi]x[-2pi, 2pi].
        3. Choose a non-default color scheme.
        4. Add a colorbar to each subplot.
    """
    # raise NotImplementedError("Problem 6 Incomplete")
    x = np.arange(-2*np.pi,2*np.pi,0.01)
    y = x.copy()
    fig = plt.figure(figsize=(8,4))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    X,Y = np.meshgrid(x,y)
    Z = np.sin(X)*np.sin(Y)/(x*y)
    c1 = ax1.pcolormesh(X,Y,Z, cmap = 'plasma')
    c2 = ax2.contourf(X,Y,Z, cmap = 'plasma')
    # ax1.colorbar(c1)
    # ax2.colorbar(c2)
    ax2.plot(x,np.sin(2*x),'--', color = 'red')
    ax1.set_xlim([-2*np.pi,2*np.pi])
    ax2.set_xlim([-2*np.pi,2*np.pi])
    ax1.set_ylim([-2*np.pi,2*np.pi])
    ax2.set_ylim([-2*np.pi,2*np.pi])
    plt.show()

prob6()

