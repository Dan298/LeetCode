class Solution(object):
    def isValid(self, s):
        key = {')': '(', ']': '[', '}': '{'}
        stack = []
        if len(s) == 1 or s[0] == ')' or s[0] == '}' or s[0] == ']':
            return False
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif len(stack) != 0 and key[char] == stack[len(stack)-1]:
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True

        return False

s = Solution()
print(s.isValid('(])'))