def fibonacci(n):
    """Function to return the first n numbers of the Fibonacci sequence."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    # Start the sequence with the first two Fibonacci numbers
    sequence = [0, 1]

    # Generate the remaining Fibonacci numbers
    for i in range(2, n):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence


# Input from user
n = int(input("Enter the number of Fibonacci numbers to generate: "))

# Output the Fibonacci sequence
print(fibonacci(n))
