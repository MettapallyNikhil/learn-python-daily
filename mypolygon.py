# Case study: interface design
# 4.1 The turtle module
# import turtle
# bob = turtle.Turtle()

# bob.fd(100)
# bob.lt(90)
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)
# bob.lt(90)
# print(bob)
# turtle.mainloop()

# 4.2 Simple repetition 

# for i in range(4):
#     print('Hello!')

# Drawing a square using a for loop

# import turtle
# bob = turtle.Turtle()
# for i in range(4)
#     bob.fd(100)
#     bob.lt(90)
# turtle.mainloop()

# 4.3 Exercises - using the turtle module.
# 1. Write a function called square that takes a parameter named t, which is a turtle. It
# should use the turtle to draw a square.
# Write a function call that passes bob as an argument to square, and then run the program again.
# import turtle
# bob = turtle.Turtle()
# def square(t):
#     for i in range(4):
#         t.fd(100)
#         t.lt(90)
# square(bob) 
# turtle.mainloop()

# 2. Add another parameter, named length, to square. 
# Modify the body so length of the sides is length, and then modify the function call to provide a second argument. 
# Run the program again. 
# Test your program with a range of values for length.

# import turtle
# bob = turtle.Turtle()
# def square(t, length):
#     for i in range(4):
#         t.fd(length)
#         t.lt(90)
# square(bob, -150) 
# turtle.mainloop()

# 3. Make a copy of square and change the name to polygon. Add another parameter
# named n and modify the body so it draws an n-sided regular polygon. Hint: The
# exterior angles of an n-sided regular polygon are 360/n degrees.

# import turtle
# bob = turtle.Turtle()
# def polygon(t, length, n):
#     for i in range(n):
#         t.fd(length)
#         t.lt(360/n)
# polygon(bob, 150, 5) 
# turtle.mainloop()

# 4. Write a function called circle that takes a turtle, t, and radius, r, as parameters and
# that draws an approximate circle by calling polygon with an appropriate length and
# number of sides. Test your function with a range of values of r.
# Hint: figure out the circumference of the circle and make sure that length * n =
# circumference.

# import turtle
# bob = turtle.Turtle()
# def circle(t, r):
#     # Calculate the number of sides for the polygon
#     n = 25
#     # Calculate the length of each side
#     length = 2 * r * 3.14159 / n
#     for i in range(n):
#         t.fd(length)
#         t.lt(360/n)
# circle(bob, 100) 
# turtle.mainloop()

# import turtle
# import math

# bob = turtle.Turtle()

# def polygon(t, length, n):
#     for i in range(n):
#         t.fd(length)
#         t.lt(360 / n)

# def circle(t, r):
#     circumference = 2 * math.pi * r
#     n = int(circumference / 3) + 3
#     length = circumference / n
#     polygon(t, length, n)

# circle(bob, 100)
# turtle.mainloop()

# 5. Make a more general version of circle called arc that takes an additional parameter angle,  
# which determines what fraction of a circle to draw. angle is in units of degrees,
# so when angle=360, arc should draw a complete circle.
# import turtle
# bob = turtle.Turtle()
# def arc(t, r, angle):
#     # Calculate the number of sides for the polygon
#     n = 100
#     # Calculate the length of each side
#     length = 2 * r * 3.14159 / n
#     # Calculate the angle of each turn
#     turn_angle = 360 / n
#     # Draw the arc
#     for i in range(int(angle / turn_angle)):
#         t.fd(length)
#         t.lt(turn_angle)

# arc(bob, 100, 180)
# turtle.mainloop()

# import turtle
# bob = turtle.Turtle()

# def polyline(t, n, length, angle):
#     """Draws n line segments with the given length and angle between them."""
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)

# polyline(bob, 100, 180, 180)
# turtle.mainloop()

