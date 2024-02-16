def merge_sort(arr):
    if len(arr)>1:
        q = len(arr)//2
        l = arr[:q]
        r = arr[q:]
        merge_sort(l)
        merge_sort(r)
        i = j = k = 0
        while i<len(l) and j <len(r):
            if l[i]<r[j]:
                arr[k] = l[i]
                i+=1
            else:
                arr[k] = r[j]
                j+=1
            k+=1
        while i < len(l):
            arr[k] = l[i]
            i+=1
            k+=1
        while j < len(r):
            arr[k] = r[j]
            j+=1
            k+=1
k=3
n=4
array1 = [1,3,5,7]
array2 = [2,4,6,8]
array3 = [0,9,10,11]
mergedarr=[array1,array2,array3]
sortedarray=[]
for a in mergedarr:
    sortedarray+=a
merge_sort(sortedarray)
print(sortedarray)

K = 3
N =  3
array1 = [1,3,7]
array2 = [2,4,8]
array3 = [9,10,11]
mergedarr=[array1,array2,array3]
sortedarray=[]
for a in mergedarr:
    sortedarray+=a
merge_sort(sortedarray)
print(sortedarray)