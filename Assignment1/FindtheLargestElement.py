def find_largest(nums: list) -> int:
    """Function to find the largest element in a list without using max()."""
    if not nums:
        raise ValueError("The list is empty.")

    # Initialize the first element as the largest
    largest = nums[0]

    # Loop through the list to find the largest element
    for num in nums[1:]:
        if num > largest:
            largest = num

    return largest


# Example usage
nums = [10, 25, 5, 42, 18]
largest_num = find_largest(nums)
print(f"The largest number is: {largest_num}")
