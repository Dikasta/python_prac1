def find_pairs(lst, K):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == K:
                result.append((lst[i], lst[j]))  # inside append() method pass tuple paranthesis '()' inside this tuple store sum pair(5, 7) ,(3, 9)
    print(result)
    return result
lst = [1, 5, 3, 7, 9]
K = 12
print(find_pairs(lst, K))


#flattern dictionary 
def fun(var, key='', sep='_'):
    di ={}
    for k,v in var.items():
        keys = f'{key}{sep}{k}' if key else k
        if isinstance(v, dict):

            di.update(fun(v, keys, sep)) # update is required to check nested dict condition
        else:
            di[keys] = v

    return di

    #print(var)

#o/p {'a': 1, 'b_x': 2, 'b_y_z': 3,  'c_m': 4}
var=  {
    'a': 1,
    'b': {'x': 2, 'y': {'z': 3}},
    'c': {'m': 4}}
