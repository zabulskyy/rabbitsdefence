from RayADT import Point, Ray
"""
Check RayADT for working
"""

p1 = Point(2,3)
p2 = Point((2, 3))
p3 = Point(p1)
assert(p1.x == p2.x == p3.x and p1.y == p2.y == p3.y)
p1 += p2
p3 += (2, 8)
p2 += 4
assert(p1.x == 4 and p1.y == 6)
assert(p2.x == 6 and p2.y == 7)
assert(p3.x == 4 and p3.y == 11)

ray = Ray(p1, (0,0))
assert(ray.b == 0 and ray.k == 1.5)
assert(str(ray) == "y = 1.5 x (Point(4, 6), Point(0, 0))")
ray -= 2
assert(str(ray) == "y = 1.5 x + 1.0 (Point(2, 4), Point(-2, -2))")

ray2 = Ray((1,1), (2,2))
ray2 -= ray
assert(ray2.k == 1.4)