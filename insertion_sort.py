def insertion_sort(arr):
    """
    Implementation of insertion sort algorithm.
    
    Args:
        arr: A list of comparable elements
    
    Returns:
        The same list sorted in ascending order
    """
    # Iterate through the array starting from the second element

    n = input(int())
    # input from console 
    
    arr = list(map(int, input().split()))

    for i in range(n):
        # Store the current element to be inserted in the right position
        key = arr[i]
        # Initialize j as the position before the current element
        j = i - 1
        
        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            print(arr)
        
        # Place the key in its correct position
        arr[j + 1] = key
    
    return arr

# Example usage
if __name__ == "__main__":
    