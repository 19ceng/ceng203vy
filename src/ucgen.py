from graphics import *

def sierpinskiT(points,level,win, label=0):    
    colormap = ['blue','red','green','white'] #,'yellow','violet','orange']
    
    p = Polygon(points)
    p.setFill(colormap[level])
    p.draw(win)    
    time.sleep(2)
    
    if level > 0:
        # sol sierpinski
        sierpinskiT([points[0],
                     getMid(points[0],points[1]),
                     getMid(points[0],points[2])],level-1,win,label=2)
        # ust sierpinski
        sierpinskiT([getMid(points[0],points[1]),
                     points[1],
                     getMid(points[1],points[2])],level-1,win,label=1)
        
        # sag sierpinski
        sierpinskiT([getMid(points[0],points[2]),
                     getMid(points[1],points[2]),
                     points[2]],level-1,win,label=3)
    
def getMid(p1,p2):
    return Point( ((p1.getX()+p2.getX()) / 2.0),
                  ((p1.getY()+p2.getY()) / 2.0) )

if __name__ == '__main__':
    win = GraphWin('st',500,500)
    win.setCoords(20,-10,80,50)
    myPoints = [Point(25,0),Point(50,43.3),Point(75,0)]
    sierpinskiT(myPoints,2,win,label=0)



