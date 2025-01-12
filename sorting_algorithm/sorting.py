# Function for  performing insertion sort in  monotonically decreasing order
def insert_sort_mono_decreasing(arr):
    # Moving across the array from the second element (index 1)
    for i in range(1, len(arr)):
        key = arr[i]  # The element to be inserted
        last_sorted = i - 1     # The index of the last element in the sorted portion

        # Moving elements of the sorted portion that are smaller than the key to the right
        while last_sorted >= 0 and arr[last_sorted] < key:
            arr[last_sorted + 1] = arr[last_sorted]  # Shifting element to the right
            last_sorted -= 1  # Moving the pointer to the left

        # Inserting the key at its correct position
        arr[last_sorted + 1] = key

# Function for printing the array
def print_array(arr):
    print(" ".join(map(str, arr)))

# Driver code
if __name__ == "__main__":
    arr = [5, 2, 9, 1, 5, 6]

    print("Unsorted Array:")
    print_array(arr)

    # Sort the array in decreasing order using insertion sort
    insert_sort_mono_decreasing(arr)

    print("Sorted Array in Monotonically Decreasing Order:")
    print_array(arr)