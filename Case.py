# Case-study #1
# Developer: Gerashchenko A.

import turtle

def square(x, y, a, color):
    '''
    Function to draw a square
    :param x: upper left corner x coordinate
    :param y: upper left corner y coordinate
    :param a: side length of a square
    :param color: color of the square
    :return: None
    '''
    turtle.up()
    turtle.setheading(0)
    turtle.goto(x, y)
    turtle.color(color)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.end_fill()

def triangle (x,y,a, color):
    '''
    Function to draw a triangle
    :param x: the vertex of the triangle x coordinate
    :param y: the vertex of the triangle y coordinate
    :param a: the side length of the triangle
    :param color: color of the triangle
    :return: None
    '''
    turtle.up()
    turtle.setheading(0)
    turtle.goto(x,y)
    turtle.color(color)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(120)
    turtle.end_fill()

def triangle_2(x,y,a,b,color):
    '''
    Function to draw a triangle
    :param x: the vertex of the triangle x coordinate
    :param y: the vertex of the triangle y coordinate
    :param a: the side length of the triangle
    :param b: the side length of the triangle
    :param color: color of the triangle
    :return: None
    '''
    turtle.up()
    turtle.setheading(0)
    turtle.goto(x,y)
    turtle.color(color)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    turtle.goto(x,y)
    turtle.end_fill()

def circle (x,y,r, color):
    '''
    Function to draw a circle
    :param x: center of the circle x coordinate
    :param y: center of the circle y coordinate
    :param r: the radius of the circle
    :param color: color of the circle
    :return:None
    '''
    turtle.up()
    turtle.setheading(0)
    turtle.goto(x, y)
    turtle.color(color)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

def rhomb(x,y,a, color):
    '''
    Function to draw a rhomb
    :param x: upper corner of the rhomb x coordinate
    :param y: upper corner of the rhomb y coordinate
    :param a: side length of the rhomb
    :param color: color of the rhomb
    :return: None
    '''
    turtle.up()
    turtle.setheading(-60)
    turtle.goto(x, y)
    turtle.color(color)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(a)
    turtle.right (120)
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(a)
    turtle.right(120)
    turtle.end_fill()

def rectangle (x,y,a,b, color):
    '''
    Function to draw a rectangle
    :param x: upper left corner x coordinate
    :param y: upper left corner y coordinate
    :param a: the side length of the rectangle
    :param b: the side length of the rectangle
    :param color: color of the rectangle
    :return: None
    '''
    turtle.up()
    turtle.setheading(0)
    turtle.goto(x, y)
    turtle.color(color)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(b)
    turtle.end_fill()

def parallelogram (x,y,a,b, color):
    '''
    Function to draw a parallelogram
    :param x: upper left corner x coordinate
    :param y: upper left corner y coordinate
    :param a: the side length of the parallelogram
    :param b: the side length of the parallelogram
    :param color: color of the parallelogram
    :return: None
    '''
    turtle.up()
    turtle.setheading(0)
    turtle.goto(x, y)
    turtle.color(color)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(b)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(b)
    turtle.right(120)
    turtle.end_fill()

def parallelogram_2 (x,y,a,b, color):
    '''
    Function to draw a parallelogram
    :param x: upper left corner x coordinate
    :param y: upper left corner y coordinate
    :param a: the side length of the parallelogram
    :param b: the side length of the parallelogram
    :param color: color of the parallelogram
    :return: None
    '''
    turtle.up()
    turtle.setheading(90)
    turtle.goto(x, y)
    turtle.color(color)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(b)
    turtle.right(120)
    turtle.forward(a)
    turtle.right(60)
    turtle.forward(b)
    turtle.right(120)
    turtle.end_fill()

def parallelogram_3 (x,y,a,b, color):
    '''
    Function to draw a parallelogram
    :param x: upper left corner x coordinate
    :param y: upper left corner y coordinate
    :param a: the side length of the parallelogram
    :param b: the side length of the parallelogram
    :param color: color of the parallelogram
    :return: None
    '''
    turtle.up()
    turtle.setheading(90)
    turtle.goto(x, y)
    turtle.color(color)
    turtle.down()
    turtle.begin_fill()
    turtle.forward(a)
    turtle.left(60)
    turtle.forward(b)
    turtle.left(120)
    turtle.forward(a)
    turtle.left(60)
    turtle.forward(b)
    turtle.left(120)
    turtle.end_fill()

def main():
    turtle.speed(0)

    parallelogram(0,0,100,50, 'blue')
    triangle(101,0, 50, 'green')
    rectangle(85,125, 15,125, 'brown')
    triangle_2(65,125,20, -20, 'orange')
    rhomb(25,26, 15, 'black')
    circle(40,-30,10, 'skyblue')
    circle(75, -30, 10, 'yellow')
    circle(110, -30, 10, 'grey')
    circle(25,11, 8, 'pink')
    parallelogram(40,125,30,20, 'lightgrey')

    rectangle(-200, 0, 100, 50, 'black')
    circle(-175, -25, 6, 'yellow')
    circle(-125, -25, 6, 'yellow')
    triangle_2(-200, 1, 20, 30, 'black')
    triangle_2(-100, 1, -20, 30, 'black')
    rhomb(-150, -25, 10, 'orange')
    triangle(-200, -50, 100, 'grey')
    parallelogram_3(-100, -100, 25, 35, 'lightgrey')
    parallelogram_2(-200, -100, 25, 35, 'lightgrey')

    square(200, 50, 100, 'sienna')
    square(230,25,40 , 'skyblue')
    triangle(300,51,-100,'crimson')
    rectangle(275,126, 20, 30, 'black')
    triangle(275,95, 20,'black')
    circle(250, 75,7, 'skyblue')
    rectangle(300,-40,20,10, 'brown')
    square(300,-30,10,'brown')
    parallelogram(301,50,25,15,'orange')
    triangle_2(310,37,-10,13, 'grey')

    rectangle(0,-200,120,40,'lightgrey')
    triangle_2(-41,-240,40,40, 'grey')
    parallelogram_2(120,-240,40,30,'darkblue')
    triangle_2(30,-200,30,30,'blue')
    triangle_2(30,-240,30,-30,'blue')
    circle(20,-230,10, 'skyblue')
    rhomb(100,-240,10,'black')
    rhomb(110,-240,10,'black')

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
