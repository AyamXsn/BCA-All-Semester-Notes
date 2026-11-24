def binary_search(sorted_values, target):
    """Return target's index in sorted_values, or -1 if not found."""
    low, high = 0, len(sorted_values) - 1
    while low <= high:
        middle = (low + high) // 2
        if sorted_values[middle] == target:
            return middle
        if sorted_values[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1

if __name__ == "__main__":
    data = [2, 4, 7, 11, 18, 25]
    print(binary_search(data, 11))  # 3

# Input requirement: values must be sorted in ascending order.
# Run: python binary_search.py
