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

# Exercise 4.1. 

# 1. Draw a stack diagram that shows the state of the program while executing 
# circle(bob,radius). You can do the arithmetic by hand or add print statements to the code.

# import turtle
# import math
# bob = turtle.Turtle()

# def polygon(t, length, n):
#     print("---- POLYGON FRAME ----")
#     print("t =", t)
#     print("length =", length)
#     print("n =", n)
#     for i in range(n):
#         print("i =", i)
#         t.fd(length)
#         t.lt(360 / n)

# def circle(t, r):
#     print("---- CIRCLE FRAME ----")
#     print("t =", t)
#     print("r =", r)
#     circumference = 2 * math.pi * r
#     print("circumference =", circumference)
#     n = int(circumference / 3) + 3
#     print("n =", n)
#     length = circumference / n
#     print("length =", length)
#     polygon(t, length, n)

# circle(bob, 100)
# turtle.mainloop()

# 2. The version of arc in Section 4.7 is not very accurate because the linear approximation of the
# circle is always outside the true circle. As a result, the Turtle ends up a few pixels away from
# the correct destination. My solution shows a way to reduce the effect of this error. Read the
# code and see if it makes sense to you. If you draw a diagram, you might see how it works.

# import turtle
# import math
# def arc(t, r, angle):
#     arc_length = 2 * math.pi * r * angle / 360
#     n = int(arc_length / 3) + 1
#     step_length = arc_length / n
#     step_angle = angle / n
#     for i in range(n):
#         t.fd(step_length)
#         t.lt(step_angle)

# def circle(t, r):
#     arc(t, r, 360)

# bob = turtle.Turtle()
# circle(bob, 100)
# turtle.mainloop()

# # Exercise 4.2. 

# # Write an appropriately general set of functions that can draw flowers
# from __future__ import print_function, division
# import math
# import turtle

# def polyline(t, n, length, angle):
#     """Draws n line segments.
#     t: Turtle
#     n: number of line segments
#     length: length of each segment
#     angle: degrees to turn after each segment
#     """
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)

# def arc(t, r, angle):
#     """Draws an arc with the given radius and angle.
#     t: Turtle
#     r: radius
#     angle: angle subtended by the arc, in degrees
#     """
#     arc_length = 2 * math.pi * r * abs(angle) / 360
#     n = int(arc_length / 3) + 1
#     step_length = arc_length / n
#     step_angle = float(angle) / n
#     polyline(t, n, step_length, step_angle)

# def circle(t, r):
#     """Draws a circle with the given radius.
#     t: Turtle
#     r: radius
#     """
#     arc(t, r, 360)

# def petal(t, r, angle):
#     """Draws a petal using two arcs.
#     t: Turtle
#     r: radius of the arcs
#     angle: angle (degrees) that subtends the arcs
#     """
#     for i in range(2):
#         arc(t, r, angle)
#         t.lt(180 - angle)

# def flower(t, n, r, angle):
#     """Draws a flower with n petals.
#     t: Turtle
#     n: number of petals
#     r: radius of the arcs
#     angle: angle (degrees) that subtends the arcs
#     """
#     for i in range(n):
#         petal(t, r, angle)
#         t.lt(360.0 / n)

# def move(t, length):
#     """Moves the turtle forward without leaving a trail.
#     t: Turtle
#     length: distance to move
#     The pen is left down after the movement.
#     """
#     t.penup()
#     t.forward(length)
#     t.pendown()

# # Create turtle
# bob = turtle.Turtle()
# # Draw three flowers
# move(bob, -100)
# flower(bob, 7, 60.0, 60.0)
# move(bob, 100)
# flower(bob, 10, 40.0, 80.0)
# move(bob, 100)
# flower(bob, 20, 140.0, 20.0)
# # Hide turtle and keep window open
# bob.hideturtle()
# turtle.mainloop()

# # Exercise 4.3. 
# # Write an appropriately general set of functions that can draw shapes

# from __future__ import print_function, division
# import math
# import turtle

# def draw_pie(t, n, r):
#     """Draws a pie, then moves into position to the right.
#     t: Turtle
#     n: number of segments
#     r: length of the radial spokes
#     """
#     polypie(t, n, r)
#     t.pu()
#     t.fd(r*2 + 10)
#     t.pd()

# def polypie(t, n, r):
#     """Draws a pie divided into radial segments.
#     t: Turtle
#     n: number of segments
#     r: length of the radial spokes
#     """
#     angle = 360.0 / n
#     for i in range(n):
#         isosceles(t, r, angle/2)
#         t.lt(angle)

