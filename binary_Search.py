def binary_search(lst, num):
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] > num:
            end = mid - 1
        elif lst[mid] < num:
            start = mid + 1
        else:
            return mid
    return None


