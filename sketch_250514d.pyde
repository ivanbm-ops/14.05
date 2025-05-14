b="a"
def setup():
    size(800,800)
def draw():
    global b
    background(0)
    text(b,300,300)
def keyPressed():
    global b
    b=key+b
