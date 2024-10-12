def merge_dicts(dict1: dict, dict2: dict) -> dict:
    """Merge two dictionaries, with dict2 values overwriting dict1 values for common keys."""
    # Copy dict1 to avoid modifying the original
    merged_dict = dict1.copy()

    # Update the merged dictionary with dict2 values
    merged_dict.update(dict2)

    return merged_dict


# Example usage
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 20, 'd': 4}

# Merging the dictionaries
merged = merge_dicts(dict1, dict2)
print(merged)
