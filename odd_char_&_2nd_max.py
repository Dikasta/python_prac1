# odd time charecter remove
# from collections import Counter
# def fun(st):
#     frq=Counter(st)
#
#     for i in frq:
#         #print(i)
#         cnt=0
#         if frq[i]%2!=0 and cnt>1:
#             del frq[i]
#
#             return True
#     return False
#
# st1="aabbcdd"
# if fun(st1):
#     print("valid")
# else:
#     print("invalid")
#
# 2nd highest number in list
# ls=[70,11,20,4,100]
# temp =ls[0]
# fir=ls[0]
# for i in range(len(ls)):
#     if ls[i]>= temp:
#         sec = fir
#         fir =ls[i]
#
# print(sec)
# print(fir)
lst =[12,3,4,1,6,9]
lst.sort()
n= len(lst) -1
#i=0
sum=24
#l =i+1

# 3sum in O(n^2)
for i in range(0, n-2):
    n1 = len(lst) - 1
    #j= 0

    l = i + 1
    while n1 > i:
        if lst[i] + lst[l] + lst[n] == sum:
            print(lst[i], lst[l], lst[n])
            #break
        if lst[i] + lst[l] + lst[n] < sum:
            i+=1
        else:
            n1-=1





