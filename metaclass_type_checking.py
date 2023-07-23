class Person:
    
    def __new__(cls,name,age):
        if not isinstance(name,str):
            raise TypeError

        if age<0 or not isinstance(age,int):
            raise TypeError
        
        instance = super().__new__(cls)

        return instance
    
    
    def __init__(self,name:str,age:int) -> None:
        self.name = name
        self.age = age




p1 = Person("Bob",25)
p2 = Person("Stiv",-15)
p3 = Person(25,15)
