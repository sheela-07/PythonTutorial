def is_prime(n):
    """Helper function to check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Input range from user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# List comprehension to generate prime numbers between start and end
prime_numbers = [n for n in range(start, end + 1) if is_prime(n)]

# Output the prime numbers
print(f"Prime numbers between {start} and {end}: {prime_numbers}")
