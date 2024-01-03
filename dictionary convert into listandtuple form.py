# dictionary converted into list and tuple formate
def fun(var,lst):
    ls =[]
    for k,v in var.items():
        if isinstance(v,dict):
            lst.append([k, fun(v,ls)])

        else:
            lst.append((k,v))
    return lst

var = {'A': 1, 'B': 2, 'C': {'a': {'p': 'vishal', 'q': {'f':123,'h':32541}}, 'b': 10}}
lst =[]
print(fun(var,lst))
#[('A', 1), ('B', 2), ['C', ['a', [('p', 'vishal'), ('q', 'gupta')], ('b', 10)]]]
[('A', 1), ('B', 2), ['C', [['a', [('p', 'vishal'), ['q', [('f', 123), ('h', 32541)]]]], ('b', 10)]]]
