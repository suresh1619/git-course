def selection(arr):
    for i in range(len(arr)):
        low=i
        for j in range(i,len(arr)):
            if arr[j]<arr[i]:
                low=j
        arr[i],arr[low]=arr[low],arr[i]
    return arr

if __name__=='__main__':
    arr=list(map(int,input().split()))
    print(selection(arr))