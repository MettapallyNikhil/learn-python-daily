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

import turtle
bob = turtle.Turtle()
for i in range(4):
    bob.fd(100)
    bob.lt(90)
turtle.mainloop()