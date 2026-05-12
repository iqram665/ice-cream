import turtle
import time

# screen setup
screen = turtle.Screen()
screen.setup(width=950, height=950)
screen.bgcolor("#46BABE") # Light cream background
screen.title("Ice Cream Maker - @iqram-visual")

t = turtle.Turtle()
t.speed(3)

# ১. Function for making an ice cream cone
def draw_cone():
    t.penup()
    t.goto(-80, 50)
    t.pendown()
    t.color("#D2B48C") # Biscuit color
    t.begin_fill()
    t.goto(80, 50)
    t.goto(0, -150)
    t.goto(-80, 50)
    t.end_fill()

# ২. Function for making an ice cream scoop
def draw_scoop(x, y, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(50)
    t.end_fill()

# ৩. YouTube Logo Creation Function
def draw_yt_logo(x, y):
    # red box
    t.penup()
    t.goto(x-50, y)
    t.pendown()
    t.color("#FF0000")
    t.begin_fill()
    for _ in range(2):
        t.forward(100)
        t.circle(10, 90)
        t.forward(40)
        t.circle(10, 90)
    t.end_fill()
    
    # white play button
    t.penup()
    t.goto(x-10, y + 15)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.goto(x-10, y + 45)
    t.goto(x+20, y + 30)
    t.goto(x-10, y + 15)
    t.end_fill()

# --- Animation Start ---

# Draw a corner
draw_cone()

# Ice Cream Making Process (Colorful Scoops)
flavors = [
    ("#8B4513", 40),  # Chocolate
    ("#FF69B4", 90),  # Strawberry
    ("#00FF7F", 140)  # Mint/Vanilla
]

for color, y_pos in flavors:
    time.sleep(0.5) # Making Effect
    draw_scoop(0, y_pos, color)

# ৪. Branding Section (YouTube Logo + Name)
# Drawing the Logo
draw_yt_logo(-110, -280)

# Channel Name
t.penup()
t.goto(60, -275)
t.color("black")
t.write("@iqram-visual", align="center", font=("Arial", 25, "bold"))

# Subscribe Message
t.goto(0, -340)
t.color("#555555")
t.write("Project Made By | Subscribe to watch Python projects", 
        align="center", font=("Verdana", 12, "italic"))

t.hideturtle()
turtle.done()