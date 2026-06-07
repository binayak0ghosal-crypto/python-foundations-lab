def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Get input range from user
start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

prime_numbers = []

# Find all prime numbers in the given range
for num in range(start, end + 1):
    if is_prime(num):
        prime_numbers.append(num)

# Display the result
print("\nPrime numbers in the range ({} to {}):".format(start, end))
print(prime_numbers)

print("\nTotal number of prime numbers found:", len(prime_numbers))
