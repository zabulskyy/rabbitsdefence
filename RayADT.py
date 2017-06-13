"""
Created by Roman Vey
11.06.2017
"""

class Point:
    """
    Class which provide point behaviour
    Needed for Ray class
    """
    

    def __init__(self, arg1=(0, 0) ,arg2=None):
        """
        Initialize class
        arg1: None, tuple, int, float, Point
        arg2: None, int, float
        """
        if (type(arg1) == int or type(arg1) == float) or \
        (type(arg2) == int or type(arg2) == float):
            self.x = arg1
            self.y = arg2
        elif arg2 is not None:
            raise TypeError
        else:
            self.x, self.y = Point.get_coords(arg1)
      


    def __len__(self):
        """
        Overwritten len() method
        """
        return 1
        
        

    def __str__(self):
        """
        Overwritten str() method
        """
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"
        
        
 
    def dist(self):
        """
        Return length of point
        """ 
        return (self.x ** 2 + self.y ** 2) ** 0.5
    


    def abs(self):
        """
        Return absolute values of point
        """
        return Point(abs(self.x), abs(self.y))
    
    

    @staticmethod
    def get_coords(what):
        """
        Class method which provide checking input file and teturn tuple of
        coords. Will be used in another methods to check input
        """
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
        """
        Check is points then return new one with added coords 
        """
        x, y = Point.get_coords(other)
        return Point(self.x + x, self.y + y)
     
    

    def __sub__(self, other):
        """
        Check is points then return new one with subtracted coords 
        """
        x, y = Point.get_coords(other)
        return Point(self.x - x, self.y - y)
    

  
    def __mul__(self, other):
        """
        Check is points then return new one with multiplicated coords 
        """  
        x, y = Point.get_coords(other)
        return Point(self.x * x, self.y * y)
    


    def __truediv__(self, other):
        """
        Check is points then return new one with divided coords ("/")
        """    
        x, y = Point.get_coords(other)
        return Point(self.x / x, self.y / y)
     

     
    def __floordiv__(self, other):
        """
        Check is points then return new one with divided coords ("//")
        """ 
        x, y = Point.get_coords(other)
        return Point(self.x // x, self.y // y)
    

    
    def __mod__(self, other):
        """
        Check is points then return new one with dividing rest coords("%")
        """ 
        x, y = Point.get_coords(other)
        return Point(self.x % x, self.y % y)
        
        
            

class Ray:
    """
    Class which provide Ray behaviour. You can create ray based into 
    two points and check is third point into Ray. Also, you can move
    Ray with ints, floats, tuples, etc.
    """
    
    
    
    def __init__(self, start_p, end_p):
        """
        Initialize Ray
        start_p: Point
        end_p: Point
        """
        x_s, y_s = Point.get_coords(start_p)
        self._start_p = Point(x_s, y_s)

        x_e, y_e = Point.get_coords(end_p)
        self._end_p = Point(x_e, y_e)

        self._set_equatation()
    

    
    def _set_equatation(self):
        """
        Initialize k and b in "y = kx + b" equatation based
        into pair of start and end points
        """
        angle = self._end_p - self._start_p
        self.k = angle.y / angle.x
        self.b = self._start_p.y - self._start_p.x * self.k


        
    def __str__(self):
        """
        Overwritten str() method
        """
        if self.b < 0:
            return "y = " + str(self.k) + " x - " + str(abs(self.b)) +\
            " (" + str(self._start_p) + ", " + str(self._end_p) + ")"
        else:
            return "y = " + str(self.k) + " x + " + str(self.b) + " (" +\
            str(self._start_p) + ", " + str(self._end_p) + ")"
        
        
        
    def __len__(self):
        """
        Overwritten len() method
        """
        return 1
       
    
    
    def __add__(self, other):
        """
        Add two rays
        Return ray based into added start and end points of two rays
        """
        if type(other) == Ray:
            return Ray(Point(self._start_p + other._start_p), Point(self._end_p + other._end_p))
        else:
            x, y = Point.get_coords(other)
            return Ray(Point(self._start_p + (x, y)), Point(self._end_p + (x, y)))
            
            
            
    def __sub__(self, other):
        """
        Subtract two rays
        Return ray based into subtracted start and end points of two rays
        """
        if type(other) == Ray:
            return Ray(Point(self._start_p - other._start_p), Point(self._end_p - other._end_p))
        else:
            x, y = Point.get_coords(other)
            return Ray(Point(self._start_p - (x, y)), Point(self._end_p - (x, y)))
        
        
        
    def get_y(self, x):
        """
        Return y from "y = kx + b" for different x
        """
        return self.k * x + self.b
        
        
    def get_x(self, y):
        """
        Return y from "y = kx + b" for different y ("x = (y - b) / k")
        """
        return (y - self.b) / self.k
        
 
      
    def is_point_in_ray(self, point):
        """
        Ckeck is point into ray
        """
        x, y = Point.get_coords(point)
        return y == self.get_y(x)
        
        
        
    def change_start_point(self, point):
        """
        Change start point and get new equatation
        """
        x, y = Point.get_coords(point)
        self._start_p = Point(x, y)
        self._set_equatation()
        
        
        
    def change_end_point(self, point):
        """
        Change end point and get new equatation
        """
        x, y = Point.get_coords(point)
        self._end_p = Point(x, y)
        self._set_equatation()
        