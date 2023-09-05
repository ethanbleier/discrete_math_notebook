def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

list = [1, 3, 5, 7, 9]
target = 7
search_result = binary_search(list, target) 
print("Algorithms:")
print(f"Binary Search: {target} found at index {search_result} in {list}")
print()