def second_lergest(arr):
    largest = second_largest = float('-inf')
    for num in arr:
        if num > largest:
            second_largest = largest
            largestb= num
        elif num > second_largest and num != largest:
            second_largest=num
    return second_largest
arr=[10,5,8,20,15]
print(second_largest(arr))

 