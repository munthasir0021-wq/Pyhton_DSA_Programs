def reverse_vowels(s):
    vowels="aeiouAEIOU"
    charts=list(s)
    left,right = 0, len(charts)-1

    while left<right:
        if charts[left] not in vowels:
            left+=1
        elif charts[right] not in vowels:
            right-=1
        else:
            charts[left],charts[right]=charts[right],charts[left]
            left+=1
            right-=1
    return "".join(charts)
print(reverse_vowels("hello world"))

        