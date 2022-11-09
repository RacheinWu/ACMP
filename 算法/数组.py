arr = input().split(" ")
n, q = int(arr[0]), int(arr[1])
arr = [int(x) for x in input().split(" ")]


def func(aim: int, count: int):
    # print(aim, count)
    # if out of boundary of array:
    if count + aim >= len(arr):
        return
    p = aim + 1
    # print(arr)
    while p < len(arr):
        # print("arr[p]=", arr[p], "arr[aim]", arr[aim])
        if arr[p] > arr[aim]:
            # print("次数-1")
            count -= 1
        if count == 0:
            print(p + 1)
            return
        p += 1
        # print("p", p, "count", count)
    # can not be found!
    print(-1)


for i in range(q):
    arr2 = input().split(" ")
    func(int(arr2[0])-1, int(arr2[1]))