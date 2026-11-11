class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for str in tokens:
            if str == "+":
                x=stack.pop()
                y=stack.pop()
                stack.append(int(y)+int(x))
            elif str == "-":
                x=stack.pop()
                y=stack.pop()
                stack.append(int(y)-int(x))
            elif str == "*":
                x=stack.pop()
                y=stack.pop()
                stack.append(int(y)*int(x))
            elif str == "/":
                x=stack.pop()
                y=stack.pop()
                if y !=0:
                    stack.append(int(y)/int(x))
                else:
                    stack.append("0")
            else:
                stack.append(str)
        return int(stack[-1])
        