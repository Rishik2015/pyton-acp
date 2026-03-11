import turtle

# Create a turtle object
t = turtle.Turtle()

# Draw the square
for _ in range(4):
    t.forward(100)  # Move forward 100 pixels
    t.left(90)      # Turn left 90 degrees

# Keep the window open
turtle.done()