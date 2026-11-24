def linear_search(values, target):
    """Return the first index of target, or -1 when it is absent."""
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1

def main():
    numbers = [12, 7, 19, 4, 7]
    target = 19
    print(linear_search(numbers, target))  # 2

if __name__ == "__main__":
    main()

# Run: python linear_search.py
# Expected result: 2
