def binary_search(list, item):
    low = 0
    up = len(list) - 1
    
    while low <= up:
        mid = (low + up) // 2
        num = list[mid]
        if num == item:
            return mid
        if num > item:
            up = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1,3,5,7,9]

print(binary_search(my_list, 7))
print(binary_search(my_list, -1))