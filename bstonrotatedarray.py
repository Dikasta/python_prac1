
def Binarysearchminelement(lst,low,high):  # find min values index into rotated array
    if low>high:
        return -1
    mid = (low+high)//2
    next = (mid+1)%high
    prev = (mid-1+high) % high
    if lst[mid]<lst[prev] and lst[mid]<lst[next] :
        return mid
    if lst[mid]<=lst[low]:
        #high=prev
        return Binarysearchminelement(lst,low,mid)
    return Binarysearchminelement(lst,mid,high)


def findbstkey(li,h,key):  # get min values index and call bst for finding key
    min_index = Binarysearchminelement(li,0, h-1)
    #print(min_index)

    if min_index== -1:
        return BinarySearch(li,0,h-1,key)
    if li[min_index] ==key:
        return min_index
    if li[0]<= key:
        return BinarySearch(li,0,min_index-1,key)
    return BinarySearch(li,min_index+1,h-1,key)

def BinarySearch(l1,l,hi,key): #binary search for find a key

    if l>hi:
        return -1
    mid1=(l+hi)//2
    if key==l1[mid1]:
        return mid1
    if key> l1[mid1]:
        return BinarySearch(l1,mid1+1,hi,key)
    return BinarySearch(l1,l,mid1-1,key)



li = [5, 6, 7, 8, 9, 10, 1, 2, 3]
h = len(li)
key = 3
l=0

print(findbstkey(li,h,key))


