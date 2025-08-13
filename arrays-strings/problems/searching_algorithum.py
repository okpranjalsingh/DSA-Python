'''
 In linear search, we check each element one by one until we find the target or reach the end of the list.

 Start from the first element > Compare with target > If match found → return index >
 If list ends → return not found.
'''


def liner_search(arr, target):
    for i in range (len(arr)):
        if arr[i] == target:
            return i
    return -1



nums = [1,2,4,5,6,8,7,9]
target = 7
result = liner_search(nums, target)
print("Element found at index:", result if result != -1 else "Not Found")