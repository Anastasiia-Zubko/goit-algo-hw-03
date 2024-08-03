"""
Task 2: Draw a Koch Snowflake Fractal
"""

import turtle

def koch_curve(t, order, size):
    """
    Draws a Koch curve using recursion.
    """
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(order, size=300):
    """
    Sets up the turtle environment and starts drawing the Koch snowflake.
    """
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()

def main():
    """
    Main function to get user input and initiate drawing the Koch curve.
    """
    try:
        order = int(input("Enter the recursion depth: "))
        draw_koch_snowflake(order)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
