class SingletonMeta(type):
    
    _instances = {}

    def __call__(cls, *args, **kwargs):
        
        if cls in cls._instances:
            
            return cls._instances[cls]

        instance = super().__call__(*args, **kwargs)

        
        cls._instances[cls] = instance
        return instance
        
        
    
    
class Hundred(metaclass=SingletonMeta): 
    def __new__(cls): 
        new_instance = super().__new__(cls) 
        setattr(new_instance, 'name', 'hundred') 
        setattr(new_instance, 'value', 100) 
        return new_instance
    
    
    
p1 = Hundred()
p2 = Hundred()

print(p1 is p2)



