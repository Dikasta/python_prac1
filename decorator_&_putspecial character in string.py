# decorator
# # def add(x):
# #     def adder(y):
# #         print(y)
# #         return x+y
# #     return adder
# # add15=add(15)
# # print(add15(10))
# #
#
#
#
# #OneTwoThree
# put special charecter in string
# input= 'OneTwoThree'
# lst = ""
# for i in input:
#     if i.isupper():
#         lst += "@" + i # here 1st upper character store with '@O'  (1st iteration output will be @O)
#         print(lst)
#
#     else:
#         lst += i # here concatinate all small character with (if condition special charecter and upper character)
#     #print(lst) #@One@Two@Three
# var = lst.split('@') # spliting string with special character '@' (after split output will be : ['', 'One', 'Two', 'Three'])
# var.remove('') # here i'm remove single code('') from list
# print(var) #['One', 'Two', 'Three']
#

# print word in reverse order
string = "geeks quiz practice code"
print(string.split()[::-1])
