from ValidType import ValidType


class Int(ValidType):
    """a descriptor for checking the correctness of the type Int"""
    def __init__(self):
        super().__init__(int)


class Float(ValidType):
    """a descriptor for checking the correctness of the type Float"""
    def __init__(self):
        super().__init__(float)


class List(ValidType):
    """a descriptor for checking the correctness of the type List"""
    def __init__(self):
        super().__init__(list)


class Person:
    """
    Class Person
    Args:
    age(int) - age of person 
    height(float) - height of person
    tags(list) - tags for person 
    favorite_foods (list) -  a person's favorite dishes
    name(str) - name of the person
    
    
    """
    
    age = Int()
    height = Float()
    tags = List()
    favorite_foods = List()
    name = ValidType(str)

    def __init__(self, name, age, height, tags, favorite_foods):
        self.name = name
        self.age = age
        self.height = height
        self.tags = tags
        self.favorite_foods = favorite_foods




try:
    
    person1 = Person("John", 15, 175.5, ["friendly", "active"], ["pizza", "pasta"])
    print(person1.name)
    print(person1.age)
    print(person1.height)
    print(person1.tags)
    print(person1.favorite_foods)

    person1.age = 40  # Assignment of the correct type, everything is fine
    person1.favorite_foods = "sushi"  # Error, as the list is expected
except ValueError as e:
    print(f"error: {e}")
