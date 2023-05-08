# union and intersection methods  belongs to only set not in list
set1={1,5,7,3,4,9,2,8}
set2 ={3,4,10,11}
set3={11,12,3}
# union using method
#print(set1.union(set2).union(set3))
 # intersection
#print(set1.intersection(set2))

s1=[1,5,7,3,4,9,2,8]
s2 =[3,4,10,11]
# union of method
s3 =s1+s2
#print([set(s3)])   # remove all duplicate from list s3
#op   [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
s4 =[]
[s4.append(i) for i in s3 if i not in s4]  # remove all duplicate from list s3 after remove all duplicate then get union of two list
#print(s4)

for i in s3:
    if i not in s4:
        s4=s4+[i]
#print(s4)   #remove all duplicate from list s3 after remove all duplicate then get union of two list
s5=[]
for i in s1:
    for j in s2:
        if i==j:
            s5=s5+[j]
print(s5)  # intersection of two list op [3, 4]




