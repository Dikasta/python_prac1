# make upper case all char into string
var= 'hello'
# var1=var[0].upper()+ var[1:]
# print(var1) #op Hello
# 2nd way
st = ''
for itr in var:
    if ord(itr)>=97 and ord(itr)<=122 :
        var1= ord(itr)-32
        st=st+chr(var1)
print(st)  # op HELLO


# make lower case all char into string
var = 'HELLO'
# var1= var[0].lower() +var[1:]
# print(var1) # op hELLO
# # 2nd way
# st = ''
# for itr in var:
#
#
#     if ord(itr)>=65 and ord(itr)<=90 :
#         var1= ord(itr)+32
#         st=st+chr(var1)
# print(st)  # op hello


