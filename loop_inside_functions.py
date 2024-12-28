def find_max(arr):
    """
    Finds the maximum value in a list of numbers.
    Parameters:
    arr (list): A list of numerical values.
    Returns:
    int/float: The maximum value in the list.
    Raises:
    ValueError: If the input list is empty.
    """

    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

arr = [1, 2, 3, 4, 5, 152, 6, 7, 8, 9]
print(find_max(arr))