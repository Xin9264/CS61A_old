def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    if raining:
        return True
    elif temp <= 60:
        return True
    else:
        return False
def wears_jacket(temp, raining):
    return temp < 60 or raining


def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    i = 1
    while i<n-1:
        i = i+1
        if n%i == 0:
            return False
    return True

x = 10 % 4
y = x
x **= 2
print(x)
print(y)