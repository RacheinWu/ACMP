
def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    if len(str(x)) == 1:
        return True
    s = str(x)
    left_point, right_point = 0, len(s)-1
    print(len(s))
    while left_point != right_point:
        if s[left_point] == s[right_point]:
            left_point += 1
            right_point -= 1
            continue
        return False
    return True

