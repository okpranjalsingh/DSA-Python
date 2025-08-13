"""
Problem: Implement linear search to find the index of a target element in an array.

Algorithm:
1. Loop through array elements from start to end.
2. Check if current element equals the target.
3. If yes, return current index.
4. If loop ends without match, return -1.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    arr = [4, 2, 7, 1, 9, 3]
    target = 7
    result = linear_search(arr, target)
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found")
