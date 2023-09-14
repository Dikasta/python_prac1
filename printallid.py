import json
import requests as req
def depth(x):
    if type(x) is dict and x:
        return 1 + max(depth(x[a]) for a in x)
    if type(x) is list and x:
        return 1 + max(depth(a) for a in x)
    return 0
import json
import requests as req
data={"page":1,"per_page":6,"total":12,"total_pages":2,
      "data":[{"id":1,"email":"george.bluth@reqres.in","first_name":"George","last_name":"Bluth","avatar":"https://reqres.in/img/faces/1-image.jpg"},
              {"id":2,"email":"janet.weaver@reqres.in","first_name":"Janet","last_name":"Weaver","avatar":"https://reqres.in/img/faces/2-image.jpg"},
              {"id":3,"email":"emma.wong@reqres.in","first_name":"Emma","last_name":"Wong","avatar":"https://reqres.in/img/faces/3-image.jpg"},
              {"id":4,"email":"eve.holt@reqres.in","first_name":"Eve","last_name":"Holt","avatar":"https://reqres.in/img/faces/4-image.jpg"},
              {"id":5,"email":"charles.morris@reqres.in","first_name":"Charles","last_name":"Morris","avatar":"https://reqres.in/img/faces/5-image.jpg"},
              {"id":6,"email":"tracey.ramos@reqres.in","first_name":"Tracey","last_name":"Ramos","avatar":"https://reqres.in/img/faces/6-image.jpg"}
              ],
      "support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}

d= depth(data)
print(d)
# lst1=[]  # store all email id into list
# lst2 =[]
# lst3 =[]
# print(data["data"])
# #data["data"] =[{'id': 1, 'email': 'george.bluth@reqres.in', 'first_name': 'George', 'last_name': 'Bluth', 'avatar': 'https://reqres.in/img/faces/1-image.jpg'}, {'id': 2, 'email': 'janet.weaver@reqres.in', 'first_name': 'Janet', 'last_name': 'Weaver', 'avatar': 'https://reqres.in/img/faces/2-image.jpg'}, {'id': 3, 'email': 'emma.wong@reqres.in', 'first_name': 'Emma', 'last_name': 'Wong', 'avatar': 'https://reqres.in/img/faces/3-image.jpg'}, {'id': 4, 'email': 'eve.holt@reqres.in', 'first_name': 'Eve', 'last_name': 'Holt', 'avatar': 'https://reqres.in/img/faces/4-image.jpg'}, {'id': 5, 'email': 'charles.morris@reqres.in', 'first_name': 'Charles', 'last_name': 'Morris', 'avatar': 'https://reqres.in/img/faces/5-image.jpg'}, {'id': 6, 'email': 'tracey.ramos@reqres.in', 'first_name': 'Tracey', 'last_name': 'Ramos', 'avatar': 'https://reqres.in/img/faces/6-image.jpg'}]
#
# for i in range(len(data["data"])):
#     lst1.append(data["data"][i]['email']) #store all email id into list
#     lst2.append(data["data"][i]['first_name']) #store all firstname into list
#     lst3.append(data["data"][i]['last_name']) ##store all lastname into list
# for j in range(len(lst1)):
#
# #['george.bluth@reqres.in', 'janet.weaver@reqres.in', 'emma.wong@reqres.in', 'eve.holt@reqres.in', 'charles.morris@reqres.in', 'tracey.ramos@reqres.in']
#     lst_s = lst1[j].split('.')
# #['george', 'bluth@reqres', 'in']
#     lst_s[1]=lst_s[1].split('@') #['george', ['bluth', 'reqres'], 'in']
#
#     if lst_s[0]==lst2[j] and lst_s[1][0]== lst3[j]:
#         pass
#     else:
#         print(lst1[j])
# data=[{'a':1},{'b':2},{'c':3},{'d':4}]
# # d=dict(data)
# # print(d)
# # print(data["data"][0])
# # getvar= 'https://api.openweathermap.org/data/2.5/weather'
# # var =req.get(getvar)
# # data=var.json() #very important
# # print(data)
#
