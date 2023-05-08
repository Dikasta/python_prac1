# json to dictionary
# import json
# json_file='''{"data":[{"stuff":[
#     {"onetype":[
#         {"id":1,"name":"John Doe"},
#         {"id":2,"name":"Don Joeh"}
#     ]},
#     {"othertype":[
#         {"id":2,"company":"ACME"}
#     ]}]
# },{"otherstuff":[
#     {"thing":
#         [[1,42],[2,2]]
#     }]
# }]}'''
# data=json.loads(json_file)
# #print(data)
# # dictionary to json
# data1={'data': [{'stuff': [{'onetype': [{'id': 1, 'name': 'John Doe'}, {'id': 2, 'name': 'Don Joeh'}]}, {'othertype': [{'id': 2, 'company': 'ACME'}]}]}, {'otherstuff': [{'thing': [[1, 42], [2, 2]]}]}]}
# print(data1['data'][0]['stuff'])
# dictin= json.dumps(data1, indent=4) # here put indent for readability
# print(dictin)
# print(type(dictin))
#fshd
data=[{'a':1},{'b':2},{'c':3},{'d':4}]
#print(data[0].values())
list=[]
list1=[]
sum=0
for itr in range(len(data)):
    print(data[itr])
    for k,v in data[itr].items():
        list1.append(v)
    #list.append(data[itr].values())
print(list1)

# print(list)
# for i in range(len(list)):
#     s= list[i].
# print(s)



