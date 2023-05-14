def twosum(nums,target):
    values = {}
    for ind,val in enumerate(nums):
        var= target-val
        if var in values:   # in 2nd iteration var is 1 then var checking to dictionary(values) key if key available then if is true
            return [values[var], ind]   # values[key like 1] get values 0 and ind in 2nd iteration 1
        else:
            values[val] =ind   # 1st iteration here values converted into key and ind treat as values then strore into dictionary values
    return [-1,-1]

num = [1, 5, 7, -1, 5]
target1 = 6
print(twosum(num, target1))

# enumerate: enumerate(iterable ,indexvalues)
# #exp1:
# l1 = ["eat", "sleep", "repeat"]
# obj1 = enumerate(l1)
# print(list(obj1)) # op [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]

#exp2:

# s1 = "geek"
# obj2 = enumerate(s1)
# print(list(obj2)) #[(0, 'g'), (1, 'e'), (2, 'e'), (3, 'k')]
# print(list(enumerate(s1,2))) #[(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')] (into enumerate function passing 2 is starting index)

