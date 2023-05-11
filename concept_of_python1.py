"""enumaration=>1. dealing with iteration and also keep count of every iteration
2.any object that supports iteration
3. Start: the index value from which the counter is to be started, by default it is 0
"""
# l1 = ["eat", "sleep", "repeat"]
# obj1=enumerate(l1)
# print(list(obj1)) # here 0 index and 'eat' values always we need to print obj1 in list without list we cant print[(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
#
# s='ggkeeks'
# obj2=enumerate(s)
# print(list(obj2)) #op [(0, 'g'), (1, 'g'), (2, 'k'), (3, 'e'), (4, 'e'), (5, 'k'), (6, 's')]

l1 = ["eat", "sleep", "repeat"]
#changing index and printing separately
# for count, ele in enumerate(l1, 100):
#     print (count, ele) #100 eat 101 sleep 102 repeat
#
for count, ele in enumerate(l1):
    print(count)
    print(ele)
''' op => 0
eat
1
sleep
2
repeat'''