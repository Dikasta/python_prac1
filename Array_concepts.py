'''1.array in python store only similar types of data like only interger or only float or only string types not mixup of integer/floate/string types
2. in python array size is expandible and srink it as per our requirement
3. by default array not supported into python for using of array first import library of array
4. 'i' =integer , 'u'= charecter, 'd'=floate '''

import array as arr
var= arr.array('i',[1,5,3,6,8,9]) # 'i' represent +ve and -ve interger values not support float or char

#reverse array
var.reverse()
print(var)  #array('i', [9, 8, 6, 3, 5, 1])

for j in range(len(var)):
    print(var[j], end=' ') # op 1 5 3 6 8 9

var.append(2)
print(var)  #op array('i', [1, 5, 3, 6, 8, 9, 2])

var.insert(1,10)
print(var)  #array('i', [1, 10, 5, 3, 6, 8, 9]) in insert 1 is index and 10 is values update on index 1
