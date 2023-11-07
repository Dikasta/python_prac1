"""
input=>list1 = [2, 3, 4, 7, 6, 10, 5, 1]
o/p #output [1,3,5,7,2,4,6,10]  1st arrange odd number then arrange even number
"""

list2 = [2, 3, 4, 7, 6, 10, 5, 1]
list1=sorted(list2)
list3=[]
list4=[]
for k in range(0, len(list1)-1):
    if list1[k]%2 == 0:
        list3 =list3+[list1[k]] # list1[k] giving data not giving values for conveting into list use []
    else:
        list4 =list4+[list1[k]]
l2= list4+list3 # op returning correct data

"""
i/p=a=[1,2,3,4,5]
b=['a','b','c','d','e']
convert into dictionary
o/p= {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
"""
a=[1,2,3,4,5]
b=['a','b','c','d','e']
c={}
for i,j in zip(a,b):
    c[i]=j
print(c)
