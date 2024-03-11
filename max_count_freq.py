def mx_fre(arr):
    dp = {}
    ans=0
    for element in arr:
        if element in dp:
            dp[element] += 1
        else:
            dp[element] = 1
    if not dp:
        return 0
    mx = max(dp.values())
    for i in dp.values():
        if i == mx:
            ans+=mx
    return ans
        

arr= [1,2,2,3,4,3]
print(mx_fre(arr))
