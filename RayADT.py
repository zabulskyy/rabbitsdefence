class Point:
    def __init__(self, arg1=(0, 0) ,arg2=None):
        if (type(arg1) == int or type(arg1) == float) or \
        (type(arg2) == int or type(arg2) == float):
            self.x = arg1
            self.y = arg2
        elif arg2 is not None:
            raise TypeError
        else:
            self.x, self.y = Point.get_coords(arg1)
            
    def __len__(self):
        return 1
        
    def __str__(self):
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"
        
    
    def dist(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
        
    def abs(self):
        return Point(abs(self.x), abs(self.y))
        
    @staticmethod
    def get_coords(what):
        if type(what) == tuple and len(what) == 2 and \
        (type(what[0]) == int or type(what[0]) == float) \
        and (type(what[1]) == int or type(what[1]) == float):
            return what[0], what[1]
        elif type(what) == Point:
            return what.x , what.y
        elif type(what) == int or type(what) == float:
            return what, what
        else:
            raise TypeError
        
    def __add__(self, other):
        x, y = Point.get_coords(other)
        return Point(self.x + x, self.y + y)
     
    def __sub__(self, other):
        x, y = Point.get_coords(other)
        return Point(self.x - x, self.y - y)
        
    def __mul__(self, other):
        x, y = Point.get_coords(other)
        return Point(self.x * x, self.y * y)
        
    def __truediv__(self, other):
        x, y = Point.get_coords(other)
        return Point(self.x / x, self.y / y)
        
    def __floordiv__(self, other):
        x, y = Point.get_coords(other)
        return Point(self.x // x, self.y // y)
        
    def __mod__(self, other):
        x, y = Point.get_coords(other)
        return Point(self.x % x, self.y % y)
        
        
            


class Ray:
    def __init__(self, start_p, end_p):
        x_s, y_s = Point.get_coords(start_p)
        self._start_p = Point(x_s, y_s)

        x_e, y_e = Point.get_coords(end_p)
        self._end_p = Point(x_e, y_e)

        self.set_equatation()
        
    def set_equatation(self):
        angle = self._end_p - self._start_p
        self.k = angle.y / angle.x
        self.b = self._start_p.y - self._start_p.x * self.k
        
    def __str__(self):
        if self.b < 0:
            return "y = " + str(self.k) + " x - " + str(abs(self.b)) +\
            " (" + str(self._start_p) + ", " + str(self._end_p) + ")"
        else:
            return "y = " + str(self.k) + " x + " + str(self.b) + " (" +\
            str(self._start_p) + ", " + str(self._end_p) + ")"
        
    def __len__(self):
        return 1
       
       
    def __add__(self, other):
        if type(other) == Ray:
            return Ray(Point(self._start_p + other._start_p), Point(self._end_p + other._end_p))
        else:
            x, y = Point.get_coords(other)
            return Ray(Point(self._start_p + (x, y)), Point(self._end_p + (x, y)))
        
        
        
    def get_y(self, x):
        return self.k * x + self.b
        
 
      
    def is_point_in_ray(self, point):
        x, y = Point.get_coords(point)
        return y == self.get_y(x)
        
        
        
    def change_start_point(self, point):
        x, y = Point.get_coords(point)
        self._start_p = Point(x, y)
        self.set_equatation()
        
        
        
    def change_end_point(self, point):
        x, y = Point.get_coords(point)
        self._end_p = Point(x, y)
        self.set_equatation()
        
        

            
r = Ray(Point(3, 7), Point(2, 5))
print(r)
r += (2, 0)
print(r)
        