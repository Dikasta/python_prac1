"""sort url based on content length"""
import requests as rst
list=['https://www.geeksforgeeks.org/python-check-url-string/','https://www.scaler.com/topics/how-to-square-a-number-in-python/']
list1=[]
for itr in list:
    #print()
    var=rst.head(itr)
    #print(var.headers)
    size_head=var.headers.get('Content-Length')
    list1=list1+[size_head] # store size_head into list like [size_head]
print(list1) #['32926', '0'] in bytes
