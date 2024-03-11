# def all_substrings(string):
#     substrings = []
#     for i in range(len(string)):
#         for j in range(i + 1, len(string) + 1):
#             substrings.append(string[i:j])
#     return substrings

# string = "hello"
# substrings = all_substrings(string)

# print(substrings)
def customSortString(order, s):
    dict1 = {char: i for i, char in enumerate(order)}
    sort_s = sorted(s, key=lambda x: dict1.get(x, len(order))) 
    result = ''.join(sort_s)
    return result

# Example usage:
order = "cba"
s = "abcd"
result = customSortString(order, s)
# print(result)

# order1 = "cba"
# s1 = "abcd"
# output1 = customSortString(order1, s1)
# print(output1)
order2 = "bcafg"
s2 = "abcd"
output2 = customSortString(order2, s2)
# print(output2) 