# def isosceles(t, r, angle):
#     """Draws an icosceles triangle.
#     The turtle starts and ends at the peak, facing the middle of the base.
#     t: Turtle
#     r: length of the equal legs
#     angle: half peak angle in degrees
#     """
#     y = r * math.sin(angle * math.pi / 180)
#     t.rt(angle)
#     t.fd(r)
#     t.lt(90+angle)
#     t.fd(2*y)
#     t.lt(90+angle)
#     t.fd(r)
#     t.lt(180-angle)

# bob = turtle.Turtle()
# bob.pu()
# bob.bk(130)
# bob.pd()

# # draw polypies with various number of sides
# size = 40
# draw_pie(bob, 5, size)
# draw_pie(bob, 6, size)
# draw_pie(bob, 7, size)
# draw_pie(bob, 8, size)

# bob.hideturtle()
# turtle.mainloop()

# Exercise 4.4. 

# The letters of the alphabet can be constructed from a moderate number of basic elements, 
# like vertical and horizontal lines and a few curves. Design an alphabet that can be drawn
# with a minimal number of basic elements and then write functions that draw the letters.

# from __future__ import print_function, division
# import string
# import turtle


# """
# To use this typewriter, you have to provide a module named letters.py
# that contains functions with names like draw_a, draw_b, etc.
# """

# # check if the reader has provided letters.py
# try:
#     import letters
# except ImportError as e:
#     message = e.args[0]
#     if message.startswith('No module'):
#         raise ImportError(message + 
#                           '\nYou have to provide a module named letters.py')


# def teleport(t, x, y):
#     """Moves the turtle without drawing a line.

#     Postcondition: pen is down

#     t: Turtle
#     x: coordinate
#     y: coordinate
#     """
#     t.pu()
#     t.goto(x, y)
#     t.pd()


# def keypress(char):
#     """Handles the event when a user presses a key.

#     Checks if there is a function with the right name; otherwise
#     it prints an error message.

#     char: string, letter to draw
#     """
#     # if we're still drawing the previous letter, bail out
#     if bob.busy:
#         return
#     else:
#         bob.busy = True

#     # figure out which function to call, and call it
#     try:
#         name = 'draw_' + char
#         func = getattr(letters, name)
#     except AttributeError:
#         print("I don't know how to draw an", char)
#         bob.busy = False
#         return

#     func(bob, size)

#     letters.skip(bob, size/2)
#     bob.busy = False


# def carriage_return():
#     """Moves to the beginning of the next line.
#     """
#     teleport(bob, -180, bob.ycor() - size*3)
#     bob.busy = False


# def presser(char):
#     """Returns a function object that executes keypress.

#     char: character to draw when the function is executed

#     returns: function with no arguments
#     """
#     def func():
#         keypress(char)
#     return func


# # create and position the turtle
# size = 20
# bob = turtle.Turtle()
# bob.busy = False
# teleport(bob, -180, 150)

# # tell world to call keypress when the user presses a key
# screen = bob.getscreen()

# for char in string.ascii_lowercase:
#     screen.onkey(presser(char), char)

# screen.onkey(carriage_return, 'Return')
# screen.listen()
# turtle.mainloop()

# Spiral

# from __future__ import print_function, division
# import turtle

# def draw_spiral(t, n, length=3, a=0.1, b=0.0002):
#     """Draws an Archimedian spiral starting at the origin.
#     Args:
#       n: how many line segments to draw
#       length: how long each segment is
#       a: how loose the initial spiral starts out (larger is looser)
#       b: how loosly coiled the spiral is (larger is looser)
#     http://en.wikipedia.org/wiki/Spiral
#     """
#     theta = 0.0

#     for i in range(n):
#         t.fd(length)
#         dtheta = 1 / (a + b * theta)
#         t.lt(dtheta)
#         theta += dtheta

# # create the world and bob
# bob = turtle.Turtle()
# draw_spiral(bob, n=1000)
# turtle.mainloop()

# # 5.1 Floor division and modulus
# a = 17
# b = 5
# print(a // b)  # floor division
# print(a % b)   # modulus

# # A movie is 143 minutes long.
# a = 143
# print(a//60)  # number of hours
# print(a%60)   # number of minutes

# # Divisibility
# x = 20
# print(x % 4)
# print(x % 3)

# # Find the Last Digit
# x = 738
# print(x % 10)

# # Last Two Digits
# x = 738
# print(x % 100)

# # Split a number
# seconds = 367
# minutes = seconds // 60
# remaining_seconds = seconds % 60
# print("Minutes:", minutes)
# print("Remaining Seconds:", remaining_seconds)

# # Split a number
# number = 947
# last_digit = number % 10
# last_two_digits = number % 100
# complete_groups_of_100 = number // 100
# remaining_after_groups = number % 100
# print("Last Digit:", last_digit)
# print("Last Two Digits:", last_two_digits)
# print("Complete Groups of 100:", complete_groups_of_100)
# print("Remaining After Groups of 100:", remaining_after_groups)

# 5.2 Boolean expressions (gives either True or False)

