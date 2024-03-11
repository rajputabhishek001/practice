def even_odd(a):
    if a & 1 == 0:return True
    else:return False

def merge(arr1, arr2) -> float:
    merge=arr1+arr2
    merge.sort()
    if len(merge) & 1 == 0:
        mid1 = len(merge) // 2 - 1
        mid2 = len(merge) // 2
        sum_of_middle_values = merge[mid1] + merge[mid2]
        median_of_sum = sum_of_middle_values / 2.0
        return median_of_sum
    else:
        middle_index = len(merge) // 2
        return merge[middle_index]
    
arr1 = [1,2]
arr2=[3,4]

print(merge(arr1,arr2))