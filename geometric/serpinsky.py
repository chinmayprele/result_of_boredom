import turtle
PROGNAME = 'Sierpinski Triangle'
#Credits: This code was written by editing the code from http://www.lpb-riannetrujillo.com/blog/python-fractal/

myPen = turtle.Turtle()
myPen.ht()
myPen.speed(10)
myPen.pencolor('black')
window = turtle.Screen()
window.setup(width=2880, height=1800, startx=10, starty=0.5)

points = [[-175,-125],[0,175],[175,-125]] #size of triangle

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2) #find midpoint

def triangle(points,depth):

    myPen.up()
    myPen.goto(points[0][0],points[0][1])
    myPen.down()
    myPen.goto(points[1][0],points[1][1])
    myPen.goto(points[2][0],points[2][1])
    myPen.goto(points[0][0],points[0][1])

    if depth>0:
        triangle([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   depth-1)
        triangle([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   depth-1)
        triangle([points[2],
                         getMid(points[2], points[1]),
                         getMid(points[0], points[2])],
                   depth-1)


triangle(points,4)
