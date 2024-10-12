def calculate(nums=None, operation="sum"):
    # Default to an empty list if nums is not provided
    if nums is None:
        nums = []

    # Check for the operation type and perform the corresponding calculation
    if operation == "sum":
        return sum(nums)
    elif operation == "product":
        product = 1
        for num in nums:
            product *= num
        return product
    else:
        return "Invalid operation"


# Example usage:
nums = [1, 2, 3, 4]
print(calculate(nums, "sum"))  # Output: 10
print(calculate(nums, "product"))  # Output: 24
print(calculate())  # Output: 0 (default sum on an empty list)
