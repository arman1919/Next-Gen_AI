from int_valid import Int

class Point2D:
    """a class for a point on a two-dimensional space"""
    x = Int(0,100)
    y = Int(0,100)
    def __init__(self,x,y) -> None:
        
        self.x = x
        self.y = y
    

class Point2DSequence: 
    """
    checking for a class Point2D instance
    checking for min length, max length
    checking for type List
    
    """
        
    def __init__(self,min_length,max_length) -> None:
        self.min_length = min_length
        self.max_length = max_length
    
    
    def __set_name__(self,owner,name):
        
        self.name = name
        
    def __set__(self,instance,value):
       
        
        
        if not isinstance(value,list):
            raise ValueError
        if  self.min_length > len(value) or  len(value) > self.max_length:
            raise ValueError
         
        for i in value:
            if not isinstance(i,Point2D):
                raise ValueError
        instance.__dict__[self.name] = value
        
    def __get__(self,instance,owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
        
      

    