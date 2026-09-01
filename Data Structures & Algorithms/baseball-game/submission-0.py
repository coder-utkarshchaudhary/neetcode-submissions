class Solution:
    def calPoints(self, operations: List[str]) -> int:
        if operations[0] in ("+", "D", "C"):
            return 0
        stack = [int(operations[0])]
        for i in range(1, len(operations)):
            if operations[i]=="+":
                if len(stack)>=2:
                    top, top_1 = stack[-1], stack[-2]
                    stack.append(top+top_1)
                else:
                    return -1
            elif operations[i]=="D":
                stack.append(stack[-1]*2)
            elif operations[i]=="C":
                stack.pop(-1)
            else:
                stack.append(int(operations[i]))
            print(stack)
        
        return sum(stack)