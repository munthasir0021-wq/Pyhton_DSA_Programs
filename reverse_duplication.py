def remove_duplication(arr):
    result=[]
    seen=set()

    for x in arr:
        if x not in seen:
            result.append(x)
            seen.add(x)
    return result

print(remove_duplication([1,2,3,2,1,4,5,3]))
