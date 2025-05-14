x=100

def setup():
    size(800,800)
def draw():
    global x
    background(0)
    fill(random(0,255),random(0,255),random(0,255))
    ellipse(400,400,x,x)
    if keyPressed:
      if key== "r":
          x=x+5
      if key== "e":
          x=x-6
    
