from turtle import*

def sechseck():
    begin_fill()
    forward(55)
    left(60)
    forward(55)
    left(60)
    forward(55)
    left(60)
    forward(55)
    left(60)
    forward(55)
    left(60)
    forward(55)
    rt(60)
    fd (55)
    lt(60)
    end_fill()
    
def zwischenschritt():
    penup()
    forward(55)
    rt (60)
    pendown()

##penup()
##right(120)
##forward(55)
##left(120)
##pendown()

pensize(3)
pencolor("brown")
fillcolor("yellow")

sechseck()
fillcolor("orange")
rt(60)
fd(-55)
sechseck()

sechseck()

sechseck()

sechseck()

sechseck()

sechseck()

hideturtle()
