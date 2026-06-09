def power(a,b):
    try:
        return a**b
    except TypeError:
        print("Type Error: power() requires numeric values")
    except OverflowError:
        print("Overflow Error: result too large")
    except Exception:
        print("Unknown Error in power()")
    return None


def factorial(n):
    try:
        if n < 0:
            raise ValueError
        f=1
        for i in range(1,n+1):
            f=f*i
        return f
    except TypeError:
        print("Type Error: factorial() requires an integer")
    except ValueError:
        print("Value Error: factorial not defined for negative numbers")
    except OverflowError:
        print("Overflow Error: result too large")
    except Exception:
        print("Unknown Error in factorial()")
    return None


def gcd(a,b):
    try:
        while b!=0:
            a,b=b,a%b
        return a
    except TypeError:
        print("Type Error: gcd() requires integer values")
    except ZeroDivisionError:
        print("Math Error: division by zero")
    except Exception:
        print("Unknown Error in gcd()")
    return None


def lcm(a,b):
    try:
        g=gcd(a,b)
        return (a*b)//g
    except TypeError:
        print("Type Error: lcm() requires integer values")
    except ZeroDivisionError:
        print("Math Error: division by zero")
    except Exception:
        print("Unknown Error in lcm()")
    return None


def is_prime(n):
    try:
        if n<=1:
            return False
        for i in range(2,n):
            if n%i==0:
                return False
        return True
    except TypeError:
        print("Type Error: is_prime() requires an integer")
    except Exception:
        print("Unknown Error in is_prime()")
    return None


def is_palindrome(n):
    try:
        t=n
        r=0
        while n>0:
            d=n%10
            r=r*10+d
            n=n//10
        return r==t
    except TypeError:
        print("Type Error: is_palindrome() requires an integer")
    except Exception:
        print("Unknown Error in is_palindrome()")
    return None


def count_digits(n):
    try:
        c=0
        while n>0:
            c=c+1
            n=n//10
        return c
    except TypeError:
        print("Type Error: count_digits() requires an integer")
    except Exception:
        print("Unknown Error in count_digits()")
    return None


def is_armstrong(n):
    try:
        t=n
        s=0
        d=count_digits(n)
        while n>0:
            r=n%10
            s=s+(r**d)
            n=n//10
        return s==t
    except TypeError:
        print("Type Error: is_armstrong() requires an integer")
    except Exception:
        print("Unknown Error in is_armstrong()")
    return None


def fibonacci(n):
    try:
        a=0
        b=1
        l=[]
        for i in range(n):
            l.append(a)
            c=a+b
            a=b
            b=c
        return l
    except TypeError:
        print("Type Error: fibonacci() requires an integer")
    except Exception:
        print("Unknown Error in fibonacci()")
    return None


def AP_sum(a,d,n):
    try:
        s=0
        for i in range(n):
            s=s+(a+i*d)
        return s
    except TypeError:
        print("Type Error: AP_sum() requires numeric values")
    except Exception:
        print("Unknown Error in AP_sum()")
    return None


def GP_sum(a,r,n):
    try:
        s=0
        for i in range(n):
            s=s+(a*(r**i))
        return s
    except TypeError:
        print("Type Error: GP_sum() requires numeric values")
    except OverflowError:
        print("Overflow Error: result too large")
    except Exception:
        print("Unknown Error in GP_sum()")
    return None


def mean(l):
    try:
        s=0
        for i in l:
            s=s+i
        return s/len(l)
    except TypeError:
        print("Type Error: mean() requires a list of numbers")
    except ZeroDivisionError:
        print("Math Error: empty list")
    except Exception:
        print("Unknown Error in mean()")
    return None


def is_perfect(n):
    try:
        s=0
        for i in range(1,n):
            if n%i==0:
                s=s+i
        return s==n
    except TypeError:
        print("Type Error: is_perfect() requires an integer")
    except Exception:
        print("Unknown Error in is_perfect()")
    return None


