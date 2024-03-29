# case 1: for  n=9  output will be 34
# def febonacci(n):
#     a=0
#     b=1
#     if n==0:
#         return a
#     if n==1:
#         return b
#     for i in range(2,n+1): #here passing n+1 why adding + one means without 1 loop only iterate 2->8  not 9 time
#         temp=a+b
#         a=b
#         b=temp
#     return b
# print(febonacci(9))

# case 2: recursion  :  n=9  output will be 34
# def febo(n):
#     if n<=1: #here madatory check <= condition without = show same output will return in -ve
#         return n
#     return febo(n-1)+febo(n-2)
# print(febo(9))

'''F(n) = F(n-1) + F(n-2)
F(n-1) = F(n-2) + F(n-3)
F(n-2) = F(n-3) + F(n-4)    : here same argument funtion call 2 time that redundant so i want that funtion need to call only one time
for that i'll use dynamic programming'''

def febo(n):
    lst =[0,1]
    for i in range(2,n+1):
        lst.append(lst[i-1]+lst[i-2])
    return lst[n]
print(febo(9))



#sdt




