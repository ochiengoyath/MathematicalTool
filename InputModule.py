# InputModule.py


# import importlib

# Standard iteration used everywhere
Loop = list(range(100))


# Accepts integer inputs only
def IntInput(n):
    n = None
    while not n:
        try:
            n = int(input('  Enter a Number:'))
        except ValueError:
            print('  Invalid Input!')
    return n


# Accepts integer inputs only without prompt message
def Value(n):
    n = None
    while not n:
        try:
            n = int(input('  '))
        except ValueError:
            print('Invalid Input!')
    return n


# Accepts string inputs only with "prompt:" as message
def Str(n):
    n = None
    while not n:
        n = (input('  prompt:'))
    return n


# Accepts float inputs only (prompt: 1st No.)
def FirstNumber(num1):
    num1 = None
    while not num1:
        try:
            num1 = int(input('  Enter the 1st No. '))
        except ValueError:
            print('  Invalid Input!, Please Enter a Number')
    return num1


# Accepts float inputs only (prompt: 2nd No.)
def SecondNumber(num2):
    num2 = None
    while not num2:
        try:
            num2 = float(input('  Enter the 2nd No: '))
        except ValueError:
            print('  Invalid Input!, Please Enter another Number')
    return num2


# Accepts integer inputs only(prompt: Enter the 1st No.)
def IntNum1(int1):
    int1 = None
    while not int1:
        try:
            int1 = int(input('  Enter the 1st No. '))
        except ValueError:
            print('  Invalid Input!, Please Enter a Whole Number')
    return int1


# Accepts integer inputs only(prompt: Enter the 2nd No.)
def IntNum2(int2):
    int2 = None
    while not int2:
        try:
            int2 = int(input('  Enter the 2nd No. '))
        except ValueError:
            print('  Invalid Input!, Please Enter a Whole Number')
    return int2


# Accepts float inputs only(prompt: Enter the 1st No.)
def FirstFloat(float1):
    float1 = None
    while not float1:
        try:
            float1 = float(input('  Enter the 1st No. '))

        except ValueError:
            print('  Invalid Number!, Please enter a Number')
    return float1


# Accepts the first value in a range of numbers (integers only)
def RangeFrom(From):
    From = None
    while not From:
        try:
            From = int(input('  Range From:'))
        except ValueError:
            print('  Invalid Input!, Please Enter a Whole Number')
    return From


# Accepts the last value in a range of numbers (integers only)
def RangeTo(To):
    To = None
    while not To:
        try:
            To = int(input('  Range To:'))
        except ValueError:
            print('  Invalid Input!, Please Enter another Whole Number')
    return To


# Defines the standard interval value in a range of numbers (integers only)
def Interval(Of):
    Of = None
    while not Of:
        try:
            Of = int(input('  Interval of:'))
        except ValueError:
            print('  Invalid Input!, Please Enter another Whole Number')
    return Of


# Defines the scope in a range of numbers (integers only)
def RangeOfNumbers(Ran):
    Ran = None
    while not Ran:
        try:
            Ran = int(input('  Enter the Range of Numbers: '))
        except ValueError:
            print('  Invalid Number!, Please enter another Integer')
    return Ran


# Accepts positive values only (can be integers or floats)
def NonNegative(Pos):
    if Pos < 0:
        print('  Please Enter a Positive Value')
        return Pos


# Sets the limit of the maximum value accepted
def TooLarge(Big, Max):
    if Big > Max:  # Compares input(Big) with a set maximum(Max)
        print('  Number too Large: Maximum Value is ', Max)
        return Big


# Checks if 1st input is greater than 2nd input; returns print statement
def GreaterThan(From, To):
    if From > To:
        print('  The Second Value must be greater than the First value ')
        return From, To


def FltIntConverter(n):
    for x in Loop:
        if n % 1 == 0:
            n = int(n)
        return n


def Switch(n):
    valid = [1, 2]
    for i in Loop:
        while n not in valid:
            print('  Valid Numbers are: 1 and 2')
            n = IntInput(None)
    return n


def Validity(e):
    valid = list(range(1, e + 1))
    for n in valid:
        while n not in valid:
            print('  You\'ve entered an Invalid input')
            print('  Valid Numbers Range from: 1 to', e)
            n = IntInput(None)


"""
def Validity(e):
    n = IntInput(None)
    valid = list(range(1, e + 1))
    while n not in valid:
        print('  You\'ve entered an Invalid input')
        print('  Valid Numbers Range from: 1 to', e)
        n = IntInput(None)





def Arrays(*a):
    ListArrays = []
    a = list(map(float, input('  \nEnter the numbers:').strip().split()))
    for val in a:
        ListArrays.append(val)
    print(Arrays)
    return a


"""


def Var(x, y, z):  # x = first value, y = last value, z = interval
    return list(range(x, y, z))


def ModuleNavigate(n):
    n = None
    while not n:
        n = str.lower(input('  '))
    return n


def LowerStr(*a):
    a = None
    while not a:
        try:
            a = (str.lower(input('  Enter the equation:')))
        except ValueError:
            print('  Invalid input! Enter for example 2*x-3')
            print('  for y = 2x-3')
    return a
