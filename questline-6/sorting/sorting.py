def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Traverse through all elements up to n-i-1
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    nums = [5, 2, 9, 1, 5, 6]
    print("Original:", nums)
    sorted_nums = bubble_sort(nums.copy())
    print("Sorted:", sorted_nums)
