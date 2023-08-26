# generic code of dictionary if you pass any key then find all values corresponding to keys
# I checked this code with many bulky dictionary data
#if you have json then convert into dictionary then procees input data

def all_keys(search_dict, key_id):# key_id is p data and search_dict is dictionary
    for i in search_dict:  # i is keys of dictionary  search_dict
        if i == key_id:
            return search_dict[i] # return values of dictionary for particular keys

def depth(y,ls, p=''):
    for k,v in y.items(): # make dictinary in key values format

        if isinstance(v, list): # check input is list
            for j in v:  # inside list contains many dictionary then iterate list iterration
                if isinstance(j, dict):  # list index data is dictionary
                    var1 = all_keys(j, p) # return all  iteration data into var_dict
                    if var1:
                        ls.append(var1)
                    elif depth(j,ls ,p):
                        print("call method")
        else:
            if isinstance(v, dict):  # check input is dict or dictionary
                var_dict = all_keys(v, p)  # return all  iteration data into var_dict
                if var_dict:
                    ls.append(var_dict)
                if depth(v,ls, p): # here ls store all data of var_dict
                        pass
    return ls
var = {
    "D" :{
        4:{
            "t":['a','b','c'],
            "he" :[1,2,3,3]
        }
    },
    "A": {
        "a": {
            "digit": [3, 4, 5],
            "flots": [1.2, 2.3],
            "t": "A"
        },
        "b": [
            {
                "names": ["John", "Anna"],
                "cities": ["Pune", "Mumbai"]
            },
            {
                "name": ["India", "UK"]
            },
            {
                "randome": {
                    "numbers": [100, 200],
                    "chars": {
                        "alpha": ["a", "b"],
                        "t": [1,3]
                    }
                }
            }
        ]
    }


}
lst=[]
print(depth(var,lst, "t")) #here pass list(lst) and store all 't' values into list from given dictionary \
# input and here get output into list format
