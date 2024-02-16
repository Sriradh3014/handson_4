def remove_duplicate(arr):
    res=[]
    for i in arr:
        if i not in res:
            res.append(i)
    return res


array = [2, 2, 2, 2, 2]
print(remove_duplicate(array))
array = [1, 2, 2, 3, 4, 4, 4, 5, 5]
print(remove_duplicate(array))