import sys
def max_sum(arr, k:int)->int:
    i,j = 0,0
    sum =0
    mx = -sys.maxsize - 1
    while(j < len(arr)):
        sum += arr[j]
        if j-i+1 < k:
            j+=1
        elif j-i+1 == k:
            mx = max(mx, sum)
            sum = sum - arr[i]
            i += 1
            j += 1
    return mx

arr = [1,2,3,4]
k = 2
print(max_sum(arr, k))
