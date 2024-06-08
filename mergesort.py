def merge(left,right):
    i,j=0,0
    merged=[]
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
    merged+=left[i:]+right[j:]
    return merged
def mergesort(arr):
    if len(arr)==1:
        return arr
    mid=len(arr)//2
    left=mergesort(arr[:mid])
    right=mergesort(arr[mid:])
    return merge(left,right)
arr=[3,4,2,1,6]
print(mergesort(arr))
#hello
