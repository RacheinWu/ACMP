class Solution:
    def longestValidParentheses(self, s: str) -> int:
        pass


def stack_fc(s: str) -> int:
    if not s:
        return 0
    res = []
    stack = []
    for i in range(len(s)):
        if stack and s[i] == ")":
            res.append(stack.pop())
            res.append(i)
        if s[i] == "(":
            stack.append(i)
    print(res)
    res.sort()
    print(res)

stack_fc(")(()())")