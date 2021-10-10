class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def fall_in_retangle(self, lowleft, upright):
        if lowleft[0] < self.x < upright[0] \
        and lowleft[1] < self.y < upright[1]:
            return True
        else:
            return False 
    def distance_from_point(self, point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2) ** 0.5

point1 = Point(10, 20)
point2 = Point(11, 22)
point3 = Point(23, 10)

print(point3.fall_in_retangle((5, 6), (7, 9)))
print(type(point1))
print(point1.x)
print(Point(10, 20).x)
print(point1.distance_from_point(point2))

class Person:

    def __init__(self, n, a):
        self.name = n
        self.age = a

person1 = Person('Giang', 27)

print(person1.name)
print(person1.age)

class House:

    def __init__(self, wall_area):
        self.wall_area = wall_area
    def paint_needed(self):
        return self.wall_area * 2.5
       
        
class Paint:

    def __init__(self, buckets, color):
        self.color = color
        self.buckets = buckets
    def total_price(self):
        if self.color == 'white':
            return self.buckets * 1.99
        else:
            return self.buckets * 2.19

# __main__ là tên chương trình chính hiện tại mình đang viết code
# nếu ở chương trình chính thì khi in ra sẽ là main
# còn nếu import vào chương trình khác thì nó sẽ là tên chương trình chứa nó
# self in a class is the variable that holds the object instance that is created by the class
# x và y là instance variable
# self.name và self.age được gọi là attribute của object
# __init__ là một method để khởi tạo object mà mới vừa tạo
# __init__ được thực thi khi object mới được tạo ra