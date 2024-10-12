def square_dict(nums):
    # Dictionary comprehension to generate dictionary of squares
    return {num: num ** 2 for num in nums}

# Input: list of integers from user
nums = list(map(int, input("Enter integers separated by spaces: ").split()))

# Function call
result = square_dict(nums)

# Output the result
print("The dictionary of squares is:", result)