# print(10 == 10)
# print(type(10) == type(10.0))

# print(10 != 10)

# x = 15
# print(x > 10)

# x = 15
# print(x < 10)

# x = 10
# print(x >= 10)

# x = 8
# print(x <= 10)

# x = 20
# print(x == 20)
# print(x != 20)
# print(x > 15)
# print(x < 15)

# a = 25
# b = 30
# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= 25)
# print(b <= 30)

# 5.3 Logical operators  and, or, not
 
# x = 5
# print(x > 0 and x < 10)

# x = 15
# print(x < 10 or x == 15)

# x = 8
# print(not x > 10)

# x = 12
# print(x > 10 and x < 20)

# x = 7
# print(x < 5 or x > 10)

# x = 20
# print(not (x == 20))

# x = 12
# print(x > 5 and x < 10 or x == 12)

# x = 18
# print((x > 10 and x < 20) or x == 5)

# x = 15
# print(not (x < 10 or x > 20))

# # 5.4 Conditional execution
# x = 10
# y = 20
# if x > 0:
#     print('x is positive')

# # 5.5 Alternative execution
# if x % 2 == 0:
#     print('x is even')
# else:
#     print('x is odd')

# # 5.6 Chained conditionals
# if x < y:
#     print('x is less than y')
# elif x > y:
#     print('x is greater than y')
# else:
#     print('x and y are equal')

# # 5.7 Nested conditionals
# if x == y:
#     print('x and y are equal')
# else:
#     if x < y:
#         print('x is less than y')
#     else:
#         print('x is greater than y')

# # 5.8 Recursion
# def countdown(n):
#     n = int(n)  # Ensure n is an integer
#     if n <= 0:
#         print('Blastoff!')
#     else:
#         print(n)
#         countdown(n-1)

# countdown(25)

# Exercise 5.1. 
 
# The time module provides a function, also named time, that returns the current
# Greenwich Mean Time in “the epoch”, which is an arbitrary time used as a reference point. On
# UNIX systems, the epoch is 1 January 1970.

# import time
# print(time.time())

# # Write a script that reads the current time and converts it to a time of day in hours, minutes, and
# # seconds, plus the number of days since the epoch.

# print("Current time in seconds since the epoch:", time.time())

# # Convert the current time to a time of day in hours, minutes, and seconds
# current_time = time.time()
# hours = int(current_time // 3600)
# minutes = int((current_time % 3600) // 60)
# seconds = int(current_time % 60)

# print(f"Current time: {hours:02d}:{minutes:02d}:{seconds:02d}")

# # Calculate the number of days since the epoch
# days = int(current_time // 86400)
# print(f"Days since the epoch: {days}")

# # Exercise 5.2. 

# # Fermat’s Last Theorem says that there are no positive integers a, b, and c such that
# # a^n + b^n = c^n   
# # for any values of n greater than 2.
# # 1. Write a function named check_fermat that takes four parameters—a, b, c and n—and
# # checks to see if Fermat’s theorem holds. If n is greater than 2 and
# # a^n + b^n = c^n
# # the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program should
# # print, “No, that doesn’t work.”

# def check_fermat(a, b, c, n):
#     if n > 2 and a**n + b**n == c**n:
#         print("Holy smokes, Fermat was wrong!")
#     else:
#         print("No, that doesn't work.")

# # 2. Write a function that prompts the user to input values for a, b, c and n, converts them to
# # integers, and uses check_fermat to check whether they violate Fermat’s theorem.
# def get_fermat_values():
#     a = int(input("Enter a value for a: "))
#     b = int(input("Enter a value for b: "))
#     c = int(input("Enter a value for c: "))
#     n = int(input("Enter a value for n: "))
#     check_fermat(a, b, c, n)

# Exercise 5.3. 

# If you are given three sticks, you may or may not be able to arrange them in a triangle.
# For example, if one of the sticks is 12 inches long and the other two are one inch long, you will not
# be able to get the short sticks to meet in the middle. For any three lengths, there is a simple test to
# see if it is possible to form a triangle:
# If any of the three lengths is greater than the sum of the other two, then you cannot
# form a triangle. Otherwise, you can. (If the sum of two lengths equals the third, they
# form what is called a “degenerate” triangle.)
# 1. Write a function named is_triangle that takes three integers as arguments, and that prints
# either “Yes” or “No”, depending on whether you can or cannot form a triangle from sticks
# with the given lengths.

def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("Yes")
    else:
        print("No")

# 2. Write a function that prompts the user to input three stick lengths, converts them to integers,
# and uses is_triangle to check whether sticks with the given lengths can form a triangle.
a = int(input("Enter the length of the first stick: "))
b = int(input("Enter the length of the second stick: "))
c = int(input("Enter the length of the third stick: "))
is_triangle(a, b, c)