n = int(input("How many numbers? "))
first = int(input("Enter number 1: "))

largest = second_largest = smallest = first

for i in range(1, n):
    num = int(input(f"Enter number {i+1}: "))
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Second Largest:", second_largest)
print("Smallest:", smallest)
