# FormulaOfPolygons

# Geometry Module 1
# Functions to calculate Area of Polygons


# Triangle (Area)
def TriAre(b, h):  # base, height
    return 1 / 2 * b * h


# Square (Area)
def SquAre(l):  # length
    return l ** 2


# Rectangle (Area)
def RecAre(l, w):  # length, width
    return l * w


# Circle (Area)
def CirAre(r):  # radius
    return 3.14 * (r ** 2)


# Rhombus (Area)
def RhoAre(l, h):  # length, height
    return l * h


# Parallelogram (Area)
def ParAre(b, h):  # base, height
    return b * h


# Geometry Module 2
# Functions to calculate Perimeter of Polygons


# Triangle (Perimeter)
def TriPer(len1, len2, len3):  # length of 3 sides
    return len1 + len2 + len3


# Square (Perimeter)
def SquPer(l):  # length
    return l * 4


# Rectangle (Perimeter)
def RecPer(l, w):  # length, width
    return (2 * l) + (2 * w)


# Circle (Circumference)
def CirPer(r):  # radius
    return (2 * 3.14) * r


# Geometry Module 3
# Functions to calculate Surface Area of solids


# Tetrahedron (Surface Area)
# The sum of 4 regular sides
def TetSur(e):  # edge
    return (e ** 2)*(3 ** 0.5)


# Cube (Surface Area)
def CubSur(l):  # length
    return 6 * (l ** 2)


# Cuboid (Surface Area)
def CuboSur(l, w, h):  # length, width, height
    return (2 * l * w) + (2 * l * h) + (2 * w * h)


# Sphere (Surface Area)
def SphSur(r):  # radius
    return 4 * 3.14 * (r ** 2)


# Cylinder (Surface Area)
def CylSur(r, h):  # radius, height
    return 2 * 3.14 * (r ** 2) + 2 * 3.14 * r * h


# Cone (Surface Area)
def ConSur(r, s):  # radius, slope
    return 3.14 * (r ** 2) + 2 * 3.14 * r * s


# Square Pyramid (Surface Area)
def SqPyrSur(l, s, h):  # length, slope, height
    return (l ** 2) + (2 * s * h)


# Rectangular Pyramid (Surface Area)
def RePyrSur(l, w, h, s):  # length, width, height, slope
    return (l * w) + (w * h) + (2 * l * s)


# Geometry Module 4
# Functions to calculate Volume of  Solids


# Tetrahedron (Volume)
def TetVol(e):  # edge
    return (e ** 3) / (6 * (2 ** 0.5))


# Cube (Volume)
def CubVol(l):  # length
    return l ** 3


# Cuboid (Volume)
def CuboVol(l, w, h):  # length, width, height
    return l * w * h


# Sphere (Volume)
def SphVol(r):  # radius
    return 4 / 3 * 3.14 * (r ** 3)


# Cylinder (Volume)
def CylVol(r, h):  # radius, height
    return 3.14 * (r ** 2) * h


# Cone (Volume)
def ConVol(r, h):  # radius, height
    return 1 / 3 * 3.14 * (r ** 2) * h


# Square Pyramid (Volume)
def SqPyrVol(bl, h):  # base length, height
    return (1 / 3 * h) * (bl ** 2)


# Rectangular Pyramid (Volume)
def RePyrVol(bl, bw, h):  # base length, base width, height
    return 1 / 3 * bl * bw * h
