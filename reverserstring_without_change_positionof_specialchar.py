st='abc/defgh$ij'
st1=list(st)
j=len(st)-1
i=0
while (i<j):
    if not st1[i].isalpha():
        i+=1
    elif not st1[j].isalpha():
        j-=1
    else:
        st1[i], st1[j]= st1[j],st1[i]
        i+=1
        j-=1
    s_out=''.join(st1)
print(s_out) # op jih/gfedc$ba
