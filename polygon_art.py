import turtle
import random

def draw_polygon(num_sides, size, orientation, location, color, border_size):
    turtle.penup()
    turtle.goto(location[0], location[1])
    turtle.setheading(orientation)
    turtle.color(color)
    turtle.pensize(border_size)
    turtle.pendown()
    for _ in range(num_sides):
        turtle.forward(size)
        turtle.left(360/num_sides)
    turtle.penup()

def get_new_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

# draw a polygon at a random location, orientation, color, and border line thickness
num_sides = random.randint(3, 5) # triangle, square, or pentagon
size = random.randint(50, 150)
orientation = random.randint(0, 90)
location = [random.randint(-300, 300), random.randint(-200, 200)]
color = get_new_color()
border_size = random.randint(1, 10)
#draw_polygon(num_sides, size, orientation, location, color, border_size)

# specify a reduction ratio to draw a smaller polygon inside the one above
reduction_ratio = 0.618

# reposition the turtle and get a new location
turtle.penup()
turtle.forward(size*(1-reduction_ratio)/2)
turtle.left(90)
turtle.forward(size*(1-reduction_ratio)/2)
turtle.right(90)
location[0] = turtle.pos()[0]
location[1] = turtle.pos()[1]

# adjust the size according to the reduction ratio
size *= reduction_ratio
random_num = random.randint(20,30)
choice = input("Enter number 1-9: ")
match choice:
    case '1':
        for _ in range(random_num):
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = get_new_color()
            border_size = random.randint(1, 10)
            draw_polygon(3, size, orientation, location, color, border_size)
    case '2':
        for _ in range(random_num):
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = get_new_color()
            border_size = random.randint(1, 10)
            draw_polygon(4, size, orientation, location, color, border_size)
    case '3':
        for _ in range(random_num):
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = get_new_color()
            border_size = random.randint(1, 10)
            draw_polygon(5, size, orientation, location, color, border_size)
    case '4':
        for _ in range(random_num):
            num_sides = random.randint(3, 5) # triangle, square, or pentagon
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = get_new_color()
            border_size = random.randint(1, 10)
            draw_polygon(num_sides, size, orientation, location, color, border_size)
    case '5':
        for _ in range(random_num):
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = get_new_color()
            border_size = random.randint(1, 10)
            draw_polygon(3, size, orientation, location, color, border_size)
            turtle.penup()
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.right(90)
            location[0] = turtle.pos()[0]
            location[1] = turtle.pos()[1]
            size *= reduction_ratio
            draw_polygon(3, size, orientation, location, color, border_size)
            turtle.penup()
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.right(90)
            location[0] = turtle.pos()[0]
            location[1] = turtle.pos()[1]
            size *= reduction_ratio
            draw_polygon(3, size, orientation, location, color, border_size)
    case '6':
        for _ in range(random_num):
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = get_new_color()
            border_size = random.randint(1, 10)
            draw_polygon(4, size, orientation, location, color, border_size)
            turtle.penup()
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.right(90)
            location[0] = turtle.pos()[0]
            location[1] = turtle.pos()[1]
            size *= reduction_ratio
            draw_polygon(4, size, orientation, location, color, border_size)
            turtle.penup()
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.right(90)
            location[0] = turtle.pos()[0]
            location[1] = turtle.pos()[1]
            size *= reduction_ratio
            draw_polygon(4, size, orientation, location, color, border_size)
    case '7':
        for _ in range(random_num):
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = get_new_color()
            border_size = random.randint(1, 10)
            draw_polygon(5, size, orientation, location, color, border_size)
            turtle.penup()
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.right(90)
            location[0] = turtle.pos()[0]
            location[1] = turtle.pos()[1]
            size *= reduction_ratio
            draw_polygon(5, size, orientation, location, color, border_size)
            turtle.penup()
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.right(90)
            location[0] = turtle.pos()[0]
            location[1] = turtle.pos()[1]
            size *= reduction_ratio
            draw_polygon(5, size, orientation, location, color, border_size)
    case '8':
        for _ in range(random_num):
            num_sides = random.randint(3, 5)
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = get_new_color()
            border_size = random.randint(1, 10)
            draw_polygon(num_sides, size, orientation, location, color, border_size)
            turtle.penup()
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.right(90)
            location[0] = turtle.pos()[0]
            location[1] = turtle.pos()[1]
            size *= reduction_ratio
            draw_polygon(num_sides, size, orientation, location, color, border_size)
            turtle.penup()
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.right(90)
            location[0] = turtle.pos()[0]
            location[1] = turtle.pos()[1]
            size *= reduction_ratio
            draw_polygon(num_sides, size, orientation, location, color, border_size)
    case '9':
        for _ in range(random_num):
            random_gen = random.randint(0,1)
            if random_gen:
                num_sides = random.randint(3, 5)
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = get_new_color()
                border_size = random.randint(1, 10)
                draw_polygon(num_sides, size, orientation, location, color, border_size)
                turtle.penup()
                turtle.forward(size*(1-reduction_ratio)/2)
                turtle.left(90)
                turtle.forward(size*(1-reduction_ratio)/2)
                turtle.right(90)
                location[0] = turtle.pos()[0]
                location[1] = turtle.pos()[1]
                size *= reduction_ratio
                draw_polygon(num_sides, size, orientation, location, color, border_size)
                turtle.penup()
                turtle.forward(size*(1-reduction_ratio)/2)
                turtle.left(90)
                turtle.forward(size*(1-reduction_ratio)/2)
                turtle.right(90)
                location[0] = turtle.pos()[0]
                location[1] = turtle.pos()[1]
                size *= reduction_ratio
                draw_polygon(num_sides, size, orientation, location, color, border_size)
            else:
                num_sides = random.randint(3, 5) # triangle, square, or pentagon
                size = random.randint(50, 150)
                orientation = random.randint(0, 90)
                location = [random.randint(-300, 300), random.randint(-200, 200)]
                color = get_new_color()
                border_size = random.randint(1, 10)
                draw_polygon(num_sides, size, orientation, location, color, border_size)
    case _:
        print("invalid input")
# draw the second polygon embedded inside the original 
#draw_polygon(num_sides, size, orientation, location, color, border_size)

# hold the window; close it by clicking the window close 'x' mark
turtle.done()