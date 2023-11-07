#print integer 5 into character o/p => "5"
# def demo(num):
#     lst =[]
#     while num > 0:
#         print(num)
#         #print(ord("0")) # "0" return 48
#         #print(chr(ord("0") + num%10))  # all 3 2 1 are str
#
#         lst.append(chr(ord("0") + num%10))
#         #print()
#         num //=10 # while is running behalf of this
#     return "".join(lst[::-1])
#     #return lst
# v=demo(123)
# print('"%s"' %v) #op "123"
# print(f"'{v}'") #op '123'
# var ='"{}"'.format(v)
# print(var)  #op "123"
# print(str(v))   #  type str 123


import sys
import sys
data = sys.stdin.readlines()
print("Counted", len(data), "lines.")

#https://stackoverflow.com/questions/1450393/how-do-i-read-from-stdin
#https://stackoverflow.com/questions/1369526/what-is-the-python-keyword-with-used-for
#https://www.geeksforgeeks.org/python-sys-module/