def degree_to_radian(x):
    try:
        return (x*3.14159/180)
    except TypeError:
        print("Type Error: degree_to_radian() requires numeric value")
    except Exception:
        print("Unknown Error in degree_to_radian()")
    return None


def quadratic_roots(a,b,c):
    try:
        d=(b**2)-(4*a*c)
        if d<0:
            print("No real roots")
            return None
        r1=(-b+(d**0.5))/(2*a)
        r2=(-b-(d**0.5))/(2*a)
        return r1,r2
    except TypeError:
        print("Type Error: quadratic_roots() requires numeric values")
    except ZeroDivisionError:
        print("Math Error: a cannot be zero")
    except Exception:
        print("Unknown Error in quadratic_roots()")
    return None


def simple_interest(p,r,t):
    try:
        return (p*r*t)/100
    except TypeError:
        print("Type Error: simple_interest() requires numeric values")
    except Exception:
        print("Unknown Error in simple_interest()")
    return None
def menu():
    print("\n====== MATHEMATICAL OPERATIONS MENU ======")
    print("1. Power (a^b)")
    print("2. Factorial")
    print("3. GCD")
    print("4. LCM")
    print("5. Prime Check")
    print("6. Palindrome Check")
    print("7. Armstrong Check")
    print("8. Fibonacci Series")
    print("9. Sum of AP")
    print("10. Sum of GP")
    print("11. Mean of Numbers")
    print("12. Perfect Number Check")
    print("13. Degree to Radian")
    print("14. Quadratic Roots")
    print("15. Simple Interest")
    print("0. Exit")
    print("========================================")


while True:
    menu()
    try:
        ch = int(input("Enter your choice: "))

        if ch == 1:
            a = float(input("Enter base: "))
            b = float(input("Enter power: "))
            print("Result:", power(a, b))

        elif ch == 2:
            n = int(input("Enter number: "))
            print("Factorial:", factorial(n))

        elif ch == 3:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("GCD:", gcd(a, b))

        elif ch == 4:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("LCM:", lcm(a, b))

        elif ch == 5:
            n = int(input("Enter number: "))
            print("Is Prime:", is_prime(n))

        elif ch == 6:
            n = int(input("Enter number: "))
            print("Is Palindrome:", is_palindrome(n))

        elif ch == 7:
            n = int(input("Enter number: "))
            print("Is Armstrong:", is_armstrong(n))

        elif ch == 8:
            n = int(input("Enter number of terms: "))
            print("Fibonacci Series:", fibonacci(n))

        elif ch == 9:
            a = float(input("Enter first term: "))
            d = float(input("Enter common difference: "))
            n = int(input("Enter number of terms: "))
            print("AP Sum:", AP_sum(a, d, n))

        elif ch == 10:
            a = float(input("Enter first term: "))
            r = float(input("Enter common ratio: "))
            n = int(input("Enter number of terms: "))
            print("GP Sum:", GP_sum(a, r, n))

        elif ch == 11:
            lst = []
            n = int(input("How many numbers? "))
            for i in range(n):
                lst.append(float(input("Enter number: ")))
            print("Mean:", mean(lst))

        elif ch == 12:
            n = int(input("Enter number: "))
            print("Is Perfect Number:", is_perfect(n))

        elif ch == 13:
            x = float(input("Enter angle in degrees: "))
            print("Radians:", degree_to_radian(x))

        elif ch == 14:
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))
            c = float(input("Enter c: "))
            print("Roots:", quadratic_roots(a, b, c))

        elif ch == 15:
            p = float(input("Enter principal: "))
            r = float(input("Enter rate: "))
            t = float(input("Enter time: "))
            print("Simple Interest:", simple_interest(p, r, t))

        elif ch == 0:
            print("Thank you! Exiting program.")
            break

        else:
            print("Invalid choice! Please try again.")

    except ValueError:
        print("Invalid input! Please enter correct values.")

