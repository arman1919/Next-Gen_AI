from typing import Any


class SlottedStruct(type):
    def __new__(cls, name, bases, dct):
        if name != 'Point':
            # Skip the base class 'Point' itself to avoid unwanted behavior
            # and only apply the custom metaclass to subclasses of 'Point'
            dct['__slots__'] = ('_coordinates',)
        return super(SlottedStruct, cls).__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        super(SlottedStruct, cls).__init__(name, bases, dct)

    

    def __repr__(self):
        return f"{self.__name__}({', '.join(str(coord) for coord in self._coordinates)})"

    def __eq__(self, other):
        if not isinstance(other, self):
            return False
        return self._coordinates == other._coordinates

    def __hash__(self):
        return hash(self._coordinates)


class Point(metaclass=SlottedStruct):
    def __init__(self, *args):
        self._coordinates = tuple(args)

    @property
    def coordinates(self):
        return self._coordinates


# Test the implementation with various N-dimensional points

class Point2D(Point):
    def __init__(self, x, y):
        super(Point2D, self).__init__(x, y)


class Point3D(Point):
    def __init__(self, x, y, z):
        super(Point3D, self).__init__(x, y, z)


class Point4D(Point):
    def __init__(self, x, y, z, w):
        super(Point4D, self).__init__(x, y, z, w)


class Point5D(Point):
    def __init__(self, x, y, z, w, v):
        super(Point5D, self).__init__(x, y, z, w, v)


# Test the implementation

point_2d_1 = Point2D(1, 2)
point_2d_2 = Point2D(1, 2)
point_2d_3 = Point2D(3, 4)

print(point_2d_1)  # Output: Point2D(1, 2)
print(point_2d_1 == point_2d_2)  # Output: True
print(point_2d_1 == point_2d_3)  # Output: False

point_3d_1 = Point3D(1, 2, 3)
point_3d_2 = Point3D(1, 2, 3)
point_3d_3 = Point3D(4, 5, 6)

print(point_3d_1)  # Output: Point3D(1, 2, 3)
print(point_3d_1 == point_3d_2)  # Output: True
print(point_3d_1 == point_3d_3)  # Output: False

point_4d_1 = Point4D(1, 2, 3, 4)
point_4d_2 = Point4D(1, 2, 3, 4)
point_4d_3 = Point4D(5, 6, 7, 8)

print(point_4d_1)  # Output: Point4D(1, 2, 3, 4)
print(point_4d_1 == point_4d_2)  # Output: True
print(point_4d_1 == point_4d_3)  # Output: False

point_5d_1 = Point5D(1, 2, 3, 4, 5)
point_5d_2 = Point5D(1, 2, 3, 4, 5)
point_5d_3 = Point5D(6, 7, 8, 9, 10)

print(point_5d_1)  # Output: Point5D(1, 2, 3, 4, 5)
print(point_5d_1 == point_5d_2)  # Output: True
print(point_5d_1 == point_5d_3)  # Output: False

