def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  

# Example usage
nums = [4, 2, 7, 1, 9, 3]
target = 7
result = linear_search(nums, target)
print("Element found at index:", result if result != -1 else "Not Found")
