# GeometryInput
# Input functions


def Length(l):
    l = None
    while not l:
        try:
            l = float(input('  Enter the Value of Length: '))
        except ValueError:
            print('  Invalid Input!, Please Enter a Number ')
    return l


def Length1(len1):
    len1 = None
    while not len1:
        try:
            len1 = float(input('  Enter the value of First Side: '))
        except ValueError:
            print('  Invalid Input!, Please Enter a Number ')
    return len1


def Length2(len2):
    len2 = None
    while not len2:
        try:
            len2 = float(input('  Enter the value of Second Side: '))
        except ValueError:
            print('  Invalid Input!, Please Enter a Number ')
    return len2


def Length3(len3):
    len3 = None
    while not len3:
        try:
            len3 = float(input('  Enter the value of Third Side: '))
        except ValueError:
            print('  Invalid Input!, Please Enter a Number ')
    return len3


def Width(w):
    w = None
    while not w:
        try:
            w = float(input('  Enter the value of Width: '))
        except ValueError:
            print('  Invalid Input!, Please Enter a Number ')
    return w


def Height(h):
    h = None
    while not h:
        try:
            h = float(input('  Enter the value of Height: '))
        except ValueError:
            print('  Invalid Input!, Please Enter a Number ')
    return h


def Base(b):
    b = None
    while not b:
        try:
            b = float(input('  Enter the value of Base: '))
        except ValueError:
            print('  Invalid Input!, Please Enter a Number ')
    return b


def Radius(r):
    r = None
    while not r:
        try:
            r = float(input('  Enter the value of Radius: '))
        except ValueError:
            print('  Invalid Input!, Please Enter a Number ')
    return r


def Slope(s):
    s = None
    while not s:
        try:
            s = float(input('  Enter the value of Slope: '))
        except ValueError:
            print('  Invalid Input!, Please Enter a Number ')
    return s


def BaseLenth(bl):
    bl = None
    while not bl:
        try:
            bl = float(input('  Enter the value of Length of Base: '))
        except ValueError:
            print('  Invalid Input!, Please Enter a Number ')
    return bl


def BaseWidth(bw):
    bw = None
    while not bw:
        try:
            bw = float(input('  Enter the value of Width of Base: '))
        except ValueError:
            print('  Invalid Input!, Please Enter a Number ')
    return bw


def EdgeLength(e):
    e = None
    while not e:
        try:
            e = float(input('  Enter the value of Edge: '))
        except ValueError:
            print('  Invalid Input!, Please Enter a Number ')
    return e


def PerWidth(pw):  # Perpendicular width
    pw = None
    while not pw:
        try:
            pw = float(input('  Enter the value of Perpendicular width of Base \n'
                             '  Think of it as the "height" of the base triangle: '))
        except ValueError:
            print('  Invalid Input!, Please Enter a Number ')
    return pw
