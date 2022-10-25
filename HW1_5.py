# Проходим через список однократно, поэтому сложность = O(n)

class Solution:
    def removeOuterParentheses(self, S):
        res = []                                        # Выходной массив
        opened = 0                                      # Счётчик незакрытых скобок
        for c in S:
            if c == '(' and opened > 0: res.append(c)
            if c == ')' and opened > 1: res.append(c)
            opened += 1 if c == '(' else -1             # Если первый символ != ( , а последний != ) - добавляем его к результирующему массиву.
        return "".join(res)

ans = Solution()
print (ans.removeOuterParentheses("(()())(())"))
print (ans.removeOuterParentheses("(()())(())(()(()))"))
print (ans.removeOuterParentheses("()()"))