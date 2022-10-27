from typing import List


# arr = [3, 4, 1, 4, 5, 12, 4, -1]


def quick_sort(arr: List[int], left: int, right: int) -> None:
    if left >= right:
        return
    i = left
    j = right
    mid = arr[right]
    while left < right:
        while left < right and mid >= arr[left]:
            left += 1
        if mid < arr[left]:
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1
        while left < right and mid <= arr[right]:
            right -= 1
        if mid > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1

        quick_sort(arr, i, left-1)
        quick_sort(arr, left, j)


arr = [49, 38, 65, 97, 76, 13, 27, 49]
quick_sort(arr, left=0, right=len(arr) - 1)
print(arr)
