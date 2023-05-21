def Balancebracket(exprn):
    stack=[]
    for ch in exprn:
        if ch in ['(','[','{']:
            stack.append(ch)
        else:
            if stack and ((stack[-1] =='('  and ch ==')') or
                          (stack[-1] == '[' and ch ==']') or
                          (stack[-1] =='{' and ch =='}')):
                stack.pop()
            else:
                return False
    return  not stack


if __name__ =='__main__':
    exp="{()}[]"
    if Balancebracket(exp):
        print("balanced")