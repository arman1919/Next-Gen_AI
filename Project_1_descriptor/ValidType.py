class ValidType:
    """Base class for validation """
    def __init__(self, data_type):
        self.data_type = data_type

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        
        if not isinstance(value, self.data_type):
            raise ValueError(f"Expected data type {self.data_type.__name__} for the attribute'{self.name}', received {type(value).__name__}")
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

