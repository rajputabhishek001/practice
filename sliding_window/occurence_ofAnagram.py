def anagram(s: str, pat: str) -> int:
    i, j = 0, 0
    dp = {}
    ans = 0

    for ele in pat:
        if ele in dp:
            dp[ele] += 1
        else:
            dp[ele] = 1

    count = len(dp)

    while j < len(s):
        if s[j] in dp:
            dp[s[j]] -= 1
            if dp[s[j]] == 0:
                count -= 1

        if j - i + 1 < len(pat):
            j += 1
        elif j - i + 1 == len(pat):
            if count == 0:
                ans += 1

            if s[i] in dp:
                dp[s[i]] += 1
                if dp[s[i]] == 1:
                    count += 1

            i += 1
            j += 1

    return ans

s = "aabaabaa"
ptr = "aaba"
print(anagram(s, ptr))

