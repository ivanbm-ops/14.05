def setup():
    size(800,800)
def draw():
    rect(random(0,800),random(0,800),50,50)
def keyPressed():
        if key=="1":
            fill(247,50,50)
        if key=="2":
            fill(50,68,247)
        if key=="3":
            fill(92,247,50)
        else: 
             fill(random(0,255),random(0,255),random(0,255))#f
                    
        
