
def firstNeg(arr, k:int)->int:
    i, j = 0,0
    dp = []
    vct = []
    while j < len(arr):
        if arr[j] < 0:
            dp.append(arr[j])
        if j-i+1 < k:
            j+=1
        elif j-i+1 == k:
            if len(dp) == 0:vct.append(0)
            else:
                vct.append(dp[0])
                if arr[i] == dp[0]:dp.pop(0)
            i+=1
            j+=1

    return vct


arr = [12,-1,-7,8,-15, 30, 16, 28]
k = 3
print(firstNeg(arr,k))