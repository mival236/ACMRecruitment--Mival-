
# Function to rotate an array
def rotate(nums, k):
    n = len(nums)
    k = k % n  # handle cases where k > n
    return nums[-k:] + nums[:-k]

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print("Original:", nums)
    rotated = rotate(nums, k)
    print(f"Rotated by {k}:", rotated)
