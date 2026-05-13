def mergesort(arr):# work on top down and devide and concur
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left1=mergesort(left)
    right1= mergesort(right)
    return merge(left1,right1)

def merge(left, right):
    res =[]
    i=j=0
    while len(left)>i and len(right)>j:
        if left[i]<right[j]:
            res.append(left[i])
            i=i+1
        else:
            res.append(right[j])
            j=j+1

    while len(left)>i:
        res.append(left[i])
        i+=1
    while len(right)>j:
        res.append(right[j])
        j+=1
    return res


if __name__ =="__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]

    var=mergesort(arr)

    print("Sorted array:", var)



# bottom up ======================

def merge(arr, left, mid, right):
    i=j=0
    k =left
    L= arr[left:mid+1]
    R = arr[mid+1:right+1]
    while i< len(L) and j<len(R):
        if L[i]<R[j]:
            arr[k]= L[i]
            i+=1

        else:
            arr[k]= R[j]
            j+=1
        k+=1
## Copy remaining elements
    while  i< len(L):
        arr[k]= L[i]
        i+=1
        k+=1
    while j< len(R):
        arr[k]= R[j]
        j+=1
        k+=1
def mergsort(arr):
    # Merge subarrays in bottom-up manner
    size =1
    n = len(arr)
    while size < n:
        for l in range(0, n-1, 2*size):
            mid = min(l+size-1, n-1) #calculate left index
            right= min(l+2*size-1, n-1)# calculate right index
            if mid< right:
                merge(arr, l, mid,right)
        size*=2


if __name__=='__main__':
    arr = [38, 27, 43, 3, 9, 82, 10]
    mergsort(arr)
print(arr)


#quick sort 
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)

arr = [1, 7, 4, 1, 10, 9, -2]
quick_sort(arr, 0, len(arr) - 1)
print(arr)


