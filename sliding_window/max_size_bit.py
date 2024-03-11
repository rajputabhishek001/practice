def longestOne(arr, k: int) -> int:
    n = len(arr)
    s,e = 0, 0
    ans = 0
    one = 0
    zero = 0
    while e < n:
        if arr[e] == 1:
            one+=1
        else:
            zero+=1
        if zero <= k:
            ans = max(ans, e-s+1)
            e+=1
        else:
            while s<=e and zero>k:
                if arr[s] == 1:one-=1
                else:zero-=1
                s+=1
            if s<=e and zero<=k:
                ans = max(ans, e-s+1)
            e+=1
    return ans

arr = [1,1,1,0,0,1,1,1,1,0]
k = 2
print(longestOne(arr, k))
         