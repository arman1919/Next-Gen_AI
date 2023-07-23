from Point2D import *


class Polygon:
    """
    Polygon class
    args:
    vertices(List of object Point2D) - vertices 
    """
    vertices = Point2DSequence(3,4)
    
    def __init__(self,vertices) -> None:
        self.vertices = vertices
        


    def append(self,x,y):
        """
        add a new point of the Point2D class
        if the number does not exceed the number of vertices
        """
        new_vertices = []
        for i in self.vertices:
            new_vertices.append(i)
        new_vertices.append(Point2D(x,y))
        
        self.vertices = new_vertices
        
        


p1 = Point2D(1,2)
p2 = Point2D(3,4)
p3 = Point2D(6,5)
p4 = Point2D(2,8)
        
vert = [p1,p2,p3,p4]

triangle = Polygon(vert)

triangle.append(5,5) #  the maximum number of vertices is 4 
