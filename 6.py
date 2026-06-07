import math

def sin_taylor(x, n):
    x = math.radians(x)
    result = 0
    for i in range(n):
        sign = (-1) ** i
        result += sign * (x ** (2*i + 1)) / math.factorial(2*i + 1)
    return result

x = float(input("Enter x in degrees: "))
n = int(input("Enter number of terms: "))
print(f"sin({x}) ≈", sin_taylor(x, n))
