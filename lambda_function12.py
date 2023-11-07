'''print 1 to 100 numbers without using loop'''
num= lambda i,a: print(i) or num(i+1,a) if i<=100 else 100
num(1,100)

'''addition'''
add=lambda  num: num+4
print(add(6))

'''multiplication with multiple agrs'''
list=[1,2,3,4,5]
for i in range(len(list)):

    mul= lambda  a,b: print(list[i]**2)
    mul(list,list)

'''odd number list'''
list_ = [34, 12, 64, 55, 75, 13, 63]
odd_list= list(filter(lambda odd :(odd%2!=0) ,list_))  # here list() method only work , this list [] will not work
print(odd_list)

'''squire using for loop with lambda'''
sqr=[lambda num=num : num**2 for num in range(0,11)]  # store the num value into num types variable(num=num :num**2)
for sq in sqr:
    print(sq() ,end=' ')

'''find minimum values'''
Minimum = lambda x, y: x if (x < y) else y
print(Minimum(35, 74))

#hfskjhfvjhbdf

