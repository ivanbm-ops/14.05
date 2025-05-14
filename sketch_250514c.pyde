x=400
y=400
def setup():
    size(800,800)
def draw():
    global x,y
    ellipse(x,y,60,60)
    if key== CODED:
        if keyCode==UP:
            y=y-1
        elif keyCode==DOWN:
            y=y+1
        elif keyCode==LEFT:
            x=x-1
        elif keyCode==RIGHT:
            x=x+1
