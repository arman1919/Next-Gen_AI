class Int:
    """
    min_value(int) - minimum value
    max_value(int) - maximum value
    
    """
    def __init__(self,min_value,max_value) -> None:
        self.min_value = min_value
        self.max_value = max_value
    
    
    def __set_name__(self,owner,name):
        
        self.name = name
    
    def __set__(self,instance,value):
        
        if not isinstance(value,int) or self.min_value > value or value > self.max_value:
            
            raise ValueError
        
        instance.__dict__[self.name] = value
    
    def __get__(self,instance, owner):
        
        
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
    
    
        
        