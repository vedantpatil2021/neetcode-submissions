class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        count = 0
        for i in range(len(tokens)):
            if tokens[i] == "+":
                count = int(stk[-2]) + int(stk[-1])
                stk.pop()
                stk.pop()
                stk.append(count)
            elif tokens[i] == "-":
                count = int(stk[-2]) - int(stk[-1])
                stk.pop()
                stk.pop()
                stk.append(count)
            elif tokens[i] == "*":
                count = int(stk[-2]) * int(stk[-1])
                stk.pop()
                stk.pop()
                stk.append(count)
            elif tokens[i] == "/":
                count = int(int(stk[-2]) / int(stk[-1]))
                stk.pop()
                stk.pop()
                stk.append(count)
            else:
                stk.append(tokens[i])

        return int(stk[-1])