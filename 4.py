import math

# Functions for different shapes
def square(side):
    area = side * side
    perimeter = 4 * side
    return area, perimeter

def rectangle(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter

def triangle(base, height):
    area = 0.5 * base * height
    return area

def circle(radius):
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    return area, perimeter

def sphere(radius):
    surface_area = 4 * math.pi * radius ** 2
    return surface_area

def cylinder(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

# Main Program
print("Select a shape:")
print("1. Square")
print("2. Rectangle")
print("3. Triangle")
print("4. Circle")
print("5. Sphere")
print("6. Cylinder")

choice = int(input("Enter your choice (1-6): "))

if choice == 1:
    side = float(input("Enter side of square: "))
    area, peri = square(side)
    print(f"Area: {area}, Perimeter: {peri}")

elif choice == 2:
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    area, peri = rectangle(l, b)
    print(f"Area: {area}, Perimeter: {peri}")

elif choice == 3:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    area = triangle(b, h)
    print(f"Area of triangle: {area}")

elif choice == 4:
    r = float(input("Enter radius: "))
    area, peri = circle(r)
    print(f"Area: {area}, Circumference: {peri}")

elif choice == 5:
    r = float(input("Enter radius: "))
    sa = sphere(r)
    print(f"Surface Area of Sphere: {sa}")

elif choice == 6:
    r = float(input("Enter radius: "))
    h = float(input("Enter height: "))
    sa = cylinder(r, h)
    print(f"Surface Area of Cylinder: {sa}")

else:
    print("Invalid choice. Please enter a number from 1 to 6.")
