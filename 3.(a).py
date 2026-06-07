nums = list(map(int, input("Enter numbers separated by space: ").split()))

largest = max(nums)
smallest = min(nums)
second_largest = sorted(set(nums))[-2] if len(set(nums)) > 1 else None

print("Largest:", largest)
print("Second Largest:", second_largest)
print("Smallest:", smallest)
