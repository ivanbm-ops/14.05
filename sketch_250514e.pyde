x=360
def setup():
    size(800,800)
def draw():
    global x
    background(0)
    push()
    translate(400,400)
    rotate(radians(x))
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(0,0,400,350)
    pop()
    push()
    translate(400,400)
    rotate(radians(x))
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(0,0,150,200)
    pop()
    push()
    translate(370,370)
    rotate(radians(x))
    fill(random(0,255),random(0,255),random(0,255))
    rect(0,0,100,50)
    pop()
def keyPressed():
    global x
    if keyPressed:
        if key=="b":
            x=x+100
        if key=="v":
            x=x-100
            
