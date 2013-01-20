

# We'll start with the notion of a vertex

# Because we're moving vertices around, their coordinates are inherently
# mutable # but we need references to them to build up larger structures so
# we're going to use a class containing a 3-tuple for the current coordinates

class Vertex:
    def __init__(self, x, y, z):
        self.coordinates = (x, y, z)

v1 = Vertex(0, 0, 0)
v2 = Vertex(0, 1, 0)


# Next we define a distance function that takes two vertices

from math import sqrt


def distance(vertex_1, vertex_2):
    return sqrt(sum((c1 - c2) ** 2 for c1, c2 in
        zip(vertex_1.coordinates, vertex_2.coordinates)))


assert distance(v1, v2) == 1.0


# An Edge pairs two vertices together

class Edge:
    def __init__(self, vertex_1, vertex_2):
        self.vertex_1 = vertex_1
        self.vertex_2 = vertex_2
    
    def length(self):
        return distance(self.vertex_1, self.vertex_2)


e1 = Edge(v1, v2)

assert e1.length() == 1.0


# We want a test for colinearity. To do that, we'll first introduce the notion
# of a 3-tuple "vector", the conversion to spherical coordinates to get a
# "direction" and then finally a test for whether two vectors are
# parallel or not

def vector(vertex_1, vertex_2):
    return tuple(c1 - c2 for c1, c2 in
        zip(vertex_1.coordinates, vertex_2.coordinates))

# (we could rewrite "distance" above to use this)

from math import acos, atan2


def direction(vector):
    r = sqrt(sum(c ** 2 for c in vector))
    theta = acos(vector[2] / r)
    phi = atan2(vector[1], vector[0])
    return (theta, phi)


assert vector(v1, v2) == (0, -1, 0)
assert direction(vector(v1, v2)) == (1.5707963267948966, -1.5707963267948966)


def colinear(*vertices):
    d = direction(vector(vertices[0], vertices[1]))
    for vertex in vertices[2:]:
        if direction(vector(vertices[0], vertex)) != d:
            return False
    return True


v3 = Vertex(0, 2, 0)
v4 = Vertex(1, 0, 0)

assert colinear(v1, v2, v3) == True
assert colinear(v1, v2, v4) == False
