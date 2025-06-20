def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Flag to check if a swap happened in this pass

        # Traverse the unsorted part of the array
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Swap adjacent elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swaps occurred, the list is already sorted
        if not swapped:
            break
